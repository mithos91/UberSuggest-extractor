import csv
import os
import re
import sys
import operator
import keyboard
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#define folder output
CSVToUsePath = "_output\extracted_bl.csv"
CSVOutputfile = "_output\_Link_Analysis.csv"
CSVTempOutputFile = "_output/tempAnalysis.csv"

#create Selenium Chrome Instance
websurfer = webdriver.Chrome(r"C:\Users\anton\Desktop\excel python test\chromedriver.exe")
#keyboard.send('alt+tab')
              
#--------------------------------------|#--------------------------------------|
#FUNCTION 01: open CSV transfer in new CSV then add column
#--------------------------------------|#--------------------------------------|

def apriecopiadati():

        with open(CSVToUsePath,"r",encoding="utf-8", newline='') as newfile01:
                temp_csv_transfer = csv.reader(newfile01)
                with open(CSVOutputfile,"w",encoding="utf-8", newline='') as newfile02:
                        temp_csv_writer = csv.writer(newfile02)
                        counter_csv=0
                        for line in temp_csv_transfer:
                                if(counter_csv == 0):
                                        line.append("Commento")
                                        temp_csv_writer.writerow(line)
                                        counter_csv +=1
                                else:
                                        temp_csv_writer.writerow(line)
                                        

                                        
        newfile01.closed
        newfile02.closed
        opencsvandscrap()

#--------------------------------------|#--------------------------------------|
#FUNCTION 02: open new CSV then scrap by line
#--------------------------------------|#--------------------------------------|
def opencsvandscrap():
        with open(CSVOutputfile,"r",encoding="utf-8", newline='') as newfile01:
                temp_reader = csv.reader(newfile01)
                with open(CSVTempOutputFile,'w',encoding='utf-8',newline='') as newfile02:
                        temp_writer = csv.writer(newfile02)
                        counter = 0
                        ForceStop = False
                        for line in temp_reader:
                                if(counter == 0):
                                        counter +=1
                                        temp_writer.writerow(line)
                                        comparelen = len(line)
                                else:
                                        if(len(line) == comparelen):                                                
                                                temp_writer.writerow(line)
                                        elif(ForceStop == False):
                                                print(line)
                                                print("----COMANDI----:")
                                                print(" - StopAll - per bloccare il processo")
                                                print(" - # - per ignorare l'elemento e non copiarlo")
                                                print("----INFORMAZIONI----:")
                                                print("Link Sorgente: " + str(line[0]))
                                                print("Titolo Pagina: " + str(line[1]))
                                                print("Target URL: " + str(line[2]))
                                                print("Anchor Text: " + str(line[3]))
                                                print("Prima Apparizione: " + str(line[4]))
                                                print("Ultima Apparizione: " + str(line[5]))
                                                print("Domain Auth: " + str(line[6]))
                                                print("Page Auth: " + str(line[7]))
                                                
                                                OpenURL(line[0])
                                                x = input("scrivi un commento: ")
                                                if(x == "StopAll"):
                                                        temp_writer.writerow(line)
                                                        newfile01.closed
                                                        newfile02.closed
                                                        os.system("taskkill /im chrome.exe /f")
                                                        os.system("taskkill /im chromedriver.exe /f")
                                                        ForceStop = True
                                                elif(x == "#"):
                                                        print("Rimosso!")
                                                else:
                                                        print(line[0])
                                                        line.append(str(x))
                                                        temp_writer.writerow(line)
                                        else:
                                                temp_writer.writerow(line)
        OverwriteThenClose()
                                                        


#--------------------------------------|#--------------------------------------|
#FUNCTION 03: Convert Temp CSV to main CSV then close
#--------------------------------------|#--------------------------------------|

def OverwriteThenClose():
        with open(CSVOutputfile,"w",encoding="utf-8", newline='') as newfile01:
                temp_writer = csv.writer(newfile01)
                with open(CSVTempOutputFile,'r',encoding='utf-8', newline='') as newfile02:
                        temp_reader = csv.reader(newfile02)
                        for line in temp_reader:
                                temp_writer.writerow(line)
        newfile01.closed
        newfile02.closed
        os.remove(CSVTempOutputFile)


#--------------------------------------|#--------------------------------------|
#FUNCTION 04: Open Internet Page
#--------------------------------------|#--------------------------------------|                
def OpenURL(url):
        url = "Https:" + url        
        websurfer.get(url)        


#--------------------------------------|#--------------------------------------|
#CODE 01: create file if doesn't exist or overwrite or stop process key listener
#--------------------------------------|#--------------------------------------|        

if not os.path.exists(CSVOutputfile):

        with open(CSVOutputfile,"w",encoding="utf-8", newline='') as newfile:
                newfile.closed
else:
        x = input("Il file esiste: vuoi sovrascriverlo? Tutti i dati andranno persi! y/n ")
        if(x == "y"):
                with open(CSVOutputfile,"w",encoding="utf-8", newline='') as newfile:
                                        newfile.closed
                                        time.sleep(1)
                                        print("Link Analysis sovrascritto")
                                        apriecopiadati()
        elif(x == "n"):
                print("Ok apro il file e non sovrascrivo")
                opencsvandscrap()
        else:
                print("Hai premuto il tasto sbagliato")
