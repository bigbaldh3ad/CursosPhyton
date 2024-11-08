#Ley de la suma

#CRECE CON RESPECTO A n DE MANERA LINEAL
def f(n):
    for i in range(n):
        print(i)
    
        
    for i in range(n):
        print(i)
        
    
# O(n) + O(n) = O(n + n) = O(2n) = O(n) -> #(LA FUNCION CRECE EN O DE N )
#ESTA FUNCION TIENE CRECIMIENTO LINEAL      




#Ley de la suma 

def f(n):
    
    #sigue creciendo de manera lineal
    for i in range(n):
        print(i)
    
    #crece en n por n 
    for i in range(n * n): #este es el loop que importa mas 
        print(i)

 
#ESTO QUIERE DECIR QUE ESTA FUNCION ES CUADRATICA       
# O(n) + O(n * n ) = O(n + n^2) = O(n^2)


#Ley de la Multiplicacion 

def f (n):
    
    
    for i in range (n):
        
        for j  in range (n):
            print(i , j)



# O(n) * O(n) = O(n * n) = O(n^2)


# Recursividad multiple 

def fibonaci (n):
    
    if n == 0 or n == 1:
        return 1
        
    return  fibonaci(n - 1) + fibonaci(n - 2)

# O(2**n) 

            