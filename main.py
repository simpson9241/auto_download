import csv
import os
import sys

if __name__=="__main__":
    link=""
    file=""
    error=0
    input=sys.argv[1]
    temp_input=input.split('.')
    input=temp_input[0]
    f=open(sys.argv[1],'r',encoding="utf-8")
    output_name=input+"_output"
    f_output=open(output_name,'w',encoding='utf-8')
    writer=csv.writer(f_output)
    reader=csv.reader(f)
    writer.writerow(["link_url","file_name","error_code"])
    for line in reader:
        link=line[0]
        file=line[1]
        temp="wget '{0}'".format(link)
        # print(temp)
        error=os.system(temp)
        error=0
        temp_link=link.split('/')
        temp_name_1=temp_link[-1].split('filename=')
        temp_name_2=temp_name_1[-1].split('&openfolder=')
        name=temp_name_1[0]+"filename="+file+"&openfolder="+'&'.join(temp_name_2[1:])
        # print(name)
        temp="mv "+'"'+name+'" '+ '"'+file+'"'
        # print(temp)
        os.system(temp)
        writer.writerow([link,file,error])
