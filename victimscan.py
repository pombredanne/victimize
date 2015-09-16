#!/usr/bin/env python2

import subprocess

args = ['java', '-jar', '/usr/bin/victims-client-1.0-SNAPSHOT-standalone.jar', '--verbose']


# Victims scan for jar file
def jarScan(jarfile_by_location):
	args_j = args[:]
	args_j.append(jarfile_by_location)
	try:
		jar_output = subprocess.check_output(args_j, stderr=subprocess.STDOUT)
		print(jar_output)
	except subprocess.CalledProcessError:
		print("Error in updating Victims")

# Victims scan for directory
def dirScan(dir_location):
	args_d = args[:]
	args_d.append('--recursive')
	args_d.append(dir_location)
	try:
		dir_output = subprocess.check_output(args_d, stderr=subprocess.STDOUT)
		print(dir_output)
	except subprocess.CalledProcessError:
		print("Error in scanning directory ")

# Victims scan for pom.xml
# This is no different from jarScan but is being created for convenience
# pomScan is for taking only pom.xml as input and nothing else. So this call
def pomScan(pomfile_by_location):
	args_p = args[:]
	args_p.append(pomfile_by_location)
	try:
		update_output = subprocess.check_output(args_p, stderr=subprocess.STDOUT)
		print(update_output)
	except subprocess.CalledProcessError:
		print("Error in Scanning pom.xml")

# Update Victims database
# Call update as required so that it's easier to update before a scan or update after a duration
def updateVictims():
	args_u = args[:]
	args_u.append('--update')
	try:
		update_output = subprocess.check_output(args_u, stderr=subprocess.STDOUT)
		print(update_output)
	except subprocess.CalledProcessError:
		print("Error in updating Victims")
		
