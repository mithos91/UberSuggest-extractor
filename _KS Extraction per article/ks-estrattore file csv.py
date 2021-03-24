import csv
import sys
import time
import os

dumpfolder = "_dumphere"
outputfolder = "_Output"

listacsvoutput =[
        'Ks',
        'Volume',
        'Position',
        'Est. Visits',
        'CPC',
        'Paid Difficulty',
        'SEO Difficulty',
        ]
dizionario = {}

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
                                dizionario.update({
                                        line[1]:{
                                                listacsvoutput[1] : line[2],
                                                listacsvoutput[2] : line[3],
                                                listacsvoutput[3]: line[4],
                                                listacsvoutput[4]: line[5],
                                                listacsvoutput[5]: line[6],
                                                listacsvoutput[6]: line[7],
                                                }
                                         }
                                        )
                csvf.closed

def printcsv():
        with open(outputfolder + "/ output.csv",'w',encoding='utf-8-sig',newline='') as csvf:
                temp_writer = csv.writer(csvf)
                temp_writer.writerow(listacsvoutput)
                for line in dizionario:
                        temp_writer.writerow([
                                line,
                                dizionario[line][listacsvoutput[1]],
                                dizionario[line][listacsvoutput[2]],
                                dizionario[line][listacsvoutput[3]],
                                dizionario[line][listacsvoutput[4]],
                                dizionario[line][listacsvoutput[5]],
                                dizionario[line][listacsvoutput[6]]
                                ])
                csvf.closed
        with open(outputfolder + "/ output.csv",'r',encoding='utf-8-sig',newline='') as csvf:
                temp_reader = csv.reader(csvf)
                next(temp_reader, None)
                sort_reader = sorted(temp_reader, key = lambda x: int(x[1]),reverse = True)
                with open(outputfolder + "/ output.csv",'w',encoding='utf-8-sig',newline='') as csvf2:
                        temp_writer = csv.writer(csvf2)
                        temp_writer.writerow(listacsvoutput)
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
        print("cartella non presente. Creazione in corso")
        input("inserisci dati csv dentro la cartella e fai ripartire il programma. Premi un tasto per chiudere")
        sys.exit()

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
                if (f.name.endswith(".csv")):
                        extract_ks(f)
                else:
                        pass
else:
        print("Non ho trovato file da analizzare.")
        print("Aggiungi file csv alla cartella _dumphere e fai ripartire il programma")
        input("premi enter per chiudere")
        sys.exit()

time.sleep(1)
printcsv()
open_ks_verificatore()
