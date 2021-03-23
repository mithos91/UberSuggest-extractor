import csv
import sys
import time
import os

output_file = "Raccolta Ks.csv"

looper = True

dictionary = {}
lista = ['£','#',';','"',',','.','/','[',']',':','~','@','<','>','?','¬','!','£','$','%','^','&','*','(',')','-','_','=','+',"|",'€']

def Looper():
        while looper == True:
                print("COMANDI:")
                print("StopAll - ferma il processo e salva su file csv")
                print("Incolla Ks:")
                line = input()
                if(line == "StopAll"):
                        print(dictionary)
                        with open(output_file,"a",encoding="utf-8-sig", newline="") as text:
                                temp_writer=csv.writer(text)                                
                                for line in dictionary:
                                        print(line)
                                        temp_writer.writerow([line])
                                sys.exit()
                elif(any(word in line for word in lista) ==False):
                        if(line.isnumeric() == False):
                                line = {line:""}
                                dictionary.update(line)
                                print(dictionary)
                else:
                        break

def filetrovato(f):
        if (f.name == output_file):
                x = input("Ho trovato un file: devo sovrascrivere? (y/n) -  ")
                if(x == "y"):
                        with open(output_file,"w",encoding="utf-8-sig", newline="") as text:
                                print(str(text) + " il file e' stato cancellato!")
                                text.closed
                                time.sleep(2)
                elif(x == "n"):
                        with open(output_file,"r",encoding="utf-8-sig", newline="") as text:
                                temp_reader = csv.reader(text)
                                for line in temp_reader:
                                        tdc = {line[0]:""}
                                        dictionary.update(tdc)
                                text.closed
                else:
                        print("Comando errato: inserisci y o n")
                        filetrovato(f)
                

#Main Code
for f in os.scandir():
        filetrovato(f)


                
while looper == True:
        Looper()
