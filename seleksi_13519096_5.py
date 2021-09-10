#Python
#Nama: Girvin Junod
#NIM: 13519096

N = int(input("Masukkan nilai N: ")) #input N
array = [0 for i in range(N*3)] #declare array
totdetik = [0 for i in range(N)] #declare array total detik
count = 1
for i in range(0, N*3, 3):#asumsi input jam benar, input elemen jam, menit, detik per jam
    array[i] = int(input("Masukkan jam dari jam ke " + str(count) + " : "))
    array[i+1] =int(input("Masukkan menit dari jam ke " + str(count) + " : "))
    array[i+2] =int(input("Masukkan detik dari jam ke " + str(count) + " : "))
    totdetik[count-1] = array[i]*3600 + array[i+1]*60 + array[i+2] #konversi ke detik semua
    count+=1
max = 0
for i in range(N): #Pengecekkan jarak max atau terlama
    for j in range(N):
        if (abs(totdetik[i] - totdetik[j]) > max):
            max = abs(totdetik[i] - totdetik[j])
hasiljam = max // 3600 #Menkonversi dari total detik balik ke jam menit detik
hasilmenit = (max - (hasiljam*3600))//60
hasildetik = (max - (hasiljam*3600) - (hasilmenit*60))
print("Jarak terlama yang didapat adalah "+ str(hasiljam) + " jam " + str(hasilmenit) + " menit " + str(hasildetik) + " detik.")

