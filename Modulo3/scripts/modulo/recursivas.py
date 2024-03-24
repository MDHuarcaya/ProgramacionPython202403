def factorial_recursivo(n:int):
    """Define el factorial recursivo"""
    if n==1 or n==0:
        return 1
    elif n<0:
        return 'Error'
    return n * factorial_recursivo(n-1)




# x = factorial_recursivo(5)
# print(x)
if __name__=='__main__':
    x = factorial_recursivo(5)
    print(x)
