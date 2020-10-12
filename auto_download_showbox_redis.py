import os
import time
import sys
import csv
from redis import Redis
from rq import Connection, Queue
from download_job_showbox import download
from rq.job import Job
import time


if __name__ == '__main__':
    #Input CSV 파일 열기
    input_csv=open(sys.argv[1],'r',encoding="utf-8")

    #input CSV 파일 이름 저장
    input=sys.argv[1]

    #input CSV 파일의 확장자 분리
    temp_input=input.split('.')
    input=temp_input[0]

    #output CSV 파일의 이름 생성
    output_name=input+"_output"

    #input CSV 파일을 읽어들이는 변수 생성
    reader=csv.reader(input_csv)

    #생성된 Job 들의 Job ID와 Job Status를 저장해놓을 리스트 변수 생성
    job_list=[]

    #다운로드 큐 생성
    download_q=Queue(connection=Redis())

    #input CSV에서 값을 읽어들여 download_q에 하나씩 추가
    #input CSV의 한 entry는 (link, filename)으로 이루어져있음
    for entry in reader:
        #download_job_showbox에서 import한 download 함수,input CSV 파일에서 읽어들인 entry, job이 timeout할 때까지의 시간을 인자로 전달
        job=download_q.enqueue(download,entry,job_timeout=10800)

        #job_list에 생성된 Job의 ID와 큐에 추가되었다는 뜻의 메시지를 한 Tuple로 job_list에 추가
        job_list.append((job.id,"queued"))

    
    done=False
    while not done:
        input_csv=open(sys.argv[1],'r',encoding="utf-8")
        reader=csv.reader(input_csv)
        output_csv=open(output_name,'w',encoding='utf-8')
        writer=csv.writer(output_csv)
        i=0
        for entry in reader:
            job_id=job_list[i][0]
            job_status=job_list[i][1]
            if job_status=="finished":
                writer.writerow([entry[0],entry[1],job_status])
                done=True
            elif job_status=="failed":
                writer.writerow([entry[0],entry[1],job_status])
                done=True
            else:
                job=Job.fetch(job_id,connection=Redis())
                current_status=job.get_status()
                writer.writerow([entry[0],entry[1],current_status])
                job_list[i]=(job_id,current_status)
                done=False
            i+=1
        time.sleep(60)
