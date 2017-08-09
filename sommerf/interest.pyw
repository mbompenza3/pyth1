import tkinter




class MainWindow(tkinter.Frame):
    def __init__(self,parent):
        super(MainWindow,self).__init__(parent)
        self.parent=parent
        self.grid(row=0,column=0)

        self.princip=tkinter.DoubleVar()
        self.princip.set(1000)
        self.rate=tkinter.DoubleVar()
        self.rate.set(5)
        self.years=tkinter.IntVar()
        self.amount=tkinter.StringVar()

        princLabel=tkinter.Label(self,text='Principal $:',anchor=tkinter.W,underline=0)
        rateLabel=tkinter.Label(self,text='Rate $:',anchor=tkinter.W,underline=0)
        yrsLabel=tkinter.Label(self,text='Years $:',anchor=tkinter.W,underline=0)
        amntLabel=tkinter.Label(self,text='Amount $:',anchor=tkinter.W)

        princScale=tkinter.Scale(self,variable=self.princip,command=self.updateUi,from_=10,to_=100000,
                                 resolution=100,orient=tkinter.HORIZONTAL)
        rateScale = tkinter.Scale(self, variable=self.rate, command=self.updateUi, from_=1, to_=100,
                                   resolution=0.25, orient=tkinter.HORIZONTAL)
        yrsScale = tkinter.Scale(self, variable=self.years, command=self.updateUi, from_=1, to_=50,
                                   orient=tkinter.HORIZONTAL)
        actAmntLabel=tkinter.Label(self,textvariable=self.amount,anchor=tkinter.E,relief=tkinter.SUNKEN)

        princLabel.grid(row=0,column=0,padx=2,pady=2,sticky=tkinter.W)
        princScale.grid(row=0,column=1,padx=2,pady=2,sticky=tkinter.EW)
        rateLabel.grid(row=1,column=0,padx=2,pady=2,sticky=tkinter.W)
        rateScale.grid(row=1,column=1,padx=2,pady=2,sticky=tkinter.EW)
        yrsLabel.grid(row=2,column=0,padx=2,pady=2,sticky=tkinter.W)
        yrsScale.grid(row=2,column=1,padx=2,pady=2,sticky=tkinter.EW)
        amntLabel.grid(row=3,column=0,padx=2,pady=2,sticky=tkinter.W)
        actAmntLabel.grid(row=3,column=1,padx=2,pady=2,sticky=tkinter.EW)
        princScale.focus_set()
        self.updateUi()
        parent.bind('<Alt-p>',lambda  *ignore:princScale.focus_set())
        parent.bind('<Control-q>',self.quit)



    def updateUi(self,*ignore):
        amount=self.princip.get()*((1+(self.rate.get()/100))**self.years.get())
        self.amount.set('{0:.2f}'.format(amount))

    def quit(self,event=None):
        self.parent.destroy()

appl=tkinter.Tk()
appl.title=('Interest')
wind=MainWindow(appl)
appl.protocol('WM_DELETE_WINDOW',wind.quit)
appl.mainloop()
