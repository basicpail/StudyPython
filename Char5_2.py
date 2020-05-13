def factorial(n):
    output = 1

    for i in range(1, n+1):
        output *= i
    return output



def recurfac(n):
    if n == 0:
        return 1
    else:
        return n*recurfac(n-1)


print("5! : {}".format(factorial(5))) 
print("10! : {}".format(factorial(10)))
print("10! : {}".format(format(recurfac(10) , ',d')))


counter = 0

def fibonacci(n):
    global counter
    counter += 1
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print("fibonacci(3):", fibonacci(3))
print("fibonacci(35):", fibonacci(35))
print("fibonacci(35) 계산에 사용된 덧셈의 횟수는 {}번 입니다.".format(counter))