create database mypokeapi;
use mypokeapi;


select * from ability;
select * from move;
select * from pokemon;
select * from type_pkm;
select * from type_move;
select * from pokemon_ability;
select * from pokemon_move;
select * from pokemon_type;

select * from pokemon_move where pokemon_id = 6;
select * from pokemon_type where pokemon_id = 6;
select * from type_pkm where id = 3;
select * from type_pkm where id = 10;
select * from pokemon_type where type_pkm_id = 40;


DROP TABLE IF EXISTS ability;
DROP TABLE IF EXISTS move;
DROP TABLE IF EXISTS pokemon;
DROP TABLE IF EXISTS type_pkm;
DROP TABLE IF EXISTS type_move;
DROP TABLE IF EXISTS pokemon_ability;
DROP TABLE IF EXISTS pokemon_move;
DROP TABLE IF EXISTS pokemon_type;


SET SQL_SAFE_UPDATES = 0;
SET SQL_SAFE_UPDATES = 1;
DELETE FROM pokemon_type;
DELETE FROM ability;
DELETE FROM move;
DELETE FROM pokemon;
DELETE FROM type_pkm;
DELETE FROM type_move;
DELETE FROM pokemon_move;
DELETE FROM pokemon_type;

