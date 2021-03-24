import csv
import sys
import time
import os

dumpfolder = "_dumphere"
outputfolder = "_Output"

#Lists tool

listanalyzer = [
        'top_backlinks',
        'top_keywords'
        ]

bllistoutput = [
        'Source URL',
        'Source Page Name',
        'Target URL',
        'Domain Auth',
        'Page Auth',
        'Link Type',
        'Anchor Text',
        'First Seen',
        'Last Seen'       
        ]
kslistoutput =[
        'Ks',
        'Volume',
        'Position',
        'Est. Visits',
        'CPC',
        'Paid Difficulty',
        'SEO Difficulty',
        ]
dizionarioks = {}
dizionariobl = {}


####
#def
####
def extract_ks(f):
        with open(f.path,'r',encoding='utf-8-sig') as csvf:
                temp_reader = csv.reader(csvf)
                headers = False
                for line in temp_reader:
                        if(headers == False):
                                headers = True
                        else:
                                dizionarioks.update({
                                        line[1]:{
                                                kslistoutput[1] : line[2],
                                                kslistoutput[2] : line[3],
                                                kslistoutput[3]: line[4],
                                                kslistoutput[4]: line[5],
                                                kslistoutput[5]: line[6],
                                                kslistoutput[6]: line[7],
                                                }
                                         }
                                        )
                csvf.closed
                
def extract_bl(f):
        with open(f.path,'r',encoding='utf-8-sig') as csvf:
                temp_reader = csv.reader(csvf)
                headers = False
                for line in temp_reader:
                        if(headers == False):
                                headers = True
                        else:
                                dizionariobl.update({
                                        line[2]:{
                                                bllistoutput[1] : line[1],
                                                bllistoutput[2] : line[3],
                                                bllistoutput[3]: line[4],
                                                bllistoutput[4]: line[5],
                                                bllistoutput[5]: line[6],
                                                bllistoutput[6]: line[7],
                                                bllistoutput[7]: line[8],
                                                bllistoutput[8]: line[9]                                                
                                                }
                                         }
                                        )
                print(dizionariobl)
                csvf.closed

def printcsvks():
        with open(outputfolder + "/ks_output.csv",'w',encoding='utf-8-sig',newline='') as csvf:
                temp_writer = csv.writer(csvf)
                temp_writer.writerow(kslistoutput)
                for line in dizionarioks:
                        temp_writer.writerow([
                                line,
                                dizionarioks[line][kslistoutput[1]],
                                dizionarioks[line][kslistoutput[2]],
                                dizionarioks[line][kslistoutput[3]],
                                dizionarioks[line][kslistoutput[4]],
                                dizionarioks[line][kslistoutput[5]],
                                dizionarioks[line][kslistoutput[6]]
                                ])
                csvf.closed
        with open(outputfolder + "/ks_output.csv",'r',encoding='utf-8-sig',newline='') as csvf:
                temp_reader = csv.reader(csvf)
                next(temp_reader, None)
                sort_reader = sorted(temp_reader, key = lambda x: int(x[1]),reverse = True)
                with open(outputfolder + "/ ks_output.csv",'w',encoding='utf-8-sig',newline='') as csvf2:
                        temp_writer = csv.writer(csvf2)
                        temp_writer.writerow(kslistoutput)
                        for line in sort_reader:
                                temp_writer.writerow(line)
        print("apertura, scrittura e chiusura avvenuta con successo")
        time.sleep(1)
        
def printcsvbl():
        with open(outputfolder + "/bl_output.csv",'w',encoding='utf-8-sig',newline='') as csvf:
                temp_writer = csv.writer(csvf)
                temp_writer.writerow(bllistoutput)
                for line in dizionariobl:
                        temp_writer.writerow([
                                line,
                                dizionariobl[line][bllistoutput[1]],
                                dizionariobl[line][bllistoutput[2]],
                                dizionariobl[line][bllistoutput[3]],
                                dizionariobl[line][bllistoutput[4]],
                                dizionariobl[line][bllistoutput[5]],
                                dizionariobl[line][bllistoutput[6]],
                                dizionariobl[line][bllistoutput[7]],
                                dizionariobl[line][bllistoutput[8]]
                                ])
                csvf.closed
        with open(outputfolder + "/bl_output.csv",'r',encoding='utf-8-sig',newline='') as csvf:
                temp_reader = csv.reader(csvf)
                next(temp_reader, None)
                sort_reader = sorted(temp_reader, key = lambda x: int(x[3]),reverse = True)
                with open(outputfolder + "/bl_output.csv",'w',encoding='utf-8-sig',newline='') as csvf2:
                        temp_writer = csv.writer(csvf2)
                        temp_writer.writerow(bllistoutput)
                        for line in sort_reader:
                                temp_writer.writerow(line)
        print("apertura, scrittura e chiusura avvenuta con successo")
        time.sleep(1)

def open_ks_verificatore():
        print("")
        print("")
        x = input("Vuoi aprire il verificatore KS? y/n ")
        if(x =="y"):
                os.system('ks-verificatore.py')
                sys.exit()
        elif(x == "n"):
                print("ok chiusura programma...")
                time.sleep(2)
        else:
                print("hai premuto un tasto sbagliato. riprova. Scrivi y or n. ")
                time.sleep(1)
                open_ks_verificatore()
        
                

                        
        
        
                        



####
#code
####


#create folder if doesn't exists
if(os.path.exists(dumpfolder)):
        pass
else:
        os.mkdir(dumpfolder)
        print("cartella dump non presente. Creazione in corso")
        input("inserisci dati csv dentro la cartella e fai ripartire il programma. Premi un tasto per chiudere")
        sys.exit()
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
                print("file trovato - " + f.name)
                counter += 1
        else:
                pass

#scan all csv in dumpfolder
if(counter >0):
        for f in os.scandir(dumpfolder):
                if (f.name.endswith(".csv") and listanalyzer[1] in f.name):
                        extract_ks(f)
                elif(f.name.endswith(".csv") and listanalyzer[0] in f.name):
                        extract_bl(f)
                else:
                        print("Non riconosco questo file -- : " + f.name)
                        pass
else:
        print("Non ho trovato file da analizzare.")
        print("Aggiungi file csv alla cartella _dumphere e fai ripartire il programma")
        input("premi enter per chiudere")
        sys.exit()

time.sleep(1)
printcsvks()
printcsvbl()
open_ks_verificatore()
