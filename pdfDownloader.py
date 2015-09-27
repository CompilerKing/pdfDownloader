__author__ = 'Samuel Decanio'

import urllib
import urllib2
import re

#finding all the links on the webpage
webpageName = raw_input("Enter webpage: ")
webpage = urllib2.urlopen(webpageName)

html = webpage.read()

print "Looking for links..."
#this regex is based on the know naming convention for the webpage
#I created this for
pdfLinks = re.findall('[E].*\.pdf', html)

savePath = raw_input("Please enter your save path: ")

print "Attempting to download links now..."
count = 1
for i in pdfLinks:
    urllib.urlretrieve(webpageName+i, savePath+ "/" + i)
    count+=1

print "Finished downloading links..."
print "Downloaded: ", count - 1