# Swiss Tournament Results Project:

## Project Specification:

Developed a database schema to track player standings as a Swiss style tournament progresses.
Used Python code to interact with the database to pair and rank players in the tournament.

## Prerequisites:

1.Latest version of Vagrant and Virtual Box that was provided in the course.
2.Python >2.7 and <3.0.


## Files Included:

tournament.sql  - this file is used to set up your database schema (the table representation 
of your data structure).

tournament.py - this file is used to provide access to your database via a library of functions   which can add, delete or query data in your database to another python program (a client program). Remember that when you define a function, it does not execute, it simply means the function is defined to run a specific set of instructions when called.

tournament_test.py - this is a client program which will use your functions written in the tournament.py module. We've written this client program to test your implementation of functions in tournament.py


## How to Run the Project:

1. To use Vagrant
	- Open a Git-Bash Terminal in Admin Mode 
	- Dana@DANA-PC~ @ $ type
	$ cd fullstack/vagrant
	- Type `vagrant up` to power up VM
2. Login to Vagrant VM
	- Type `vagrant ssh` (this logs you in)
	- `vagrant@vagrant-ubuntu-trusty-32:~$
3. Change to the correct folder:
	- Type:
		`vagrant@vagrant-ubuntu-trusty-32:~$`cd vagrant/tournament`
4. Run the tests
	- `vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$`
	- At $ type python `tournament_test.py`

## Results expected from `tournament_test.py`:

You should be able to see the following output once all your tests have passed:
`vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py`
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!

## Licence:

Partybarge LLC
