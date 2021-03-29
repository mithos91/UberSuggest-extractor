import csv
import sys
import time
import os

dumpfolder = "_dumphere"
outputfolder = "_Output"

#Lists tool

listanalyzer = [
        'backlink-profile',
        'download'
        ]

bllistoutput =[
        'Data',
        'Source Domain',
        'Source URL',
        'Target URL',
        'Anchor Text',
        'Status',
        'REL',
        'Auth',
        'Trust',
        'Stability',
        'Opportunity',
        'Traffic'
        ]
blcoutnelist=[
        'Targeted Link',
        'Occurencies'
        ]
blauthaggl = [
        'Domain',
        'Auth',
        'Trust',
        'Stability',
        'Opportunity',
        'Traffic'
        ]
dizionariobl = {}
dizionariobl2 ={}

globalcounter = 0

####
#def
####
def extract_bl_bottom(f):
        global globalcounter
        with open(f.path,'r',encoding='utf-8-sig') as csvf:
                temp_reader = csv.reader(csvf)
                headers = False
                for line in temp_reader:
                        if(headers == False):
                                headers=True
                        else:
                                dizionariobl.update({globalcounter:{}})
                                counter = 0
                                if(len(line)>1):
                                        sums = line[0] + line[1]
                                        for subline in sums.split(';'):
                                                subline.replace('"','')
                                                if(subline == ""):
                                                        print("found")
                                                dizionariobl[globalcounter].update({
                                                        bllistoutput[counter] : subline
                                                        })
                                                counter +=1
                                        globalcounter +=1                                       
                                else:
                                        for subline in line[0].split(';'):
                                                subline.replace('"','')
                                                if(subline == ""):
                                                        print("found")
                                                dizionariobl[globalcounter].update({
                                                        bllistoutput[counter] : subline
                                                        })
                                                counter +=1
                                        globalcounter +=1
                csvf.closed

def extract_bl_top(f):
        with open(f.path,'r',encoding='utf-8-sig') as csvf:
                temp_reader= csv.reader(csvf)
                temp_list = []
                header= False
                for line in temp_reader:
                        counter = 0                        
                        if(header == False):
                                header = True
                        else:
                                for char in line[0].split('\t'):
                                        if(counter == 0 or counter == 5 or counter == 6 or counter == 7 or counter == 8 or counter == 9):
                                                temp_list.append(char)
                                                counter += 1
                                        else:
                                                counter += 1
                                dizionariobl2.update({
                                        temp_list[0] : {
                                                blauthaggl[1] :  temp_list[1],
                                                blauthaggl[2] : temp_list[2],
                                                blauthaggl[3] : temp_list[3],
                                                blauthaggl[4] : temp_list[4],
                                                blauthaggl[5] : temp_list[5]                                                
                                                }
                                        })
                                temp_list=[]

                
def printcsvbl():
        with open(outputfolder + "/bl_output.csv",'w',encoding='utf-8-sig',newline='') as csvf:
                temp_writer = csv.writer(csvf)
                temp_writer.writerow(bllistoutput)
                for line in dizionariobl:
                        temp_writer.writerow([
                                dizionariobl[line][bllistoutput[0]],
                                dizionariobl[line][bllistoutput[1]],                                
                                dizionariobl[line][bllistoutput[2]],
                                dizionariobl[line][bllistoutput[3]],
                                dizionariobl[line][bllistoutput[4]],
                                dizionariobl[line][bllistoutput[5]],
                                dizionariobl[line][bllistoutput[6]],
                                dizionariobl2[str(dizionariobl[line][bllistoutput[1]]).replace('"','')][blauthaggl[1]],
                                dizionariobl2[str(dizionariobl[line][bllistoutput[1]]).replace('"','')][blauthaggl[2]],
                                dizionariobl2[str(dizionariobl[line][bllistoutput[1]]).replace('"','')][blauthaggl[3]],
                                dizionariobl2[str(dizionariobl[line][bllistoutput[1]]).replace('"','')][blauthaggl[4]],
                                dizionariobl2[str(dizionariobl[line][bllistoutput[1]]).replace('"','')][blauthaggl[5]]
                                ])
                csvf.closed
        print("apertura, scrittura e chiusura avvenuta con successo")
        time.sleep(1)
        
        
def printblcounter():
        dictcounter= {}
        listcounter = []
        counter = 0
        while counter < len(dizionariobl):
                tempvoc = str(dizionariobl[counter]['Target URL']).replace('"','')
                listcounter.append(tempvoc)
                counter += 1
        for item in listcounter:
                if(item in dictcounter):
                        dictcounter[item] += 1
                else:
                        dictcounter[item] = 1
        with open(outputfolder + "/bl_counter.csv",'w',encoding='utf-8-sig',newline='') as csvf:
                temp_writer = csv.writer(csvf)
                temp_writer.writerow(blcoutnelist)
                #mette ordine in dizionario boh
                res = {val[0] : val[1] for val in sorted(dictcounter.items(), key = lambda x: (-x[1], x[0]))}
                dict(sorted(dictcounter.items(), key=lambda item: item[1]))
                for value in res:
                        temp_writer.writerow([
                                value,
                                dictcounter[value]
                                ])
        



####
#code
####


#create folder if doesn't exists
if(os.path.exists(dumpfolder)):
        pass
else:
        os.mkdir(dumpfolder)
        print("cartella dump non presente. Creazione in corso")
if(os.path.exists(outputfolder)):
        pass
else:
        os.mkdir(outputfolder)
        print("cartella output non presente. Creazione in corso")

#if no csv in dumpfolder
counter= 0
print("cerco file .csv")
for f in os.scandir(dumpfolder):
        if(f.name.endswith(".csv")):
                counter += 1

if(counter == 0):
        print("Non ci sono file nella cartella _dumphere")
        print("")
        print("")
        input("Chiusura forzata. Inserisci i files e riprova")
        sys.exit()

#scan all csv in dumpfolder
if(counter >0):
        for f in os.scandir(dumpfolder):
                if(f.name.endswith(".xls") and listanalyzer[0] in f.name):
                        extract_bl_top(f)
                elif(f.name.endswith(".csv") and listanalyzer[1] in f.name):
                        extract_bl_bottom(f)
                else:
                        print("Non riconosco questo file -- : " + f.name)
                        pass
else:
        print("Non ho trovato file da analizzare.")
        print("Aggiungi file csv nella cartella _dumphere e fai ripartire il programma")
        input("premi enter per chiudere")
        sys.exit()

time.sleep(1)
printcsvbl()
printblcounter()
