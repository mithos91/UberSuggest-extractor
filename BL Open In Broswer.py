import webbrowser
import csv
import os
import re
import sys
import operator
import keyboard
import time


#define folder output
CSVToUsePath = "_output\extracted_bl.csv"
CSVOutputfile = "_output\_Link_Analysis.csv"
CSVTempOutputFile = "_output/tempAnalysis.csv"


              
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
                                                print(line)
                                        elif(ForceStop == False):
                                                print(line)
                                                print("")
                                                print("StopAll per bloccare il processo")
                                                print("")
                                                OpenURL(line[0])
                                                x = input("scrivi un commento: ")
                                                os.system("taskkill /im chrome.exe /f")
                                                if(x == "StopAll"):
                                                        newfile01.closed
                                                        newfile02.closed
                                                        ForceStop = True
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
        webbrowser.open(url, new=0, autoraise=True)
        time.sleep(1)
        keyboard.send('alt+tab')
        


#--------------------------------------|#--------------------------------------|
#CODE 01: create file if doesn't exist or overwrite or stop process key listener
#--------------------------------------|#--------------------------------------|        

if not os.path.exists(CSVOutputfile):

        with open(CSVOutputfile,"w",encoding="utf-8", newline='') as newfile:
                newfile.closed
else:
        print("Il file esiste: vuoi sovrascriverlo? Tutti i dati andranno persi! y/n ")
        filebool = True
        while filebool==True:
                try:
                        if(keyboard.is_pressed("y")):
                                with open(CSVOutputfile,"w",encoding="utf-8", newline='') as newfile:
                                        newfile.closed
                                        time.sleep(1)
                                        print("Link Analysis sovrascritto")
                                        apriecopiadati()
                                        filebool = False
                        elif(keyboard.is_pressed("n")):
                                print("Ok, processo fermato")
                                break
                        else:
                                pass
                except:
                        print("Hai premuto un tasto sbagliato")
                        time.sleep(1)
                        break


opencsvandscrap()






"""

#open and locally hold data from csv


with open(CSVToUsePath,'r', encoding='utf-8-sig') as csvf:
        csvReader = csv.DictReader(csvf)
        sortlist = sorted(csvReader,key=operator.itemgetter("Domain Auth"), reverse = True)
        i= 0
csvf.closed

with open(CSVToUsePath,'w', encoding='utf-8-sig',newline='') as csvf:
        fieldnames = ['Source Link','Source Page','Target URL','Anchor Text','Domain Auth','Page Auth']
        csvWriter = csv.DictWriter(csvf, fieldnames=fieldnames)
        csvWriter.writeheader()
        for line in sortlist:
                csvWriter.writerow(line)
csvf.closed
print('end')



"""












"""


url = 'http://docs.python.org/'

# Windows path
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'


webbrowser.get().open(url)


"""
