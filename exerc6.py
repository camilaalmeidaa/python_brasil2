def compara():
    
    num1 = float(input("*Exercicio6* Digite um numero: "))
    num2 = float(input("*Exercicio6* Digite outro numero: "))
    num3 = float(input("*Exercicio6* Digite outro numero: "))
    
    if(num1 > num2 and num1 > num3):
        
        print(num1,"é o maior numero\n")
    
    elif(num2 > num1 and num2 > num3):
        
        print(num2,"é o maior numero\n")
    
    else:
        
        print(num3,"é o maior numero\n")
    