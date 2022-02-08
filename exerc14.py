def conceito():
    
    n1 = float(input("*Exercicio14* Digite a primeira nota: "))
    n2 = float(input("*Exercicio14* Digite a segunda nota: "))
    
    media = (n1 + n2) / 2
    
    if(media >= 9):
        
        conceito = 'A'
        print("Notas:",n1,n2,"\nMédia:",media,"\nConceito:",conceito,"\nAPROVADO")
        
    elif(media >= 7.5):
        
        conceito = 'B'
        print("Notas:",n1,n2,"\nMédia:",media,"\nConceito:",conceito,"\nAPROVADO")
        
    
    elif(media >= 6):
        
        conceito = 'C'
        print("Notas:",n1,n2,"\nMédia:",media,"\nConceito:",conceito,"\nAPROVADO")
        
    
    elif(media >= 4):
        
        conceito = 'D'
        print("Notas:",n1,n2,"\nMédia:",media,"\nConceito:",conceito,"\nREPROVADO")
        
    else:
        
        conceito = 'E'
        print("Notas:",n1,n2,"\nMédia:",media,"\nConceito:",conceito,"\nREPROVADO")
      