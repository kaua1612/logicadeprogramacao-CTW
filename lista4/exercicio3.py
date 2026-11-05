desg = 0 
ciclo = 0

while desg < 500:
    ciclo += 1 
    if ciclo > 70 : 
        desg += 10
    
    elif ciclo <= 70 :
        desg +=7 

print("O número de ciclos foi de: ",ciclo)
print("A quantidade de desgaste foi de: ",desg)