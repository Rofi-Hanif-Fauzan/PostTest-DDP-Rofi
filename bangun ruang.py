# Nama: Rofi Hanif Fauzan
# Nim: 2309116026


print ("Selamat datang di kalkulator volume bangun ruang")
print ("------")
print ("Silahakan pilih bangun ruang yang ingin dihitung volumenya:")
print ("1. Bola")
print ("2. Tabung")
print ("3. Limas")

while True:
    operasi = int(input("Pilih bangun ruang: "))


    if operasi == 1:
        phi = 3.14
        jari_jari = float(input("Masukkan jari-jari: "))
        jari_pangkat = jari_jari**3
        volume = (4/3)*phi*jari_pangkat

        print(f"Volume = (4/3) x {phi} x {jari_pangkat}")
        print(f"Hasilnya adalah = {volume}")
        lanjut = str(input("Mau hitung lagi? (y/t): "))
        if lanjut == "t":
            break

        elif lanjut == "y":
            continue
        else:
            print("Tidak valid")

    elif operasi == 2:
        phi2 = 3.14
        jari_jari2 = float(input("Masukkan jari-jari: "))
        tinggi = float(input("Masukkan tinggi: "))
        jari_pangkat2 = jari_jari2**2
        volume2 = phi2*jari_pangkat2*tinggi

        print(f"Volume = {phi2} x {jari_pangkat2} x {tinggi}")
        print(f"Hasilnya adalah = {volume2}")
        lanjut = str(input("Mau hitung lagi? (y/t): "))
        if lanjut == "t":
            break

        elif lanjut == "y":
            continue
        else:
            print("Tidak valid")

    elif operasi == 3:
        luas_alas = float(input("Masukkan luas alas: "))
        tinggi2 = float(input("Masukkan tinggi: "))
        volume3 = (1/3)*luas_alas*tinggi2

        print(f"Volume = (1/3) x {luas_alas} x {tinggi2}")
        print(f"Hasilnya adalah = {volume3}")
        lanjut = str(input("Mau hitung lagi? (y/t): "))
        if lanjut == "t":
            break

        elif lanjut == "y":
            continue
        else:
            print("Tidak valid")

    else:
        print("Tolong masukkan angka yang benar :)")