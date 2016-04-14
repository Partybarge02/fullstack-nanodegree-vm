-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--Create the database tournament:

drop database if exists tournament;
create database tournament;
--connects to the tournament database, drops connection to previous database
\c tournament; 

--Create tournament database tables:

--Table Players - players id and fullname:

create table Players(
	player_id serial primary key,
	full_name text);

--A match has an id, and the id of a winner and a loser (which 
--have a foreign key constraint to Players)

create table Matches(
	match_id serial primary key,
	winner_id integer references players(player_id),
	loser_id integer references players(player_id));




