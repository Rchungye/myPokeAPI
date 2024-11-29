import requests
from app import db, app
from sqlalchemy import insert
from app.Models.Pkm import Pokemon, TypePkm
from app.Models.Ability import Ability
from app.Models.Move import Move, TypeMove

def fetch_data(url):
    """Helper function to fetch data from PokeAPI"""
    response = requests.get(url)
    return response.json()

def seed_pokemon_types():
    """Fetch and insert all Pokemon types"""
    print("Seeding Pokemon types...")
    types_data = fetch_data('https://pokeapi.co/api/v2/type')
    
    for type_entry in types_data['results']:
        type_detail = fetch_data(type_entry['url'])
        type_pkm = TypePkm(
            nombre=type_detail['name']
        )
        db.session.add(type_pkm)
    
    db.session.commit()
    print("Pokemon types seeded successfully!")

def seed_move_types():
    """Fetch and insert move types (same as pokemon types in PokeAPI)"""
    print("Seeding move types...")
    types_data = fetch_data('https://pokeapi.co/api/v2/type')
    
    for type_entry in types_data['results']:
        type_move = TypeMove(
            nombre=type_entry['name']
        )
        db.session.add(type_move)
    
    db.session.commit()
    print("Move types seeded successfully!")

def seed_moves():
    """Fetch and insert 165 moves from gen 1"""
    print("Seeding moves...")
    moves_data = fetch_data('https://pokeapi.co/api/v2/move?limit=165')
    
    type_moves = {type_move.nombre: type_move.id for type_move in TypeMove.query.all()}
    
    for move_entry in moves_data['results']:
        move_detail = fetch_data(move_entry['url'])
        if move_detail['generation']['name'] == 'generation-i':
            description = next((effect['effect'] for effect in move_detail['effect_entries'] 
                            if effect['language']['name'] == 'en'), 'No description available')
            # Truncar la descripción si es necesario
            description = description[:997] + '...' if len(description) > 1000 else description
            
            move = Move(
                nombre=move_detail['name'],
                damage=move_detail['power'] if move_detail['power'] is not None else 0,
                type_move_id=type_moves[move_detail['type']['name']],
                descripcion=description
            )
            db.session.add(move)
    
    db.session.commit()
    print("Moves seeded successfully!")

def seed_abilities():
    """Fetch and insert abilities for the first 151 Pokemon"""
    print("Seeding abilities...")
    seen_abilities = set()
    
    # Fetch all Pokemon first
    pokemon_data = fetch_data('https://pokeapi.co/api/v2/pokemon?limit=151')
    
    for pokemon_entry in pokemon_data['results']:
        pokemon_detail = fetch_data(pokemon_entry['url'])
        
        for ability_info in pokemon_detail['abilities']:
            ability_name = ability_info['ability']['name']
            
            if ability_name not in seen_abilities:
                ability_detail = fetch_data(ability_info['ability']['url'])
                ability = Ability(
                    nombre=ability_name,
                    descripcion=next((effect['effect'] for effect in ability_detail['effect_entries'] 
                                    if effect['language']['name'] == 'en'), 'No description available')
                )
                db.session.add(ability)
                seen_abilities.add(ability_name)
    
    db.session.commit()
    print("Abilities seeded successfully!")

def seed_pokemon():
    """Fetch and insert the first 151 Pokemon with their relationships"""
    print("Seeding Pokemon...")
    pokemon_data = fetch_data('https://pokeapi.co/api/v2/pokemon?limit=151')
    
    # Create lookup dictionaries
    types = {type_pkm.nombre: type_pkm for type_pkm in TypePkm.query.all()}
    moves = {move.nombre: move for move in Move.query.all()}
    abilities = {ability.nombre: ability for ability in Ability.query.all()}
    
    for pokemon_entry in pokemon_data['results']:
        pokemon_detail = fetch_data(pokemon_entry['url'])
        
        pokemon = Pokemon(
            nombre=pokemon_detail['name'],
            hp=pokemon_detail['stats'][0]['base_stat'],
            attack=pokemon_detail['stats'][1]['base_stat'],
            defense=pokemon_detail['stats'][2]['base_stat'],
            special_attack=pokemon_detail['stats'][3]['base_stat'],
            special_defense=pokemon_detail['stats'][4]['base_stat'],
            speed=pokemon_detail['stats'][5]['base_stat'],
            weight=pokemon_detail['weight'] / 10  # Convert to kg
        )
        
        # Add types
        for type_info in pokemon_detail['types']:
            type_name = type_info['type']['name']
            if type_name in types:
                pokemon.types.append(types[type_name])
        
        # Add moves (only gen 1 moves)
        for move_info in pokemon_detail['moves']:
            move_name = move_info['move']['name']
            if move_name in moves:
                pokemon.moves.append(moves[move_name])
        
        # Add abilities
        for ability_info in pokemon_detail['abilities']:
            ability_name = ability_info['ability']['name']
            if ability_name in abilities:
                pokemon.abilities.append(abilities[ability_name])
        
        db.session.add(pokemon)
    
    db.session.commit()
    print("Pokemon seeded successfully!")

def seed_db():
    """Main function to seed the database"""
    with app.app_context():
        print("Starting database seeding...")
        
        # Clear existing data
        Move.query.delete()
        Ability.query.delete()
        Pokemon.query.delete()
        TypeMove.query.delete()
        TypePkm.query.delete()
        db.session.commit()
        
        # Seed in order of dependencies
        seed_pokemon_types()
        seed_move_types()
        seed_moves()
        seed_abilities()
        seed_pokemon()
        
        print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_db()