def sexo():
    
    sex = input("*Exercicio3* Digite F para feminino e M para masculino: ")
    
    if(sex == 'F' or sex == 'f'):
        
        print("F - Feminino\n")
        
    elif(sex == 'M' or sex == 'm'):
        
        print("M - Masculino\n")
    
    else:
        
        print("Sexo inválido\n")