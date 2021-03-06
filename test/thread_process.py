
# # None Thread

# import time

# def long_task():  # 3초의 시간이 걸리는 함수
#     for i in range(3):
#         time.sleep(1)  # 1초간 대기한다.
#         print("working:%s\n" % i)

# print("Start")

# for i in range(3):  # long_task를 3회 수행한다.
#     long_task()

# print("End")


##########################################################


# # Thread (but "End"가 미리 출력)

# import time
# import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

# def long_task():
#     for i in range(3):
#         time.sleep(1)
#         print("working:%s\n" % i)

# print("Start")

# threads = []
# for i in range(3):
#     t = threading.Thread(target=long_task)  # 스레드를 생성한다.
#     threads.append(t) 

# for t in threads:
#     t.start()  # 스레드를 실행한다.

# print("End")


##########################################################

# # Thread

# import time
# import threading

# def long_task():
#     for i in range(3):
#         time.sleep(1)
#         print("working:%s\n" % i)

# print("Start")

# threads = []
# for i in range(3):
#     t = threading.Thread(target=long_task)
#     threads.append(t)

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()  # join으로 스레드가 종료될때까지 기다린다.

# print("End")


##########################################################


# # Single Thread

# from threading import Thread
# import time

# def work(id, start, end, result):
#     total = 0
#     for i in range(start, end):
#         total += i
#     result.append(total)
#     return

# if __name__ == "__main__":
#     START, END = 0, 100000000
#     result = list()
#     th1 = Thread(target=work, args=(1, START, END, result))

#     print("실행")
#     start = time.time()
    
#     th1.start()
#     th1.join()

#     end = time.time()
#     print("종료, 수행시간: %f 초" % (end - start))

# print(f"Result: {sum(result)}")


# # 실행
# # 종료, 수행시간: 7.249892 초
# # Result: 4999999950000000


##########################################################


# # Multi Thread (2개)

# from threading import Thread
# import time


# def work(id, start, end, result):
#     total = 0
#     for i in range(start, end):
#         total += i
#     result.append(total)
#     return


# if __name__ == "__main__":
#     START, END = 0, 100000000
#     result = list()
#     th1 = Thread(target=work, args=(1, START, END//2, result))
#     th2 = Thread(target=work, args=(2, END//2, END, result))

#     print("실행")
#     start = time.time()
    
#     th1.start()
#     th2.start()
#     th1.join()
#     th2.join()

#     end = time.time()
#     print("종료, 수행시간: %f 초" % (end - start))

# print(f"Result: {sum(result)}")

# # 실행
# # 종료, 수행시간: 6.734275 초
# # Result: 4999999950000000


# # -> GIL 정책으로 수행시간 큰 차이 없음

# # GIL(Global Interpreter Lock)
# # 언어에서 자원을 보호하기 위해 락(Lock) 정책을 사용하고 그 방법 또한 다양하다. 
# # 파이썬에서는 하나의 프로세스 안에 모든 자원의 락(Lock)을 글로벌(Global)하게 관리함으로써 
# # 한번에 하나의 쓰레드만 자원을 컨트롤하여 동작하도록 한다.


# # GIL이 적용되는 것은 cpu 동작에서이고 쓰레드가 cpu 동작을 마치고 
# # I/O 작업을 실행하는 동안에는 다른 쓰레드가 cpu 동작을 동시에 실행할 수 있다. 

# # "cpu 동작이 많지 않고 I/O동작이 더 많은 프로그램에서는 멀티 쓰레드만으로 성능적으로 큰 효과를 얻을 수 있다."


##########################################################

# Multi Process

from multiprocessing import Process, Queue
import time

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return


if __name__ == "__main__":
    START, END = 0, 100000000
    result = Queue()
    th1 = Process(target=work, args=(1, START, END // 2, result))
    th2 = Process(target=work, args=(2, END // 2, END, result))

    print("실행")
    start = time.time()

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp

    end = time.time()
    print("종료, 수행시간: %f 초" % (end - start))
    print(f"Result: {total}")


# 실행
# 종료, 수행시간: 4.093691 초
# Result: 4999999950000000


# # 실행시간 크게 개선

# # multiprocessing 모듈의 가장 큰 장점은 threding 모듈과 구현 방식이 거의 같아서 
# # 기존에 쓰레드 방식으로 구현한 코드를 쉽게 이식할 수 있다는 점

# # 프로세스는 각자가 고유한 메모리 영역을 가지기 때문에 쓰레드에 비하면 메모리 사용이 늘어난다는 단점이 있지만, 
# # 이 방식을 통해 싱글 머신 아키텍처로부터 여러 머신을 사용하는 분산 애플리케이션으로 쉽게 전환할 수 있다.

# # 각각의 프로세스가 자신만의 메모리 공간을 사용하기 때문에 
# # 프로세스간 데이터 교환을 위해 multiprocessing.Queue 객체를 사용해야 한다. 
# # multiprocessing 모듈에서는 Queue 이외에도 Pipe 객체를 지원하여 데이터 교환을 돕는다.


# # [Thread vs Process]

# # 결론적으로 말하자면, 
# # 파이썬에서 병렬처리를 구현하는 방식은 두가지로 멀티 쓰레드를 사용하거나 멀티 프로세스를 사용하는 것이다. 
# # 쓰레드는 가볍지만 GIL로 인해 계산 처리를 하는 작업은 한번에 하나의 쓰레드에서만 작동하여 
# # cpu 작업이 적고 I/O 작업이 많은 병렬 처리 프로그램에서 효과를 볼 수 있다.

# # 프로세스는 각자가 고유한 메모리 영역을 가지기 때문에 더 많은 메모리를 필요로 하지만, 
# # 각각 프로세스에서 병렬로 cpu 작업을 할 수 있고 이를 이용해 여러 머신에서 동작하는 분산 처리 프로그래밍도 구현할 수 있다.

# 각자의 장단점을 고려하여 자신의 프로그램에 잘 맞는 방식을 사용하자.
