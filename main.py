import tkinter
import time

class D_Clock(tkinter.Tk):
    def __init__(self):
        super().__init__()
        #configuration
        self.title("Digital Clock")
        self.geometry('400x400')
        self.configure(bg='black')
        
        #lable for clock
        localtime = time.localtime()
        result = time.strftime('%I:%M:%S', localtime)
        self.D_C = tkinter.Label(self,text=f'{result}',fg='red', bg='black', font=('Helvetica', 75))
        #self.D_C.grid(row=5,column=5)
        self.D_C.pack(ipadx=20, ipady=60,)
        self.update_C()
    #update clock every second
    def string(self):
        localtime = time.localtime()
        result = time.strftime('%I:%M:%S', localtime)
        return result
    
    def update_C(self):
        self.D_C.configure(text=self.string())
        self.D_C.after(1000,self.update_C)
    

clock1 = D_Clock()
clock1.mainloop()

