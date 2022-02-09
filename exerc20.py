def aprova():
    
    n1 = float(input("*Exercicio20* Digite a primeira nota: "))
    n2 = float(input("*Exercicio20* Digite a segunda nota: "))
    n3 = float(input("*Exercicio20* Digite a terceira nota: "))
    
    media = (n1 + n2 + n3) / 3
    
    if(media == 10):
        
        print("Média:",media,"Aprovado com distinção\n")
    
    elif(media >= 7):
        
        print("Média:",media,"Aprovado\n")
        
    else:
        
        print("Média:",media,"Reprovado\n")