M = {1: 0, 2: 1}

def fib(n):
    if n in M:
        return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]

n = int(input("Номер элемента = "))
print("Значение:",fib(n))

