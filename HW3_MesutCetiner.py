#datayı sözlüğe dönüştürme 
data=open("data.txt","w")
data.write("Name: Mesut\nSurname: Cetiner\n Gender: Male\nUsername: Feellikeleven\nJob: Student")
data.close()
data=open("data.txt","r")
data.read()
list=[i for i in data.split('\n') if len(i)>1]
dictionary ={i.split(':')[0]:i.split(':')[1] for i in list}
print(dictionary)
data.close()