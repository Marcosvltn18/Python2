#--------------------------------------------------------------------
# Ejercicio 6
# a) div_nat(n, m), si m > n devuelve 0, si m <= n div_nat(n-m,m) + 1

def div_nat(m,n):
    '''
    Diseño de datos:
    n: integer
    m: integer 
    Signatura:
    div_nat: (int,int) -> int
    Proposito:
    Calcula el numero div_nat de un numero entero dado.
    Ejemplo:
    div_nat(2,1) = 0
    div_nat(2,2) = 1
    div_nat(1,2) = 2
    '''
    if (n > m):
        return 0
    else:
        return 1 + div_nat(m-n,n) 
    
def test_div_nat():
    for x in range(1, 500):
        for y in range(1, 500):
            assert div_nat(x,y) == x // y



