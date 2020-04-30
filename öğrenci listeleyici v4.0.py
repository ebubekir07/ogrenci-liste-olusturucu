from tkinter import *
import sqlite3
from tkinter.ttk import Combobox
from tkinter import messagebox
con = sqlite3.connect("veritabani.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(no INT,ad TEXT,soyad TEXT,sinif INT,sube TEXT,tc INT,tel INT,ay TEXT,gun INT,yil INT,bolum TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS dersler(no INT,mat INT,fizik INT,kimya INT,biyo INT,edeb INT,tarih INT,fel INT,din INT,ing INT,beden INT,muzik INT,alm INT,cog INT,secedb INT,tkmt INT,pisk INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS saatler(no INT,smat INT,sfizik INT,skimya INT,sbiyo INT,sedeb INT,starih INT,sfel INT,sdin INT,sing INT,sbeden INT,smuzik INT,salm INT,scog INT,ssecedb INT,stkmt INT,spisk INT,toplam INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS chek(no INT,cmat INT,cfizik INT,ckimya INT,cbiyo INT,cedeb INT,ctarih INT,cfel INT,cdin INT,cing INT,cbeden INT,cmuzik INT,calm INT,ccog INT,csecedb INT,ctkmt INT,cpisk INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS kullanicilar(kuladi TEXT,sifre TEXT,yetki INT)")

def notlarigetir():
    gorno = notgoren.get()
    cursor.execute("select count(no) from ogrenciler WHERE no={}".format(gorno))
    gornovarmi = cursor.fetchone()[0]
    if (gornovarmi == 0):
        messagebox.showinfo("Uyarı", "Bu numaraya ait öğrenci bulunamadı.")
    cursor.execute("SELECT ad FROM ogrenciler WHERE no={}".format(gorno))
    getirad = cursor.fetchone()[0]
    cursor.execute("SELECT bolum FROM ogrenciler WHERE no={}".format(gorno))
    getiralan = cursor.fetchone()[0]
    notgoren.delete(first=0, last=22)
    gorpenc = Tk()
    gorpenc.title("Öğrencinin Not Tablosu : {}".format(getirad))
    gorpenc.geometry("500x360+450+250")
    cursor.execute("SELECT * FROM chek WHERE no={}".format(gorno))
    notchek = cursor.fetchone()
    matvardeger = notchek[1]
    fizvardeger = notchek[2]
    kimvardeger = notchek[3]
    biyovardeger = notchek[4]
    edebvardeger = notchek[5]
    tarvardeger = notchek[6]
    felvardeger = notchek[7]
    dinvardeger = notchek[8]
    ingvardeger = notchek[9]
    bedvardeger = notchek[10]
    muzvardeger = notchek[11]
    almvardeger = notchek[12]
    cogvardeger = notchek[13]
    secedbvardeger = notchek[14]
    tkmtvardeger = notchek[15]
    pskvardeger = notchek[16]

    cursor.execute("SELECT * FROM saatler WHERE no={}".format(gorno))
    notsaat = cursor.fetchone()
    matders = notsaat[1]
    fizders = notsaat[2]
    kimders = notsaat[3]
    biyoders = notsaat[4]
    edebders = notsaat[5]
    tarders = notsaat[6]
    felders = notsaat[7]
    dinders = notsaat[8]
    ingders = notsaat[9]
    bedders = notsaat[10]
    muzders = notsaat[11]
    almders = notsaat[12]
    cogders = notsaat[13]
    secedbders = notsaat[14]
    tkmtders = notsaat[15]
    pskders = notsaat[16]
    derssaat = notsaat[17]
    cursor.execute("SELECT * FROM dersler WHERE no={}".format(gorno))
    dersnotu = cursor.fetchone()

    sonuc = Label(gorpenc, width=22, anchor="w", text="Ortalama=")
    sonuc.grid(row=0, column=3)
    ortdurum = Label(gorpenc, width=15, text="")
    ortdurum.grid(row=0, column=4)

    tesk = Label(gorpenc, width=22, anchor="w", text="Teşekkür için gereken puan=")
    tesk.grid(row=1, column=3)
    tesgos = Label(gorpenc, width=15, text="")
    tesgos.grid(row=1, column=4)

    takd = Label(gorpenc, width=22, anchor="w", text="Takdir için gereken puan=")
    takd.grid(row=2, column=3)
    takgos = Label(gorpenc, width=15, text="")
    takgos.grid(row=2, column=4)

    belge = Label(gorpenc, width=22, anchor="w", text="Belge=")
    belge.grid(row=3, column=3)
    belgedurum = Label(gorpenc, font=("Comic Sans MS", 11, "bold"), width=15, text="")
    belgedurum.grid(row=3, column=4)

    matlab = Label(gorpenc, anchor="w", text="Matematik=")
    matlab.grid(row=0, column=0)

    edeblab = Label(gorpenc, width=8, anchor="w", text="Edebiyat=")
    edeblab.grid(row=4, column=0)
    tarihlab = Label(gorpenc, width=8, anchor="w", text="Tarih=")
    tarihlab.grid(row=5, column=0)
    fellab = Label(gorpenc, width=8, anchor="w", text="Felsefe=")
    fellab.grid(row=6, column=0)
    dinlab = Label(gorpenc, width=8, anchor="w", text="Din K.=")
    dinlab.grid(row=7, column=0)
    inglab = Label(gorpenc, width=8, anchor="w", text="İngilizce=")
    inglab.grid(row=8, column=0)
    bedlab = Label(gorpenc, width=8, anchor="w", text="Beden=")
    bedlab.grid(row=9, column=0)
    muzlab = Label(gorpenc, width=8, anchor="w", text="Müz/Gör=")
    muzlab.grid(row=10, column=0)
    almlab = Label(gorpenc, width=8, anchor="w", text="Almanca=")
    almlab.grid(row=11, column=0)

    smatlab = Label(gorpenc, width=8, text=dersnotu[1])
    smatlab.grid(row=0, column=1)

    sedeblab = Label(gorpenc, width=8, text=dersnotu[5])
    sedeblab.grid(row=4, column=1)
    starihlab = Label(gorpenc, width=8, text=dersnotu[6])
    starihlab.grid(row=5, column=1)
    sfellab = Label(gorpenc, width=8, text=dersnotu[7])
    sfellab.grid(row=6, column=1)
    sdinlab = Label(gorpenc, width=8, text=dersnotu[8])
    sdinlab.grid(row=7, column=1)
    singlab = Label(gorpenc, width=8, text=dersnotu[9])
    singlab.grid(row=8, column=1)
    sbedlab = Label(gorpenc, width=8, text=dersnotu[10])
    sbedlab.grid(row=9, column=1)
    smuzlab = Label(gorpenc, width=8, text=dersnotu[11])
    smuzlab.grid(row=10, column=1)
    salmlab = Label(gorpenc, width=8, text=dersnotu[12])
    salmlab.grid(row=11, column=1)

    def alanmfgos():
        fizlab = Label(gorpenc, width=8, anchor="w", text="Fizik=")
        fizlab.grid(row=1, column=0)
        kimlab = Label(gorpenc, width=8, anchor="w", text="Kimya=")
        kimlab.grid(row=2, column=0)
        biyolab = Label(gorpenc, width=8, anchor="w", text="Biyoloji=")
        biyolab.grid(row=3, column=0)

        sfizlab = Label(gorpenc, width=8, text=dersnotu[2])
        sfizlab.grid(row=1, column=1)
        skimlab = Label(gorpenc, width=8, text=dersnotu[3])
        skimlab.grid(row=2, column=1)
        sbiyolab = Label(gorpenc, width=8, text=dersnotu[4])
        sbiyolab.grid(row=3, column=1)

        matnot = dersnotu[1]
        kimyanot = dersnotu[3]
        fiziknot = dersnotu[2]
        biyonot = dersnotu[4]
        edebnot = dersnotu[5]
        tarihnot = dersnotu[6]
        felnot = dersnotu[7]
        dinnot = dersnotu[8]
        ingnot = dersnotu[9]
        bednot = dersnotu[10]
        muziknot = dersnotu[11]
        almnot = dersnotu[12]

        mat = matnot * matders
        fizik = fiziknot * fizders
        kimya = kimyanot * kimders
        biyo = biyonot * biyoders
        edeb = edebnot * edebders
        tarih = tarihnot * tarders
        fel = felnot * felders
        din = dinnot * dinders
        ing = ingnot * ingders
        bed = bednot * bedders
        muzik = muziknot * muzders
        alm = almnot * almders
        ort = (mat + fizik + kimya + biyo + edeb + tarih + fel + din + ing + bed + muzik + alm) / derssaat

        if 70 <= ort < 85:
            if (0 < matnot < 50) or (0 < fiziknot < 50) or (0 < kimyanot < 50) or (0 < biyonot < 50) or (
                    0 < edebnot < 50) or (0 < tarihnot < 50) or (0 < felnot < 50) or (0 < dinnot < 50) or (
                    0 < ingnot < 50) or (0 < bednot < 50) or (0 < muziknot < 50) or (0 < almnot < 50):
                tak = 85 - ort
                belgedurum.config(text="Belge yok zayıf var", bg="red")
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))

            elif (matnot == 0) or (fiziknot == 0) or (kimyanot == 0) or (biyonot == 0) or (edebnot == 0) or (
                    tarihnot == 0) or (felnot == 0) or (dinnot == 0) or (ingnot == 0) or (bednot == 0) or (
                    muziknot == 0) or (almnot == 0):
                tak = 85 - ort
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))
                belgedurum.config(text="Teşekkür", bg="orange")
            else:
                tak = 85 - ort
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))
                belgedurum.config(text="Teşekkür", bg="orange")
        ##==============================================================================================================##
        elif 85 <= ort <= 100:
            if (0 < matnot < 50) or (0 < fiziknot < 50) or (0 < kimyanot < 50) or (0 < biyonot < 50) or (
                    0 < edebnot < 50) or (0 < tarihnot < 50) or (0 < felnot < 50) or (0 < dinnot < 50) or (
                    0 < ingnot < 50) or (0 < bednot < 50) or (0 < muziknot < 50) or (0 < almnot < 50):
                belgedurum.config(text="Belge yok zayıf var", bg="red")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
            elif (matnot == 0) or (fiziknot == 0) or (kimyanot == 0) or (biyonot == 0) or (edebnot == 0) or (
                    tarihnot == 0) or (felnot == 0) or (dinnot == 0) or (ingnot == 0) or (bednot == 0) or (
                    muziknot == 0) or (almnot == 0):
                belgedurum.config(text="Takdir", bg="green")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
            else:
                belgedurum.config(text="Takdir", bg="green")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
        ##===============================================================================================================##
        else:
            tes = 70 - ort
            tak = 85 - ort
            tesgos.config(text=round(tes, 2))
            takgos.config(text=round(tak, 2))
            belgedurum.config(text="Belge yok", bg="red")

        ortdurum.config(text=round(ort, 2))

    def alantmgos():

        coglab = Label(gorpenc, width=8, anchor="w", text="Coğrafya=")
        coglab.grid(row=1, column=0)
        secedblab = Label(gorpenc, width=8, anchor="w", text="S. Edebiyat=")
        secedblab.grid(row=2, column=0)
        tkmtlab = Label(gorpenc, width=8, anchor="w", text="Tkmt=")
        tkmtlab.grid(row=3, column=0)
        psklab = Label(gorpenc, width=8, anchor="w", text="Psikoloji=")
        psklab.grid(row=12, column=0)

        scoglab = Label(gorpenc, width=8, text=dersnotu[13])
        scoglab.grid(row=1, column=1)
        ssecedblab = Label(gorpenc, width=8, text=dersnotu[14])
        ssecedblab.grid(row=2, column=1)
        stkmtlab = Label(gorpenc, width=8, text=dersnotu[15])
        stkmtlab.grid(row=3, column=1)
        spsklab = Label(gorpenc, width=8, text=dersnotu[16])
        spsklab.grid(row=12, column=1)

        matnot = dersnotu[1]
        edebnot = dersnotu[5]
        tarihnot = dersnotu[6]
        felnot = dersnotu[7]
        dinnot = dersnotu[8]
        ingnot = dersnotu[9]
        bednot = dersnotu[10]
        muziknot = dersnotu[11]
        almnot = dersnotu[12]
        cognot = dersnotu[13]
        secedbnot = dersnotu[14]
        tkmtnot = dersnotu[15]
        psknot = dersnotu[16]

        mat = matnot * matders
        cog = cognot * cogders
        secedb = secedbnot * secedbders
        tkmt = tkmtnot * tkmtders
        edeb = edebnot * edebders
        tarih = tarihnot * tarders
        fel = felnot * felders
        din = dinnot * dinders
        ing = ingnot * ingders
        bed = bednot * bedders
        muzik = muziknot * muzders
        alm = almnot * almders
        psk = psknot * pskders

        ort = (mat + cog + secedb + tkmt + edeb + tarih + fel + din + ing + bed + muzik + alm + psk) / derssaat

        if 70 <= ort < 85:
            if (0 < matnot < 50) or (0 < cognot < 50) or (0 < psknot < 50) or (0 < secedbnot < 50) or (
                    0 < tkmtnot < 50) or (0 < edebnot < 50) or (0 < tarihnot < 50) or (0 < felnot < 50) or (
                    0 < dinnot < 50) or (0 < ingnot < 50) or (0 < bednot < 50) or (0 < muziknot < 50) or (
                    0 < almnot < 50):
                tak = 85 - ort
                belgedurum.config(text="Belge yok zayıf var", bg="red")
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))
            elif (matnot == 0) or (cognot == 0) or (psknot == 0) or (secedbnot == 0) or (tkmtnot == 0) or (
                    edebnot == 0) or (tarihnot == 0) or (felnot == 0) or (dinnot == 0) or (ingnot == 0) or (
                    bednot == 0) or (muziknot == 0) or (almnot == 0):
                tak = 85 - ort
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))
                belgedurum.config(text="Teşekkür", bg="orange")
            else:
                tak = 85 - ort
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))
                belgedurum.config(text="Teşekkür", bg="orange")
        ##==============================================================================================================##
        elif 85 <= ort <= 100:
            if (0 < matnot < 50) or (0 < cognot < 50) or (0 < psknot < 50) or (0 < secedbnot < 50) or (
                    0 < tkmtnot < 50) or (0 < edebnot < 50) or (0 < tarihnot < 50) or (0 < felnot < 50) or (
                    0 < dinnot < 50) or (0 < ingnot < 50) or (0 < bednot < 50) or (0 < muziknot < 50) or (
                    0 < almnot < 50):
                belgedurum.config(text="Belge yok zayıf var", bg="red")
                tesgos.config(text="Yeterli")
                takgos.config(tjext="Yeterli")

            elif (matnot == 0) or (cognot == 0) or (psknot == 0) or (secedbnot == 0) or (tkmtnot == 0) or (
                    edebnot == 0) or (tarihnot == 0) or (felnot == 0) or (dinnot == 0) or (ingnot == 0) or (
                    bednot == 0) or (muziknot == 0) or (almnot == 0):
                belgedurum.config(text="Takdir", bg="green")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
            else:
                belgedurum.config(text="Takdir", bg="green")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
        ##==============================================================================================================##
        else:
            tes = 70 - ort
            tak = 85 - ort
            tesgos.config(text=round(tes, 2))
            takgos.config(text=round(tak, 2))
            belgedurum.config(text="Belge yok", bg="red")
        ##==============================================================================================================##
        ortdurum.config(text=round(ort, 2))

    if (getiralan == "MF"):
        alanmfgos()
    else:
        alantmgos()

    def kisiekleme():
        ad = str(aden.get()).capitalize()
        soyad = str(soyaden.get()).capitalize()
        sinif = int(sinifen.get())
        no = int(oknoen.get())
        sube = str(subeen.get()).capitalize()
        tc = int(tcen.get())
        tel = int(telen.get())
        ay = str(dogumay.get())
        gun = int(dogumgun.get())
        yil = int(dogumyil.get())
        bolum = str(alan.get())
        cursor.execute("select count(*) from ogrenciler WHERE no={}".format(no))
        kontrol2 = cursor.fetchone()

        if (kontrol2[0] == 1):
            uyarilabel.config(text="Bu numaraya sahip öğrenci \n listede mevcut.")

        elif(len(str(tc))!=11):
           print("Geçerli bir tc no girin")
           uyarilabel.config(text="Geçerli bir tc no girin.")

        elif (len(str(tel)) != 10):
            print("geçerli tel gir")
            uyarilabel.config(text="Geçerli bir telefon no girin.")

        else:
            pencere2.destroy()
            cursor.execute(
                "INSERT INTO ogrenciler VALUES('{} ','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(no, ad,
                                                                                                                soyad,
                                                                                                                sinif,
                                                                                                                sube,
                                                                                                                tc, tel,
                                                                                                                ay, gun,
                                                                                                                yil,
                                                                                                                bolum))
            cursor.execute(
                "INSERT INTO dersler VALUES('{} ','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    no, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""))
            cursor.execute(
                "INSERT INTO saatler VALUES('{} ','6','4','4','4','5','2','2','2','4','2','2','2','4','3','2','2','')".format(
                    no))
            cursor.execute(
                "INSERT INTO chek VALUES('{}','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0')".format(
                    no))
            con.commit()
            listele()

    def kisiekleme():
        ad = str(aden.get()).capitalize()
        soyad = str(soyaden.get()).capitalize()
        sinif = int(sinifen.get())
        no = int(oknoen.get())
        sube = str(subeen.get()).capitalize()
        tc = int(tcen.get())
        tel = int(telen.get())
        ay = str(dogumay.get())
        gun = int(dogumgun.get())
        yil = int(dogumyil.get())
        bolum = str(alan.get())
        cursor.execute("select count(*) from ogrenciler WHERE no={}".format(no))
        kontrol2 = cursor.fetchone()

        if (kontrol2[0] == 1):
            uyarilabel.config(text="Bu numaraya sahip öğrenci \n listede mevcut.")

        elif (len(str(tc)) != 11):
            print("Geçerli bir tc no girin")
            uyarilabel.config(text="Geçerli bir tc no girin.")

        elif (len(str(tel)) != 10):
            print("geçerli tel gir")
            uyarilabel.config(text="Geçerli bir telefon no girin.")

        else:
            pencere2.destroy()
            cursor.execute(
                "INSERT INTO ogrenciler VALUES('{} ','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(no, ad,
                                                                                                                soyad,
                                                                                                                sinif,
                                                                                                                sube,
                                                                                                                tc, tel,
                                                                                                                ay, gun,
                                                                         bolum))
            cursor.execute(
                "INSERT INTO dersler VALUES('{} ','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    no, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""))
            cursor.execute(
                "INSERT INTO saatler VALUES('{} ','6','4','4','4','5','2','2','2','4','2','2','2','4','3','2','2','')".format(
                    no))
            cursor.execute(
                "INSERT INTO chek VALUES('{}','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0')".format(
                    no))
            con.commit()
            listele()
def kisiekleme():
    ad=str(aden.get()).capitalize()
    soyad=str(soyaden.get()).capitalize()
    sinif=int(sinifen.get())
    no=int(oknoen.get())
    sube=str(subeen.get()).capitalize()
    tc=int(tcen.get())
    tel=int(telen.get())
    ay=str(dogumay.get())
    gun=int(dogumgun.get())
    yil=int(dogumyil.get())
    bolum=str(alan.get())
    cursor.execute("select count(*) from ogrenciler WHERE no={}".format(no))
    kontrol2 = cursor.fetchone()

    if (kontrol2[0] == 1):
        uyarilabel.config(text="Bu numaraya sahip öğrenci \n listede mevcut.")

    elif (len(str(tc)) != 11):
        print("Geçerli bir tc no girin")
        uyarilabel.config(text="Geçerli bir tc no girin.")

    elif (len(str(tel)) != 10):
        print("geçerli tel gir")
        uyarilabel.config(text="Geçerli bir telefon no girin.")

    else:
        pencere2.destroy()
        cursor.execute("INSERT INTO ogrenciler VALUES('{} ','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(no,ad,soyad,sinif,sube,tc,tel,ay,gun,yil,bolum))
        cursor.execute("INSERT INTO dersler VALUES('{} ','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(no,"","","","","","","","","","","","","","","",""))
        cursor.execute("INSERT INTO saatler VALUES('{} ','6','4','4','4','5','2','2','2','4','2','2','2','4','3','2','2','')".format(no))
        cursor.execute("INSERT INTO chek VALUES('{}','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0')".format(no))
        con.commit()
        listele()
def pencereekle():
    global aden,soyaden,sinifen,oknoen,subeen,tcen,telen,dogumay,ayen,dogumgun,dogumyil,uyarilabel,pencere2,alan,kisiekleme
    pencere2 = Tk()
    pencere2.title("Yeni Öğrenci")
    pencere2.geometry("250x360+450+250")
    yilen = IntVar(pencere2)
    gunen = IntVar(pencere2)
    ayen = StringVar(pencere2)
    alan = StringVar(pencere2)

    eklelabad = Label(pencere2,text="Ad:",width=7,anchor="w")
    eklelabad.grid(row=1,column=0)
    aden = Entry(pencere2,width=20)
    aden.grid(row=1,column=1)

    eklelabsoyad = Label(pencere2,text="Soyad:",width=7,anchor="w")
    eklelabsoyad.grid(row=2,column=0)
    soyaden = Entry(pencere2,width=20)
    soyaden.grid(row=2,column=1)

    eklelabsinif = Label(pencere2,text="Sınıf:",width=7,anchor="w")
    eklelabsinif.grid(row=3,column=0)
    sinifen = Entry(pencere2,width=20)
    sinifen.grid(row=3,column=1)

    eklelabokno = Label(pencere2,text="Okul No:",width=7,anchor="w")
    eklelabokno.grid(row=4,column=0)
    oknoen = Entry(pencere2,width=20)
    oknoen.grid(row=4,column=1)

    eklesube = Label(pencere2,text="Şube:",width=7,anchor="w")
    eklesube.grid(row=5,column=0)
    subeen = Entry(pencere2,width=20)
    subeen.grid(row=5,column=1)

    ekletc = Label(pencere2,text="Tc. No:",width=7,anchor="w")
    ekletc.grid(row=6,column=0)
    tcen = Entry(pencere2,width=20)
    tcen.grid(row=6,column=1)


    ekletel = Label(pencere2,text="Telefon:",width=7,anchor="w")
    ekletel.grid(row=7,column=0)
    telen = Entry(pencere2,width=20)
    telen.grid(row=7,column=1)

    bolumler= ["MF","TM"]
    labelalan = Label(pencere2,text="Alan:",width=7,anchor="w")
    labelalan.grid(row=8,column=0)
    alanen = Combobox(pencere2,values=bolumler,state="readonly",width=17 ,textvariable=alan)
    alanen.grid(row=8,column=1)
    alanen.current(0)

    labelay = Label(pencere2,text="D. Ayı:",width=7,anchor="w")
    labelay.grid(row=9,column=0)
    dogumay = Combobox(pencere2,values=aylar,state="readonly",width=17 ,textvariable=ayen)
    dogumay.grid(row=9,column=1)
    dogumay.current(0)

    gunen.set(1)
    labelgun = Label(pencere2,text="D. Günü:",width=7,anchor="w")
    labelgun.grid(row=10,column=0)
    dogumgun=Spinbox(pencere2,from_=1,to=31,width=18,textvariable=gunen)
    dogumgun.grid(row=10,column=1)

    yilen.set(2002)
    labelyil = Label(pencere2,text="D. Yılı:",width=7,anchor="w")
    labelyil.grid(row=11,column=0)
    dogumyil=Spinbox(pencere2,from_=1950,to=2030,width=18,textvariable=yilen)
    dogumyil.grid(row=11,column=1)

    uyarilabel=Label(pencere2,text="",width=30)
    uyarilabel.grid(row=13,column=0,columnspan=2)

    eklebuton = Button(pencere2,text="Ekle",command=kisiekleme)
    eklebuton.grid(row=12,column=1)
def oturumkapat():
    pencere.destroy()
    oturum()
def sifredogru():
    global notnoen,notgoren,aylar,listele,pencere
    sifrepenc.destroy()
    pencere = Tk()
    pencere.title("Öğrenci Listeleme v3.0")
    pencere.geometry("920x600+25+25")

    uyariyetki=Label(pencere,bg="blue",text=girilenkuladi,width=12)
    uyariyetki.place(relx=0.85,rely=0.001)
    def kaydirici(self, event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))
    frame = Frame(pencere)
    frame.place(relx=-0.005,rely=0.057)
    yscrollbar = Scrollbar(frame)
    yscrollbar.grid(column=1, row=0, sticky=N+S)
    #yscrollbar.pack(fill="y",side="right")

    canvas = Canvas(frame,height = 560,yscrollcommand=yscrollbar.set)
    canvas.grid(column=0, row=0)
    #canvas.pack(side="right")
    yscrollbar.config(command=canvas.yview)

    frame = Frame(canvas)
    canvas.create_window(4, 4, window=frame, anchor='nw')
    frame.bind("<Configure>", kaydirici)

    labelno1 = Label(pencere,text="Okul No",bg="purple",width=10,height=2)
    labelno1.grid(row=0,column=0)
    labelad = Label(pencere,text="Ad",bg="red",width=15,height=2)
    labelad.grid(row=0,column=1)
    labelsoyad = Label(pencere,text="Soyad",bg="green",width=15,height=2)
    labelsoyad.grid(row=0,column=2)
    labelno = Label(pencere,text="Sınıf",bg="orange",width=10,height=2)
    labelno.grid(row=0,column=3)
    def mevcutsayi():
        global mevcut
        cursor.execute("select count(*) from ogrenciler ")
        deger = cursor.fetchone()
        mevcut=deger[0]
    def kisigetir():
        gelenno=getiren.get()
        getiren.delete(first=0,last=22)
        cursor.execute("select count(*) from ogrenciler WHERE no={}".format(gelenno))
        kontrol3 = cursor.fetchone()
        if(kontrol3[0]==0):
             messagebox.showinfo("Öğrenci Bilgileri","Bu numaraya ait öğrenci bulunamadı.")
        else:
            cursor.execute("SELECT * FROM ogrenciler WHERE no={}".format(gelenno))
            gelenveri = cursor.fetchone()
            messagebox.showinfo("Öğrenci Bilgileri",
                                "Ad : {}\nSoyad : {}\nNumara : {}\nSınıf : {}\nŞube : {}\nTc : {}\nTelefon : {}\nD. Tarihi : {}/{}/{}".format(gelenveri[1],gelenveri[2],
                                                                              gelenveri[0],gelenveri[3],gelenveri[4],gelenveri[5],gelenveri[6],gelenveri[8],gelenveri[7],gelenveri[9]))
    def kisisil():
        silinecek=silen.get()
        silen.delete(first=0,last=22)

        cursor.execute("select count(*) from ogrenciler WHERE no={}".format(silinecek))
        kontrol1 = cursor.fetchone()
        if (kontrol1[0]==0):
            messagebox.showinfo("Uyarı","Bu numaraya ait öğrenci bulunamadı.")
        else:
            cursor.execute("DELETE FROM ogrenciler WHERE no={}".format(silinecek))
            con.commit()
            listele()
    def verialno():
        global datano
        cursor.execute('SELECT no FROM ogrenciler ORDER BY no ASC')
        con.commit()
        datano = cursor.fetchall()
        #print(datano)
    def verialad():
        global dataad
        cursor.execute('SELECT ad FROM ogrenciler ORDER BY no ASC')
        con.commit()
        dataad = cursor.fetchall()
        #print(dataad)
    def verialsoy():
        global datasoy
        cursor.execute('SELECT soyad FROM ogrenciler ORDER BY no ASC')
        con.commit()
        datasoy = cursor.fetchall()
        #print(datasoy)
    def verialsinif():
        global datasinif
        cursor.execute('SELECT sinif FROM ogrenciler ORDER BY no ASC')
        con.commit()
        datasinif = cursor.fetchall()
    labelno= ""
    labelogad=""
    labelogsoyad=""
    labelogsınıf=""
    def listele():
        verialno()
        verialad()
        verialsoy()
        verialsinif()
        mevcutsayi()
        for i in range(mevcut+1):
            satir=1
            degerdata=0
            satir=satir+i
            degerdata= degerdata + i
            a=str(i)
            labelno= "abc"
            labelogad ="qwe"
            labelogsoyad="zxc"
            labelogsınıf="asd"
            labelno = labelno + a
            labelogad=labelogad +a
            labelogsoyad=labelogsoyad + a
            labelogsınıf=labelogsınıf + a
            labelno = Label(frame,text="",width=10)
            labelno.grid(row=satir,column=0)
            labelogad = Label(frame,text="",width=15)
            labelogad.grid(row=satir,column=1)
            labelogsoyad = Label(frame,text="",width=15)
            labelogsoyad.grid(row=satir,column=2)
            labelogsınıf = Label(frame,text="",width=10)
            labelogsınıf.grid(row=satir,column=3)
        for i in range(mevcut):
            satir=1
            degerdata=0
            satir=satir+i
            degerdata= degerdata + i
            a=str(i)
            labelno= "abc"
            labelogad ="qwe"
            labelogsoyad="zxc"
            labelogsınıf="asd"
            labelno = labelno + a
            labelogad=labelogad +a
            labelogsoyad=labelogsoyad + a
            labelogsınıf=labelogsınıf + a
            labelno = Label(frame,text=datano[degerdata],bg="dark grey",relief="solid",width=10)
            labelno.grid(row=satir,column=0)
            labelogad = Label(frame,text=dataad[degerdata],bg="grey",relief="solid",width=15)
            labelogad.grid(row=satir,column=1)
            labelogsoyad = Label(frame,text=datasoy[degerdata],bg="darkgrey",relief="solid",width=15)
            labelogsoyad.grid(row=satir,column=2)
            labelogsınıf = Label(frame,text=datasinif[degerdata],bg="grey",relief="solid",width=10)
            labelogsınıf.grid(row=satir,column=3)
    mevcutsayi()
    if(mevcut>0):
        listele()
    aylar = ['Ocak', 'Şubat', 'Mart', 'Nisan','Mayıs', 'Haziran',"Temmuz","Ağustos",
               "Eylül","Ekim","Kasım","Aralık"]
    if(yetkiseviyesi==2):

        cizgilab2=Label(pencere,text="___________________________________",width=27)
        cizgilab2.place(relx=0.65,rely=0.12)
        bilgilab1=Label(pencere,text="Öğrenci Sil",
                      font=("Comic Sans MS",11,"bold"),width=15)
        bilgilab1.place(relx=0.69,rely=0.001)
        silno = Label(pencere,text="Okul No:",width=10,anchor="w")
        silno.place(relx=0.68,rely=0.05)
        silen = Entry(pencere,width=10)
        silen.place(relx=0.76,rely=0.05)
        silbuton = Button(pencere,text="Sil",command=kisisil,width=6)
        silbuton.place(relx=0.77,rely=0.09)
        eklebuton = Button(pencere,text="Yeni Öğrenci Ekle",command=pencereekle)
        eklebuton.place(relx=0.72,rely=0.16)
    cizgilab2=Label(pencere,text="___________________________________",width=27)
    cizgilab2.place(relx=0.43,rely=0.28)

    bilgilab3=Label(pencere,text="Not Gir",
                      font=("Comic Sans MS",11,"bold"),width=15)
    bilgilab3.place(relx=0.47,rely=0.15)
    notlab = Label(pencere,text="Okul No:",width=10,anchor="w")
    notlab.place(relx=0.46,rely=0.20)
    notnoen = Entry(pencere,width=10)
    notnoen.place(relx=0.54,rely=0.20)
    notgirbuton = Button(pencere,text="Tamam",command=notgir,width=6)
    notgirbuton.place(relx=0.55,rely=0.24)

    cizgilab=Label(pencere,text="___________________________________",width=27)
    cizgilab.place(relx=0.43,rely=0.12)

    bilgilab2=Label(pencere,text="Bilgileri Getir",
                      font=("Comic Sans MS",11,"bold"),width=15)
    bilgilab2.place(relx=0.47,rely=0.001)
    getirno = Label(pencere,text="Okul No:",width=10,anchor="w")
    getirno.place(relx=0.46,rely=0.05)
    getiren = Entry(pencere,width=10)
    getiren.place(relx=0.54,rely=0.05)
    getirbuton = Button(pencere,text="Getir",command=kisigetir,width=6)
    getirbuton.place(relx=0.55,rely=0.09)

    bilgilab4=Label(pencere,text="Notları Gör",
                      font=("Comic Sans MS",11,"bold"),width=15)
    bilgilab4.place(relx=0.47,rely=0.32)
    notgorlab = Label(pencere,text="Okul No:",width=10,anchor="w")
    notgorlab.place(relx=0.46,rely=0.37)
    notgoren = Entry(pencere,width=10)
    notgoren.place(relx=0.54,rely=0.37)
    notgorbuton = Button(pencere,text="Tamam",command=notlarigetir,width=6)
    notgorbuton.place(relx=0.55,rely=0.41)
    oturumkapatbuton=Button(pencere,text="Oturumu Kapat",command=oturumkapat,width=11)
    oturumkapatbuton.place(relx=0.87,rely=0.92)
    pencere.mainloop()
def notgir():
    notno=notnoen.get()
    cursor.execute("select count(no) from ogrenciler WHERE no={}".format(notno))
    notnovarmi=cursor.fetchone()[0]
    if(notnovarmi==0):
        messagebox.showinfo("Uyarı", "Bu numaraya ait öğrenci bulunamadı.")

    cursor.execute("SELECT ad FROM ogrenciler WHERE no={}".format(notno))
    datanotad = cursor.fetchone()[0]
    cursor.execute("SELECT bolum FROM ogrenciler WHERE no={}".format(notno))
    datanotalan = cursor.fetchone()[0]
    notnoen.delete(first=0,last=22)
    notpenc = Tk()
    notpenc.title("Not Girişi : {}".format(datanotad))
    notpenc.geometry("330x360")

    matsv=IntVar(notpenc)
    fizsv=IntVar(notpenc)
    kimsv=IntVar(notpenc)
    biyosv=IntVar(notpenc)
    edebsv=IntVar(notpenc)
    tarsv=IntVar(notpenc)
    felsv=IntVar(notpenc)
    dinsv=IntVar(notpenc)
    ingsv=IntVar(notpenc)
    bedsv=IntVar(notpenc)
    muzsv=IntVar(notpenc)
    almsv=IntVar(notpenc)
    cogsv=IntVar(notpenc)
    secedbsv=IntVar(notpenc)
    tkmtsv=IntVar(notpenc)
    psksv=IntVar(notpenc)

    cursor.execute("SELECT * FROM dersler WHERE no={}".format(notno))
    dersnotu = cursor.fetchone()
    matnot = dersnotu[1]
    fiziknot = dersnotu[2]
    kimyanot = dersnotu[3]
    biyonot = dersnotu[4]
    edebnot = dersnotu[5]
    tarihnot = dersnotu[6]
    felnot = dersnotu[7]
    dinnot = dersnotu[8]
    ingnot = dersnotu[9]
    bednot = dersnotu[10]
    muziknot = dersnotu[11]
    almnot = dersnotu[12]
    cognot = dersnotu[13]
    secedbnot = dersnotu[14]
    tkmtnot = dersnotu[15]
    psknot = dersnotu[16]
    def alanmf():
        global matvardeger, edebvardeger, tarvardeger, felvardeger, dinvardeger, ingvardeger, bedvardeger, muzvardeger, almvardeger
        global matders, edebders, tarders, felders, dinders, ingders, bedders, muzders, almders
        def girisyapma():
            matders=int(matsv.get())
            kimders=int(kimsv.get())
            fizders=int(fizsv.get())
            biyoders=int(biyosv.get())
            edebders=int(edebsv.get())
            tarders=int(tarsv.get())
            felders=int(felsv.get())
            dinders=int(dinsv.get())
            ingders=int(ingsv.get())
            bedders=int(bedsv.get())
            muzders=int(muzsv.get())
            almders=int(almsv.get())

            matvardeger=int(matvar.get())
            kimvardeger=int(kimvar.get())
            fizvardeger=int(fizvar.get())
            biyovardeger=int(biyovar.get())
            edebvardeger=int(edebvar.get())
            tarvardeger=int(tarvar.get())
            felvardeger=int(felvar.get())
            dinvardeger=int(dinvar.get())
            ingvardeger=int(ingvar.get())
            bedvardeger=int(bedvar.get())
            muzvardeger=int(muzvar.get())
            almvardeger=int(almvar.get())

            derssaat= matders + kimders +fizders +biyoders+edebders+tarders+felders+dinders+ingders+bedders+muzders+almders

            if matvardeger==0:
                matnot=0
                derssaat=derssaat-matders
            else:
                matnot=float(matnotgir.get())
        ##-----------------------------------------##
            if kimvardeger == 0:
                kimyanot=0
                derssaat=derssaat-kimders
            else:
                kimyanot = float(kimyanotgir.get())
        ##-----------------------------------------##
            if fizvardeger == 0:
                fiziknot=0;
                derssaat=derssaat-fizders
            else:
                fiziknot = float(fiziknotgir.get())
        ##-----------------------------------------##
            if biyovardeger == 0:
                biyonot=0
                derssaat=derssaat-biyoders
            else:
                biyonot = float(biyonotgir.get())
        ##-----------------------------------------##
            if edebvardeger == 0:
                edebnot=0
                derssaat=derssaat-edebders
            else:
                edebnot = float(edebnotgir.get())
        ##-----------------------------------------##
            if tarvardeger == 0:
                tarihnot=0
                derssaat=derssaat-tarders
            else:
                tarihnot = float(tarihnotgir.get())
        ##-----------------------------------------##
            if felvardeger==0:
               felnot=0
               derssaat=derssaat-felders
            else:
                felnot = float(felnotgir.get())
        ##-----------------------------------------##
            if dinvardeger==0:
                dinnot=0
                derssaat=derssaat-dinders
            else:
                dinnot = float(dinnotgir.get())
        ##-----------------------------------------##
            if ingvardeger==0:
                ingnot=0
                derssaat=derssaat-ingders
            else:
                ingnot = float(ingnotgir.get())
        ##-----------------------------------------##
            if bedvardeger==0:
                bednot=0
                derssaat=derssaat-bedders
            else:
                bednot = float(bednotgir.get())
        ##-----------------------------------------##
            if muzvardeger==0:
                muziknot=0
                derssaat=derssaat-muzders
            else:
                muziknot = float(muziknotgir.get())
        ##-----------------------------------------##
            if almvardeger==0:
                almnot=0
                derssaat=derssaat-almders
            else:
                almnot = float(almnotgir.get())
            cursor.execute("UPDATE saatler SET smat = {} WHERE no = {}".format(matders,notno))
            cursor.execute("UPDATE saatler SET sfizik = {} WHERE no = {}".format(fizders,notno))
            cursor.execute("UPDATE saatler SET skimya = {} WHERE no = {}".format(kimders,notno))
            cursor.execute("UPDATE saatler SET sbiyo = {} WHERE no = {}".format(biyoders,notno))
            cursor.execute("UPDATE saatler SET sedeb = {} WHERE no = {}".format(edebders,notno))
            cursor.execute("UPDATE saatler SET starih = {} WHERE no = {}".format(tarders,notno))
            cursor.execute("UPDATE saatler SET sfel = {} WHERE no = {}".format(felders,notno))
            cursor.execute("UPDATE saatler SET sdin = {} WHERE no = {}".format(dinders,notno))
            cursor.execute("UPDATE saatler SET sing = {} WHERE no = {}".format(ingders,notno))
            cursor.execute("UPDATE saatler SET sbeden = {} WHERE no = {}".format(bedders,notno))
            cursor.execute("UPDATE saatler SET smuzik = {} WHERE no = {}".format(muzders,notno))
            cursor.execute("UPDATE saatler SET salm = {} WHERE no = {}".format(almders,notno))
            cursor.execute("UPDATE saatler SET toplam = {} WHERE no = {}".format(derssaat,notno))

            cursor.execute("UPDATE dersler SET mat = {} WHERE no = {}".format(matnot,notno))
            cursor.execute("UPDATE dersler SET kimya = {} WHERE no = {}".format(kimyanot,notno))
            cursor.execute("UPDATE dersler SET fizik = {} WHERE no = {}".format(fiziknot,notno))
            cursor.execute("UPDATE dersler SET biyo = {} WHERE no = {}".format(biyonot,notno))
            cursor.execute("UPDATE dersler SET edeb = {} WHERE no = {}".format(edebnot,notno))
            cursor.execute("UPDATE dersler SET tarih = {} WHERE no = {}".format(tarihnot,notno))
            cursor.execute("UPDATE dersler SET fel = {} WHERE no = {}".format(felnot,notno))
            cursor.execute("UPDATE dersler SET din = {} WHERE no = {}".format(dinnot,notno))
            cursor.execute("UPDATE dersler SET ing = {} WHERE no = {}".format(ingnot,notno))
            cursor.execute("UPDATE dersler SET beden = {} WHERE no = {}".format(bednot,notno))
            cursor.execute("UPDATE dersler SET muzik = {} WHERE no = {}".format(muziknot,notno))
            cursor.execute("UPDATE dersler SET alm = {} WHERE no = {}".format(almnot,notno))

            cursor.execute("UPDATE chek SET cmat = {} WHERE no = {}".format(matvardeger,notno))
            cursor.execute("UPDATE chek SET cfizik = {} WHERE no = {}".format(fizvardeger,notno))
            cursor.execute("UPDATE chek SET ckimya = {} WHERE no = {}".format(kimvardeger,notno))
            cursor.execute("UPDATE chek SET cbiyo = {} WHERE no = {}".format(biyovardeger,notno))
            cursor.execute("UPDATE chek SET cedeb = {} WHERE no = {}".format(edebvardeger,notno))
            cursor.execute("UPDATE chek SET ctarih = {} WHERE no = {}".format(tarvardeger,notno))
            cursor.execute("UPDATE chek SET cfel = {} WHERE no = {}".format(felvardeger,notno))
            cursor.execute("UPDATE chek SET cdin = {} WHERE no = {}".format(dinvardeger,notno))
            cursor.execute("UPDATE chek SET cing = {} WHERE no = {}".format(ingvardeger,notno))
            cursor.execute("UPDATE chek SET cbeden = {} WHERE no = {}".format(bedvardeger,notno))
            cursor.execute("UPDATE chek SET cmuzik = {} WHERE no = {}".format(muzvardeger,notno))
            cursor.execute("UPDATE chek SET calm = {} WHERE no = {}".format(almvardeger,notno))
            con.commit()
            notpenc.destroy()
        cursor.execute("SELECT * FROM saatler WHERE no={}".format(notno))
        notsaat=cursor.fetchone()
        matders = notsaat[1]
        fizders = notsaat[2]
        kimders = notsaat[3]
        biyoders = notsaat[4]
        edebders = notsaat[5]
        tarders = notsaat[6]
        felders = notsaat[7]
        dinders = notsaat[8]
        ingders = notsaat[9]
        bedders = notsaat[10]
        muzders = notsaat[11]
        almders = notsaat[12]

        cursor.execute("SELECT * FROM chek WHERE no={}".format(notno))
        notchek = cursor.fetchone()
        matvardeger = notchek[1]
        fizvardeger = notchek[2]
        kimvardeger = notchek[3]
        biyovardeger = notchek[4]
        edebvardeger = notchek[5]
        tarvardeger = notchek[6]
        felvardeger = notchek[7]
        dinvardeger = notchek[8]
        ingvardeger = notchek[9]
        bedvardeger = notchek[10]
        muzvardeger = notchek[11]
        almvardeger = notchek[12]

        aynidersler()
        fizvar = IntVar(notpenc,value=fizvardeger)
        fizen = IntVar(notpenc,value=fiziknot)
        fizikchk = Checkbutton(notpenc,width=10, text="Fizik=",variable= fizvar,anchor="w")
        fizikchk.grid(row=1,column=0)
        fiziknotgir = Entry(notpenc,width="8",textvariable=fizen)
        fiziknotgir.grid(row=1,column=1)
        fizsv.set(fizders)
        fizspin=Spinbox(notpenc,from_=1,to=10,width=2,textvariable=fizsv)
        fizspin.grid(row=1,column=2,sticky="w")
##================================================================
        kimvar = IntVar(notpenc,value=kimvardeger)
        kimen = IntVar(notpenc,value=kimyanot)
        kimyachk  = Checkbutton(notpenc,width=10,text = "Kimya=",variable=kimvar,anchor="w")
        kimyachk.grid(row=2,column=0)
        kimyanotgir = Entry(notpenc,width="8",textvariable=kimen)
        kimyanotgir.grid(row=2,column=1)
        kimsv.set(kimders)
        kimspin=Spinbox(notpenc,from_=1,to=10,width=2,textvariable=kimsv)
        kimspin.grid(row=2,column=2,sticky="w")
 ##================================================================
        biyovar = IntVar(notpenc,value=biyovardeger)
        biyoen = IntVar(notpenc,value=biyonot)
        biyochk = Checkbutton(notpenc,width=10, text="Biyoloji=",variable=biyovar,anchor="w")
        biyochk.grid(row=3,column=0)
        biyonotgir = Entry(notpenc,width="8",textvariable=biyoen)
        biyonotgir.grid(row=3,column=1)
        biyosv.set(biyoders)
        biyospin=Spinbox(notpenc,from_=1,to=10,width=2,textvariable=biyosv)
        biyospin.grid(row=3,column=2,sticky="w")
 ##================================================================

        pskchk = Label(notpenc,width=12, text="",anchor="w")
        pskchk.grid(row=12,column=0)
        psknotgir  = Label(notpenc,width="8",text = "")
        psknotgir.grid(row=12,column=1)
        pskspin  = Label(notpenc,width="3",text = "")
        pskspin.grid(row=12,column=2,sticky="w")

        def sec():
            if(tamvar.get()==1):
                matchk.select()
                fizikchk.select()
                kimyachk.select()
                biyochk.select()
                edebchk.select()
                tarihchk.select()
                felchk.select()
                dinchk.select()
                ingchk.select()
                bedchk.select()
                muzikchk.select()
                almchk.select()
            else:
                matchk.deselect()
                fizikchk.deselect()
                kimyachk.deselect()
                biyochk.deselect()
                edebchk.deselect()
                tarihchk.deselect()
                felchk.deselect()
                dinchk.deselect()
                ingchk.deselect()
                bedchk.deselect()
                muzikchk.deselect()
                almchk.deselect()
        tamvar= IntVar(notpenc)
        tamami = Checkbutton(notpenc,width=10, text="Tümünü seç",command=sec,variable=tamvar,anchor="w")
        tamami.grid(row=13,column=0)

        giris = Button(notpenc,text="Kaydet",command=girisyapma)
        giris.place(relx=0.37,rely=0.90)
        ortdurum = Label(notpenc,width=15,text="")
        ortdurum.grid(row=0,column=5)
    def alantm():
        global matvardeger, edebvardeger, tarvardeger, felvardeger, dinvardeger, ingvardeger, bedvardeger, muzvardeger, almvardeger
        global matders, edebders, tarders, felders, dinders, ingders, bedders, muzders, almders
        def girisyapma():
            matders=int(matsv.get())
            edebders=int(edebsv.get())
            tarders=int(tarsv.get())
            felders=int(felsv.get())
            dinders=int(dinsv.get())
            ingders=int(ingsv.get())
            bedders=int(bedsv.get())
            muzders=int(muzsv.get())
            almders=int(almsv.get())
            cogders=int(cogsv.get())
            secedbders=int(secedbsv.get())
            tkmtders=int(tkmtsv.get())
            pskders=int(psksv.get())

            matvardeger=int(matvar.get())
            edebvardeger=int(edebvar.get())
            tarvardeger=int(tarvar.get())
            felvardeger=int(felvar.get())
            dinvardeger=int(dinvar.get())
            ingvardeger=int(ingvar.get())
            bedvardeger=int(bedvar.get())
            muzvardeger=int(muzvar.get())
            almvardeger=int(almvar.get())
            cogvardeger=int(cogvar.get())
            secedbvardeger=int(secedbvar.get())
            tkmtvardeger=int(tkmtvar.get())
            pskvardeger=int(pskvar.get())
            derssaat= matders + cogders +secedbders +tkmtders+pskders+edebders+tarders+felders+dinders+ingders+bedders+muzders+almders
         ##-----------------------------------------##
            matvardeger=int(matvar.get())
            if matvardeger==0:
                matnot=0
                derssaat=derssaat-matders
            else:
                matnot = float(matnotgir.get())

        ##-----------------------------------------##
            cogvardeger=int(cogvar.get())
            if cogvardeger == 0:
                cognot=0
                derssaat=derssaat-cogders
            else:
                cognot = float(cognotgir.get())

        ##-----------------------------------------##
            secedbvardeger=int(secedbvar.get())
            if secedbvardeger == 0:
                secedbnot=0;
                derssaat=derssaat-secedbders
            else:
                secedbnot = float(secedbnotgir.get())
        ##-----------------------------------------##
            tkmtvardeger=int(tkmtvar.get())
            if tkmtvardeger == 0:
                tkmtnot=0
                derssaat=derssaat-tkmtders
            else:
                tkmtnot = float(tkmtnotgir.get())
        ##-----------------------------------------##
            if edebvardeger == 0:
                edebnot=0
                derssaat=derssaat-edebders
            else:
                edebnot = float(edebnotgir.get())
        ##-----------------------------------------##
            if tarvardeger == 0:
                tarihnot=0
                derssaat=derssaat-tarders
            else:
                tarihnot = float(tarihnotgir.get())
        ##-----------------------------------------##
            if felvardeger==0:
               felnot=0
               derssaat=derssaat-felders
            else:
                felnot = float(felnotgir.get())
        ##-----------------------------------------##
            if dinvardeger==0:
                dinnot=0
                derssaat=derssaat-dinders
            else:
                dinnot = float(dinnotgir.get())
        ##-----------------------------------------##
            if ingvardeger==0:
                ingnot=0
                derssaat=derssaat-ingders
            else:
                ingnot = float(ingnotgir.get())
        ##-----------------------------------------##
            if bedvardeger==0:
                bednot=0
                derssaat=derssaat-bedders
            else:
                bednot = float(bednotgir.get())
        ##-----------------------------------------##
            if muzvardeger==0:
                muziknot=0
                derssaat=derssaat-muzders
            else:
                muziknot = float(muziknotgir.get())
        ##-----------------------------------------##
            if almvardeger==0:
                almnot=0
                derssaat=derssaat-almders
            else:
                almnot = float(almnotgir.get())

        ##-----------------------------------------##
            pskvardeger=int(pskvar.get())
            if pskvardeger==0:
                psknot=0
                derssaat=derssaat-pskders
            else:
                psknot = float(psknotgir.get())
            cursor.execute("UPDATE dersler SET pisk = {} WHERE no = {}".format(psknot,notno))
            cursor.execute("UPDATE dersler SET tkmt = {} WHERE no = {}".format(tkmtnot, notno))
            cursor.execute("UPDATE dersler SET mat = {} WHERE no = {}".format(matnot, notno))
            cursor.execute("UPDATE dersler SET cog = {} WHERE no = {}".format(cognot, notno))
            cursor.execute("UPDATE dersler SET secedb = {} WHERE no = {}".format(secedbnot, notno))
            cursor.execute("UPDATE dersler SET edeb = {} WHERE no = {}".format(edebnot,notno))
            cursor.execute("UPDATE dersler SET tarih = {} WHERE no = {}".format(tarihnot,notno))
            cursor.execute("UPDATE dersler SET fel = {} WHERE no = {}".format(felnot,notno))
            cursor.execute("UPDATE dersler SET din = {} WHERE no = {}".format(dinnot,notno))
            cursor.execute("UPDATE dersler SET ing = {} WHERE no = {}".format(ingnot,notno))
            cursor.execute("UPDATE dersler SET beden = {} WHERE no = {}".format(bednot,notno))
            cursor.execute("UPDATE dersler SET muzik = {} WHERE no = {}".format(muziknot,notno))
            cursor.execute("UPDATE dersler SET alm = {} WHERE no = {}".format(almnot,notno))

            cursor.execute("UPDATE saatler SET spisk = {} WHERE no = {}".format(pskders, notno))
            cursor.execute("UPDATE saatler SET smat = {} WHERE no = {}".format(matders,notno))
            cursor.execute("UPDATE saatler SET stkmt = {} WHERE no = {}".format(tkmtders,notno))
            cursor.execute("UPDATE saatler SET scog = {} WHERE no = {}".format(cogders,notno))
            cursor.execute("UPDATE saatler SET ssecedb = {} WHERE no = {}".format(secedbders,notno))
            cursor.execute("UPDATE saatler SET sedeb = {} WHERE no = {}".format(edebders,notno))
            cursor.execute("UPDATE saatler SET starih = {} WHERE no = {}".format(tarders,notno))
            cursor.execute("UPDATE saatler SET sfel = {} WHERE no = {}".format(felders,notno))
            cursor.execute("UPDATE saatler SET sdin = {} WHERE no = {}".format(dinders,notno))
            cursor.execute("UPDATE saatler SET sing = {} WHERE no = {}".format(ingders,notno))
            cursor.execute("UPDATE saatler SET sbeden = {} WHERE no = {}".format(bedders,notno))
            cursor.execute("UPDATE saatler SET smuzik = {} WHERE no = {}".format(muzders,notno))
            cursor.execute("UPDATE saatler SET salm = {} WHERE no = {}".format(almders,notno))
            cursor.execute("UPDATE saatler SET toplam = {} WHERE no = {}".format(derssaat,notno))

            cursor.execute("UPDATE chek SET cpisk = {} WHERE no = {}".format(pskvardeger, notno))
            cursor.execute("UPDATE chek SET cmat = {} WHERE no = {}".format(matvardeger,notno))
            cursor.execute("UPDATE chek SET ctkmt = {} WHERE no = {}".format(tkmtvardeger,notno))
            cursor.execute("UPDATE chek SET ccog = {} WHERE no = {}".format(cogvardeger,notno))
            cursor.execute("UPDATE chek SET csecedb = {} WHERE no = {}".format(secedbvardeger,notno))
            cursor.execute("UPDATE chek SET cedeb = {} WHERE no = {}".format(edebvardeger,notno))
            cursor.execute("UPDATE chek SET ctarih = {} WHERE no = {}".format(tarvardeger,notno))
            cursor.execute("UPDATE chek SET cfel = {} WHERE no = {}".format(felvardeger,notno))
            cursor.execute("UPDATE chek SET cdin = {} WHERE no = {}".format(dinvardeger,notno))
            cursor.execute("UPDATE chek SET cing = {} WHERE no = {}".format(ingvardeger,notno))
            cursor.execute("UPDATE chek SET cbeden = {} WHERE no = {}".format(bedvardeger,notno))
            cursor.execute("UPDATE chek SET cmuzik = {} WHERE no = {}".format(muzvardeger,notno))
            cursor.execute("UPDATE chek SET calm = {} WHERE no = {}".format(almvardeger,notno))
            con.commit()
            notpenc.destroy()

        cursor.execute("SELECT * FROM saatler WHERE no={}".format(notno))
        notsaat=cursor.fetchone()
        matders = notsaat[1]
        edebders = notsaat[5]
        tarders = notsaat[6]
        felders = notsaat[7]
        dinders = notsaat[8]
        ingders = notsaat[9]
        bedders = notsaat[10]
        muzders = notsaat[11]
        almders = notsaat[12]
        cogders = notsaat[13]
        secedbders = notsaat[14]
        tkmtders = notsaat[15]
        pskders = notsaat[16]

        cursor.execute("SELECT * FROM chek WHERE no={}".format(notno))
        notchek = cursor.fetchone()
        matvardeger = notchek[1]
        edebvardeger = notchek[5]
        tarvardeger = notchek[6]
        felvardeger = notchek[7]
        dinvardeger = notchek[8]
        ingvardeger = notchek[9]
        bedvardeger = notchek[10]
        muzvardeger = notchek[11]
        almvardeger = notchek[12]
        cogvardeger = notchek[13]
        secedbvardeger = notchek[14]
        tkmtvardeger = notchek[15]
        pskvardeger = notchek[16]
        aynidersler()
        cogvar = IntVar(notpenc,value=cogvardeger)
        cogen = IntVar(notpenc,value=cognot)
        cogchk  = Checkbutton(notpenc,text = "Coğrafya=", variable= cogvar,width="10",anchor="w")
        cogchk.grid(row=1,column=0)
        cognotgir = Entry(notpenc,width="8",textvariable= cogen)
        cognotgir.grid(row=1,column=1)
        cogsv.set(cogders)
        cogspin=Spinbox(notpenc,from_=1,to=10,width=2,textvariable=cogsv)
        cogspin.grid(row=1,column=2,sticky="w")
     ##================================================================
        secedbvar = IntVar(notpenc,value=secedbvardeger)
        secedben = IntVar(notpenc,value=secedbnot)
        secedbchk  = Checkbutton(notpenc,text = "Seçmeli Edb.=",  variable= secedbvar,width="10",anchor="w")
        secedbchk.grid(row=2,column=0)
        secedbnotgir = Entry(notpenc,width="8",textvariable=secedben)
        secedbnotgir.grid(row=2,column=1)
        secedbsv.set(secedbders)
        secedbspin=Spinbox(notpenc,from_=1,to=10,width=2,textvariable=secedbsv)
        secedbspin.grid(row=2,column=2,sticky="w")
     ##================================================================
        tkmtvar = IntVar(notpenc,value=tkmtvardeger)
        tkmten = IntVar(notpenc,value=tkmtnot)
        tkmtchk  = Checkbutton(notpenc,text = "Tkmt=", variable= tkmtvar,width="10",anchor="w")
        tkmtchk.grid(row=3,column=0)
        tkmtnotgir = Entry(notpenc,width="8",textvariable=tkmten )
        tkmtnotgir.grid(row=3,column=1)
        tkmtsv.set(tkmtders)
        tkmtspin=Spinbox(notpenc,from_=1,to=10,width=2,textvariable=tkmtsv)
        tkmtspin.grid(row=3,column=2,sticky="w")
    ##=================================================
        edebvar = IntVar(notpenc, value=edebvardeger)
        edeben = IntVar(notpenc, value=edebnot)
        edebchk = Checkbutton(notpenc, width=10, text="Edebiyat=", variable=edebvar, anchor="w")
        edebchk.grid(row=4, column=0)
        edebnotgir = Entry(notpenc, width="8", textvariable=edeben)
        edebnotgir.grid(row=4, column=1)
        edebsv.set(edebders)
        edebspin = Spinbox(notpenc, from_=1, to=10, width=2, textvariable=edebsv)
        edebspin.grid(row=4, column=2, sticky="w")
#   #===================================================
        pskvar = IntVar(notpenc,value=pskvardeger)
        psken = IntVar(notpenc,value=psknot)
        pskchk = Checkbutton(notpenc,text="Psikoloji=", variable=pskvar,width="10",anchor="w")
        pskchk.grid(row=12,column=0)
        psknotgir = Entry(notpenc,width="8",textvariable= psken)
        psknotgir.grid(row=12,column=1)
        psksv.set(pskders)
        pskspin=Spinbox(notpenc,from_=1,to=10,width=2,textvariable=psksv)
        pskspin.grid(row=12,column=2,sticky="w")
     ##================================================================
        giris = Button(notpenc,text="Kaydet",command=girisyapma)
        giris.place(relx=0.37,rely=0.90)

        def sectm():
            if(tamvartm.get()==1):
                matchk.select()
                cogchk.select()
                secedbchk.select()
                tkmtchk.select()
                edebchk.select()
                tarihchk.select()
                felchk.select()
                dinchk.select()
                ingchk.select()
                bedchk.select()
                muzikchk.select()
                almchk.select()
                pskchk.select()
            else:
                matchk.deselect()
                cogchk.deselect()
                secedbchk.deselect()
                tkmtchk.deselect()
                edebchk.deselect()
                tarihchk.deselect()
                felchk.deselect()
                dinchk.deselect()
                ingchk.deselect()
                bedchk.deselect()
                muzikchk.deselect()
                almchk.deselect()
                pskchk.deselect()
        tamvartm= IntVar(notpenc)
        tamami = Checkbutton(notpenc,width=10, text="Tümünü seç",command=sectm,variable=tamvartm,anchor="w")
        tamami.grid(row=13,column=0)
    def aynidersler():
        global matvar,edebvar,tarvar,dinvar,felvar,ingvar,bedvar,muzvar,almvar
        global matnotgir,edebnotgir,tarihnotgir,dinnotgir,felnotgir,ingnotgir,bednotgir,muziknotgir,almnotgir
        global matchk,edebchk,tarihchk,dinchk,felchk,ingchk,bedchk,muzikchk,almchk
        matvar = IntVar(notpenc, value=matvardeger)
        maten = IntVar(notpenc, value=matnot)
        matchk = Checkbutton(notpenc, text="Matematik=", variable=matvar, width="10", anchor="w")
        matchk.grid(row=0, column=0)
        matnotgir = Entry(notpenc, width="8", textvariable=maten)
        matnotgir.grid(row=0, column=1)
        matsv.set(matders)
        matspin = Spinbox(notpenc, from_=1, to=10, width=2, textvariable=matsv)
        matspin.grid(row=0, column=2, sticky="w")

        edebvar = IntVar(notpenc, value=edebvardeger)
        edeben = IntVar(notpenc, value=edebnot)
        edebchk = Checkbutton(notpenc, width=10, text="Edebiyat=", variable=edebvar, anchor="w")
        edebchk.grid(row=4, column=0)
        edebnotgir = Entry(notpenc, width="8", textvariable=edeben)
        edebnotgir.grid(row=4, column=1)
        edebsv.set(edebders)
        edebspin = Spinbox(notpenc, from_=1, to=10, width=2, textvariable=edebsv)
        edebspin.grid(row=4, column=2, sticky="w")
        ##================================================================
        tarvar = IntVar(notpenc, value=tarvardeger)
        tarihen = IntVar(notpenc, value=tarihnot)
        tarihchk = Checkbutton(notpenc, width=10, text="Tarih=", variable=tarvar, anchor="w")
        tarihchk.grid(row=5, column=0)
        tarihnotgir = Entry(notpenc, width="8", textvariable=tarihen)
        tarihnotgir.grid(row=5, column=1)
        tarsv.set(tarders)
        tarspin = Spinbox(notpenc, from_=1, to=10, width=2, textvariable=tarsv)
        tarspin.grid(row=5, column=2, sticky="w")
        ##================================================================
        felvar = IntVar(notpenc, value=felvardeger)
        felen = IntVar(notpenc, value=felnot)
        felchk = Checkbutton(notpenc, width=10, text="Felsefe=", variable=felvar, anchor="w")
        felchk.grid(row=6, column=0)
        felnotgir = Entry(notpenc, width="8", textvariable=felen)
        felnotgir.grid(row=6, column=1)
        felsv.set(felders)
        felspin = Spinbox(notpenc, from_=1, to=10, width=2, textvariable=felsv)
        felspin.grid(row=6, column=2, sticky="w")
        ##================================================================
        dinvar = IntVar(notpenc, value=dinvardeger)
        dinen = IntVar(notpenc, value=dinnot)
        dinchk = Checkbutton(notpenc, width=10, text="Din K.=", variable=dinvar, anchor="w")
        dinchk.grid(row=7, column=0)
        dinnotgir = Entry(notpenc, width="8", textvariable=dinen)
        dinnotgir.grid(row=7, column=1)
        dinsv.set(dinders)
        dinspin = Spinbox(notpenc, from_=1, to=10, width=2, textvariable=dinsv)
        dinspin.grid(row=7, column=2, sticky="w")
        ##================================================================
        ingvar = IntVar(notpenc, value=ingvardeger)
        ingen = IntVar(notpenc, value=ingnot)
        ingchk = Checkbutton(notpenc, width=10, text="İngilizce=", variable=ingvar, anchor="w")
        ingchk.grid(row=8, column=0)
        ingnotgir = Entry(notpenc, width="8", textvariable=ingen)
        ingnotgir.grid(row=8, column=1)
        ingsv.set(ingders)
        ingspin = Spinbox(notpenc, from_=1, to=10, width=2, textvariable=ingsv)
        ingspin.grid(row=8, column=2, sticky="w")
        ##================================================================
        bedvar = IntVar(notpenc, value=bedvardeger)
        bedenn = IntVar(notpenc, value=bednot)
        bedchk = Checkbutton(notpenc, width=10, text="Beden=", variable=bedvar, anchor="w")
        bedchk.grid(row=9, column=0)
        bednotgir = Entry(notpenc, width="8", textvariable=bedenn)
        bednotgir.grid(row=9, column=1)
        bedsv.set(bedders)
        bedspin = Spinbox(notpenc, from_=1, to=10, width=2, textvariable=bedsv)
        bedspin.grid(row=9, column=2, sticky="w")
        ##================================================================
        muzvar = IntVar(notpenc, value=muzvardeger)
        muzen = IntVar(notpenc, value=muziknot)
        muzikchk = Checkbutton(notpenc, width=10, text="Müz/Gör=", variable=muzvar, anchor="w")
        muzikchk.grid(row=10, column=0)
        muziknotgir = Entry(notpenc, width="8", textvariable=muzen)
        muziknotgir.grid(row=10, column=1)
        muzsv.set(muzders)
        muzspin = Spinbox(notpenc, from_=1, to=10, width=2, textvariable=muzsv)
        muzspin.grid(row=10, column=2, sticky="w")
        ##================================================================
        almvar = IntVar(notpenc, value=almvardeger)
        almen = IntVar(notpenc, value=almnot)
        almchk = Checkbutton(notpenc, width=10, text="Almanca=", variable=almvar, anchor="w")
        almchk.grid(row=11, column=0)
        almnotgir = Entry(notpenc, width="8", textvariable=almen)
        almnotgir.grid(row=11, column=1)
        almsv.set(almders)
        almspin = Spinbox(notpenc, from_=1, to=10, width=2, textvariable=almsv)
        almspin.grid(row=11, column=2, sticky="w")
    if(datanotalan=="MF"):
        alanmf()
    elif(datanotalan=="TM"):
        alantm()

def oturum():
    global sifrepenc,girilenka,girilensif
    sifrepenc = Tk()
    sifrepenc.title("Oturum Açın")
    sifrepenc.geometry("300x110+520+285")
    uyariks = Label(sifrepenc, text="", width=30)
    uyariks.grid(row=3, column=0, columnspan=2)
    cursor.execute("select count(yetki) from kullanicilar")
    kulsayisi = cursor.fetchone()[0]
    if (kulsayisi == 0):
        cursor.execute("INSERT INTO kullanicilar VALUES('{}','{}','{}')".format("admin", "admin", 2))
        con.commit()
        uyariks.config(text="Şifre : admin")
    cursor.execute("SELECT kuladi FROM kullanicilar")
    ka = cursor.fetchall()
    var = IntVar(sifrepenc)
    kullanicilab = Label(sifrepenc, text="Kullanıcı Adı : ", width=15)
    kullanicilab.grid(row=0, column=0)
    girilenka = Combobox(sifrepenc, values=ka, state="readonly", width=17, textvariable=var)
    girilenka.grid(row=0, column=1)
    girilenka.current(0)

    sifrelab = Label(sifrepenc, text="Şifre : ", width=15)
    sifrelab.grid(row=1, column=0)
    girilensif = Entry(sifrepenc, width=20)
    girilensif.grid(row=1, column=1)
    def kontrolet():
        global yetkiseviyesi, girilenkuladi
        girilenkuladi = girilenka.get()
        girilensifre = girilensif.get()

        cursor.execute("SELECT sifre FROM kullanicilar WHERE kuladi='{}'".format(girilenkuladi))
        cekilensifre = cursor.fetchone()
        gelensifre = cekilensifre[0]
        if (gelensifre == girilensifre):
            cursor.execute("SELECT yetki FROM kullanicilar WHERE kuladi='{}'".format(girilenkuladi))
            yetkiseviyesi = cursor.fetchone()[0]
            sifredogru()
        else:
            uyariks.config(text="Hatalı kullanıcı adı veya şifre")
    girisbuton = Button(sifrepenc, text="Giriş yap", command=kontrolet)
    girisbuton.grid(row=2, column=12)
    sifrepenc.mainloop()
oturum()


