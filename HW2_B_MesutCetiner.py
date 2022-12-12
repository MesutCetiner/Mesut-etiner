#sayıdan büyük veya eşit en küçük asal sayıyı bulma:

def asal_sayi(sayi):
    if(sayi==1): 
        return False
    elif(sayi==2): 
        return True
    else:
        for i in range(2,sayi): 
           if(sayi%i==0):
                return False
        return True
sayi=int(input("Bir sayı giriniz:"))
while True:
    if(asal_sayi(sayi)):
        print(sayi)
        break
    else: 
        sayi+=1