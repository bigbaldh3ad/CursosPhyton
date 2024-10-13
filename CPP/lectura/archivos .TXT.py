#Leer un archivo linea por linea
"""with open ('Historia.txt','r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas las lineas en una lista
"""with open ('Historia.txt','r') as file:
    lines = file.readline()
    print(lines)"""

#Añadir texto
"""with open ('Historia.txt','a') as file:  
    file.write("\n\n By:Fernando GPT") """
    
#sobreescribir texto
with open ('Historia.txt','w') as file:
       file.write("\n\n By:FernandoshgahgT")
       