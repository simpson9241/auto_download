import csv
import os
import sys

if __name__=="__main__":
    file=""
    current_program_id=0
    input=sys.argv[1]
    temp_input=input.split('.')
    input=temp_input[0]
    f=open(sys.argv[1],'r',encoding="utf-8")
    output_name=input+"_output"
    f_output=open(output_name,'w',encoding='utf-8')
    writer=csv.writer(f_output)
    reader=csv.reader(f)
    writer.writerow(["program_id","episode_id","title","episode_title","episode_image_error","episode_video_error"])
    for line in reader:
        program_id=line[0]
        episode_id=line[1]
        title=line[3]
        episode_title=line[4]
        program_images_url=line[11]
        episode_images_url=line[12]
        episode_videos_url=line[13]
        if current_program_id==0:
            current_program_id=program_id
            temp="mkdir '"+title+"'"
            os.system(temp)
            temp="wget '{0}' -P ./'{1}'".format(program_images_url,title)
            error=os.system(temp)
        elif current_program_id!=program_id:
            current_program_id=program_id
            temp="mkdir '"+title+"'"
            os.system(temp)
            temp="wget '{0}' -P ./'{1}'".format(program_images_url,title)
            error=os.system(temp)

        temp="mkdir '"+title+"'/"+"'"+episode_title+"'"
        os.system(temp)

        temp="wget '{0}' -P ./'{1}'/'{2}'".format(episode_images_url,title,episode_title)
        episode_image_error=os.system(temp)

        temp="wget '{0}' -P ./'{1}'/'{2}'".format(episode_videos_url,title,episode_title)
        episode_video_error=os.system(temp)

        writer.writerow([program_id,episode_id,title,episode_title,episode_image_error,episode_video_error])
