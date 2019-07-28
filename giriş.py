while True:
    x = (input("Üye mi olmak istiyorsunuz Giriş yapmak mı?"))
    #Üyelik kısmı
    if x=="Üye" or x=="Üye olmak" or x=="üye" or x=="üye olmak":

        ad = (input("Ad ve Soyadınızı giriniz"))
        sifre = (input("Şifrenizi belirleyiniz"))
        mail = (input("E-mailinizi giriniz"))
    bilgiler =[ad,sifre,mail]

    #Giriş kısmı
    if x=="Giriş" or x=="Giriş yapmak" or x=="giriş" or x=="giriş yapmak":
        g_mail = (input("E-mail:"))
        g_sifre = (input("Şifre:"))
        if g_mail == (mail) and g_sifre == (sifre):
                print("Giriş Başarılı . Hoşgeldin",ad)
                break
        elif g_mail != (mail) and g_sifre == (sifre):
            print("E-mail yanlış , giriş başarısız")
        elif g_mail == (mail) and g_sifre != (sifre):
            print("Şifre yanlış , giriş başarısız")
        else:
            print("Giriş başarısız , üye olmaya ne dersin?")


