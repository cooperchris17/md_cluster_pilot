'''
This script does final cleaning
it deletes empty lines and cleans up the punctuation
The regular expressions were compiled by trial and error
By seeing what punctuation mistakes still remained and adding extra patterns
'''

import re, os, glob

for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            with open(file, 'r') as input:
                filedata = input.read()
                # delete all empty lines
                filedata = re.sub(r'^$\n', '', filedata, flags=re.MULTILINE)
                # add a period to the end of each line
                filedata = re.sub(r'$', '.', filedata, flags=re.MULTILINE)
                # clean lines that have spaces before a period
                filedata = re.sub(r'   .$', '.', filedata, flags=re.MULTILINE)
                filedata = re.sub(r'  .$', '.', filedata, flags=re.MULTILINE)
                filedata = re.sub(r' .$', '.', filedata, flags=re.MULTILINE)
                # clean places where periods have been added after ? and ,
                filedata = re.sub(r'\?.$', '?', filedata, flags=re.MULTILINE)
                filedata = re.sub(r'\? .$', '?', filedata, flags=re.MULTILINE)
                filedata = re.sub(r',.$', '.', filedata, flags=re.MULTILINE)
                # and '?.' at the end of lines
                filedata = re.sub(r'\?.$', '?', filedata, flags=re.MULTILINE)
                # clean '?,' and ' ?' and ',?' and ' ,' at any point in the text
                filedata = re.sub(r'\?,', '?', filedata, flags=re.MULTILINE)
                filedata = re.sub(r' \?', '?', filedata, flags=re.MULTILINE)
                filedata = re.sub(r',\?', '?', filedata, flags=re.MULTILINE)
                filedata = re.sub(r' ,', ',', filedata, flags=re.MULTILINE)
                # clean any single spaces + ', ' at the start of a line
                filedata = re.sub(r'^ ', '', filedata, flags=re.MULTILINE)
                filedata = re.sub(r'^, ', '', filedata, flags=re.MULTILINE)
                # clean any new empty lines now have a period on them
                filedata = re.sub(r'^.$', '', filedata, flags=re.MULTILINE)
                # delete all empty lines again
                filedata = re.sub(r'^$\n', '', filedata, flags=re.MULTILINE)
                # clean ',,' to ','
                filedata = re.sub(r',,', ',', filedata, flags=re.MULTILINE)
                # another space pattern
                filedata = re.sub(r'    .$', '.', filedata, flags=re.MULTILINE)
                # clean any empty lines that now have a space period on them
                filedata = re.sub(r'^ .$', '', filedata, flags=re.MULTILINE)
                # delete all empty lines for one last time
                filedata = re.sub(r'^$\n', '', filedata, flags=re.MULTILINE)


                with open("temp.txt", "w") as output:
                    output.write(filedata)

            # replace file with original name
            os.replace('temp.txt', file)
