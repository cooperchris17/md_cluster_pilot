'''
This script extracts the text from the body of the xml files
and saves them in a .txt file
You need to create a new folder 'text_only'
It should be run after anonymised words have been replaced
You need to install Beautiful Soup and lxml for this to work
There are 2 more cleaning scripts to run
'''

from bs4 import BeautifulSoup
import glob, os

for file in glob.iglob('*.xml'):
    file_name = file[0:4]
    with open(file, 'r') as input:
        contents = input.read()
        soup = BeautifulSoup(contents,'xml')
        body = soup.find_all('body')
        for body in body:
            with open('text_only/'+file_name+'.txt', 'w') as f:
                f.write(body.get_text())
