def decrescente():
    
    num1 = float(input("*Exercicio9* Digite um numero: "))
    num2 = float(input("*Exercicio9* Digite outro numero: "))
    num3 = float(input("*Exercicio9* Digite outro numero: "))
    
    maior = 0
    meio = 0
    menor = 0
    
    if(num1 > num2 and num1 > num3 and num2 > num3):
        
        maior = num1
        meio = num2
        menor = num3
        
    
    elif(num1 > num2 and num1 > num3 and num3 > num2):
        
        maior = num1
        meio = num3 
        menor = num2
    
    elif(num2 > num1 and num2 > num3 and num1 > num3):
        
        maior = num2
        meio = num1
        menor = num3
    
    elif(num2 > num1 and num2 > num3 and num3 > num1):
        
        maior = num2
        meio = num3
        menor = num1
    
    
    elif(num3 > num1 and num3 > num2 and num1 > num2):
        
        maior = num3
        meio = num1
        menor = num2
    
    else:
        
        maior = num3
        meio = num2
        menor = num1
     
    print("A ordem decrescente é:",maior,meio,menor,"\n") 
    
    