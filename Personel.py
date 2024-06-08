class Personel():
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.personel_no = personel_no
        self.ad = ad
        self.soyad = soyad
        self.departman = departman
        self.maas = maas

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

    def __str__(self):
        return "Personel Bilgileri:\n   Personel No: {}\n   Ad: {}\n   Soyad: {}\n   Departman: {}\n   Maas: {}".format(
            self.personel_no,
            self.ad,
            self.soyad,
            self.departman,
            self.maas)

personel1 = Personel("no", "ad", "soyad", "departman", "maas")
personel2 = Personel("no", "ad", "soyad", "departman", "maas")
print(personel1)
print(personel2)




    
        
        