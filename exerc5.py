def media():
    
    n1 =  float(input("*Exercicio5* Digite a primeira nota: "))
    n2 =  float(input("*Exercicio5* Digite a segunda nota: "))
    
    media = (n1+n2)/2
    
    if(media == 10):
        
        print("Aprovado com Distinção\n")
        
    elif(media >= 7):
            
        print("Aprovado\n")
    
    else:
        
        print("Reprovado\n")