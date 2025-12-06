def cache(func):
    memo = {}  # 存储计算结果
    def wrapper(n):
        if n not in memo:#if n not in memo: 的作用是检查当前输入 n 是否已经计算过并缓存。
                         #如果没有缓存，就计算并存储结果；如果已经缓存，就直接返回缓存的结果，避免重复计算。


            memo[n] = func(n)
        return memo[n]
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 计算后缓存结果