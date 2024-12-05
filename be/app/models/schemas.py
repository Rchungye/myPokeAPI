from marshmallow import Schema, fields

class TypePkmSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)

class MoveSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)

class AbilitySchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)

class PokemonSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    sprite = fields.Str(required=True)
    types = fields.Nested(TypePkmSchema, many=True)
    moves = fields.Nested(MoveSchema, many=True)
    abilities = fields.Nested(AbilitySchema, many=True)