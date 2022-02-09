def carne():
    
    tipo = input("*Exercicio28* Digite o tipo da carne (File duplo / Alcatra / Picanha): ")
    qtde = float(input("*Exercicio28* Digite a quantidade em kg: "))
    pag = input("*Exercicio28* Digite a forma de pagamento: ")
    
    if(qtde > 5):
        
        if(tipo == 'File duplo'):
            
            preco = 5.8 * qtde
        
        elif(tipo == 'Alcatra'):
            
            preco = 6.8 * qtde
        
        elif(tipo == 'Picanha'):
            
            preco = 7.8 * qtde
    
    else:
        
        if(tipo == 'File duplo'):
            
            preco = 4.9 * qtde
        
        elif(tipo == 'Alcatra'):
            
            preco = 5.9 * qtde
        
        elif(tipo == 'Picanha'):
            
            preco = 6.9 * qtde
    
    if(pag == 'cartao Tabajara'):
        
        preco_total = 0.9 * preco
    
    else:
        
        preco_total = preco
        
    print("Valor: R$",preco)
    
        