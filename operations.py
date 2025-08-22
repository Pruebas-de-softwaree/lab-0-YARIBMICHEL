def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    
    return a / b  

def power(a, b):
    return a ^ b  

def square_root(x):
    import math
    return math.sqrt(x)

def average(list):
    return sum(list) / len(list)

def maximum(list):
    return min(list) 


if __name__ == "__main__":

    print("start test")

    print(add(2,3))
    print(add(7,2))
    print(subtract(9,3))
    print(multiply(7,2))
    #print(divide(6,0)) #error, no se divide entre 0
    #print(power(2,0)) #error, cualquier numero a la potencia 0 es 1
    #print(square_root(-100))# no hay raices negativas
    print(average()) #no hay promedios de listas vacias



    print("MID test 2")







    print("end test")

