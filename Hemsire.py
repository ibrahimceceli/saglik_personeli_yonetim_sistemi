from Personel import Personel

class Hemsire(Personel):
    #Initializer metot
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)        
        self.calisma_saati = calisma_saati
        self.sertifika = sertifika
        self.hastane = hastane

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

    def get_calisma_saati(self):
        return self.calisma_saati
        
    def set_calisma_saati(self, yeni_calisma_saati):
        self.calisma_saati = yeni_calisma_saati 
        
    def get_sertifika(self):
        return self.sertifika
        
    def set_sertifika(self, yeni_sertifika):
        self.sertifika = yeni_sertifika 
        
    def get_hastane(self):
        return self.hastane
        
    def set_hastane(self, yeni_hastane):
        self.hastane = yeni_hastane

    #Maaş arttırma metodu
    def maas_arttir(self):
        yuzde = 10
        self.maas = self.maas + self.maas/yuzde
        return "Yeni Maaş: {}".format(self.maas)

    #Str metoduyla hemşire bilgilerini yazdırıyoruz
    def __str__(self):
        return "Hemsire Bilgileri:\n   Personel No: {}\n   Ad: {}\n   Soyad: {}\n   Departman: {}\n   Maas: {} TL\n   Calisma Saati: {} saat\n   Sertifika: {}\n   Hastane: {}\n".format(
            self.personel_no,
            self.ad,
            self.soyad,
            self.departman,
            self.maas,
            self.calisma_saati,
            self.sertifika,
            self.hastane)

#Oluşturulan 3 adet hemşire nesnesi   
hemsire1 = Hemsire("HMS1", "Selin", "Kozak", "Yenidoğan Hemşireliği", 40000, 45, "Yenidoğan Yoğun Bakım Hemşireliği", "İzmir Seyfi Demirsoy Eğitim ve Araştırma Hastanesi")
hemsire2 = Hemsire("HMS2", "Zeynep", "Akça", "Ortopedi Hemşireliği", 43000, 49, "Hastane Afet ve Acil Durum Planlaması Eğiticisi", "İzmir Tınaztepe Hastanesi")
hemsire3 = Hemsire("HMS3", "İrem", "Kabak", "Yoğun Bakım Hemşireliği", 38000, 47, "Enfeksiyon Kontrol Hemşireliği", "İzmir Bozyaka Eğitim ve Araştırma Hastanesi")
#print(hemsire1.maas_arttir())