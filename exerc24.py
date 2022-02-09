def escolha_operacao():
    
    n1 = float(input("*Exercicio24* Digite um numero: "))
    n2 = float(input("*Exercicio24* Digite outro numero: "))
    
    opcao = input("*Exercicio24* Digite qual operacao voce deseja realizar: a - par ou impar / b - positivo ou negativo / c - inteiro ou decimal: ")
    
    if(opcao == 'a'):
        
        if((n1 % 2 == 0) and (n2 % 2 == 0)):
            
            print(n1,"e",n2,"são pares\n")
        
        elif((n1 % 2 == 0) and (n2 % 2 != 0)):
            
            print(n1,"é par e",n2,"é ímpar\n")
        
        elif((n2 % 2 == 0) and (n1 % 2 != 0)):
            
            print(n2,"é par e",n1,"é ímpar\n")
            
        else:
            
            print(n1,"e",n2,"são ímpares\n")
            
    elif(opcao == 'b'):
        
        if((n1 > 0) and (n2 > 0)):
            
            print(n1,"e",n2,"são positivos\n")
        
        elif((n1 > 0) and (n2 < 0)):
            
            print(n1,"é positivo e",n2,"é negativo\n")
        
        elif((n2 > 0) and (n1 < 0)):
            
            print(n2,"é positivo e",n1,"é negativo\n")
        
        else:
            
            print(n1,"e",n2,"são negativos\n")
    
    elif(opcao == 'c'):
        
        if((n1 // 1 == n1) and (n2 // 1 == n2)): 
            
            print(n1,"e",n2,"são inteiros\n")
        
        elif((n1 // 1 == n1) and (n2 // 1 != n2)):
            
            print(n1,"é inteiro e",n2,"é decimal\n")
            
        elif((n2 // 1 == n2) and (n1 // 1 != n1)):
            
            print(n2,"é inteiro e",n1,"é decimal\n")
        
        else:
            
            print(n1,"e",n2,"são decimais\n")
            
            
    