def equacao():
    
    a = float(input("*Exercicio16* Digite o 'a' da equacao de 2 grau: "))
    b = float(input("*Exercicio16* Digite o 'b' da equacao de 2 grau: "))
    c = float(input("*Exercicio16* Digite o 'c' da equacao de 2 grau: "))
    
    delta = ((b * b) - (4 * a * c))
    raiz1 = (-b + (delta ** 1/2))/2*a
    raiz2 = (-b - (delta ** 1/2))/2*a
    
    if(a == 0):
        
        print("Essa equacao não é de segundo grau\n")
    
    else:
        
        if(delta == 0):
            
            print("A equacao não possui raizes reais\n")
        
        elif(delta == 1):
            
            print("A raiz da equacao é:",raiz1,"\n")
        
        else:
            
            print("As raizes da equacao são:",raiz1, raiz2,"\n")
        
        