import csv
import sys
import time
import os
import re

listaks = []
listaks2=[]

outputfolder = "_Output"
filetxt = "Raccolta KS da inserire.txt"

####
#def
####

def ApriCSVinDict(f):
        with open(f,'r',encoding='utf-8-sig',newline='') as csvf:
                csv_reader = csv.reader(csvf)
                for line in csv_reader:
                        listaks.append(line[0])
                ScanPasted()

def ScanPasted():
        print("Copia ed incolla il testo")
        x = input()
        print("")
        print("")
        print("Le parole mancanti sono:")
        print("")
        print("")
        if(x =="StopAll"):
                sys.exit
        elif(x !=""):
                i=0
                length = len(listaks)-1
                while i <=  len(listaks)-1:
                        if(i==0):
                                i=1
                        if(re.search(rf"\b{str(listaks[i])}\b", x, re.IGNORECASE)):
                                i+=1
                                pass
                        else:
                                listaks2.append(listaks[i])
                                print(listaks[i])
                                i+=1
                                pass
                savefile()

        else:
                print("non hai incollato nessun valore")

def savefile():
        with open(outputfolder + '/' + filetxt,'w') as txtf:
                txtf.closed
        for line in listaks2:
                with open(outputfolder + '/' + filetxt,'a') as txtf:
                        txtf.write(line)
                        txtf.write("\n")
                        txtf.closed


def openfile():
        
        print("")
        print("")
        x = input("Vuoi aprire il blocco note con tutte le ks ? y/n ")
        if (x=="y"):
                temp_file_opening = outputfolder + '/' + filetxt
                os.system("notepad.exe " + temp_file_opening)
                sys.exit()
        elif(x=="n"):
                print("Ok chiudo il programma...")
                time.sleep(1)
                sys.exit()
        else:
                print("hai premuto il tasto sbagliato. Riprova. Scrivi y o n -")
                time.sleep(1)
                openfile()
        
####                
#code
####
                        
for f in os.scandir(outputfolder):
        if (f.name == " ks_output.csv"):
                ApriCSVinDict(f)

openfile()


