def turno():
    
    opcao = input("*Exercicio10* Digite a opção de turno escolhido: M-matutino ou V-Vespertino ou N- Noturno: ")
    
    if(opcao == 'M' or opcao == 'm'):
        
        print("Bom Dia!")
    
    elif(opcao == 'V' or opcao == 'v'):
        
        print("Boa Tarde!")
    
    elif(opcao == 'N' or opcao == 'n'):
        
        print("Boa Noite!")
        
    else:
        
        print("Valor Inválido!")