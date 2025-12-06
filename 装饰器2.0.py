def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)  # 重复执行3次
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")