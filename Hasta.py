
class Hasta():
    #Initializer metot
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi, doktor, hemsire):
        self.hasta_no = hasta_no
        self.ad = ad
        self.soyad = soyad
        self.dogum_tarihi = dogum_tarihi
        self.hastalik = hastalik
        self.tedavi = tedavi
        self.doktor = doktor
        self.hemsire = hemsire

    #Get-set metotları
    def get_personel_no(self):
        return self.personel_no
    
    def set_personel_no(self, yeni_personel_no):
        self.personel_no = yeni_personel_no
    
    def get_ad(self):
        return self.ad
    
    def set_ad(self, yeni_ad):
        self.ad = yeni_ad
    
    def get_soyad(self):
        return self.soyad
    
    def set_soyad(self, yeni_soyad):
        self.soyad = yeni_soyad
    
    def get_dogum_tarihi(self):
        return self.dogum_tarihi
    
    def set_dogum_tarihi(self, yeni_dogum_tarihi):
        self.dogum_tarihi = yeni_dogum_tarihi
        
    def get_hastalik(self):
        return self.hastalik
    
    def set_hastalik(self, yeni_hastalik):
        self.hastalik = yeni_hastalik

    def get_tedavi(self):
        return self.tedavi
        
    def set_tedavi(self, yeni_tedavi):
        self.tedavi = yeni_tedavi 

    #Tedavi süresini hesaplayan metot
    def tedavi_suresi_hesapla(self):
        tedavi_suresi = 50 
        return "   Tahmini tedavi süresi: {} gün".format(tedavi_suresi)

    #Str metoduyla hasta bilgilerini yazdırıyoruz
    def __str__(self):
        return "Hasta Bilgileri:\n   Hasta No: {}\n   Ad: {}\n   Soyad: {}\n   Dogum Tarihi: {}\n   Hastalik: {}\n   Tedavi: {}\n   Doktor: {}\n   Hemsire: {}\n".format(
            self.hasta_no,
            self.ad,
            self.soyad,
            self.dogum_tarihi,
            self.hastalik,
            self.tedavi,
            self.doktor,
            self.hemsire)

#Oluşturulan 3 adet hasta nesnesi  
hasta1 = Hasta("HST1", "Emre", "Güneş", "06.03.1987", "Böbrek taşı", "Ağrı kesici ilaç", "Ahmet Yılmaz", "Selin Kozak")
hasta2 = Hasta("HST2", "Salih", "Koca", "13.01.2000", "Egzama", "Nemlendirici İlaç", "Mehmet Şahin", "Zeynep Akça")
hasta3 = Hasta("HST3", "Cemre", "Tokat", "22.11.1995", "Kızamık", "Destekleyici Bakım", "Cenk Güçlü", "İrem Kabak")
#print(hasta1.tedavi_suresi_hesapla())