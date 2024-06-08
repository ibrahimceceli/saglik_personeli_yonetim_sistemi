from Personel import Personel

class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)        
        self.uzmanlik = uzmanlik
        self.deneyim_yili = deneyim_yili
        self.hastane = hastane

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
    
    def get_departman(self):
        return self.departman
    
    def set_departman(self, yeni_departman):
        self.departman = yeni_departman
        
    def get_maas(self):
        return self.maas
    
    def set_maas(self, yeni_maas):
        self.maas = yeni_maas

    def get_uzmanlik(self):
        return self.uzmanlik
        
    def set_uzmanlik(self, yeni_uzmanlik):
        self.uzmanlik = yeni_uzmanlik 
        
    def get_deneyim_yili(self):
        return self.deneyim_yili
        
    def set_deneyim_yili(self, yeni_deneyim_yili):
        self.deneyim_yili = yeni_deneyim_yili 
        
    def get_hastane(self):
        return self.hastane
        
    def set_hastane(self, yeni_hastane):
        self.hastane = yeni_hastane

    def maas_arttir(self):
        yuzde = 10
        self.maas = self.maas + self.maas/yuzde
        return "Yeni Maaş: {}".format(self.maas)

    def __str__(self):
        return "Doktor Bilgileri:\n   Personel No: {}\n   Ad: {}\n   Soyad: {}\n   Departman: {}\n   Maas: {}\n   Uzmanlik: {}\n   Deneyim Yili: {}\n   Hastane: {}".format(
            self.personel_no,
            self.ad,
            self.soyad,
            self.departman,
            self.maas,
            self.uzmanlik,
            self.deneyim_yili,
            self.hastane)
    
doktor1 = Doktor("no", "ad", "soyad", "departman", 10000, "uzmanlik", "yil", "hastane")
#doktor2 = Doktor("no", "ad", "soyad", "departman", "maas", "uzmanlik", "yil", "hastane")
#doktor3 = Doktor("no", "ad", "soyad", "departman", "maas", "uzmanlik", "yil", "hastane")
print(doktor1)
#print(doktor2)
#print(doktor3)
print(doktor1.maas_arttir())

