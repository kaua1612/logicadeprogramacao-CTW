ciclo = 0 

temp = float(input("Digite a temperatura do forno: "))

while temp < 1000: 
    if temp < 800:
        temp = temp+50
        
    
    elif temp >= 800 and temp <1000 :
        temp = temp + 20
        
    
    else:
        print("Sua temperatura já esta maior ou igual a 1000! ")
    
    ciclo += 1 

print("A quantidade de ciclos necessarios foi de: ",ciclo)
print("A temperatura final é de: ",temp)
