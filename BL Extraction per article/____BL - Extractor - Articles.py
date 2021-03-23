import csv
import json
import os
import re
import sys
import time
import operator

#define and create folder for output
folderoutput = "_output"

if not os.path.exists(folderoutput):
        os.mkdir(folderoutput)

#create CSV files if not exist
dictallfiles = {"0":"extracted_bl"}
#ask if overwrite
wannacancel = input("Sovrascrivere se ci sono dei file? y/n ")
for dictfiles in dictallfiles:
        if not os.path.exists(folderoutput + "/" + dictallfiles[dictfiles] + ".csv"):
               with open(folderoutput + "/" + dictallfiles[dictfiles] + ".csv","w") as newfile:
                       newfile.closed
        elif os.path.exists(folderoutput + "/" + dictallfiles[dictfiles] + ".csv"):
                if(wannacancel == "y"):
                        os.remove(folderoutput + "/" + dictallfiles[dictfiles] + ".csv")
                        print(dictallfiles[dictfiles] + ".csv - Rimosso")
                elif(wannacancel =="n"):
                        print("ok... fermo il processo")
                        sys.exit()
                else:
                        print('ops... tasto sbagliato, usa "y" o "n"')
                        sys.exit()
                        break

print("Caricamento...")
time.sleep(1)

#global list for dict building
dictbuilding = [
        "Link Sorgente",
        "Titolo Pagina",
        "Target Url",
        "Anchor Text",
        "Prima Apparizione",
        "Ultima Apparizione",
        "Domain Auth",
        "Page Auth"
        ]

#global dictionaries
newdict = {}











#CODE START


#--------------------------------------|#--------------------------------------|
#FUNCTION 01: Check all csv dumped here
#--------------------------------------|#--------------------------------------|

def FileScraper():
        with os.scandir() as p:
                for file in p:
                        if(file.name.endswith(".csv")):                                
                                Renamer(file)
        with os.scandir() as p:
                for file in p:
                        if(file.name.endswith(".csv")):
                                MergeAllData(file)
        Printer()
                        
#--------------------------------------|#--------------------------------------|
#FUNCTION 02: Open CSV, Check owner then change CSV name
#--------------------------------------|#--------------------------------------|
def Renamer(file):
        with open(file.path,'r',encoding="utf-8",newline="") as csvf:
                temp_reader = csv.reader(csvf)
                counter = 0
                renamer = ""
                for ln in temp_reader:
                        if(counter !=1):
                                counter +=1
                        elif(counter ==1):
                                renamer = ln[3]
                                renamer = renamer[2:]
                                renamer = renamer.replace("/","¬")
                                counter +=1
                                #restart reader otherwise will start from line 3
                                csvf.seek(0)
                                print(renamer)
                                break

                if not(os.path.exists(renamer + ".csv")):
                        with open(renamer + ".csv",'w',encoding="utf-8",newline="") as csvf2:                        
                                temp_writer = csv.writer(csvf2)                                
                                for line in temp_reader:
                                        print(line)
                                        temp_writer.writerow(line)
                                csvf2.closed
                else:
                        print("File: " + renamer + ".csv exists")

                csvf.closed
        if not "¬" in file.path:
                os.remove(file.path)

#--------------------------------------|#--------------------------------------|
#FUNCTION 03: Merge all data in a single dictionary
#--------------------------------------|#--------------------------------------|
def MergeAllData(file):
        with open(file,'r',encoding='utf-8', newline='') as csvf2:
                temp_reader = csv.reader(csvf2)
                counter = 0
                for line in temp_reader:
                        if(counter == 0):
                                counter = 1
                        else:
                                newdict.update({
                                        line[2] : {
                                                dictbuilding[1] : line[1],
                                                dictbuilding[2] : line[3],
                                                dictbuilding[3] : line[7],
                                                dictbuilding[4] : line[8],
                                                dictbuilding[5] : line[9],
                                                dictbuilding[6] : line[4],
                                                dictbuilding[7] : line[5]                                              
                                                }
                                        })

#--------------------------------------|#--------------------------------------|
#FUNCTION 03: Print all in one CSV
#--------------------------------------|#--------------------------------------|                        
                        
def Printer():
        with open(folderoutput + "/" + dictallfiles[dictfiles] + ".csv",'w',encoding='utf-8',newline='') as csvf:
                temp_writer = csv.DictWriter(csvf,fieldnames=dictbuilding)        
                for line in newdict:
                        temp_writer.writerow({
                                dictbuilding[0] : line,
                                dictbuilding[1] : newdict[line][dictbuilding[1]],
                                dictbuilding[2] : newdict[line][dictbuilding[2]],
                                dictbuilding[3] : newdict[line][dictbuilding[3]],
                                dictbuilding[4] : newdict[line][dictbuilding[4]],
                                dictbuilding[5] : newdict[line][dictbuilding[5]],
                                dictbuilding[6] : newdict[line][dictbuilding[6]],
                                dictbuilding[7] : newdict[line][dictbuilding[7]]
                                })
        with open(folderoutput + "/" + dictallfiles[dictfiles] + ".csv",'r',encoding='utf-8',newline='') as csvf:
                temp_reader = csv.reader(csvf)
                sort_reader = sorted(temp_reader, key = lambda x: int(x[6]),reverse = True)
                print(sort_reader)
                with open(folderoutput + "/" + dictallfiles[dictfiles] + ".csv",'w',encoding='utf-8',newline='') as csvf2:
                        temp_writer = csv.writer(csvf2)
                        temp_writer.writerow(dictbuilding)
                        for line in sort_reader:
                                temp_writer.writerow(line)
                
                
        print('end')
        
        
                        

FileScraper()
