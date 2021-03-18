import csv
import json
import os
import re
import sys

#define and create folder for output
folderoutput = "_output"

if not os.path.exists(folderoutput):
        os.mkdir(folderoutput)

#create JSONs files if not exist
dictallfiles = {"0":"extracted_ks","1":"extracted_bl","2":"extracted_top_pages"}
wannacancel = input("Vuoi sovrascrivere i dati? y/n ")
for dictfiles in dictallfiles:
        if not os.path.exists(folderoutput + "/" + dictallfiles[dictfiles] + ".json"):
                open(folderoutput + "/" + dictallfiles[dictfiles] + ".json","w")
        elif(wannacancel == "y"):
                open(folderoutput + "/" + dictallfiles[dictfiles] + ".json","w")
                print("file " + dictallfiles[dictfiles] + ".json" + " sovrascritto")
        elif(wannacancel =="n"):
                print("ok... fermo il processo")
                sys.exit()
        else:
                print('ops... tasto sbagliato, usa "y" o "n"')
                sys.exit()
                break

#counters
folders = 0
global kscounter,blcounter,tgcounter
kscounter,blcounter,tgcounter = 0,0,0

#global dictionaries
ksdict = {}
bldict = {}
tgdict = {}

#CODE START

#create dictionary in output then for each file in folder,
#check name and start specific routines     
def combinestart(foldername, folderpath):

        #============================
        #check file name wildcard   #
        #============================
        
        for file in os.scandir(folderpath):
                if(re.search("ubersuggest.",str(file.name))):
                        extract_ks(file)                        
                elif(re.search("backlink.",str(file.name))):
                        extract_bl(file)
                elif(re.search("top_pages.",str(file.name))):
                        extract_top_pages(file)


#--------------------------------------|
#--------------------------------------|
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
                                "Volume" : rows["Volume"],
                                "SEO Difficulty" : rows["SEO Difficulty"]
                                        }
                      
        #counter
        kscounter += 1
        #open JSON writer the json.dumps()
        if(kscounter==folders):
                with open(folderoutput + "/" + dictallfiles["0"] + ".json","a", encoding="utf-8") as jsonf:
                        jsonf.write(json.dumps(ksdict,indent=4))


#--------------------------------------|
#--------------------------------------|
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
                                "Domain Auth" : rows["Domain Authority"],
                                "Page Auth" : rows["Page Authority"],
                                "Target URL" : rows["Target URL"],
                                "Anchor Text" : rows["Anchor Text"]
                                }
                        
        blcounter += 1
        #open JSON writer the json.dumps()
        if(blcounter == folders):
                with open(folderoutput + "/" + dictallfiles["1"] + ".json","a", encoding="utf-8") as jsonf:
                        jsonf.write(json.dumps(bldict,indent=4))


#--------------------------------------|
#--------------------------------------|
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
                                "Est. Visits" : rows["Est. Visits"],
                                "Backlinks" : rows["Backlinks"],
                                "Facebook Shares" : rows["Facebook Shares"],
                                "Pinterest Shares" : rows["Pinterest Shares"]
                                }
                        
        tgcounter += 1
        #open JSON writer the json.dumps()
        if(tgcounter == folders):
                with open(folderoutput + "/" + dictallfiles["2"] + ".json","a", encoding="utf-8") as jsonf:
                        jsonf.write(json.dumps(tgdict,indent=4))





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
                print("Found Routine = " + entry.name)
        else:
                combinestart(entry.name,entry.path)
                
#--------------------------------------|#--------------------------------------|
#CODE: convert JSON into CSV
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
                                                                      'Est. Visite' : tempjson[key]["Est. Visits"],
                                                                      'Backlinks' : tempjson[key]["Backlinks"],
                                                                      'Facebook Shares' : tempjson[key]["Facebook Shares"],                                                                      
                                                                      'Pinterest Shares' : tempjson[key]["Pinterest Shares"]})
                        #rimuovi il JSON non serve piu'
                        os.remove(file)

                else:
                        print("Qualcosa e' andato storto?")

print("Processo completato")


                            
                        


