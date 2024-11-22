from tkinter import*

def clear_fields(txtbx1, txtbx2, txtbx3, txtbx4):
    print('clear boxes')
    txtbx1.delete(0, "end")
    txtbx2.delete(0, "end")
    txtbx3.delete(0, "end")
    txtbx4.delete(0, "end")
   
# This is your calc button!

def btns(winmain,txtbx1,txtbx2, txtbx3, txtbx4):
    cmdcalc = Button(winmain,font=("Monotype Corsiva", 20),
                     text="CALC", command=lambda : cal(txtbx1,txtbx2, txtbx3, txtbx4))
    cmdcalc.place(x=300,y=500)
    
#This is your clear button!
def btns2(winmain,txtbx1,txtbx2, txtbx3, txtbx4):
    cmdclear = Button(winmain,font=("Monotype Corsiva", 20),
                      text="CLEAR", command=lambda : clear_fields(txtbx1,txtbx2, txtbx3,txtbx4))
    cmdclear.place(x=500,y=500)


def cal(txtbx1,txtbx2,txtbx3,txtbx4):
    work=txtbx1.get()
    try:
        work=float(work)
        if work<0:
            txtbx4.insert(0, 'Must be positive number')
        else:
            Celsius=work-273.15
            txtbx2.insert(0, Celsius)
            Fah=(9/5)*(work-273)+32
            txtbx3.insert(0,Fah)
    except:
        txtbx4.insert(0, 'invalid number')
    return

def quit_app():
        root.destroy()


def main():
    winmain=Tk()
    winmain.geometry('800x600+600+300')
    winmain.title('Jacquetta A. Nealon')
    winmain.configure(bg='blue')
    
    #These are my labels!
    lbltext = Label(winmain,text='Temperature Conversion', font=('Monotype Corsiva',30))
    lbltext.place(x=250,y=1)
    
    lbltext1 = Label(winmain,text='Kelvin:', font=('Monotype Corsiva',30))
    lbltext1.place(x=100,y=120)
    
    lbltext2 = Label(winmain,text='Celsius:', font=('Monotype Corsiva',30))
    lbltext2.place(x=100,y=220)
    
    lbltext3 = Label(winmain,text='Fahrenheit:', font=('Monotype Corsiva',30))
    lbltext3.place(x=100,y=300)
    
  #These are my textboxes!
    txtbx1= Entry(winmain,width=50)
    txtbx1.place(x=300,y=100)
    
    txtbx2= Entry(winmain,width=50)
    txtbx2.place(x=300,y=200)
    
    txtbx3= Entry(winmain,width=50)
    txtbx3.place(x=300,y=300)
    
    txtbx4= Entry(winmain,width=75)
    txtbx4.place(x=300,y=400)

    btns(winmain, txtbx1, txtbx2, txtbx3, txtbx4)
    btns2(winmain, txtbx1, txtbx2, txtbx3, txtbx4)

    winmain.mainloop()
main()



   


