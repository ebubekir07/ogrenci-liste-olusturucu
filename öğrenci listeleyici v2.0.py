from tkinter import *
import sqlite3
from tkinter.ttk import Combobox
from tkinter import messagebox
pencere = Tk()
pencere.title("Veri")
pencere.geometry("900x600+25+25")


bosluk = Label(pencere,text="",width=7)
bosluk.grid(row=3,column=5)
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




bilgilab1=Label(pencere,text="Öğrenci Sil",
                  font=("Comic Sans MS",11,"bold"),width=30,anchor="w")
bilgilab1.grid(row=0,column=8,columnspan=9)

bilgilab2=Label(pencere,text="Bilgileri Getir",
                  font=("Comic Sans MS",11,"bold"),width=15)
bilgilab2.grid(row=0,column=11,columnspan=12)

con = sqlite3.connect("veritabani.db")
cursor = con.cursor()
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
######################3
cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(no INT,ad TEXT,soyad TEXT,sinif INT,sube TEXT,tc INT,tel INT,ay TEXT,gun INT,yil INT)")
cursor.execute('SELECT no FROM ogrenciler ORDER BY no ASC')
################################3

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
    cursor.execute("select count(*) from ogrenciler WHERE no={}".format(no))
    kontrol2 = cursor.fetchone()
    
    if (kontrol2[0]==1):
        uyarilabel.config(text="Bu numaraya sahip öğrenci \n listede mevcut.")
    
    elif(len(str(tc))!=11):
       print("Geçerli bir tc no girin")
       uyarilabel.config(text="Geçerli bir tc no girin.")

    elif(len(str(tel))!=10):
        print("geçerli tel gir")
        uyarilabel.config(text="Geçerli bir telefon no girin.")
    
        



            
    else:
        pencere2.destroy()
        cursor.execute("INSERT INTO ogrenciler VALUES('{} ','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(no,ad,soyad,sinif,sube,tc,tel,ay,gun,yil))
        con.commit()
        cursor.execute('SELECT no FROM ogrenciler ORDER BY no ASC')
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
    #print(datasinif)


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

silno = Label(pencere,text="Okul No:",width=10,anchor="w")
silno.grid(row=1,column=8)
silen = Entry(pencere,width=10)
silen.grid(row=1,column=9)

bosluklab=Label(pencere,text="",width=7)
bosluklab.grid(row=1,column=10)

getirno = Label(pencere,text="Okul No:",width=10,anchor="w")
getirno.grid(row=1,column=11)
getiren = Entry(pencere,width=10)
getiren.grid(row=1,column=12)
def pencereekle():
    global aden,soyaden,sinifen,oknoen,subeen,tcen,telen,dogumay,dogumgun,dogumyil,uyarilabel,pencere2,ayen
    pencere2 = Tk()
    pencere2.title("Yeni Öğrenci")
    pencere2.geometry("250x360+450+250")
    yilen = IntVar(pencere2)
    gunen = IntVar(pencere2)
    ayen = StringVar(pencere2)
    
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


    labelay = Label(pencere2,text="D. Ayı:",width=7,anchor="w")
    labelay.grid(row=8,column=0)
    dogumay = Combobox(pencere2,values=aylar,state="readonly",width=17 ,textvariable=ayen)
    dogumay.grid(row=8,column=1)
    dogumay.current(0)

    gunen.set(1)
    labelgun = Label(pencere2,text="D. Günü:",width=7,anchor="w")
    labelgun.grid(row=9,column=0)
    dogumgun=Spinbox(pencere2,from_=1,to=31,width=18,textvariable=gunen)
    dogumgun.grid(row=9,column=1)

    yilen.set(2002)
    labelyil = Label(pencere2,text="D. Yılı:",width=7,anchor="w")
    labelyil.grid(row=10,column=0)
    dogumyil=Spinbox(pencere2,from_=1950,to=2030,width=18,textvariable=yilen)
    dogumyil.grid(row=10,column=1)

    uyarilabel=Label(pencere2,text="",width=30)
    uyarilabel.grid(row=12,column=0,columnspan=2)
    
    eklebuton = Button(pencere2,text="Ekle",command=kisiekleme)
    eklebuton.grid(row=11,column=1)

eklebuton = Button(pencere,text="Yeni Öğrenci Ekle",command=pencereekle)
eklebuton.place(relx=0.65,rely=0.20)



silbuton = Button(pencere,text="Sil",command=kisisil)
silbuton.grid(row=2,column=9)

getirbuton = Button(pencere,text="Getir",command=kisigetir)
getirbuton.grid(row=2,column=12)


pencere.mainloop()
