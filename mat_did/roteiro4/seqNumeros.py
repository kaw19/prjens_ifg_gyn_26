def printCrescente(n):          # define a função
    for i in range(n):          # imprime de '1' a 'n'
        print(i+1, end=", ")
    print("\b\b.")

def printDecrescente(n):        # define a função
    for i in range(n):          # imprime de 'n' a '1'
        print(n-i, end=", ")
    print("\b\b.")