# auto_download

환경 세팅
-----

1. Python3 설치
2. pip3 설치
3. redis-server 설치
4. redis, rq 설치


서버 준비
-----

1. 입력할 csv 파일
2. 서버 파이썬 파일
3. 다운로드 메소드 파이썬 파일

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
<pre><code>python3 [파이썬 파일] --url [서버 URL 주소]</code></pre>
<pre><code>python3 [파이썬 파일] --url redis://[ip 주소]:[포트 번호]/[DB 번호]</code></pre>
