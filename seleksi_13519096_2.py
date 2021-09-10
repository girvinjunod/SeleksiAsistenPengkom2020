#Python
#Nama: Girvin Junod
#NIM: 13519096

N = int(input("Masukkan jumlah elemen array: ")) #input N
a = [0 for i in range(N)] #declare array
for i in range(N): #input elemen array
    a[i] = int(input("Masukkan elemen array ke "+ str(i+1) +" : "))
if (N != 1): #cek kasus 1 elemen, dianggap 1 elemen bukan baris
    cekgeo = 1
    cekarit = 1
else:
    cekgeo = 0
    cekarit = 0
#cek geometri
i = 0
while ((i< N-1) and cekgeo == 1):
    if ((a[i+1] % a[i]) != 0): #kalau baris geometri maka harusnya setiap elemen i+1 jika dibagi elemen i tidak ada sisa
        cekgeo = 0
    i +=1
#cek arit
j = 2
while ((j<N) and cekarit==1): #kalau baris aritmatika maka selisih elemen i+1 dan i sama
    selisih = a[1] - a[0] #declare selisih dimasukkan ke dalam loop agar tidak error ketika N = 1
    if (a[j] - a[j-1] != selisih):
        cekarit = 0
    j +=1
if (cekarit == 1 and cekgeo ==1):
    print("Array membentuk barisan geometri dan membentuk barisan aritmatika.")
elif (cekarit == 1 and cekgeo ==0):
    print("Array tidak membentuk barisan geometri dan membentuk barisan aritmatika.")
elif (cekarit == 0 and cekgeo ==1):
    print("Array membentuk barisan geometri dan tidak membentuk barisan aritmatika.")
else:
    print("Array tidak membentuk barisan geometri dan tidak membentuk barisan aritmatika.")