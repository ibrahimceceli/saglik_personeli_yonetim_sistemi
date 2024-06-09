class Personel():
    #Initializer metot
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.personel_no = personel_no
        self.ad = ad
        self.soyad = soyad
        self.departman = departman
        self.maas = maas

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
    
    def get_departman(self):
        return self.departman
    
    def set_departman(self, yeni_departman):
        self.departman = yeni_departman
        
    def get_maas(self):
        return self.maas
    
    def set_maas(self, yeni_maas):
        self.maas = yeni_maas

    #Str metoduyla personel bilgilerini yazdırıyoruz
    def __str__(self):
        return "Personel Bilgileri:\n   Personel No: {}\n   Ad: {}\n   Soyad: {}\n   Departman: {}\n   Maas: {}\n".format(
            self.personel_no,
            self.ad,
            self.soyad,
            self.departman,
            self.maas)

#Oluşturulan 2 adet personel nesnesi
personel1 = Personel("PRS1", "Ferhat", "Kara", "İş Sağlığı ve Güvenliği", 30000)
personel2 = Personel("PRS2", "Kemal", "Tok", "Hasta Kabul ve Kayıt", 35000)
#print(personel1)
#print(personel2)





    
        
        