def posto():
    
    comb = input("*Exercicio26* Digite o tipo de combustivel: A - Alcool e G - Gasolina: ")
    litros = float(input("*Exercicio26* Digite a quantidade de litros: "))
    
    if((comb == 'a') or (comb == 'A')):
        
        if(litros <= 20):
            
            preco_litro = 0.97 * 1.9
            preco = litros * preco_litro
        
        else:
            
            preco_litro = 0.95 * 1.9
            preco = litros * preco_litro
            
    elif((comb == 'g') or (comb == 'G')):
        
        if(litros <= 20):
            
            preco_litro = 0.96 * 2.5
            preco = litros * preco_litro
            
        
        else:
            
            preco_litro = 0.94 * 2.5
            preco = litros * preco_litro
            
    else:
        
        print("Escolha invalida. Digite novamente\n")
        
    print("Valor: R$",preco,"\n")
            