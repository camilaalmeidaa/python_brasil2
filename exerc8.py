def preco():
    
    p1 = float(input("*Exercicio8* Digite o preco do primeiro produto: "))
    p2 = float(input("*Exercicio8* Digite o preco do segundo produto: "))
    p3 = float(input("*Exercicio8* Digite o preco do terceiro produto: "))
    
    menor = 0
    
    if(p1 < p2 and p1 < p3):
        
        menor = p1
        print("O produto mais barato custa R$",menor,"e é o primeiro produto\n")
    
    elif(p2 < p1 and p2 < p3):
        
        menor = p2
        print("O produto mais barato custa R$",menor,"e é o segundo produto\n")
        
    else:
        
        menor = p3
        print("O produto mais barato custa R$",menor,"e é o terceiro produto\n")
        
  