import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间：{end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()