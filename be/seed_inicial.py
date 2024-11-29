import requests
from app import db, app
from sqlalchemy import insert
from app.Models.Pkm import Pokemon, TypePkm, pokemon_type
from app.Models.Move import Move, TypeMove, pokemon_move
from app.Models.Ability import Ability, pokemon_ability

def seed_db():
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

        # Seed Pokemon Types
        print("\nSeeding Pokemon Types...")
        type_response = requests.get('https://pokeapi.co/api/v2/type')
        types_data = type_response.json()['results']
        type_map = {}  # To store type_name: type_id mapping
        
        for type_data in types_data:
            new_type = TypePkm(nombre=type_data['name'])
            db.session.add(new_type)
            db.session.flush()
            type_map[type_data['name']] = new_type.id
            print(f"Added Type: {type_data['name']}")
        db.session.commit()

        # Seed Move Types
        print("\nSeeding Move Types...")
        move_type_map = {}  # To store type_name: type_id mapping
        for type_name in type_map.keys():
            new_move_type = TypeMove(nombre=type_name)
            db.session.add(new_move_type)
            db.session.flush()
            move_type_map[type_name] = new_move_type.id
            print(f"Added Move Type: {type_name}")
        db.session.commit()

        # Seed Moves (Generation 1)
        print("\nSeeding Moves...")
        moves_response = requests.get('https://pokeapi.co/api/v2/move?limit=165')
        moves_data = moves_response.json()['results']
        move_map = {}  # To store move_name: move_id mapping
        
        for move_url in moves_data:
            move_detail = requests.get(move_url['url']).json()
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

        # Create a set to store unique abilities
        ability_map = {}  # To store ability_name: ability_id mapping

        # Seed Pokemon and their abilities
        print("\nSeeding Pokemon, Abilities, and Relationships...")
        pokemon_response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
        pokemon_data = pokemon_response.json()['results']
        
        for poke_url in pokemon_data:
            poke_detail = requests.get(poke_url['url']).json()
            
            print(f"\nProcessing Pokemon: {poke_detail['name'].upper()}")
            
            # Get the front_default sprite URL
            sprite_url = poke_detail['sprites']['front_default']
            
            # Create Pokemon instance with only required fields
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
                
                # If ability doesn't exist, create it
                if ability_name not in ability_map:
                    ability_detail = requests.get(ability_data['ability']['url']).json()
                    new_ability = Ability(nombre=ability_name)
                    db.session.add(new_ability)
                    db.session.flush()
                    ability_map[ability_name] = new_ability.id
                    print(f"[NEW] {ability_name}", end=" ")
                else:
                    print(ability_name, end=" ")

                # Add ability to pokemon
                stmt = pokemon_ability.insert().values(
                    pokemon_id=new_pokemon.id,
                    ability_id=ability_map[ability_name]
                )
                db.session.execute(stmt)
            print()

            db.session.commit()
            print(f"Sprite URL: {sprite_url}")
            print("-" * 50)

        print("\nSeeding completed successfully!")

if __name__ == "__main__":
    seed_db()