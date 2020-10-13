# auto_download

주요 기능
-----
* 다운로드 url, 파일명으로 구성되어 있는 csv 파일을 읽어 Worker들이 Redis Queue에서 Job을 가져와 자동으로 파일을 다운로드
* 진행되고 있는 Job들의 진행 상황을 Redis Server가 있는 컴퓨터에 csv로 저장
* 모든 Job이 끝나면 Redis Server가 구동되고 있던 컴퓨터에서 돌아가고 있던 Server 프로그램이 종료


환경 세팅
-----

1. Python3 설치
2. pip3 설치
3. redis-server 설치
4. redis, rq 설치
5. 또는 docker로 실행
6. 위의 설치는 install.sh를 실행해서 진행할 수도 있음
<pre><code>sh install.sh</code></pre>
7. 다운로드 방식이나 url, csv 구조 등의 차이로 인해 그때그때 코드들을 조금씩 수정해야함

서버 준비
-----

1. 입력할 csv 파일
2. 서버 파이썬 파일
3. 다운로드 메소드 파이썬 파일
4. redis.conf에서 bind 값이 0.0.0.0인지 확인

서버 실행
-----

1. 서버 실행
<pre><code>redis-server --protected-mode no</code></pre>
2. 서버 파이썬 파일 실행
<pre><code>python3 [파이썬 파일] [csv 파일]</code></pre>


서버 redis 큐 확인 및 테이블 초기화
-----

1. redis-cli 실행
2. 테이블 확인
<pre><code>KEYS '[검색할 것]'</code></pre>
3. 큐 모든 job 삭제
<pre><code>FLUSHALL</code></pre>
4. 상태 저장
<pre><code>SAVE</code></pre>
5. 서버 끄기
<pre><code>SHUTDOWN</code></pre>


Worker 준비
-----

1. worker 파이썬 파일
2. 다운로드 메소드 파이썬 파일

Worker 실행
-----

1. 워커 실행
<pre><code>rq worker --url [서버 URL 주소]</code></pre>
<pre><code>rq worker --url redis://[ip 주소]:[포트 번호]/[DB 번호]</code></pre>
