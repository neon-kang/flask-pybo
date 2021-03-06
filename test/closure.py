# # use class
# class Mul:
#     def __init__(self, m):
#         self.m = m

#     def mul(self, n):
#         return self.m * n

# if __name__ == "__main__":
#     mul3 = Mul(3)
#     mul5 = Mul(5)

#     print(mul3.mul(10))  # 30 출력
#     print(mul5.mul(10))  # 50 출력


###################################################


# # use class and __call__ func
# class Mul:
#     def __init__(self, m):
#         self.m = m

#     def __call__(self, n):
#         return self.m * n


# if __name__ == "__main__":
#     mul3 = Mul(3)
#     mul5 = Mul(5)

#     print(mul3(10))  # 30 출력
#     print(mul5(10))  # 50 출력


###################################################


# # use closure
# def mul_of(m):
#     def mul(n):
#         return m * n
#     return mul


# if __name__ == "__main__":
#     mul3 = mul_of(3)
#     mul5 = mul_of(5)

#     print(mul3(10))  # 30 출력
#     print(mul5(10))  # 50 출력


###################################################


# # use closure
# import time

# def decorate(original_func):   # 기존 합수를 입력으로 받는다.
#     def wrapper():
#         start = time.time()
#         original_func()    # 기존 함수를 수행한다.
#         end = time.time()
#         print("함수 수행시간: %f 초" % (end - start))
#     return wrapper


# def myfunc():
#     """ 데코레이터 확인 함수 """
#     print("함수가 실행됩니다.")


# decorated_myfunc = decorate(myfunc)
# decorated_myfunc()


###################################################



# # use closure (단, myfunc()에 전달인자가 있는 경우 오류)
# import time

# def decorate(original_func):   # 기존 합수를 입력으로 받는다.
#     def wrapper():
#         start = time.time()
#         original_func()    # 기존 함수를 수행한다.
#         end = time.time()
#         print("함수 수행시간: %f 초" % (end - start))
#     return wrapper

# @decorate
# def myfunc():
#     """ 데코레이터 확인 함수 """
#     print("함수가 실행됩니다.")

# myfunc()


###################################################


# # use closure (단, myfunc() 함수 속성값을 유지하지 못한다)
# import time

# def decorate(original_func):
#     def wrapper(*args, **kwargs):   # *args, **kwargs 매개변수 추가
#         start = time.time()
#         original_func(*args, **kwargs)  # 전달받은 *args, **kwargs를 입력파라미터로 기존함수 수행
#         end = time.time()
#         print("함수 수행시간: %f 초" % (end - start))
#     return wrapper


# @decorate
# def myfunc(msg):
#     """ 데코레이터 확인 함수 """
#     print("'%s'을 출력합니다." % msg)


# myfunc("You need python")

# print(myfunc)
# # <function decorate.<locals>.wrapper at 0x000001E595410C10>
# help(myfunc)
# # Help on function wrapper in module __main__:
# # wrapper(*args, **kwargs)


###################################################



# # use closure (last),  @functools.wraps(original_func) 사용

import time
import functools


def decorate(original_func):
    @functools.wraps(original_func)
    def wrapper(*args, **kwargs):   # *args, **kwargs 입력인수 추가
        start = time.time()
        original_func(*args, **kwargs)  # 전달받은 *args, **kwargs를 입력파라미터로 기존함수 수행
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
    return wrapper


@decorate
def myfunc(msg):
    """ 데코레이터 확인 함수 """
    print("'%s'을 출력합니다." % msg)


myfunc("You need python")


print(myfunc)
# <function myfunc at 0x000002B25AA3E310>
help(myfunc)
# Help on function myfunc in module __main__:
# myfunc(msg)
#    데코레이터 확인 함수



###################################################