def compara2():
    
    num1 = float(input("*Exercicio7* Digite um numero: "))
    num2 = float(input("*Exercicio7* Digite outro numero: "))
    num3 = float(input("*Exercicio7* Digite outro numero: "))
    maior = 0
    menor = 0
    
    if(num1 > num2 and num1 > num3 and num2 < num3):
        
        maior = num1
        menor = num2
    
    elif(num1 > num2 and num1 > num3 and num3 < num2):
        
        maior = num1
        menor = num3
    
    elif(num2 > num1 and num2 > num3 and num1 < num3):
        
        maior = num2
        menor = num1
    
    elif(num2 > num1 and num2 > num3 and num3 < num1):
        
        maior = num2
        menor = num3
    
    
    elif(num3 > num1 and num3 > num2 and num1 < num2):
        
        maior = num3
        menor = num1
    
    else:
        
        maior = num3
        menor = num2
        
    print("O maior numero é",maior,"e o menor numero é",menor,"\n")
        
    