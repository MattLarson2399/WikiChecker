import wikipediaapi
from googlesearch import search 
import csv
import re

#load name, birth year from file

names = []
years = []

with open('standardinput.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
        	names.append(row[0])
        	years.append(row[1])
        line_count += 1


#google search name + birth year + wiki
candidates = []
for num in range(len(names)):
    query = names[num]  + years[num] + " Wikipedia"
    for j in search(query, num=1, stop=1, pause=2):
        candidates.append(j)

print(candidates)

#use a regular expression to get everything after /wiki/
#use the wikipedia api to check if it is the right person



wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)
page_py = wiki_wiki.page('Philby')
print(page_py.text)

#check if it is the birth year

#write to file as CSV
#add description to CSV?