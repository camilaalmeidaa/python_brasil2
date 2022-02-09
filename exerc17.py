def bissexto():
    
    ano = int(input("*Exercicio17* Digite um ano e veremos se ele é bissexto: "))
    
    if (ano %4 ==0 and ano % 100 != 0) or (ano % 400 == 0):
        
        print("É bissexto\n")
        
    else:
        
        print("Não é bissexto\n")