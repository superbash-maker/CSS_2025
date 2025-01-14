# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:45:58 2025

@author: user-pc
"""

import requests as req
import os

# Create a folder for the bioact
try:
    os.mkdir("bioact")
except FileExistsError:
    pass

# Define the URL of the .gov webpage
base = 'https://phytochem.nal.usda.gov'

# Change range according to first and last entry of webpage search
for bio in range(1, 21):
    compurl = "/biological-activities-chemicals-csv-export/"+str(bio)+"/all?page&_format=csv"
    # Send a GET request to the webpage
    res = req.get(base+compurl)
    if os.path.isfile("bioact/"+str(bio)+".csv"):
        print(str(bio)+" already downloaded")
    else:
        csv = open("bioact/"+str(bio)+".csv","wb")
        csv.write(res.content)
        csv.close()
        print("Downloading "+str(bio))
