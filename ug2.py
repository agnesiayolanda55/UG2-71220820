def hitung_volume_tabung(diameter, tinggi):
    jari_jari = diameter / 2
    volume = 3.14 * (jari_jari ** 2) * tinggi
    return volume

def hitung_volume_kubus(sisi):
    volume = sisi ** 3
    return volume

def hitung_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

print("==================== KALKULATOR CERDAS ==================== ")
print("Pilihlah bangun yang ingin anda hitung(inputan angka saja:)")
print(" 1.Tabung\n","2.Kubus\n","3.Balok\n")

pilihan = int(input(">>"))

if pilihan==1:
    diameter = int(input("Masukkan diameter(cm):"))
    tinggi = int(input("Masukkan tinggi:"))
    volume_tabung = hitung_volume_tabung(diameter, tinggi)
    print("Volume tabung adalah " ,volume_tabung,  "cm")
elif pilihan == 2:
    sisi = int(input("Masukkan sisi(cm) : "))
    volume_kubus = hitung_volume_kubus(sisi)
    print("Volume kubus adalah" ,volume_kubus,  "cm")
elif pilihan == 3:
    panjang = int(input("Masukkan panjang cm) : "))
    lebar = int(input("Masukkan lebar(cm) : "))
    tinggi = int(input("Masukkan tinggi(cm) : "))
    volume_balok = hitung_volume_balok(panjang, lebar, tinggi)
    print("Volume balok adalah",volume_balok, "cm")



