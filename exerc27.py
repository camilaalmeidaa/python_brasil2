def frutas():
    
    morangos = float(input("*Exercicio 27* Digite a quantidade em kg de morangos: "))
    macas = float(input("*Exercicio 27* Digite a quantidade em kg de macas: "))
    
    peso = morangos + macas
    
    if(morangos > 5):
        
        preco_morango = 2.2 * morangos
        
    else:
        
        preco_morango = 2.5 * morangos
    
    
    if(macas > 5):
        
        preco_maca = 1.5 * macas
    
    else:
        
        preco_maca = 1.8 * macas
        
        
    valor_total = preco_morango + preco_maca
    
    if((peso > 8) or (valor_total > 25)):
        
        preco_final = 0.9 * valor_total
        
    else:
        
        preco_final = valor_total
        
    print("Valor: R$",preco_final,"\n")