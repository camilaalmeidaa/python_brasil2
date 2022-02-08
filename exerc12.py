def salario():
    
    valor_hora = float(input("*Exercicio12* Digite o valor ganho por hora: "))
    horas = float(input("*Exercicio12* Digite a quantidade de horas trabalhadas no mes: "))
    
    salario_bruto = valor_hora * horas
    inss = 0.1 * salario_bruto
    fgts = 0.11 * salario_bruto
    
    if(salario_bruto > 2500):
        
        ir = 0.2 * salario_bruto
        descontos = ir + inss
        salario_liquido = salario_bruto - descontos
        
        print("Salário Bruto: R$",salario_bruto,"\n(-) IR (20%): R$",ir,"\n(-) INSS (10%): R$",inss,"\nFGTS (11%): R$",fgts,"\nTotal de descontos: R$",descontos,"\nSalario liquido: R$",salario_liquido,"\n")
    
    elif(salario_bruto > 1500):
        
        ir = 0.1 * salario_bruto
        descontos = ir + inss
        salario_liquido = salario_bruto - descontos
    
        print("Salário Bruto: R$",salario_bruto,"\n(-) IR (10%): R$",ir,"\n(-) INSS (10%): R$",inss,"\nFGTS (11%): R$",fgts,"\nTotal de descontos: R$",descontos,"\nSalario liquido: R$",salario_liquido,"\n")
        
    elif(salario_bruto > 900):
        
        ir = 0.05 * salario_bruto
        descontos = ir + inss
        salario_liquido = salario_bruto - descontos
    
        print("Salário Bruto: R$",salario_bruto,"\n(-) IR (5%): R$",ir,"\n(-) INSS (10%): R$",inss,"\nFGTS (11%): R$",fgts,"\nTotal de descontos: R$",descontos,"\nSalario liquido: R$",salario_liquido,"\n")
        
    else:
        
        ir = 0
        descontos = ir + inss
        salario_liquido = salario_bruto - descontos
    
        print("Salário Bruto: R$",salario_bruto,"\n(-) IR (isento): ----\n(-) INSS (10%): R$",inss,"\nFGTS (11%): R$",fgts,"\nTotal de descontos: R$",descontos,"\nSalario liquido: R$",salario_liquido,"\n")
        
        