import csv
import sys
import time
import os
import re

listaks = []
listaks2=[]

def ApriCSVinDict(f):
        with open(f,'r',encoding='utf-8-',newline='') as csvf:
                csv_reader = csv.reader(csvf)
                for line in csv_reader:
                        listaks.append(line[0])
                ScanPasted()

def ScanPasted():
        x = input()
        if(x =="StopAll"):
                sys.exit
        elif(x !=""):
                i=0
                length = len(listaks)-1
                while i <=  len(listaks)-1:
                        if(re.search(rf"\b{str(listaks[i])}\b", x, re.IGNORECASE)):
                                i+=1
                                pass
                        else:
                                listaks2.append(listaks[i])
                                i+=1
                                pass
                savefile()

        else:
                print("non hai incollato nessun valore")

def savefile():
        with open('Raccolta KS da inserire.txt','w') as txtf:
                txtf.closed
        for line in listaks2:
                with open('Raccolta KS da inserire.txt','a') as txtf:
                        txtf.write(line)
                        txtf.write("\n")
                        txtf.closed
        sys.exit
                
                
        
for f in os.scandir():
        if (f.name.endswith(".csv")):
                ApriCSVinDict(f)

