import json
from random import randint
from membership_system import Membership_system
import time
class Sistem:
    """kullanıcının hesap bilgilerini tutuan sınıf"""
    def __init__(self):

        self.calistir()
        self.durum=True
        self.veriler=self.verileriAl()
        
    def calistir(self):

        """seçim bilgilerine göre fonksiyona atayan fonksiyon"""
        while True: 
            self.menugoster()
            secim=self.menuSecimYap()
        
            if secim==1:
                self.girisYap()
            if secim==2:
                self.kayitOl()
            if secim==3:
                self.sifremiUnuttum()
            if secim==4:
                print("\nÇıkış yapılıyor... \n")
                time.sleep(1)
                print("Başarılı bir şekilde çıkış yapıldı.\n")
                break
        
    def menugoster(self):
        print("""
 ********* OnurSPORT CENTER YÖNETİCİ PANELİ *********

1-Giris Yap
2-Kayıt Ol
3-Şifremi Unuttum
4-Çıkış           
   
              """)
        
    def menuSecimYap(self):
        """
        menü seçiminin yapıldığı sınıf

        Returns:
            int: seçim numarasını alıyo
        """
        while True:
            try:
                secim = int(input("Seçiminizi giriniz: "))
                while secim <1 or secim > 4:
                    secim = int(input("Lütfen 1 ila 4 arasında değer giriniz:"))
                break
            except ValueError:
                print("Lütfen sayı giriniz! \n")
        return secim
                
    def verileriAl(self):
        """
        verilerin alınıp kullanicilar.json a aktaran fonksiyon
    
        """
        try:
            with open("kullanicilar.json","r") as dosya:
                veriler = json.load(dosya)
        except FileNotFoundError:
            with open ("kullanicilar.json","w")as dosya:
                dosya.write("{}")
            with open("kullanicilar.json","r") as dosya:
                veriler = json.load(dosya)
        
        return veriler
                

    def girisYap(self):
        """
        kullanıcının bilgileri alan fonksiyon
        
        """
        kadi=input("Kullanıcı adını giriniz: ")
        sifre=input("Şifrenizi giriniz: ")
        self.kontrolEt(kadi,sifre)
        self.durum=self.kontrolEt(kadi,sifre)
        if self.durum:
            self.girisBasarili()
            Membership_system().calistir()
        else:
            self.girisBasarisiz("Kullanıcı adı veya şifre yanlış.")
            time.sleep(1)
    def kayitOl(self):
        adi = input("Kullanıcı adını giriniz: ")
        while True:
            sifre = input("Şifrenizi giriniz: ")
            tsifre = input ("Şifrenizi tekrar giriniz: ")

            if sifre == tsifre:
                break
            else:
                print("Şifreler eşleşmiyor. Lütfen tekrar giriniz: ")
        email = input("E-psta adresinizi giriniz: ")
        
        self.durum = self.kayitVarmi(adi,email)
        
        if self.durum:
            print("Kullanıcı adı veya e-posta sistemde kayıtlı.")
        else:
            aktivasyonKodu=self.aktivasyonKoduGonder()
            akdurum=self.aktivasyonKontrol(aktivasyonKodu)
            if akdurum:
                self.kaydet(adi,sifre,email)
            else:
                print("Aktivasyon geçersiz.")
                time.sleep(1)
    
    def sifremiUnuttum(self):
        """
        şifre degistirme fonksiyonu
        
        """
        email=input("E-posta adresinizi giriniz: ")
        if self.mailvarMi(email):
            with open("aktivasyon.txt","w") as dosya:
                aktivasyon = str(randint(1000,9999))
                dosya.write(aktivasyon)
            aktgir = input("Şifre değişim işlemi için gönderilen aktivasyon kodunu giriniz: ")
            if aktgir == aktivasyon:
                while True:
                    
                    yeniSifre=input("Yeni şifrenizi giriniz: ")
                    yeniSifreT=input("Yeni şifrenizi tekrar giriniz: ")
            
                    if yeniSifre == yeniSifreT:
                        break
                    else:
                        print("Girdiğiniz şifreler uyuşmuyor.Tekrar giriniz: ")
    
            self.veriler = self.verileriAl()
            
            for kullanici in self.veriler["kullanicilar"]:
                if kullanici["mail"] == email:
                    kullanici["sifre"] = str(yeniSifre)
            with open("kullanicilar.json","w") as dosya:
                json.dump(self.veriler,dosya)
                print("Şifre başarıyla değişti.")
                time.sleep(1)
            
            
        else:
            time.sleep(1)
            print("Böyle bir mail sistemde kayıtlı değil.")

    
    def mailvarMi(self,mail):
        """_summary_

        Args:
            mail (_type_): _description_

        """
        self.veriler = self.verileriAl()
        for kullanici in self.veriler["kullanicilar"]:
            if kullanici["mail"]==mail:
                return True
        
        return False
    

    def kontrolEt(self,kadi,sifre):
        self.veriler=self.verileriAl()
        for kullanici in self.veriler["kullanicilar"]:
            if kullanici["kadi"] == kadi and kullanici["sifre"]==sifre and kullanici["timeout"]=="0" and kullanici["aktivasyon"]=="Y":
                return True
        
        return False
    

    def girisBasarisiz(self,sebep):
        print(sebep)
    def girisBasarili(self):
        print("Giriş Yapılıyor...")
        time.sleep(1)
        self.durum = False
        
        
    def kayitVarmi(self,kadi,mail):
        self.veriler=self.verileriAl()
        try:
            for kullanici in self.veriler["kullanicilar"]:
                if kullanici["kadi"] == kadi and kullanici["mail"] ==mail:
                    return True
        except KeyError:
            return False
        return False
    

    def aktivasyonKoduGonder(self):
        with open("aktivasyon.txt","w") as dosya:
            aktivasyon = str(randint(1000,9999))
            dosya.write(aktivasyon)
        return aktivasyon
    def aktivasyonKontrol(self,aktivasyon):
        aktivasyonKoduAl=input("Aktivasyon kodunuzu giriniz: ")
        if aktivasyon == aktivasyonKoduAl:
            return True
        else:
            return False
        
    def kaydet(self,kadi,sifre,email):
        """_summary_

        Args:
            kadi (_type_): _description_
            sifre (_type_): _description_
            email (_type_): _description_
        """
        self.veriler=self.verileriAl()
        try:
            self.veriler["kullanicilar"].append({"kadi":kadi,"sifre":sifre,"mail":email,"aktivasyon":"Y","timeout":"0"})  
        except  KeyError:
            self.veriler["kullanicilar"]=[]
            self.veriler["kullanicilar"].append({"kadi":kadi,"sifre":sifre,"mail":email,"aktivasyon":"Y","timeout":"0"}) 
        with open("kullanicilar.json","w") as dosya:
            json.dump(self.veriler,dosya)
            print("Kayıt başarıyla oluşturuldu.")
            time.sleep(1)


