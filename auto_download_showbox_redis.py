import os
import time
import sys
import csv
from redis import Redis
from rq import Connection, Queue
from download_job import download
from rq.job import Job
import time


if __name__ == '__main__':
    input_csv=open(sys.argv[1],'r',encoding="utf-8")
    input=sys.argv[1]
    temp_input=input.split('.')
    input=temp_input[0]
    output_name=input+"_output"
    reader=csv.reader(input_csv)
    job_list=[]
    download_q=Queue(connection=Redis())

    for entry in reader:
        link=entry[0]
        filename=entry[1]
        job=download_q.enqueue(download,entry,job_timeout=10800)
        job_list.append(job.id)

    done=False
    while not done:
        input_csv=open(sys.argv[1],'r',encoding="utf-8")
        reader=csv.reader(input_csv)
        output_csv=open(output_name,'w',encoding='utf-8')
        writer=csv.writer(output_csv)
        i=0
        for entry in reader:
            job_id=job_list[i]
            job=Job.fetch(job_id,connection=Redis())
            status=job.get_status()
            writer.writerow([entry[0],entry[1],status])
            i+=1
            if status == "finished":
                done=True
            elif status == "failed":
                done=True
            else:
                done=False
        time.sleep(60)
