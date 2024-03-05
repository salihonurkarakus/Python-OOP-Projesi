import json
import sqlite3
from bmi import BMI
import time
class Membership_system:
    """ Üyelik işlemlerinin bilgilerini tutan sınıf"""
    def __init__(self):


        self.fiyat = 0
    
    def connect_database(self):
        """
        database oluştuğu ve bilgilerin gönderildiği sınıf
        """
        self.database_connect= sqlite3.connect("user_info.db")
        self.imlec= self.database_connect.cursor()
        self.imlec.execute("""CREATE TABLE IF NOT EXISTS user(id INTEGER, isim TEXT, soyad TEXT, yas INTEGER, spor_dali TEXT, boy FLOAT, kilo FLOAT ,bmi FLOAT) """)
        
    def bilgi_al(self):
        """
        Üyelerin bilgilerinin alındığı sınıf.
        
        """
        
        self.u_ad= input("Ad: ")
        self.u_soyad=input("Soyad: ")
        self.u_age=int(input("Yaş: "))
        self.u_spor_dali=input("Spod Dalı: ")
        self.u_weight= float(input("Kilo: "))
        self.u_height= float(input("Boy: "))
        self.bmi=BMI(self.u_height,self.u_weight).bmi_value()
        self.u_id=int(input("Üye Numarası: "))
        self.connect_database()
        self.imlec.execute(f"""INSERT INTO user VALUES("{self.u_id}","{self.u_ad}", "{self.u_soyad}", "{self.u_age}", "{self.u_spor_dali}", "{self.u_height}", "{self.u_weight}", "{self.bmi}")""")
        self.database_connect.commit()
        self.database_connect.close()
        print("üye eklendi.")
        
        
    def calistir(self):
        """
        kullanıcının seçim değerine göre ilgili fonksiyona gönderen fonksiyon
        
        """
        while True:
            time.sleep(1)
            self.menugoster()
            secim=self.menusu_secimi_yap()
            if secim==1:
                time.sleep(1)
                self.menugoster2()
                self.uye_ekle()
            if secim==2:
                self.uye_listesi()
            if secim==3:
                self.uye_ara()
            if secim==4:
                self.uye_sil()
            if secim ==5:
                self.uyelik_bedeli()
            if secim == 6:
                
                print("Yönetici Paneline Dönülüyor...")
                
                time.sleep(0.75)
                
                break
    def menugoster(self):
    
        print("""
 ********* OnurSPORT CENTER Üye Kayıt Sistemi *********

1) Kursiyer Ekle
2) Kursiyer Listele
3) Kursiyer Sorgula
4) Kursiyer Sil
5) Kursiyer Ücret Hesapla
6) Çıkış             

              """)
    
    def menusu_secimi_yap(self):
        """
        kullanıcının yapacağı işlemi kullanıcıdan alan sınıf
        Returns:
            int:  kullanıcının seçtiği işlem numarası
        """
        while True:
            try:
                secim = int(input("Yapılacak işlemin numarasını giriniz: "))
                while secim <1 or secim>6:
                    secim = int(input("Lütfen 1 ila 6 arasında bir sayi giriniz: "))
                break
            except ValueError:
                print("Lütfen sayı giriniz: \n")
        return secim
    time.sleep(1)
    def menugoster2(self):
        print("""
Üyelik Seçenekleri:           

1-Fitness
2-Yoga
3-Plates
4-Kick Box      
5-MMA  
               """)

    def uye_ekle(self):
        """
        Üye ekleme fonksiyonu
        
        """
        
        self.bilgi_al()
     
 
    def uye_listesi(self):
        """Üye listesini database den alıp yazdıran fonksiyon"""
       
        self.connect_database()
        users=self.database_connect.execute("""SELECT * FROM user""").fetchall()
        time.sleep(1)
        print(users)
        
    def uye_ara(self):
        """Üye aramasını yapan sınıf. Üye bilgilerini database den çekiyor"""
        
        isim= input("İsim: ")
        soyisim= input("Soyisim: ")
        self.connect_database()
        users=self.database_connect.execute(f"""SELECT * FROM user WHERE isim= "{isim}" and soyad= "{soyisim}" """).fetchone()
        time.sleep(1)
        print(users)
        if users == None:
            time.sleep(1)
            print("Aradığınız kullanıcı bulunamadı.")

                
    def uye_sil(self):
        """
        Üye silme işlemini yapan fonksiyon.
        
        
        """
        isim= input("İsim: ")
        soyisim= input("Soyisim: ")
        self.connect_database()
        self.database_connect.execute(f"""DELETE  FROM user WHERE isim ="{isim}" and soyad = "{soyisim}" """)
        print("Üye Silindi")
        
        self.database_connect.commit()
        self.database_connect.close()
        time.sleep(1)
    def uyelik_bedeli(self):
        """Üyelik ücretinin  hesaplandığı sınıf"""
        
        isim=input("İsim: ")
        soyisim=input("Soyisim: ")
        self.connect_database()
        price=self.database_connect.execute(f""" SELECT spor_dali FROM user WHERE isim="{isim}" and soyad="{soyisim}" """).fetchone()
        time.sleep(1)
        if price =='1':
            print("Borcunuz 150 TL dir.")
        elif price == '2':
            print("Borcunuz 75 TL dir.")
        elif price == '3':
            print("Borcunuz 120 TL dir.")
        elif price == '4':
            print("Borcunuz 115 TL dir.")
        else:
            print("Borcunuz 135 TL dir.")
        self.database_connect.commit()
        self.database_connect.close()
        
        
                
        

    
