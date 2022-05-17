import os, re
import pandas as pd
from operator import itemgetter

if (os.name == "nt"):
    rootPath = 'C:/Users/peter/Documents/spark'
elif (os.name == "posix"):
    rootPath = '/home/muddy/Tresors/Documentsacer/KULeuven/AdvAnaBusi/A3'
fileType = 'part-00000'
notInclude = 'crc'
files = []
directories = []
messages = []
df = pd.DataFrame()
dfAll = pd.DataFrame()
print(dfAll.shape[0])
channel1 = 'xQcOW'
channel2 = 'summit1g'
channel3 = 'BangerTV'
channel4 = 'matthewkheafy'
#{"datetime": "2022-04-29T07:19:58.742682",
# "username": "hitorange",
# "channel": "#xqcow",
# "message": "add"}

i=0
for dirpath, dirnames, filenames in os.walk(rootPath):
    for file in os.scandir(dirpath):
        if not('-' in file.path):
            continue
        else:
            if file.is_file():
                if (str(file).find(fileType) != -1) and (str(file).find('crc') == -1):
                    df = pd.DataFrame(pd.read_json(file, orient='records', lines=True, encoding = 'ISO-8859-1'))
                    df.drop(df.columns[[0]], axis = 1, inplace = True)
                    dfAll = pd.concat([dfAll, df])
                    print(dfAll.shape)


dfAll.to_csv("messages.csv", index=False)
