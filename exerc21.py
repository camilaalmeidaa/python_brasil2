def caixa():
    
    saque = int(input("*Exercicio21* Digite o valor do saque (minimo: 6 e maximo: 600): "))
    
    cem = saque // 100
    cinquenta = (saque - (cem * 100)) // 50
    dez = ((saque - (cem * 100) ) - (cinquenta * 50)) // 10
    cinco = ((saque - (cem * 100) ) - (cinquenta * 50) - (dez * 10)) // 5
    um = ((saque - (cem * 100) ) - (cinquenta * 50) - (dez * 10)) % 5
    
    
    
    if((saque >= 6) and (saque <= 600)):
        
        print("Saque:",saque,"=",cem,"nota(s) de 100",cinquenta,"nota(s) de 50",dez,"nota(s) de 10",cinco,"nota(s) de 5 e",um,"nota(s) de 1\n")
    
    else:
        
        print("Valor inválido\n")
        
    
   
    
    
    