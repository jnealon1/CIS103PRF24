from tkinter import *
def main():
    print('--> start <--')
    mainwin = Tk()
    color='pink'
    wcan = Canvas(mainwin,bg=color, width=600,height=800)
    wcan.pack()
    wcan.create_oval(391, 391, 165, 165, fill='white',outline="orange", width=5)
    
    wcan.create_oval(250, 250, 196, 196, fill='orange',outline="black", width=5)
    wcan.create_oval(325, 200, 370, 250, fill='orange',outline="black", width=5)
    
    wcan.create_line(281,281, 281, 300, width=10, fill="purple")
    
    wcan.create_line(200,350, 350, 350, width=10, fill="gray")
    wcan.create_line(350,350, 200, 400, width=10, fill="gray")
    wcan.create_line(200,400, 200, 350, width=10, fill="gray")

   
    
 
    mainwin.mainloop()
main()
