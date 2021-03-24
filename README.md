# UberSuggest-extractor
This Python code lets you to extract data from several csv in one. 
I programmed it in order to be used with UberSuggest. If you want to use with other providers, you need to edit it or just wait until I publish the next version.
These data will be filtered without duplicates.

My-site: [numerable.it](https://numerable.it)

HOW TO USE:
Create a folder and paste the Extractor.py
Create a folder for each sets of files you want to analyze
Do not add other files in the main directory
Each folder has to have 3 files and each one has to be partially named as (wild card present):

 -backlinks.csv
 
 -Top_pages_
 
 -ubersuggest_
 
 

Once clicked, write y then enter and the program will do its magic.

/--UPDATE 24.03.2021 --/
Added _Template Articles. How to use:
- Start 01[xxx].py
- Add top pages keywords / top pages backlinlks .csvs in dump folder
- Start 01[xxx].py again and follow instructions
- Start 02[xxx].py then paste your text to check if clipboard text has any scrapped ks. It will report missing ks in a text file
- Start 03[xxx].py use it if you want to analyze sites by csv list.
