def my_decorator(func):
    def wrapper():
        print("装饰器：函数执行前")
        func()  # 执行原函数
        print("装饰器：函数执行后")
    return wrapper
#装饰器（Decorator） 是一种在不修改原函数代码的情况下，动态扩展函数功能的方式。
# 它本质上是一个高阶函数（接受函数作为参数并返回函数）
@my_decorator  # 使用装饰器
def say_hello():
    print("Hello!")

say_hello()

#2.0
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}，参数：args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)  # 返回原函数的结果
    return wrapper

@log_args
def add(a, b):
    return a + b

print(add(3, 5))

#3.0. 多个装饰器叠加使用
#可以同时使用多个装饰器，执行顺序是从下往上（靠近函数的最先执行）：
def decorator1(func):
    def wrapper():
        print("装饰器1：执行前")
        func()
        print("装饰器1：执行后")
    return wrapper

def decorator2(func):
    def wrapper():
        print("装饰器2：执行前")
        func()
        print("装饰器2：执行后")
    return wrapper

@decorator1
@decorator2
def say_hi():
    print("Hi!")

say_hi()
#4.0