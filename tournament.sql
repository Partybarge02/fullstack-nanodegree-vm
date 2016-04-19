-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--Create the database tournament:

DROP DATABASE if exists tournament;
CREATE DATABASE tournament;
--connects to the tournament database, drops connection to previous database
\c tournament; 

--Create tournament database tables:

--Table Players - players id and fullname:

CREATE TABLE Players(
	player_id SERIAL PRIMARY KEY,
	full_name TEXT);

--A match has an id, and the id of a winner and a loser (which 
--have a foreign key constraint to Players)

CREATE TABLE Matches(
	match_id SERIAL PRIMARY KEY,
	winner_id INTEGER REFERENCES players(player_id),
	loser_id INTEGER REFERENCES players(player_id));




