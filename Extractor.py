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

#create JSONs files if not exist
dictallfiles = {"0":"extracted_ks","1":"extracted_bl","2":"extracted_top_pages"}

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
time.sleep(3)

#counters
folders = 0
global kscounter,blcounter,tgcounter
kscounter,blcounter,tgcounter = 0,0,0

#global dictionaries
ksdict = {}
bldict = {}
tgdict = {}











#CODE START


#--------------------------------------|#--------------------------------------|
#FUNCTION 01: Check if file name has this string then call appropriate function
#--------------------------------------|#--------------------------------------|


#create dictionary in output then for each file in folder,
#check name and start specific routines     
def combinestart(foldername, folderpath):
        for file in os.scandir(folderpath):
                if(re.search("ubersuggest.",str(file.name))):
                        extract_ks(file)                        
                elif(re.search("backlink.",str(file.name))):
                        extract_bl(file)
                elif(re.search("top_pages.",str(file.name))):
                        extract_top_pages(file)






#--------------------------------------|#--------------------------------------|
#FUNCTION 02: extract data from CSV into JSON
#--------------------------------------|#--------------------------------------|


#Extract ks from file then put in json
def extract_ks(file):
        global kscounter
        #open CSV reader by DictReader
        with open(file.path,encoding='utf-8-sig') as csvf:
                csvReader = csv.DictReader(csvf)
                #Convert into Dict and add it to data
                for rows in csvReader:
                        #assuming column "No" exists as primary key
                        key = rows["Keywords"]
                        ksdict[key] = {
                                "Volume" : int(rows["Volume"]),
                                "SEO Difficulty" : int(rows["SEO Difficulty"])
                                        }
                      
        #counter
        kscounter += 1
        #open JSON writer the json.dumps()
        if(kscounter==folders):
                with open(folderoutput + "/" + dictallfiles["0"] + ".json","a", encoding="utf-8") as jsonf:
                        jsonf.write(json.dumps(ksdict,indent=4))








#Extract bl from file then put in json
def extract_bl(file):
        global blcounter
        #open CSV reader by DictReader
        with open(file.path,encoding='utf-8-sig') as csvf:
                csvReader = csv.DictReader(csvf)

                #Convert into Dict and add it to data
                for rows in csvReader:
                        
                        #assuming column "No" exists as primary key
                        key = rows["Source URL"]
                        bldict[key] = {
                                "Source Page Title" : rows["Source Page Title"],
                                "Domain Auth" : int(rows["Domain Authority"]),
                                "Page Auth" : int(rows["Page Authority"]),
                                "Target URL" : rows["Target URL"],
                                "Anchor Text" : rows["Anchor Text"]
                                }
                        
        blcounter += 1
        #open JSON writer the json.dumps()
        if(blcounter == folders):
                with open(folderoutput + "/" + dictallfiles["1"] + ".json","a", encoding="utf-8") as jsonf:
                        jsonf.write(json.dumps(bldict,indent=4))








#Extract top pages from file then put in json        
def extract_top_pages(file):
        global tgcounter
        #open CSV reader by DictReader
        with open(file.path,encoding='utf-8-sig') as csvf:
                csvReader = csv.DictReader(csvf)

                #Convert into Dict and add it to data
                for rows in csvReader:
                        
                        #assuming column "No" exists as primary key
                        key = rows["URL"]
                        tgdict[key] = {
                                "Title" : rows["Title"],
                                "Est. Visits" : int(rows["Est. Visits"]),
                                "Backlinks" : int(rows["Backlinks"]),
                                "Facebook Shares" : int(rows["Facebook Shares"]),
                                "Pinterest Shares" : int(rows["Pinterest Shares"])
                                }
                        
        tgcounter += 1
        #open JSON writer the json.dumps()
        if(tgcounter == folders):
                with open(folderoutput + "/" + dictallfiles["2"] + ".json","a", encoding="utf-8") as jsonf:
                        jsonf.write(json.dumps(tgdict,indent=4))

#--------------------------------------|#--------------------------------------|
#FUNCTION 03: sort all CSV extracted by choosen column
#--------------------------------------|#--------------------------------------|

                        
def sorterone(filename,whichlinesort):
        with open(filename,"r",encoding="utf-8", newline='') as apri_csv:

                #definisci il nome del file temp giusto per comodita'
                tempname = folderoutput + "/temp.csv"
                
                if os.path.exists(tempname):
                        os.remove(tempname)
                
                #copia contenuto csv originale
                temp_csv = csv.reader(apri_csv)


                #loop
                counter = 0
                with open(tempname,"w",encoding="utf-8", newline='') as f:
                        temp_csv_for_sort = csv.writer(f)
                        for row in temp_csv:
                                if (counter == 0):
                                        counter += 1
                                        headers = row
                                else:
                                        temp_csv_for_sort.writerow(row)
                                
                        with open(tempname,"r",encoding="utf-8", newline='') as f:
                                temp_csv_for_sort = csv.reader(f)
                                temp_sorter = sorted(temp_csv_for_sort, key=lambda x:int(x[whichlinesort]), reverse=True)        
                        with open(filename,"w",encoding="utf-8", newline='') as f:
                                csv_temp_writer = csv.writer(f)
                                csv_temp_writer.writerow(headers)
                                for line in temp_sorter:
                                        csv_temp_writer.writerow(line)
                os.remove(tempname)



#--------------------------------------|#--------------------------------------|
#CODE 01: look for files in folders then call function to check by file name
#--------------------------------------|#--------------------------------------|



#loop for each folder
for entry in os.scandir():
        if(entry.name == folderoutput or entry.name.endswith(".py")):
                continue
        else:
                folders +=1
                
for entry in os.scandir():
        if(entry.name == folderoutput):
                print("Found Folder = " + entry.name)
        elif(entry.name.endswith(".py")):
                print("Found Routine - ignore file = " + entry.name)
        else:
                combinestart(entry.name,entry.path)

#--------------------------------------|#--------------------------------------|
#CODE 02: convert JSON into CSV
#--------------------------------------|#--------------------------------------|


for file in os.scandir(folderoutput):
        #usa solo i file JSON nella cartella
        if(file.name.endswith(".json")):

                #Procedi JSON to CSV per KS
                #suddividi e crea csv annessi
                if(file.name == dictallfiles["0"] + ".json"):                
                        with open(file.path) as jsonf:
                                tempjson = json.load(jsonf)
                                with open(folderoutput + "/" + dictallfiles["0"] + ".csv","w",encoding="utf-8", newline='') as apri_csv:
                                        nomecampi = ['Keyword', 'Volume' , 'SEO Difficulty']
                                        oggetto_csv = csv.DictWriter(apri_csv, fieldnames=nomecampi)
                                        oggetto_csv.writeheader()
                                        for key in tempjson.keys():
                                                oggetto_csv.writerow({'Keyword' : key,
                                                                      'Volume' : tempjson[key]["Volume"],
                                                                      'SEO Difficulty' : tempjson[key]["SEO Difficulty"]})
                        #rimuovi il JSON non serve piu'
                        os.remove(file)

                        #riapri il file per rimetterlo in ordine
                        sorterone(str(folderoutput+"/"+str(file.name).replace(".json","")+".csv"),1)


                #Procedi JSON to CSV per BL
                #suddividi e crea csv annessi                        
                elif(file.name == dictallfiles["1"] + ".json"):
                        with open(file.path) as jsonf:
                                tempjson = json.load(jsonf)
                                with open(folderoutput + "/" + dictallfiles["1"] + ".csv","w",encoding="utf-8", newline='') as apri_csv:
                                        nomecampi = ['Source Link','Source Page','Target URL','Anchor Text' , 'Domain Auth', 'Page Auth']
                                        oggetto_csv = csv.DictWriter(apri_csv, fieldnames=nomecampi)
                                        oggetto_csv.writeheader()
                                        for key in tempjson.keys():
                                                oggetto_csv.writerow({'Source Link' : key,
                                                                      'Source Page' : tempjson[key]["Source Page Title"],
                                                                      'Target URL' : tempjson[key]["Target URL"],
                                                                      'Anchor Text' : tempjson[key]["Anchor Text"],
                                                                      'Domain Auth' : tempjson[key]["Domain Auth"],
                                                                      'Page Auth' : tempjson[key]["Page Auth"]})
                        #rimuovi il JSON non serve piu'
                        os.remove(file)
                        #riapri il file per rimetterlo in ordine
                        sorterone(str(folderoutput+"/"+str(file.name).replace(".json","")+".csv"),4)

                #Procedi JSON to CSV per TG
                #suddividi e crea csv annessi
                elif(file.name == dictallfiles["2"] + ".json"):
                        with open(file.path) as jsonf:
                                tempjson = json.load(jsonf)
                                with open(folderoutput + "/" + dictallfiles["2"] + ".csv","w",encoding="utf-8", newline='') as apri_csv:
                                        nomecampi = ['Pagina', 'Titolo' , 'Est. Visite', 'Backlinks','Facebook Shares', 'Pinterest Shares']
                                        oggetto_csv = csv.DictWriter(apri_csv, fieldnames=nomecampi)
                                        oggetto_csv.writeheader()
                                        for key in tempjson.keys():
                                                oggetto_csv.writerow({'Pagina' : key,
                                                                      'Titolo' : tempjson[key]["Title"],
                                                                      'Est. Visite' : int(tempjson[key]["Est. Visits"]),
                                                                      'Backlinks' : tempjson[key]["Backlinks"],
                                                                      'Facebook Shares' : tempjson[key]["Facebook Shares"],                                                                      
                                                                      'Pinterest Shares' : tempjson[key]["Pinterest Shares"]})
                        #chiudi il file
                        apri_csv.closed
                        #rimuovi il JSON non serve piu'
                        os.remove(file)
                        #riapri il file per rimetterlo in ordine
                        sorterone(str(folderoutput+"/"+str(file.name).replace(".json","")+".csv"),2)
                                

                else:
                        print("Il file non deve essere analizzato")

print("Processo completato")


                            
                        


