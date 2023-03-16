import matplotlib.pyplot as plt
from random import randint

def pengunjung():
    ###menginput nama, asal daerah, dan alasan
    nama= str(input("Masukkan Nama            : "))
    daerah = str(input("Masukkan Asal daerah     : "))
    alasan = str(input("Masukkan Alasan Berlibur : "))

    ### merandom angka untuk teka teki
    print("\n==== Sebelum Memilih Wisata",nama,", Silahkan Isi Penjumlahan Terlebih Dahulu ====\n")
    angka1 = randint(0,10)
    angka2 = randint(0,10)
    jawaban = 100
    salah = True
    while(salah):
        jawaban = input("Berapa Penjumlahan Dari "+ str(angka1) + "+" + str(angka2) +" :\n")
        try:
            if(int(jawaban)!=(int(angka1)+int(angka2))):
                print("!!!! Jawaban Salah. Coba Lagi Sampai Benar !!!! \n")
            else :
                salah = False
        except:
            print("Silahkan Masukkan Angka .")
            salah = True
    print("\n< < < Yay Jawaban Kamu Benar > > > ")

    ###mengambil data wisata
    fileWisata = open("wisata.txt", "r")
    wisata = fileWisata.read().split("\n")

    ###menyimpan data kategori dan kabupaten wisata yang ada
    kabupaten = []
    kota = []
    for i in range(len(wisata)):
        cekWisata = wisata[i].split("+&+")
        if (len(cekWisata)>3):
            if(cekWisata[3]=="kabupaten"):
                if(cekWisata[1] not in kabupaten):
                    kabupaten.append(cekWisata[1])
            else:
                if(cekWisata[1] not in kota):
                    kota.append(cekWisata[1])
    fileWisata.close()

    salah = True
    while (salah) :
        print(" ")
        print("= = = Silahkan Pilih = = = ")
        print("Anda Akan Mengunjungi : ")
        print("1. Kabupaten")
        print("2. Kota")
        tempat = input("Pilihan Anda : ")

        if (tempat=='1'):
            ##########################
            ###menampilkan data kabupaten untuk dipilih user
            print("")
            print("Silahkan Pilih Kabupaten Yang Ingin Anda Kunjungi : ")
            for i in range(len(kabupaten)):
                print((i+1), kabupaten[i])
            tempatTerpilih = input("Pilih Tempat : ")
            salahi = True
            while (salahi):
                try :
                    tempatTerpilih = kabupaten[int(tempatTerpilih)-1]
                    salahi = False
                except :
                    print("\nSilahkan Masukkan Angka 1 - " + str(len(kabupaten)))
                    tempatTerpilih = input("Pilih Tempat : ")
            salah = False
        elif (tempat == '2'):
            ##########################
            ###menampilkan data kota untuk dipilih user
            print("")
            print("Silahkan Pilih Kota Yang Ingin Anda Kunjungi : ")
            for i in range(len(kota)):
                print((i+1), kota[i])
            tempatTerpilih = input("Pilih Tempat : ")
            salahi = True
            while (salahi):
                try :
                    tempatTerpilih = kota[int(tempatTerpilih)-1]
                    salahi = False
                except :
                    print("\nSilahkan masukkan angka 1 - " + str(len(kota)))
                    tempatTerpilih = input("Pilih Tempat : ")
            salah = False
        else :
            print("\n! Silahkan Pilih Angka 1 Atau 2 !")

    ##########################
    ###menampilkan tempat wisata yang cocok
    print("")
    print("Berikut Tempat Wisata Yang Mungkin Anda Suka : ")
    fileWisata = open("wisata.txt", "r")
    wisata = fileWisata.read().split("\n")
    tidakDitemukan = True
    urutan = 1
    for i in range(len(wisata)):
        cekWisata = wisata[i].split("+&+")
        if (len(cekWisata)>3):
            kabWisata = cekWisata[1]
            if kabWisata == tempatTerpilih :
                print(urutan, ". "+cekWisata[0] + " => " + cekWisata[2])
                tidakDitemukan = False
                urutan +=1
                print("===================================")
    fileWisata.close()
    if(tidakDitemukan):
        print("Maaf Kami Tidak Menemukan Hasil Wisata Yang Cocok :(")
    print("")
    input("Tekan Y Atau Enter Jika Selesai :)")


def admin():
    ###memasukkan password admin
    print("")
    user = input("Username : ")
    pswd = input("Password : ")

    if(user!= 'admin' or pswd!='admin'):
        print("!!! Maaf, Username atau Password Anda Salah !!!")
        print("")
        print("")
    else :
        berhenti = False
        while(berhenti==False):
            print("")
            print("")
            print("Menu Admin :")
            print("1. Tambah Data Wisata")
            print("2. Edit Data Wisata")
            print("3. Hapus Data Wisata")
            print("0. Keluar")

            pilihMenu = input("Masukkan Pilihan : ")
        
            print("")

            if(pilihMenu=='1'):
                nama = input("Masukkan Nama Wisata                    : ")
                lokasi = input("Masukkan Lokasi Wisata                  : ")
                keterangan = input("Masukkan Hal Menarik Dari Wisata        : ")
                tempat = input("Pilih 1 Jika Kabupaten Atau 2 Jika Kota : ")
                salah = True
                while(salah):
                    if(tempat=="1"):
                        tempat = "kabupaten"
                        salah=False
                    elif(tempat=="2"):
                        tempat = "kota"
                        salah= False
                    else:
                        print("\n! ! ! Masukkan 1 Atau 2 ! ! !\n ")
                        tempat = input("Pilih 1 Jika Kabupaten Atau 2 Jika Kota : ")
                        salah = True

                fileWisata = open("wisata.txt", "a")
                fileWisata.write("\n"+nama+"+&+"+lokasi+"+&+"+keterangan+"+&+"+tempat)
                fileWisata.close()
                print("= = Selamat Wisata "+nama+" Berhasil Ditambahkan :) = = ")
            elif(pilihMenu=='2'):
                print("Data Wisata Tersimpan : \n")
                fileWisata = open("wisata.txt", "r")
                wisata = fileWisata.read().split("\n")
                for i in range(len(wisata)):
                    cekWisata = wisata[i].split("+&+")
                    if (len(cekWisata)>3):
                        namaWisata = cekWisata[0]
                        lokasiWisata = cekWisata[1]
                        keteranganWisata = cekWisata[2]
                        tempatWisata = cekWisata[3]
                        
                        print(str(i+1) + ". " + namaWisata + " ("+tempatWisata + " "  + lokasiWisata  + ") || " + keteranganWisata) 
                        print("=================================================")
                fileWisata.close()
                print("")
                salah = True
                while(salah):
                    try:
                        dataTerpilih = int(input("Pilih Data Untuk Di Edit : "))
                        salah = False
                        if(dataTerpilih < 1 or dataTerpilih > len(wisata)):
                            print("\nMasukkan 1 - "+str(len(wisata)))
                            salah=True
                    except:
                        print("\nMasukkan 1 - "+str(len(wisata)))
                        salah=True

                nama = input("Masukkan Nama Wisata                    : ")
                lokasi = input("Masukkan Lokasi Wisata                  : ")
                keterangan = input("Masukkan Hal Menarik Dari Wisata        : ")
                tempat = input("Pilih 1 Jika Kabupaten Atau 2 Jika Kota : ")
                salah = True
                while(salah):
                    if(tempat=="1"):
                        tempat = "kabupaten"
                        salah=False
                    elif(tempat=="2"):
                        tempat = "kota"
                        salah= False
                    else:
                        print("Masukkan 1 Atau 2")
                        tempat = input("Pilih 1 Jika Kabupaten Atau 2 Jika Kota : ")
                        salah = True

                dataBaru = ""
                fileWisata = open("wisata.txt", "r")
                wisata = fileWisata.read().split("\n")
                for i in range(len(wisata)):
                    if(dataTerpilih-1 != i):
                        dataBaru += wisata[i]
                    else:
                        dataBaru += nama+"+&+"+lokasi+"+&+"+keterangan+"+&+"+tempat
                    
                    if(i+1!=len(wisata)):
                        dataBaru+= "\n"
                fileWisata.close()

                fileWisata = open("wisata.txt", "w")
                fileWisata.write(dataBaru)
                fileWisata.close()

                print("\n= = = Selamat !!! Data Berhasil Diubah = = =")
                
            elif(pilihMenu=='3'):
                print("Data Wisata Tersimpan    : \n")
                fileWisata = open("wisata.txt", "r")
                wisata = fileWisata.read().split("\n")
                for i in range(len(wisata)):
                    cekWisata = wisata[i].split("+&+")
                    if (len(cekWisata)>3):
                        namaWisata = cekWisata[0]
                        lokasiWisata = cekWisata[1]
                        keteranganWisata = cekWisata[2]
                        tempatWisata = cekWisata[3]
                        
                        print(str(i+1) + ". " + namaWisata + " ("+tempatWisata + " " + lokasiWisata  + ") || " + keteranganWisata) 
                        print("=================================================")
                fileWisata.close()
                print("")
                salah = True
                while(salah):
                    try:
                        dataTerpilih = int(input("Pilih Data Untuk Dihapus   : "))
                        salah = False
                        if(dataTerpilih < 1 or dataTerpilih > len(wisata)):
                            print("Masukkan 1 - "+str(len(wisata)))
                            salah=True
                    except:
                        print("Masukkan 1 - "+str(len(wisata)))
                        salah=True

                dataBaru = ""
                fileWisata = open("wisata.txt", "r")
                wisata = fileWisata.read().split("\n")
                for i in range(len(wisata)):
                    if(dataTerpilih-1 != i):
                        dataBaru += wisata[i]
                        if(i+1!=len(wisata)-1):
                            dataBaru+= "\n"
                fileWisata.close()

                fileWisata = open("wisata.txt", "w")
                fileWisata.write(dataBaru)
                fileWisata.close()

                print("\n= = = Selamat Data Berhasil Dihapus = = =")
            elif(pilihMenu=='0'):
                berhenti = True
            else :
                print("Silahkan Masukkan 1 - 3")
def visualisasi():
    berhenti=False
    while(berhenti==False):
        print("")
        print("")
        print("Menu Visualisasi :")
        print("1. Jumlah Wisata Kota dan Kabupaten")
        print("2. Jumlah Wisata di Kota")
        print("3. Jumlah Wisata di Kabupaten")
        print("4. Jumlah Pengunjung Wisata di Kota")
        print("5. Jumlah Pengunjung Wisata di Kabupaten")
        print("0. Keluar")
        
        pilihMenu = input("Pilihan : ")
        
        print("")
        print("")
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
        bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]

        if(pilihMenu=='1'):
            ###mengambil data wisata
            fileWisata = open("wisata.txt", "r")
            wisata = fileWisata.read().split("\n")

            ###menghitung data kategori dan kabupaten wisata yang ada
            kabupaten = 0
            kota = 0
            print(len(wisata))
            for i in range(len(wisata)):
                cekWisata = wisata[i].split("+&+")
                if (len(cekWisata)>3):
                    if(cekWisata[3]=="kabupaten"):
                        kabupaten+=1
                    elif(cekWisata[3]=="kota"):
                        kota+=1
            fileWisata.close()
            
            labels = ['Kota', 'Kabupaten']
            quantity = [kota, kabupaten]
            colors = ['yellowgreen', 'lightskyblue']

            total = sum(quantity)

            plt.title('Jumlah Tempat Wisata')
            plt.pie(quantity, labels=labels, colors=colors,
                    autopct=lambda s: '{:.0f}'.format(s * total / 100), shadow=True, startangle=90)

            plt.axis('equal')
            plt.show()
        elif(pilihMenu=='2'):
            ###mengambil data wisata
            fileWisata = open("wisata.txt", "r")
            wisata = fileWisata.read().split("\n")

            ###menyimpan data kategori dan kabupaten wisata yang ada
            tempat = []
            jumlah = []
            for i in range(len(wisata)):
                cekWisata = wisata[i].split("+&+")
                if (len(cekWisata)>3):
                    if(cekWisata[3]=="kota"):
                        if(cekWisata[1] not in tempat):
                            tempat.append(cekWisata[1])
                            jumlah.append(0)
            for j in range(len(tempat)):
                for k in range(len(wisata)):
                    cekWisata = wisata[k].split("+&+")
                    if (len(cekWisata)>3):
                        if(tempat[j]==cekWisata[1]):
                            jumlah[j]+=1
            fileWisata.close()
            

            plt.figure()
            plt.bar(tempat, jumlah, color=colors)

            plt.title('Jumlah Wisata di Kota')
            plt.ylabel('Jumlah Wisata')

            plt.show()
        elif(pilihMenu=='3'):
            ###mengambil data wisata
            fileWisata = open("wisata.txt", "r")
            wisata = fileWisata.read().split("\n")

            ###menyimpan data kategori dan kabupaten wisata yang ada
            tempat = []
            jumlah = []
            for i in range(len(wisata)):
                cekWisata = wisata[i].split("+&+")
                if (len(cekWisata)>3):
                    if(cekWisata[3]=="kabupaten"):
                        if(cekWisata[1] not in tempat):
                            tempat.append(cekWisata[1])
                            jumlah.append(0)
            for j in range(len(tempat)):
                for k in range(len(wisata)):
                    cekWisata = wisata[k].split("+&+")
                    if (len(cekWisata)>3):
                        if(tempat[j]==cekWisata[1]):
                            jumlah[j]+=1
            fileWisata.close()
            

            plt.figure()
            plt.barh(tempat, jumlah, color=colors)

            plt.title('Jumlah Wisata di Kabupaten')
            plt.xlabel('Jumlah Wisata')

            plt.show()
        
        elif(pilihMenu=='4'):
            ###mengambil data wisata
            fileWisata = open("wisata.txt", "r")
            wisata = fileWisata.read().split("\n")

            ###menyimpan data kategori dan kabupaten wisata yang ada
            tempat = []
            for i in range(len(wisata)):
                cekWisata = wisata[i].split("+&+")
                if (len(cekWisata)>3):
                    if(cekWisata[3]=="kota"):
                        tempat.append(cekWisata[0])
            fileWisata.close()
            print("Pilih Wisata Yang Akan Ditampilkan Data Pengunjungnya")
            for i in range(len(tempat)):
                print(i+1, ". ", tempat[i])
            
            salah = True
            while(salah):
                try:
                    tempatTerpilih = int(input("Pilihan : "))
                    salah = False
                    if(tempatTerpilih < 1 or tempatTerpilih > len(tempat)):
                        print("Masukkan 1 - "+str(len(tempat)))
                        salah=True
                except:
                    print("Masukkan 1 - "+str(len(tempat)))
                    salah=True
    
            jumlah = []
            for i in range(12):
                jumlah.append(randint(200,1000))
            plt.plot(bulan, jumlah)

            plt.xlabel('Bulan')
            plt.ylabel('Jumlah Pengunjung')

            plt.title('Jumlah Pengunjung di Wisata '+tempat[tempatTerpilih-1] + " Tahun 2020")
            plt.grid(True)

            plt.show()
        elif(pilihMenu=='5'):
            ###mengambil data wisata
            fileWisata = open("wisata.txt", "r")
            wisata = fileWisata.read().split("\n")

            ###menyimpan data kategori dan kabupaten wisata yang ada
            tempat = []
            for i in range(len(wisata)):
                cekWisata = wisata[i].split("+&+")
                if (len(cekWisata)>3):
                    if(cekWisata[3]=="kabupaten"):
                        tempat.append(cekWisata[0])
            fileWisata.close()
            print("Pilih Wisata Yang Akan Ditampilkan Data Pengunjungnya ")
            for i in range(len(tempat)):
                print(i+1, ". ", tempat[i])
                
            salah = True
            while(salah):
                try:
                    tempatTerpilih = int(input("Pilihan : "))
                    salah = False
                    if(tempatTerpilih < 1 or tempatTerpilih > len(tempat)):
                        print("Masukkan 1 - "+str(len(tempat)))
                        salah=True
                except:
                    print("Masukkan 1 - "+str(len(tempat)))
                    salah=True
            
            jumlah = []
            for i in range(12):
                jumlah.append(randint(200,1000))
            plt.plot(bulan, jumlah)

            plt.xlabel('Bulan')
            plt.ylabel('Jumlah Pengunjung')

            plt.title('Jumlah Pengunjung di Wisata '+tempat[tempatTerpilih-1] + " Tahun 2020")
            plt.grid(True)

            plt.show()
        elif(pilihMenu=='0'):
            berhenti = True
        else :
            print("Silahkan Masukkan Angka 0 - 5")
        

berhenti = False
while(berhenti==False):
    print(" ")
    print("============================================================")
    print("===== SELAMAT DATANG DI PROGRAM WISATA SUMATERA UTARA ======")
    print("============================================================")
    print(" ")
    print("Menu utama :")
    print("1. Pengunjung")
    print("2. Visualisasi")
    print("3. Admin")
    print("0. Keluar")
    
    pilihMenu = input("Masukkan Angka Pilihan : ")
    
    print("")
    print("")

    if(pilihMenu=='1'):
        print("SELAMAT DATANG! SILAHKAN ISI DATA DIRI TERLEBIH DAHULU :) \n")
        pengunjung()
    elif(pilihMenu=='2'):
        print("\n= = PILIH MANA = = ")
        visualisasi()
    elif(pilihMenu=='3'):
        print("= Masukkan Username dan Password Terlebih Dahulu :) = ")
        admin()
    elif(pilihMenu=='0'):
        print("< < < SAMPAI JUMPA KEMBALI > > > \n")
        berhenti = True
    else :
        print("Silahkan Masukkan Angka Dari 0 - 3")
