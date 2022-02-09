def num():
    
    numero = int(input("*Exercicio19* Digite um numero menor que 1000: "))
    
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10
    
    if(numero >= 1000):
        
        print("O numero precisa ser menor que 1000. Digite outro numero.\n")
        
    else:
        
        print("O numero tem:",centena,"centena(s),",dezena,"dezena(s) e",unidade,"unidade(s)\n")
    