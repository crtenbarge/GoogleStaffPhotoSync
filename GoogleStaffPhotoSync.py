## Photos must be in an online folder and the photo must be named using the user email 
## addresses with a ".jpg" after. If PNG files are used, please change this lin line 22.
## Please set the url to the online directory in line 25


#Notice name of csv must be userEmails.csv. This can be changed in lines 9 and 13


import csv
import os


bashCommandQ = 'alias gam="python ~/gam/gam.py"'
os.system(bashCommandQ)
bashCommandX = 'python ~/gam/gam.py print users suspended > userEmails.csv'
os.system(bashCommandX)

#open the csv
with open('userEmails.csv', 'rb') as f:
    reader = csv.reader(f)
    print 'Lets get this party started!'
    for row in reader:
		bashCommandZ = 'python ~/gam/gam.py user %s update photo http://cdn.lssd.org/staff/%s.jpg' % (row[0], row[0])
		os.system(bashCommandZ)			
    print 'Sync complete'
