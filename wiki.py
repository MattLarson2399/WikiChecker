import wikipediaapi
from googlesearch import search 

#load name, birth year from file
#google search name + birth year + wiki 

wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)
page_py = wiki_wiki.page('Philby')
print(page_py.text)

#write to file as CSV