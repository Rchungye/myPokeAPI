import requests
import asyncio
import aiohttp
from app import db, app
from sqlalchemy import insert
from app.Models.Pkm import Pokemon, TypePkm, pokemon_type
from app.Models.Move import Move, TypeMove, pokemon_move
from app.Models.Ability import Ability, pokemon_ability

# Función wrapper para mantener compatibilidad
def seed_db():
    asyncio.run(seed_db_async())

# Función auxiliar para hacer peticiones asíncronas
async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

# Procesa un batch de pokemon de forma asíncrona
async def process_pokemon_batch(session, pokemon_urls, type_map, move_map, ability_map):
    tasks = []
    for url in pokemon_urls:
        tasks.append(fetch_data(session, url['url']))
    
    pokemon_details = await asyncio.gather(*tasks)
    
    for poke_detail in pokemon_details:
        sprite_url = poke_detail['sprites']['front_default']
        
        new_pokemon = Pokemon(
            nombre=poke_detail['name'],
            sprite=sprite_url
        )
        db.session.add(new_pokemon)
        db.session.flush()

        # Add types
        print("Types:", end=" ")
        for type_data in poke_detail['types']:
            type_id = type_map[type_data['type']['name']]
            stmt = pokemon_type.insert().values(
                pokemon_id=new_pokemon.id,
                type_pkm_id=type_id
            )
            db.session.execute(stmt)
            print(type_data['type']['name'], end=" ")
        print()

        # Add moves
        print("Moves:", end=" ")
        for move_data in poke_detail['moves'][:4]:
            move_name = move_data['move']['name']
            if move_name in move_map:
                stmt = pokemon_move.insert().values(
                    pokemon_id=new_pokemon.id,
                    move_id=move_map[move_name]
                )
                db.session.execute(stmt)
                print(move_name, end=" ")
        print()

        # Add abilities
        print("Abilities:", end=" ")
        for ability_data in poke_detail['abilities']:
            ability_name = ability_data['ability']['name']
            
            if ability_name not in ability_map:
                ability_url = ability_data['ability']['url']
                ability_detail = await fetch_data(session, ability_url)
                new_ability = Ability(nombre=ability_name)
                db.session.add(new_ability)
                db.session.flush()
                ability_map[ability_name] = new_ability.id
                print(f"[NEW] {ability_name}", end=" ")
            else:
                print(ability_name, end=" ")

            stmt = pokemon_ability.insert().values(
                pokemon_id=new_pokemon.id,
                ability_id=ability_map[ability_name]
            )
            db.session.execute(stmt)
        print()

        print(f"Processed Pokemon: {poke_detail['name'].upper()}")
        print("-" * 50)

# Función principal asíncrona
async def seed_db_async():
    with app.app_context():
        # Clear existing data
        print("\nCleaning existing data...")
        db.session.query(pokemon_move).delete()
        db.session.query(pokemon_type).delete()
        db.session.query(pokemon_ability).delete()
        Move.query.delete()
        TypeMove.query.delete()
        Pokemon.query.delete()
        TypePkm.query.delete()
        Ability.query.delete()
        db.session.commit()

        async with aiohttp.ClientSession() as session:
            # Fetch types
            print("\nFetching types...")
            type_data = await fetch_data(session, 'https://pokeapi.co/api/v2/type')
            type_map = {}
            move_type_map = {}

            # Create both TypePkm and TypeMove at the same time
            for type_item in type_data['results']:
                # Create TypePkm
                new_type = TypePkm(nombre=type_item['name'])
                db.session.add(new_type)
                db.session.flush()
                type_map[type_item['name']] = new_type.id

                # Create TypeMove
                new_move_type = TypeMove(nombre=type_item['name'])
                db.session.add(new_move_type)
                db.session.flush()
                move_type_map[type_item['name']] = new_move_type.id

                print(f"Added Type: {type_item['name']}")
            
            db.session.commit()

            # Fetch moves
            print("\nFetching moves...")
            moves_data = await fetch_data(session, 'https://pokeapi.co/api/v2/move?limit=165')
            move_map = {}
            
            move_tasks = [fetch_data(session, move['url']) for move in moves_data['results']]
            move_details = await asyncio.gather(*move_tasks)

            for move_detail in move_details:
                if move_detail['generation']['name'] == 'generation-i':
                    new_move = Move(
                        nombre=move_detail['name'],
                        type_move_id=move_type_map[move_detail['type']['name']]
                    )
                    db.session.add(new_move)
                    db.session.flush()
                    move_map[move_detail['name']] = new_move.id
                    print(f"Added Move: {move_detail['name']} (Type: {move_detail['type']['name']})")
            db.session.commit()

            # Fetch Pokemon
            print("\nFetching Pokemon...")
            pokemon_data = await fetch_data(session, 'https://pokeapi.co/api/v2/pokemon?limit=151')
            
            # Process Pokemon in batches
            batch_size = 10
            ability_map = {}
            
            for i in range(0, len(pokemon_data['results']), batch_size):
                batch = pokemon_data['results'][i:i + batch_size]
                await process_pokemon_batch(session, batch, type_map, move_map, ability_map)
                db.session.commit()
                print(f"Completed batch {i//batch_size + 1}/{(len(pokemon_data['results'])//batch_size) + 1}")

        print("\nSeeding completed successfully!")

if __name__ == "__main__":
    asyncio.run(seed_db_async())