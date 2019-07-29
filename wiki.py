import wikipediaapi
from googlesearch import search 
import csv
import re

#general strategy
#after finding using google, create a dictionary to save the person's name (in original format)
#make array of arrays for final results
#if it matches birth year, add an array containg name (as originally given), birth year, URL, first sentence of wikipedia article to final results
#write to output file


#load name, birth year from file
names = []
years = []
titles_to_names = {}

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
        titles_to_names[j] = names[num]


#obtains the titles of articles
titles = []
corresponding_years = []
for num in range(len(candidates)):
    if candidates[num][0:30] == "https://en.wikipedia.org/wiki/":
        titles.append(candidates[num][30: ])
        corresponding_years.append(years[num]) 
#use the wikipedia api to check if it is the right person
#need to keep track of the year here, make a separate array?
wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)



#checks if Category: Year births' is one of the categories
#if not, look for a disambiguation page
#if disambiguation page exists, searches text for the right year
#checks corresponding wikipedia page
for num in range(len(titles)):
    wiki_page = wiki_wiki.page(titles[num])
    #print_categories(wiki_page)
    #print(type(wiki_page))
    cats = wiki_page.categories
    string = 'Category:' + corresponding_years[num] + ' births'
    if string in cats:
        print(titles[num])
    else:
        query = titles_to_names["https://en.wikipedia.org/wiki/" + titles[num]]  + " Wikipedia disambiguation"




page_py = wiki_wiki.page('Philby')
print(page_py.text)

#check if it is the birth year
#do this by checking if it is in the category "year births"
#check yale using "Yale University Alumni" maybe
#if it isn't check for the existence of a disambiguation page

#write to file as CSV
#add description to CSV?