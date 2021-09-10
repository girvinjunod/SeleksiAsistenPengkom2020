#Python
#Nama: Girvin Junod
#NIM: 13519096

N = int(input("Masukkan nilai N: ")) #input N
catur = [[0 for j in range(N)] for i in range(N)] #declare array papan catur
for i in range(N): #input elemen catur
    for j in range(N):
        catur[i][j] = input("Masukkan elemen baris " + str(i+1) + " kolom " + str(j+1) + " : ")#asumsi input jumlah ratu benar
#cek danger zone kuda
danger = [[0 for j in range(N+4)] for i in range(N+4)] #array daerah tidak aman buat ratu, dibuat N+4 agar tidak ada error kelebihan dari array
for i in range(N):
    for j in range(N):
        if (catur[i][j] == 'K'): #input semua area yang bisa dijangkau kuda, array dibuat +2 semua agar tidak ada error kelebihan array
            danger[i+2+2][j+2+1] = 1
            danger[i+2+2][j+2-1] = 1
            danger[i+2-2][j+2+1] = 1
            danger[i+2-2][j+2-1] = 1
            danger[i +2 +1][j+2+2] = 1
            danger[i +2 -1][j+2+2] = 1
            danger[i +2 +1][j+2-2] = 1
            danger[i+2-1][j+2-2] = 1
safe = 1
for i in range(N): #Pengecekkan keamanan ratu
    for j in range(N):
        if catur[i][j] == 'R':
            if danger[i+2][j+2] == 1:
                safe = 0
if safe ==0:
    print("Ratu tidak aman dari serangan kuda.")
else:
    print("Ratu aman dari serangan kuda.")