def is_prime(num):
    divisores = 0
    for i in range(1,num+1):
        if num % i == 0:
            divisores += 1
    
    if divisores != 2:
        return print("Não é primo")
    else:
        return print("É primo")
    

is_prime(97)
