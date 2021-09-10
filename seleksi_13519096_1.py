#Python
#Nama: Girvin Junod
#NIM: 13519096

N = int(input("Masukkan jumlah ronde: ")) #input jumlah ronde
mor = input("Masukkan urutan Tuan Mor: ") #asumsi input string selalu sesuai jumlah N dan benar
vin = input("Masukkan urutan Tuan Vin: ")
skorm = 0
skorv = 0
for i in range(N): #mengecek menang kalah
    if (mor[i] == 'P' and vin[i] == 'R'):
        skorm +=1
    elif (mor[i] == 'S' and vin[i] == 'P'):
        skorm +=1
    elif (mor[i] == 'R' and vin[i] == 'S'):
        skorm +=1
    elif (vin[i] == 'P' and mor[i] == 'R'):
        skorv += 1
    elif (vin[i] == 'S' and mor[i] == 'P'):
        skorv += 1
    elif (vin[i] == 'R' and mor[i] == 'S'):
        skorv += 1
if skorv > skorm:
    print("Pemenangnya adalah Tuan Vin.")
elif skorm > skorv:
    print("Pemenangnya adalah Tuan Mor.")
else:
    print("Permainan berakhir seri.")