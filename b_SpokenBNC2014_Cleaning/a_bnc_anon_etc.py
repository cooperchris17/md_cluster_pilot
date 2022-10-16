'''
This script replaces tags for anonymous names, places, etc with actual names, etc
Names were chosen that did not occur in the Spoken BNC2014
It also replaces pauses with a comma and <trunc> (like a false start) with a comma
'''

import re, os, glob

# https://stackoverflow.com/questions/15175142/how-can-i-do-multiple-substitutions-using-regex

def multiple_replace(dict, text):
  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)

if __name__ == "__main__":
    # keys =  how the word is written in the text, values = how it should be amended
    # this R script was used as a starting point:
    # https://github.com/elenlefoll/TextbookEnglish/blob/main/3_Data/BNCspoken_nomark-up_JackJill.R
    # the names, places, etc are based on The Simpsons and did not exist in the corpus except '17th of December'
    # https://simpsonswiki.com/wiki/Main_Page
    dict = {
            '<anon type="name" nameType="m"/>' : 'Waylon',
            '<anon type="name" nameType="f"/>' : 'Sherri',
            '<anon type="name" nameType="n"/>' : 'Terri',
            '<anon type="place"/>' : 'Sprooklyn',
            '<anon type="telephoneNumber"/>' : '355-1337',
            '<anon type="address"/>' : 'Fudgetown',
            '<anon type="email"/>' : 'ned.flanders@springface.com',
            '<anon type="financialDetails"/>' : '5316',
            '<anon type="socialMediaName"/>' : '@ComicBookGuy',
            '<anon type="dateOfBirth"/>' : '17th of December',
            # '<anon type="miscPersonalInfo"/>' : '?', -> difficult to replace with one word, so deleted
            ' <pause dur="short"/>' : ',',
            ' <pause dur="long"/>' : ',',
            '<trunc>' : '', # this is like a false start or similar
            '</trunc>' : ', '
        }

for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.xml'): # avoid editing .py files, etc
            with open(file, 'r') as input:
                filedata = input.read()
                new_text = multiple_replace(dict, filedata)
                with open("temp.xml", "w") as output:
                    output.write(new_text)

            # replace file with original name
            os.replace('temp.xml', file)
