print("""
***************************************
Esen Bank'a Hoşgeldiniz

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için Q'ya basınız.
*************************************** 
""")

bakiye = 1000


while True:

    app = input("Yapmak istediğiniz işlemi Numara olarak giriniz: ")

    if (app == '1'):
        print(bakiye, "TL bakiyeniz bulunmaktadır")
    elif (app == '2'):
        yatirma = int(input("Yatırmak istediğiniz değeri giriniz: "))
        bakiye = bakiye + yatirma
        print("Işlem tamamlandı")
    elif (app == '3'):
        cekme = int(input("Para çekeceğiniz miktarı Giriniz: "))
        bakiye -= cekme
        if bakiye < 0:
            print("Bakiye Yetersiz !")
            bakiye += cekme
        else:
            print("Islem tamamlandi")
    elif (app == 'q' or app == 'Q'):
        print("Çıkış yapılıyor.. ")
        break
    else:
        print("Hatalı Tuşlama yaptınız !")
