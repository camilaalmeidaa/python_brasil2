def reajuste():
    
    salario = float(input("*Exercicio11* Digite seu salário: "))
    
    if(salario >= 1500):
        
        reajuste = 0.05 * salario
        novo_salario = salario + reajuste 
        
        print("O salário antes do reajuste:",salario,"\nO percentual de aumento aplicado: 5%\nO valor do aumento:",reajuste,"\nO novo salário:",novo_salario,"\n")
    
    elif(salario > 700):
        
        reajuste = 0.1 * salario
        novo_salario = salario + reajuste 

        print("O salário antes do reajuste:",salario,"\nO percentual de aumento aplicado: 10%\nO valor do aumento:",reajuste,"\nO novo salário:",novo_salario,"\n")
    
    elif(salario > 280):
        
        reajuste = 0.15 * salario
        novo_salario = salario + reajuste 
        
        print("O salário antes do reajuste:",salario,"\nO percentual de aumento aplicado: 15%\nO valor do aumento:",reajuste,"\nO novo salário:",novo_salario,"\n")
    
    else:
        
        reajuste = 0.2 * salario
        novo_salario = salario + reajuste 
        
        print("O salário antes do reajuste:",salario,"\nO percentual de aumento aplicado: 20%\nO valor do aumento:",reajuste,"\nO novo salário:",novo_salario,"\n")