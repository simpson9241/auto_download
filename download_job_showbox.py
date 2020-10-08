import csv
import os
import sys

def download(entry):
    link=entry[0]
    filename=entry[1]
    temp="wget '{0}'".format(link)
    # print(temp)
    error=os.system(temp)
    temp_link=link.split('/')
    temp_name_1=temp_link[-1].split('filename=')
    temp_name_2=temp_name_1[-1].split('&openfolder=')
    name=temp_name_1[0]+"filename="+filename+"&openfolder="+'&'.join(temp_name_2[1:])
    # print(name)
    temp="mv "+'"'+name+'" '+ '"'+filename+'"'
    # print(temp)
    os.system(temp)
