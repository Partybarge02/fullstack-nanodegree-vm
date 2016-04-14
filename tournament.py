#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database dbconnect."""
    dbconnect =  psycopg2.connect("dbname=tournament")
    cursor = dbconnect.cursor()
    return dbconnect, cursor

def deleteMatches():
    """Remove all the match records from the database."""
    dbconnect, cursor = connect()
    cursor.execute("DELETE FROM matches;")
    dbconnect.commit()
    dbconnect.close()

def deletePlayers():
    """Remove all the player records from the database."""
    dbconnect, cursor = connect()
    cursor.execute("DELETE FROM Players;")
    dbconnect.commit()
    dbconnect.close()

def countPlayers():
    """Returns the number of players currently registered."""    
    dbconnect, cursor = connect()
    cursor.execute("SELECT count(*) FROM Players;")
    count = cursor.fetchone()[0]
    dbconnect.close()
    return count
 
def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    clean_name = bleach.clean(name,)
    dbconnect, cursor = connect()
    cursor.execute ("INSERT INTO Players (full_name) VALUES (%s)", (clean_name,))
    dbconnect.commit()
    dbconnect.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    dbconnect, cursor = connect()
    cursor.execute("SELECT Players.player_id, players.full_name, " +
                   "(SELECT COUNT(*) FROM Matches WHERE winner_id = Players.player_id) AS wins, " +
                   "(SELECT COUNT(*) FROM Matches WHERE winner_id = Players.player_id OR loser_id = Players.player_id) " +
                   "FROM Players " +
                   "ORDER BY wins DESC;")
    rankings = cursor.fetchall()
    dbconnect.close()
    return rankings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    dbconnect, cursor = connect()
    cursor.execute ("INSERT INTO Matches (winner_id, loser_id)VALUES(%s,%s)",(winner, loser))
    dbconnect.commit()
    dbconnect.close()
 
def swissPairings():
    """Returns a list of match_pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the rankings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    dbconnect, cursor = connect()
    rankings = playerStandings()
    match_pairs = []
    for id in range(0,len(rankings)-1,2):
        pair = (rankings[id][0],rankings[id][1],rankings[id+1][0],rankings[id+1][1])
        match_pairs.append(pair)
    dbconnect.close()
    return match_pairs

