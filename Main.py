# İhtiyacımız olan kütüphaneleri import ettik.
import time
from IPython.display import Image
Image('/content/Machine.png')

print("☕ Robin Coffee Venduring Machine ☕")

# Makine Resmi
machine = "/content/Machine.png"

# Kahve Resimleri
espresso = "/content/Espresso.png"
cappucino = "/content/Cappucino.png"
filter_coffee = "/content/Filtre Kahve.png"
mocha = "/content/Mocha.png"
flat_white = "/content/Flat White.png"
latte = "/content/Latte.png"
special_coffee = "/content/Special Robin Coffee.png"

# Resmi görüntülemek için
display(Image(data=machine, width=350, height=400))

# Sözlük olarak kahve menümüzü tanımladık.
kahve_menu = {
    "Espresso": 19,
    "Cappucino" : 30,
    "Special Robin Coffee": 28,
    "Latte": 24 , 
    "Filtre Kahve": 22,
    "Mocha": 32 ,
    "Flat White": 26
      }

class Otomat():

 def __init__(self, durum ="KAPALI", miktar = 0 , kahve = {"Espresso": 19,"Cappucino" : 30 ,"Special Robin Coffee": 28,"Latte": 24 , "Filtre Kahve": 22,"Mocha": 32 ,"Flat White": 26}):
        self.durum = durum
        self.miktar = miktar
        self.kahve = kahve
        
 def open(self):
        if(self.durum == "AÇIK"):
            print("Otomat açık.")
        else:
            self.durum = "KAPALI"
            print("Otomat açılacak.")
					  						
 def close(self):
        if(self.durum == "KAPALI"):
            print("Otomat kapalı.")
        else:
            self.durum = "KAPALI"
            print("Otomat kapanacak.")

 def menu_goruntuleme():
          print("-----Robin-Coffee-Menü-------")
        
for item in list(kahve_menu.keys()):
          print(f"{item.upper():<10} : {kahve_menu[item]} ₺")

def fiyat_hesaplama(kahve,sayı):
      assert sayı >= 0 , "Seçim sayınız 0 ve 0'dan küçük olmamalıdır."

      if kahve not in list(kahve_menu.keys()):
         return None
      else:
         return kahve_menu[kahve] * sayı

def miktar():
    seker_miktarı = input("Kahvenize ne kadar şeker eklemek istersiniz? ")
    shot_miktarı = input("Kahvenize ne kadar shot espresso eklemek istersiniz? ")
    sut_miktarı = input("Kahvenize ne kadar ml süt eklemek istersiniz? ")

def tercih():
    secim = input("Kahvenizi soğuk mu sıcak mı istersiniz? ")
    if secim == soguk:
        print("Kahvenize buz ekleniyor..")
    elif secim == sıcak:
        print("Kahveniz sıcacık hazırlanıyor..")

def icim():
    tercih = input("Kahveniz yumuşak içim olsun ister misiniz (+5 TL)? ")
    if tercih == evet:
        print("Kahveniz yumuşak içimli hazırlanıyor..")
        fiyat =+5
    else:
        pass

def kahve_secim():
 menu_goruntuleme()
 print("İstediğiniz kahveyi giriniz. Çıkış yapmak için '0'ı tuşlayınız.")

  secilen_kahveler = []
  secim_sayısı = []

  odenecek_fiyat = 0

# Resim görüntüleme komutu ile zamansal çakışma yaşadığı için input alabilmek için time ile 1 sn uyuttuk.
  time.sleep(1)

  while 1:
    secilen_urun = input("Kahve ismini giriniz: ")
    if secilen_urun == "0":
      print("Fiş kaydedilip ödenecek tutar hesaplanıyor...")
      break
    if secilen_urun == espresso:
      display(Image(data=espresso, width=350, height=400))

    secim_sayısı = int(input(f"{secilen_urun}'den kaç tane istiyorsunuz? "))
    fiyat = fiyat_hesaplama(secilen_urun,secim_sayısı)
    if fiyat is None:
      print(" Kahve seçildi, başka kahve istiyorsanız giriniz..")
    else:
      print(f"Ödenecek tutar: {fiyat} ₺ .\n Onaylamak için 'evet' iptal etmek için 'hayır' ifadesini giriniz.")
      kontrol = input("Satın almayı onaylıyor musunuz? ")
      if kontrol == "evet":
        print("Onaylandı.")
        print("-"*40)
        odenecek_fiyat += fiyat
        secilen_kahveler.append(secilen_urun)
        print(f"Ara Toplam: {odenecek_fiyat} ₺")
      elif kontrol == "hayır":
        print("Satın alma iptal edildi.")
        print("-"*40)

  return odenecek_fiyat , secilen_kahve , secim_sayısı

def main():

    otomat = Otomat()

    print("""
        -----------Otomat Komutları-----------
        1. Otomatı Aç
        2. Otomatı Kapat
        3. Siparişi Bitir
        4. Kahve Ekle
        5. Şeker/Shot/Süt Miktarı Değiştir (Ekle/Kaldır)
        6. Soğuk/Sıcak Ayarı
        7. Şeker/Yumuşak İçim Ayarı
        8. Çıkış
        """)
   
    time.sleep(1)

    while(True):

        komut = input("Lütfen otomata basarak komut giriniz: ")

        if(komut == "8"):
            time.sleep(1)
            print("-------------------------------------------------------")
            print("|                                                      |")
            print(f"     Ödemeniz gereken tutar {odenecek_fiyat} ₺'dir.")
            print("|                                                      |")
            print("\n  Sağlıklı güzel günler dileriz.\n   Bizi Tercih Ettiğiniz İçin Teşekkürler!\n  ----------------Afiyet Olsun!-------------")
            print("|                                                      |")
            print("-------------------------------------------------------")

            time.sleep(1)
            print("Otomat kapatılıyor.")
            break

        elif(komut == "1"):
            otomat.open()

        elif(komut == "2"):
            otomat.close()

        elif(komut == "3"):
            otomat.fiyat_hesaplama()

        elif(komut == "4"):
            otomat.kahve_secim()

        elif(komut == "5"):
            otomat.miktar()

        elif(komut == "6"):
            otomat.sıcaklık()

        elif(komut == "7"):
            otomat.icim()

        else:
            print("Uyarı! Bilinmeyen Komut")

main()
