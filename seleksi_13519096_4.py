#Python
#Nama: Girvin Junod
#NIM: 13519096

N = int(input("Masukkan nilai N: "))#input nilai N
K = int(input("Masukkan nilai K: ")) #input nilai K
digit = [0 for i in range(N)] #declare array digit
for i in range(N):
    digit[i] = int(input("Masukkan digit ke "+ str(i+1)+ " : ")) #input elemen digit
sum = 0
i = 0
while (N>0):#Merubah ke basis 10
    sum+= digit[i]*(K**(N-1))
    N-=1
    i +=1
print("Bilangan dalam basis 10 adalah " + str(sum))