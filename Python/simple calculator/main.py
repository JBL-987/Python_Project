from tkinter import*
import tkinter.font as font
import math

def cetak(nilai):
    current = text_result.get()
    text_result.delete(0,END)
    text_result.insert(0, str(current)+str(nilai))

def tambah():
    nomor_awal = text_result.get()
    global n_awal
    global mtk
    mtk = "penjumlahan"
    n_awal = int(nomor_awal)
    text_result.insert(n_awal,"+")

def kurang():
    nomor_awal = text_result.get()
    global n_awal
    global mtk
    mtk = "pengurangan"
    n_awal = int(nomor_awal)
    text_result.insert(n_awal,"-")


def bagi():
    nomor_awal = text_result.get()
    global n_awal
    global mtk
    mtk = "pembagian"
    n_awal = int(nomor_awal)
    text_result.insert(n_awal,"/")


def kali():
    nomor_awal = text_result.get()
    global n_awal
    global mtk
    mtk = "perkalian"
    n_awal = int(nomor_awal)
    text_result.insert(n_awal,"*")


def sisabagi():
    nomor_awal = text_result.get()
    global n_awal
    n_awal = int(nomor_awal)
    text_result.delete(0,END)
    text_result.insert(0,n_awal /100)


def pangkat():
    nomor_awal = text_result.get()
    global n_awal
    n_awal = int(nomor_awal)
    text_result.delete(0,END)
    text_result.insert(0,n_awal **2)

def akar():
    nomor_awal = text_result.get()
    global n_awal
    n_awal = int(nomor_awal)
    text_result.delete(0,END)
    text_result.insert(0,math.sqrt(n_awal))

def hapus():
    text_result.delete(0,END)

def hapus_satu():
    nomor_akhir = text_result.get()  
    if nomor_akhir:
        n_awal = nomor_akhir[:-1] 
        text_result.delete(0, END)  
        text_result.insert(0, n_awal)  


def samadengan():
    nomor_akhir = text_result.get()
    text_result.delete(0,END)
    result = eval(nomor_akhir)
    text_result.insert(0, result)

    if mtk == "penjumlahan":
        text_result.insert(0,n_awal + int(nomor_akhir))
    elif mtk == "pengurangan":
        text_result.insert(0,n_awal - int(nomor_akhir))
    elif mtk == "pembagian":
        text_result.insert(0,n_awal / int(nomor_akhir))
    elif mtk == "perkalian":
        text_result.insert(0,n_awal * int(nomor_akhir))
    
root = Tk()
root.title("Simple")
root["bg"] = "#d1d1d1"
root.geometry("310x400")

myfont  = font.Font(size=15)

text_result = Entry(root,width=25,borderwidth=0)
text_result["font"]= myfont
text_result["bg"] = "#d1d1d1"
text_result.grid(row = 0,columnspan=4,pady=20,padx=20)

btn  = Button(root,text="1",padx = 30,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(1))
btn2  = Button(root,text="2",padx = 30,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(2))
btn3  = Button(root,text="3",padx = 30,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(3))
btn4  = Button(root,text="4",padx = 30,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(4))
btn5 = Button(root,text="5",padx = 30,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(5))
btn6  = Button(root,text="6",padx = 30,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(6))
btn7  = Button(root,text="7",padx = 30,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(7))
btn8  = Button(root,text="8",padx = 30,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(8))
btn9  = Button(root,text="9",padx = 30,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(9))
btn0  = Button(root,text="0",padx = 30,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(0))
tam = Button(root,text="+",padx = 30,bg="#878787",fg="white", pady = 20,command=tambah)
kur = Button(root,text="-",padx = 30,bg="#878787",fg="white", pady = 20,command=kurang)
bag  = Button(root,text="/",padx = 30,bg="#878787",fg="white", pady = 20,command=bagi)
kal = Button(root,text="x",padx = 30,bg="#878787",fg="white", pady = 20,command=kali)
pang = Button(root,text="x2",padx = 30,bg="#878787",fg="white", pady = 20,command=pangkat)
ak2 = Button(root,text="sq2",padx = 25,bg="#878787",fg="white", pady = 20,command=akar)
sisbag = Button(root,text="%",padx = 30,bg="#878787",fg="white", pady = 20,command=sisabagi)
hap = Button(root,text="AC",padx = 30,bg="#878787",fg="white", pady = 20,command=hapus)
delete1 = Button(root,text="C",padx = 30,bg="#878787",fg="white", pady = 20,command=hapus_satu)
equal = Button(root,text="=",padx = 60,bg="skyblue", pady = 20,command=samadengan)


btn.grid(row=1,column=0,pady=2)
btn2.grid(row=3,column=1,pady=2)
btn3.grid(row=3,column=2,pady=2)
btn4.grid(row=2,column=0,pady=2)
btn5.grid(row=2,column=1,pady=2)
btn6.grid(row=2,column=2,pady=2)
btn7.grid(row=3,column=0,pady=2)
btn8.grid(row=1,column=1,pady=2)
btn9.grid(row=1,column=2,pady=2)
btn0.grid(row=4,column=1,pady=2)

tam.grid(row=1,column=3,pady=2)
kur.grid(row=2,column=3,pady=2)
bag.grid(row=3,column=3,pady=2)
kal.grid(row=4,column=3,pady=2)
hap.grid(row=4,column=0,pady=2)
delete1.grid(row=5,column=0,pady=2)
equal.grid(row=5,column=3,columnspan=2)
pang.grid(row =5,column=2,pady=2)
ak2.grid(row =5,column=1,pady=2)
sisbag.grid(row =4,column=2,pady=2)



root.mainloop()
