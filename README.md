# DeltaSysAdTask2
Task 2 of Delta Inductions for System Administrator 2015
##Usage:
$./spawn.py location

##What it does:
Creates a script to create a database with a single column, and creates another script to insert the system time into that column.
Creates a cron job to run the second script (inserting the time) every 10 minutes on the user's cron file.

##Note: Make sure spawn.py is set to executable

##Dependencies:

os

sys

time

MySQLdb

You need mysql installed.
