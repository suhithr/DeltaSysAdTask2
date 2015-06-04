#!/usr/bin/python
#make sure the script is executable
import sys
import os

location = sys.argv[1];

#Script 1 is created
def buildDB():

	code = '''\
#!/usr/bin/python
import MySQLdb
con = MySQLdb.connect(host="localhost", user="user", passwd="user")
cursor = con.cursor()
sql = 'CREATE DATABASE IF NOT EXISTS d4'
cursor.execute(sql)
sql = "USE d4"
cursor.execute(sql)
sql = "CREATE TABLE IF NOT EXISTS theTable (now TINYTEXT)"
cursor.execute(sql)
'''
	print code
	f = open(location + 'build.py', 'w')
	f.write(code)
	os.system('chmod a+x ' + location + 'build.py')
	f.close

#Script 2 is created
def addTime():
	code = '''\
#!/usr/bin/python
import MySQLdb
import time
con = MySQLdb.connect(host="localhost", user="user", passwd="user")
cursor = con.cursor()
sql = "USE d4"
cursor.execute(sql)
now = time.strftime("%H:%M:%S")
sql = 'INSERT INTO theTable (now) VALUES (%s)'
cursor.execute(sql, (now))
con.commit()
'''
	f = open(location + 'addTime.py', 'w')
	f.write(code)
	os.system('chmod a+x ' + location + 'addTime.py')
	f.close

writeCron = 'echo' + ' "*/10 * * * * /usr/bin/python ' + location + 'addTime.py" '
command = '(crontab -l;' + writeCron +')| crontab -'
os.system(command)