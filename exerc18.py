def checa_data():
    
    print("*******DÚVIDA*******")
    
    data = input("*Exercicio18* Digite uma data no formato dd/mm/aaaa: ")
    
    lista = data.split('/')
    valida = False
    
    print(lista[0])
    print(lista[1])
    print(lista[2])
    
    if(((lista[1]) == 1) or ((lista[1]) == 3) or ((lista[1]) == 5) or ((lista[1]) == 7) or ((lista[1]) == 8) or ((lista[1]) == 10) or ((lista[1]) == 12)):
        
        if((lista[0]) <= 31):
            
             valida = True
  
    elif(lista[1] == 4 or lista[1] == 6 or lista[1] == 9 or lista[1] == 11):
        
        if(lista[0] <= 30):
            
             valida = True
             
    elif lista[1] == 2:
       
        if (lista[2] % 4 == 0 and lista[2] % 100 != 0) or (lista[2] % 400 == 0):
            
            if(lista[0] <= 29):
                
                valida = True
                
        elif(lista[0] <= 28):
            
            valida = True
    
    
    if(valida):
        
        print("Data válida\n")
        
    else:
        
        print("Inválida\n")
              
#22/12/2020
    