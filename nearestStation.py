#!/usr/bin/python

import sys
import json
import urllib
import math
import philly_location_find

url = urllib.urlopen('http://www3.septa.org/hackathon/Stops/?req1=23') 
json_parse = json.loads(url.read().decode('utf-8')) # load the url and decode it
from pprint import pprint #print on pretty format

philly = philly_location_find.getLoc() #import the data from philly_location_find

distances = {} # dictionary created to store the value name
count = 0 
for i in json_parse:
	lat = i['lat'] # store all the value of latitude
	lng = i['lng'] #store all the value of longitude
	
	d = (((philly[0] - lat) ** (2)) + ((philly[1] - lng) ** 2)) # used (x2-x1)^2 + (y2-y1)^2 
	#to measure the distance and did the square root of measured distance. 	
	distance = math.sqrt(d)
	# stores key and value of the distance so that we can retrive the information later. 
	distances[distance] = count
	count = count + 1
	#for key, value in i.items():
		#distance[key] = value
	#	distance[dictances[i]] = distance[i]
values = sorted(distances, reverse=True) #sort the values in ascending order  

#check wheter any optional argument is provided while running the code.
if len(sys.argv) < 2 :
	for i in range(5): #if no argument provided will print the first five nearest stop information
		result=(json_parse[distances[values[i]]])
		dis = values[i]
		print dis, result['stopname'], (result ['lat'], result['lng'])
else : #if provide then will provide the information according to the optional argument provided.
	argument = sys.argv[1]	
	required_int = argument.split("n") # split the first argument.	
	for j in range(int(required_int[1])):	#takes just the part after -n
		result = (json_parse[distances[values[j]]])
		dis = values[j] # stores value of distance
		#print distance, stopname, latitude and longitude
		print dis, result['stopname'], (result ['lat'], result['lng'])
#Note: Example:  "python findStops.py -n10" will give 10 nearest septa stops information.
