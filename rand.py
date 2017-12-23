#!/usr/bin/python
# A script to retrive the random numbers from the www.random.org webpage
# The HTTP api are given from the random.org website.

import urllib.request

fhand = urllib.request.urlopen('https://www.random.org/integers/?num=25&min=1&max=400&col=1&base=10&format=plain&rnd=new')
f = open("random.txt","w+")
f.write("The random numbers are:")
for line in fhand:
 print(int(line.strip()))
# The random numbers are added to the random.txt file during the execution of the code 
 f= open("random.txt","a")
 f.write("%d " %(int(line.strip())))
 f.close()
