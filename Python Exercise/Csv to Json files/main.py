import json
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--csvfile_arg')
args=parser.parse_args()
dictionary={}
headerlist=[]

jsonfile=open("convertJson.json","w")
with open(args.csvfile_arg,"r") as csvfile:
    lines=csvfile.readlines()
    headerlist = lines[0].split(",")
    for row in lines[1:]:
        row_split=row.split(",")

        dictionary.update({headerlist[0]:row_split[0],headerlist[1]:row_split[1],headerlist[2]:row_split[2],
                           headerlist[3]:row_split[3],headerlist[4]:row_split[4]})
        print(dictionary)

        #with open("convertJson.json","w") as jsonfile:

        jsonfile.write(json.dumps(dictionary,indent=4))
        jsonfile.write("\n")








