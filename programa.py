n = 0
alcool = 0
gasolina = 0
diesel = 0
while(n!=4):
    n = int(input())
    if(n = 1):
        alcool+=1
    elif(n=2):
        gasolina+=1
    elif(n=3):
        diesel+=1
print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(alcool,gasolina,diesel))