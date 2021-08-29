#!/usr/bin/python3.6
#parses the planets.csv file
import os
import csv

filename = "/home/bob/scripts/textfiles/planets.txt"

with open(filename,'r') as csv_file:
	readContents= csv_file.readlines()
	#print(readContents)
	for line in readContents:
		print(line,end='')
		print(line.split(", - "))

print("++++++++")	
print("finished")
