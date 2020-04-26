from tkinter import *
import sqlite3
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





bilgilab=Label(pencere,text="Yeni Öğrenci Ekle",
                  font=("Comic Sans MS",11,"bold"),anchor="w",width=20)
bilgilab.grid(row=0,column=7)

bilgilab1=Label(pencere,text="Öğrenci Sil",
                  font=("Comic Sans MS",11,"bold"),width=20)
bilgilab1.grid(row=0,column=8,columnspan=9)

bilgilab2=Label(pencere,text="Bilgileri Getir",
                  font=("Comic Sans MS",11,"bold"),width=20)
bilgilab2.place(relx=0.74,rely=0.15)

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
                            "Ad : {}\nSoyad : {}\nSınıf : {}\nNumara : {}".format(gelenveri[1],gelenveri[2],
                                                                          gelenveri[3],gelenveri[0]))
    
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
cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(no INT,ad TEXT,soyad TEXT,sinif INT)")
cursor.execute('SELECT no FROM ogrenciler ORDER BY no ASC')
################################3

def kisiekleme():
    ad=str(aden.get())
    soyad=str(soyaden.get())
    sinif=int(sinifen.get())
    no=int(oknoen.get())
    aden.delete(first=0,last=30)
    soyaden.delete(first=0,last=30)
    sinifen.delete(first=0,last=30)
    oknoen.delete(first=0,last=30)
    cursor.execute("select count(*) from ogrenciler WHERE no={}".format(no))
    kontrol2 = cursor.fetchone()
    if (kontrol2[0]==1):
        messagebox.showinfo("Uyarı","Bu numaraya sahip öğrenci listede mevcut.")
    else:
        
        cursor.execute("INSERT INTO ogrenciler VALUES('{} ','{}','{}','{}')".format(no,ad,soyad,sinif))
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


silno = Label(pencere,text="Okul No:",width=10,anchor="w")
silno.grid(row=1,column=8)
silen = Entry(pencere,width=10)
silen.grid(row=1,column=9)

getirno = Label(pencere,text="Okul No:",width=10,anchor="w")
getirno.grid(row=6,column=8)
getiren = Entry(pencere,width=10)
getiren.grid(row=6,column=9)

eklelabad = Label(pencere,text="Ad:",width=7,anchor="w")
eklelabad.grid(row=1,column=6)
aden = Entry(pencere,width=20)
aden.grid(row=1,column=7)

eklelabsoyad = Label(pencere,text="Soyad:",width=7,anchor="w")
eklelabsoyad.grid(row=2,column=6)
soyaden = Entry(pencere,width=20)
soyaden.grid(row=2,column=7)

eklelabsinif = Label(pencere,text="Sınıf:",width=7,anchor="w")
eklelabsinif.grid(row=3,column=6)
sinifen = Entry(pencere,width=20)
sinifen.grid(row=3,column=7)

eklelabokno = Label(pencere,text="Okul No:",width=7,anchor="w")
eklelabokno.grid(row=4,column=6)
oknoen = Entry(pencere,width=20)
oknoen.grid(row=4,column=7)

eklebuton = Button(pencere,text="Ekle",command=kisiekleme)
eklebuton.place(relx=0.62,rely=0.22)

silbuton = Button(pencere,text="Sil",command=kisisil)
silbuton.place(relx=0.86,rely=0.10)

getirbuton = Button(pencere,text="Getir",command=kisigetir)
getirbuton.place(relx=0.86,rely=0.25)


pencere.mainloop()
