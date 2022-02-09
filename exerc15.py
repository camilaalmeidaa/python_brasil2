def triangulo():
    
    l1 = float(input("*Exercicio15* Digite o tamanho do primeiro lado do triangulo: "))
    l2 = float(input("*Exercicio15* Digite o tamanho do segundo lado do triangulo: "))
    l3 = float(input("*Exercicio15* Digite o tamanho do terceiro lado do triangulo: "))
    
    if((l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2):
        
        if(l1 == l2 == l3):
            
            print("Triangulo Equilatero\n")
        
        elif(l1 == l2 or l1 == l3 or l2 == l3):
            
            print("Triangulo Isosceles\n")
        
        else:
            
            print("Triangulo Escaleno\n")
        
    else:
        
        print("Não podemos formar um triangulo como os lados informados.\n")