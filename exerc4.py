def letra():
    
    let = input("*Exercicio4* Digite uma letra: ")
    
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    if(let == 'a' or let == 'e' or let == 'i' or let =='o' or let == 'u' or let == 'A' or let == 'E' or let == 'I' or let == 'O' or let == 'U'):
        
        print("A letra é uma vogal\n")
    
    else:
        
        print("A letra é uma consoante\n")