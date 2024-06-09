from Personel import personel1, personel2
from Doktor import doktor1, doktor2, doktor3
from Hemsire import hemsire1, hemsire2, hemsire3
from Hasta import hasta1, hasta2, hasta3
import pandas as pd
import numpy as np

def main():
    '''girdi = input("1. Tum personel\n2. Doktor\n3. Hemsire\n4. Hasta\nBilgilerini gostermek istediginiz personeli tuslayiniz: ")

    if(girdi == "1"):
        print("Tum Personel Bilgileri Gosteriliyor...")
        try:
            print(personel1)
            print(personel2)
            print(doktor1)
            print(doktor2)
            print(doktor3)
            print(hemsire1)
            print(hemsire2)
            print(hemsire3)
        except ValueError:
            print("Personel bilgileri gosterilemedi.")
            
    elif(girdi == "2"):
        print("Doktor Bilgileri Gosteriliyor...")
        try:
            print(doktor1)
            print(doktor2)
            print(doktor3)
        except ValueError:
            print("Doktor bilgileri gosterilemedi.")

    elif(girdi == "3"):
        print("Hemsire Bilgileri Gosteriliyor...")
        try:
            print(hemsire1)
            print(hemsire2)
            print(hemsire3)
        except ValueError:
            print("Hemsire bilgileri gosterilemedi.")

    elif(girdi == "4"):
        print("Hasta Bilgileri Gosteriliyor...")
        try:
            print(hasta1)
            print(hasta2)
            print(hasta3)
        except ValueError:
            print("Hasta bilgileri gosterilemedi.")

    else:
        print("\nHatali giris yaptiniz.")'''

    veri = {
    "personel_no": ["PRS1", "PRS2", "DR1", "DR2", "DR3", "HMS1", "HMS2", "HMS3", None, None, None],
    "ad": ["Ferhat", "Kemal", "Ahmet", "Mehmet", "Cenk", "Selin", "Zeynep", "İrem", "Emre", "Salih", "Cemre"],
    "soyad": ["Kara", "Tok", "Yılmaz", "Şahin", "Güçlü", "Kozak", "Akça", "Kabak", "Güneş", "Koca", "Kabak"],
    "departman": ["İş Sağlığı ve Güvenliği", "Hasta Kabul ve Kayıt", "doktor", "doktor", "doktor", "Yenidoğan Hemşireliği", "Ortopedi Hemşireliği", "Yoğun Bakım Hemşireliği", None, None, None],
    "maas": [30000, 35000, 60000, 80000, 90000, 40000, 43000, 38000, None, None, None],
    "uzmanlik": [None, None, "Nefroloji", "El Cerrahisi", "Alerjik Göğüs Hastalıkları", None, None, None, None, None, None],
    "deneyim_yili": [None, None, 14, 23, 19, None, None, None, None, None, None],
    "hastane": [None, None, "İzmir Seyfi Demirsoy Eğitim ve Araştırma Hastanesi", "İzmir Tınaztepe Hastanesi", "İzmir Bozyaka Eğitim ve Araştırma Hastanesi", "İzmir Seyfi Demirsoy Eğitim ve Araştırma Hastanesi", "İzmir Tınaztepe Hastanesi", "İzmir Bozyaka Eğitim ve Araştırma Hastanesi", None, None, None],
    "calisma_saati": [None, None, None, None, None, 45, 49, 47, None, None, None],
    "sertifika": [None, None, None, None, None, "Yenidoğan Yoğun Bakım Hemşireliği", "Hastane Afet ve Acil Durum Planlaması Eğiticisi", "Enfeksiyon Kontrol Hemşireliği", None, None, None],
    "hasta_no": [None, None, None, None, None, None, None, None, "HST1", "HST2", "HST3"],
    "dogum_tarihi": [None, None, None, None, None, None, None, None, "06.03.1987", "13.01.2000", "22.11.1995"],
    "hastalik": [None, None, None, None, None, None, None, None, "Böbrek taşı", "Egzama", "Kızamık"],
    "tedavi": [None, None, None, None, None, None, None, None, "Ağrı kesici ilaç", "Nemlendirici İlaç", "Destekleyici Bakım"]
    }

    df = pd.DataFrame(veri)
    df.fillna(0, inplace=True)
    #print(df)
    
    #doktor_listesi = [personel_no for personel_no in veri["personel_no"] if personel_no and personel_no.startswith("DR")]

    doktorlar = df[df["departman"] == "doktor"]

    uzmanlik_alani = doktorlar.groupby("uzmanlik").size()
    print("Uzmanlık alanlarına göre doktor sayısı:\n", uzmanlik_alani)

    bes_yil_deneyimli_doktorlar = doktorlar[doktorlar["deneyim_yili"] > 5]
    print("\n5 yıldan fazla deneyime sahip doktor sayısı:", bes_yil_deneyimli_doktorlar.shape[0])

    hastalar = df.tail(3)
    print("\nHasta adına göre sıralanmış DataFrame:\n", hastalar)

    '''maas_yedi_bin_ustu = df[df["maas"] > 7000]
    print("Maaşı 7000 TL üzerinde olan personeller:\n", maas_yedi_bin_ustu)

    df["dogum_tarihi"] = pd.to_datetime(df["dogum_tarihi"], errors="coerce")
    dogum_tarihi_filtre = df[(df["dogum_tarihi"] >= "1990-01-01") & (df["departman"] == "Hasta")]
    print("Doğum tarihi 1990 ve sonrası olan hastalar:\n", dogum_tarihi_filtre)

    yeni_df = df[["ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastalik", "tedavi"]]
    print("Yeni DataFrame:\n", yeni_df)'''


if __name__ == "__main__":
    main()