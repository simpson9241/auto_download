import os
import time
from rq import Connection, Queue
from rq_task import test_fib

def main():
    fib_range=range(30,40)

    q=Queue()
    async_results=[q.enqueue(test_fib,x) for x in fib_range]

    start_time=time.time()

    done=False

    while not done:
        os.system('clear')

        print('Asynchronously: (now=%.2f)' % (time.time()-start_time,))
        done=True
        for i, x in enumerate(async_results):
            result=x.return_value
            if result is None:
                done=False
                result='(calculating)'

            print('fib(%d) = %s' % (i, result))
        print('')
        time.sleep(0.2)

    print('Done')

if __name__ == '__main__':
    with Connection():
        main()
