#!/usr/bin/env python2

import os
import magic
from validfile import validateFile
from victimscan import dirScan, jarScan, pomScan, updateVictims


# Instance to extract file mime type - Python-magic library
file_by_mime = magic.Magic(mime=True)

def update():
	updateVictims()

def initiateScan(path_holder):
	
	# Check if the argument is a file
	#If a file and jar, war or ear, or pom.xml run victims on the file
	if os.path.isfile(path_holder) and java_archivetype(path_holder):
		# Perform victims scan on a jar file
		jarScan(path_holder)

	# Check if the argument passed in a 
	elif os.path.isdir(path_holder):
		# Scan  the directory with victims recursively for CVE
		dirScan(path_holder)
	elif pom_filetype(path_holder):
		#Scan the pom.xml for CVEs
		pomScan(path_holder)

	# Error with scan or user params
	else:
		print("[-] Error occured with scan or user input")

def java_archivetype(file_to_check):
	
	file_in_question = file_to_check
	
	# If the file is a compressed file zip, gz, jar, war, ear we are accepting the file
	
	# Check for type compressed or type jar
	if (file_by_mime.from_file(file_in_question) == 'application/zip' or
		file_by_mime.from_file(file_in_question) == 'application/jar'):
		print("Acceptable MIME Type")
		return True
	
	else:
		print("Jar file or a binary?! Something's not right with the scanner")
		return False

def pom_filetype(file_to_check):

	file_in_question = file_to_check
	# Examining pom.xml seperately - to quickly call dependency-check or maven if needed
	if (file_by_mime.from_file(file_in_question) == 'text/plain' or 
		file_by_mime.from_file(file_in_question) == 'application/xml'):
		print("probably a text file or xml file")
		# From validfile.py -- part of reason -- reuse of a function
		return validateFile(file_in_question)
		
	else:
		print("pom.xml is invalid OR something is wrong")
		return False

