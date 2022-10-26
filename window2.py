from tkinter import Tk, StringVar, ttk
from tkinter import *
from tkinter import messagebox
import time
import random
#from tkcalendar import DateEntry

window2 = Tk()
window2.title("SRA Railways")
window2.geometry("1000x800")

photo = PhotoImage(file="image1.png")
pic = Label(window2, image=photo).pack()

T_Class = StringVar()
Adult = IntVar()
Child = IntVar()
Origin = StringVar()
Des = StringVar()
Train = StringVar()
Amount = StringVar()
D_timing = StringVar()
D_Date = StringVar()

# -----------------------------f1-Class-Quantity-----------------------#
f1 = Frame(window2, width=350, height=350, bd=8, relief='raise')
f1.place(x=140, y=180)

lblextra = Label(f1, font=('arial', 12, 'bold'), text='  ', bd=8, pady=5)
lblextra.grid(row=1, column=3, sticky=W)

lblClass = Label(f1, font=('century gothic', 18, 'bold'), text='CLASS', bd=8)
lblClass.grid(row=0, column=0, sticky=W)

chkEconomy = Radiobutton(f1, font=('arial', 12, 'bold'), text='Economy', variable=T_Class, value="Economy")
chkEconomy.grid(row=1, column=0, sticky=W)

chkBuisness = Radiobutton(f1, font=('arial', 12, 'bold'), text='Buisness', variable=T_Class, value="Business")
chkBuisness.grid(row=2, column=0, sticky=W)

chkACSleeper = Radiobutton(f1, font=('arial', 12, 'bold'), text='AC Sleeper', variable=T_Class, value="AC Sleeper")
chkACSleeper.grid(row=3, column=0, sticky=W)

lblQuantity = Label(f1, font=('century gothic', 18, 'bold'), text='QUANTITY', bd=8)
lblQuantity.grid(row=4, column=0, sticky=W)

lblAdult = Label(f1, font=('arial', 12, 'bold'), text='Adult', bd=8)
lblAdult.grid(row=5, column=0, sticky=W)
cboAdult = ttk.Combobox(f1, textvariable=Adult, state='readonly', font=('arial', 12, 'bold'), width=20)
cboAdult['value'] = ('1', '2', '3', '4', '5', '6')
cboAdult.current(0)
cboAdult.grid(row=5, column=1)

lblChild = Label(f1, font=('arial', 12, 'bold'), text='Child', bd=8)
lblChild.grid(row=6, column=0, sticky=W)
cboChild = ttk.Combobox(f1, textvariable=Child, state='readonly', font=('arial', 12, 'bold'), width=20)
cboChild['value'] = ('0', '1', '2', '3', '4', '5', '6')
cboChild.current(0)
cboChild.grid(row=6, column=1)

# -------------------------------f2-Destination-Train-----------------------#

f2 = Frame(window2, width=350, height=350, bd=8, relief='raise')
f2.place(x=515, y=180)

lblJourney = Label(f2, font=('century gothic', 18, 'bold'), text='JOURNEY', bd=8)
lblJourney.grid(row=0, column=0, sticky=W)

lblextra = Label(f2, font=('arial', 12, 'bold'), text='  ', bd=8, pady=5)
lblextra.grid(row=1, column=3, sticky=W)

lblFrom = Label(f2, font=('arial', 12, 'bold'), text='From:', bd=8, pady=5)
lblFrom.grid(row=1, column=0, sticky=W)
cboFrom = ttk.Combobox(f2, textvariable=Origin, state='readonly', font=('arial', 12, 'bold'), width=20)
cboFrom['value'] = ('','Karachi')
cboFrom.current(1)
cboFrom.grid(row=1, column=1)

lblTo = Label(f2, font=('arial', 12, 'bold'), text='To:', bd=8, pady=5)
lblTo.grid(row=2, column=0, sticky=W)
cboTo = ttk.Combobox(f2, textvariable=Des, state='readonly', font=('arial', 12, 'bold'), width=20)
cboTo['value'] = ('', 'Lahore', 'Islamabad', 'Quetta', 'Peshawar')
cboTo.current(0)
cboTo.grid(row=2, column=1)

lblTime = Label(f2, font=('arial', 12, 'bold'), text='Departure Date:', bd=8, pady=5)
lblTime.grid(row=3, column=0, sticky=W)

#calender = DateEntry(f2, font="Arial 10", cursor="hand2", textvariable=D_Date, date_pattern='dd / mm / y')
#calender.place(x=170, y=148)

lblSTrain = Label(f2, font=('century gothic', 18, 'bold'), text='SELECT TRAIN', bd=8, pady=5)
lblSTrain.grid(row=4, column=0, sticky=W)

lblTrain = Label(f2, font=('arial', 12, 'bold'), text='Train:', bd=8)
lblTrain.grid(row=5, column=0, sticky=W)
cboTrain = ttk.Combobox(f2, textvariable=Train, state='readonly', font=('arial', 12, 'bold'), width=20)
cboTrain['value'] = ('', 'Karakoram', 'Shalimar', 'Karachi Express', 'Bahauddin Zikkriya')
cboTrain.current(0)
cboTrain.grid(row=5, column=1)
# -------------------------------f3-Selecting Estimate Fare-----------------------#
f3 = Frame(window2, width=700, height=100, bd=8, relief='raise')
f3.place(x=160, y=490)
lblClass = Label(f3, font=("arial", 15, 'bold'), text="Class", width=10, bd=12)
lblClass.grid(row=0, column=0, sticky=W)
lblClass1 = Label(f3, font=("arial", 15, 'bold'), textvariable=T_Class, width=10, bd=12, relief="sunken")
lblClass1.grid(row=1, column=0, sticky=W)

lblAdult = Label(f3, font=("arial", 15, 'bold'), text="Adult", width=10, bd=12)
lblAdult.grid(row=0, column=1, sticky=W)
lblAdult1 = Label(f3, font=("arial", 15, 'bold'), textvariable=Adult, width=10, bd=12, relief="sunken")
lblAdult1.grid(row=1, column=1, sticky=W)

lblChild = Label(f3, font=("arial", 15, 'bold'), text="Child", width=10, bd=12)
lblChild.grid(row=0, column=2, sticky=W)
lblChild1 = Label(f3, font=("arial", 15, 'bold'), textvariable=Child, width=10, bd=12, relief="sunken")
lblChild1.grid(row=1, column=2, sticky=W)

lblTo = Label(f3, font=("arial", 15, 'bold'), text="Destination", width=10, bd=12)
lblTo.grid(row=0, column=4, sticky=W)
lblTo1 = Label(f3, font=("arial", 15, 'bold'), textvariable=Des, width=10, bd=12, relief="sunken")
lblTo1.grid(row=1, column=4, sticky=W)

lblTo = Label(f3, font=("arial", 15, 'bold'), text="Origin", width=10, bd=12)
lblTo.grid(row=0, column=3, sticky=W)
lblTo1 = Label(f3, font=("arial", 15, 'bold'), textvariable=Origin, width=10, bd=12, relief="sunken")
lblTo1.grid(row=1, column=3, sticky=W)

lblTrain_Name = Label(f3, font=("arial", 15, 'bold'), text="Train", width=10, bd=12)
lblTrain_Name.grid(row=3, column=0, sticky=W)
lblTrain_Name1 = Label(f3, font=("arial", 15, 'bold'), textvariable=Train, width=22, bd=12, relief="sunken")
lblTrain_Name1.grid(row=3, column=1, columnspan=2, sticky=W)

lbl_timing = Label(f3, font=("arial", 15, 'bold'), text="Timing", width=10, bd=12)
lbl_timing.grid(row=2, column=3, sticky=W)
lbl_timing1 = Label(f3, font=("arial", 15, 'bold'), textvariable=D_timing, width=10, bd=12, relief="sunken")
lbl_timing1.grid(row=2, column=4, sticky=W)

lbl_d_date = Label(f3, font=("arial", 15, 'bold'), text="Date", width=10, bd=12)
lbl_d_date.grid(row=2, column=0, sticky=W)
lbl_d_date1 = Label(f3, font=("arial", 15, 'bold'), textvariable=D_Date, width=22, bd=12, relief="sunken")
lbl_d_date1.grid(row=2, column=1, columnspan=2, sticky=W)


def total():
    if T_Class.get() == "Business" and Des.get() == "Quetta" or Train.get() == "Karachi Express":
        adultFare = float(2500)
        childFare = float(1200)
        Cquantity = float(Child.get())
        Aquantity = float(Adult.get())
        tot = ((adultFare * Aquantity) + (childFare * Cquantity))
        Amount.set("RS {0:.2f}".format(tot))
        D_timing.set("18 30")
        if Train.get() != "Karachi Express":
            messagebox.showerror("Alert", "Only Karachi Express goes to Quetta")
            reset()
    elif T_Class.get() == "Business" and Des.get() == "Lahore" :
        adultFare = float(2100)
        childFare = float(1000)
        Cquantity = float(Child.get())
        Aquantity = float(Adult.get())
        tot = ((adultFare * Aquantity) + (childFare * Cquantity))
        Amount.set("RS {0:.2f}".format(tot))
        D_timing.set("15 30")
        if Train.get() != "Karakoram" and Train.get() != "Shalimar":
            messagebox.showerror("Alert", "Please select b/w Karakoram and Shalimar")
            reset()
    elif T_Class.get() == "Business" and Des.get() == "Peshawar":
        adultFare = float(3000)
        childFare = float(1500)
        Cquantity = float(Child.get())
        Aquantity = float(Adult.get())
        tot = ((adultFare * Aquantity) + (childFare * Cquantity))
        Amount.set("RS {0:.2f}".format(tot))
        D_timing.set("09 30")
        if Train.get() != "Bahauddin Zikkriya":
            messagebox.showerror("Alert", "Only Bahauddin Zikkriya goes to Peshawar")
            reset()
    elif T_Class.get() == "Business" and Des.get() == "Islamabad" or Train.get() == "Karakoram" or Train.get() == "Shalimar":
        adultFare = float(2200)
        childFare = float(1100)
        Cquantity = float(Child.get())
        Aquantity = float(Adult.get())
        tot = ((adultFare * Aquantity) + (childFare * Cquantity))
        Amount.set("RS {0:.2f}".format(tot))
        D_timing.set("15 30")
        if Train.get() != "Karakoram" and Train.get() != "Shalimar":
            messagebox.showerror("Alert", "Please select b/w Karakoram and Shalimar")
            reset()
    elif T_Class.get() == "Economy" and Des.get() == "Quetta" or Train.get() == "Karachi Express":
        adultFare = float(2500)
        childFare = float(1200)
        Cquantity = float(Child.get())
        Aquantity = float(Adult.get())
        tot = ((adultFare * Aquantity) + (childFare * Cquantity))
        Amount.set("RS {0:.2f}".format(tot))
        D_timing.set("18 30")
        if Train.get() != "Karachi Express":
            messagebox.showerror("Alert", "Only Karachi Express goes to Quetta")
            reset()
    elif T_Class.get() == "Economy" and Des.get() == "Lahore" or Train.get() == "Karakoram" or Train.get() == "Shalimar":
        adultFare = float(2100)
        childFare = float(1000)
        Cquantity = float(Child.get())
        Aquantity = float(Adult.get())
        tot = ((adultFare * Aquantity) + (childFare * Cquantity))
        Amount.set("RS {0:.2f}".format(tot))
        D_timing.set("15 30")
        if Train.get() != "Karakoram" and Train.get() != "Shalimar":
            messagebox.showerror("Alert", "Please select b/w Karakoram and Shalimar")
            reset()
    elif T_Class.get() == "Economy" and Des.get() == "Peshawar" or Train.get() == "Bahauddin Zikkriya":
        adultFare = float(3000)
        childFare = float(1500)
        Cquantity = float(Child.get())
        Aquantity = float(Adult.get())
        tot = ((adultFare * Aquantity) + (childFare * Cquantity))
        Amount.set("RS {0:.2f}".format(tot))
        D_timing.set("09 30")
        if Train.get() != "Bahauddin Zikkriya":
            messagebox.showerror("Alert", "Only Bahauddin Zikkriya goes to Peshawar")
            reset()
    elif T_Class.get() == "Economy" and Des.get() == "Islamabad" or Train.get() == "Karakoram" or Train.get() == "Shalimar":
        adultFare = float(2200)
        childFare = float(1100)
        Cquantity = float(Child.get())
        Aquantity = float(Adult.get())
        tot = ((adultFare * Aquantity) + (childFare * Cquantity))
        Amount.set("RS {0:.2f}".format(tot))
        if Train.get() != "Karakoram" and Train.get() != "Shalimar":
            messagebox.showerror("Alert", "Please select b/w Karakoram and Shalimar")
            reset()
    elif T_Class.get() == "AC Sleeper" and Des.get() == "Quetta" or Train.get() == "Karachi Express":
        adultFare = float(2500)
        childFare = float(1200)
        Cquantity = float(Child.get())
        Aquantity = float(Adult.get())
        tot = ((adultFare * Aquantity) + (childFare * Cquantity))
        Amount.set("RS {0:.2f}".format(tot))
        D_timing.set("18 30")
        if Train.get() != "Karachi Express":
            messagebox.showerror("Alert", "Only Karachi Express goes to Quetta")
            reset()
    elif T_Class.get() == "AC Sleeper" and Des.get() == "Lahore" or Train.get() == "Karakoram" or Train.get() == "Shalimar":
        adultFare = float(2100)
        childFare = float(1000)
        Cquantity = float(Child.get())
        Aquantity = float(Adult.get())
        tot = ((adultFare * Aquantity) + (childFare * Cquantity))
        Amount.set("RS {0:.2f}".format(tot))
        D_timing.set("15 30")
        D_timing.set("15 30")
        if Train.get() != "Karakoram" and Train.get() != "Shalimar":
            messagebox.showerror("Alert", "Please select b/w Karakoram and Shalimar")
            reset()
    elif T_Class.get() == "AC Sleeper" and Des.get() == "Peshawar" or Train.get() == "Bahauddin Zikkriya":
        adultFare = float(3000)
        childFare = float(1500)
        Cquantity = float(Child.get())
        Aquantity = float(Adult.get())
        tot = ((adultFare * Aquantity) + (childFare * Cquantity))
        Amount.set("RS {0:.2f}".format(tot))
        D_timing.set("09 30")
        if Train.get() != "Bahauddin Zikkriya":
            messagebox.showerror("Alert", "Only Bahauddin Zikkriya goes to Peshawar")
            reset()
    elif T_Class.get() == "AC Sleeper " and Des.get() == "Islamabad":
        adultFare = float(2200)
        childFare = float(1100)
        Cquantity = float(Child.get())
        Aquantity = float(Adult.get())
        tot = (adultFare * Aquantity) + (childFare * Cquantity)
        Amount.set("RS {0:.2f}".format(tot))
        D_timing.set("15 30")
        if Train.get() != "Karakoram" and Train.get() != "Shalimar":
            messagebox.showerror("Alert", "Please select b/w Karakoram and Shalimar")
            reset()


# ------------------------------------------------------------------------------#


lblAmount = Label(f3, font=("arial", 15, 'bold'), text="Total Amount", width=10, bd=12)
lblAmount.grid(row=3, column=3, sticky=W)
lblAmount1 = Label(f3, font=("arial", 15, 'bold'), textvariable=Amount, width=10, bd=12, relief="sunken")
lblAmount1.grid(row=3, column=4, columnspan=5, sticky=W)


# -------------------------------------------------------------------------------

def reset():
    T_Class.set("")
    Adult.set("1")
    Child.set("")
    Origin.set("Karachi")
    Des.set("")
    Train.set("")
    Amount.set("")
    D_timing.set("")
    return


def back(x):
    pass


def window3():
    window2.destroy()
    window3 = Tk()
    window3.geometry("700x700")
    window3.title("SRA Railways")
    window3.resizable(0,0)

    ticket_label = Label(window3, text="TICKET", fg="black", font=("Times New Roman", 30, "underline bold"))
    ticket_label.pack(padx=20, ipady=10)

    icon = PhotoImage(file="image1.png")
    logo = Label(window3, image=icon)
    logo.pack()

    mainframe = Frame(window3, width=900, height=700, bd=5, relief='groove')
    mainframe.pack()

    lblHead = Label(mainframe, font=("arial", 12, "bold"), text=("SRA Railways"), width=37, fg= "white" , bg= "green")
    lblHead.grid(row = 0, column=0,columnspan = 3, sticky=W)

    lblTime = Label(mainframe, font=("arial", 12, "bold"), text=("Time"), width=10, bd=8, relief='groove')
    lblTime.grid(row=1, column=0, sticky=W)
    lblTime1 = Label(mainframe, font=("arial", 12), text=time.strftime('%H:%M:%S %p'), width=10, bd=8)
    lblTime1.grid(row=2, column=0, sticky=W)

    lblDate = Label(mainframe, font=("arial", 12, "bold"), text=("Date"), width=10, bd=8, relief='groove')
    lblDate.grid(row=1, column=1, sticky=W)
    lblDate1 = Label(mainframe, font=("arial", 12), text=time.strftime("%d/%m/%Y"), width=10, bd=8)
    lblDate1.grid(row=2, column=1, sticky=W)

    Ticket_No = StringVar()
    x = random.randint(109, 5324)
    randomRef = str(x)
    Ticket_No.set("SRA" + randomRef)

    Cabin_No=StringVar()
    y=random.randint(1,12)
    randomCabin=str(y)
    Cabin_No.set(randomCabin)

    ticket_num = Label(mainframe, font=("arial", 12, "bold"), text="Ticket No.", width=10, bd=8, relief='groove')
    ticket_num.grid(row=1, column=2, sticky=W)
    ticket_num1 = Label(mainframe, font=("arial", 12), textvariable=Ticket_No, width=10, bd=8)
    ticket_num1.grid(row=2, column=2, sticky=W)

    lblClass = Label(mainframe, font=("arial", 15, 'bold'), text="Class", width=10, bd=2, relief='groove')
    lblClass.grid(row=5, column=0, sticky=W)
    lblClass1 = Label(mainframe, font=("arial", 15), width=10, bd=1)
    lblClass1.grid(row=6, column=0, sticky=W)
    lblClass1.configure(text = T_Class.get())

    lblAdult = Label(mainframe, font=("arial", 15, 'bold'), text="Adult", width=10, bd=2, relief='groove')
    lblAdult.grid(row=5, column=1, sticky=W)
    lblAdult1 = Label(mainframe, font=("arial", 15), width=10, bd=1)
    lblAdult1.grid(row=6, column=1, sticky=W)
    lblAdult1.configure(text=Adult.get())

    lblChild = Label(mainframe, font=("arial", 15, 'bold'), text="Child", width=10, bd=2, relief='groove')
    lblChild.grid(row=5, column=2, sticky=W)
    lblChild1 = Label(mainframe, font=("arial", 15), width=10, bd=1)
    lblChild1.grid(row=6, column=2, sticky=W)
    lblChild1.configure(text=Child.get())

    lblTrain = Label(mainframe, font=("arial", 15, 'bold'), text="Train", width=10, bd=2, relief='groove')
    lblTrain.grid(row=7, column=0, sticky=W)
    lblTrain1 = Label(mainframe, font=("arial", 15), width=20, bd=2, relief='groove')
    lblTrain1.grid(row=7, column=1,columnspan=2, sticky=W)
    lblTrain1.configure(text=Train.get())

    lblCabin = Label(mainframe, font=("arial", 15, 'bold'), text="Cabin #", width=10, bd=2, relief='groove')
    lblCabin.grid(row=8, column=0, sticky=W)
    lblCabin1 = Label(mainframe, font=("arial", 15), width=20, bd=2, relief='groove',textvariable=Cabin_No)
    lblCabin1.grid(row=8, column=1,columnspan=2, sticky=W)

    lblFrom = Label(mainframe, font=("arial", 15, 'bold'), text="From", width=10, bd=2, relief='groove')
    lblFrom.grid(row=9, column=0, sticky=W)
    lblFrom1 = Label(mainframe, font=("arial", 15), width=20, bd=2, relief='groove')
    lblFrom1.grid(row=9, column=1, columnspan=2, sticky=W)
    lblFrom1.configure(text = Origin.get())

    lblTo = Label(mainframe, font=("arial", 15, 'bold'), text="To", width=10, bd=2, relief='groove')
    lblTo.grid(row=10, column=0, sticky=W)
    lblTo1 = Label(mainframe, font=("arial", 15), width=20, bd=2,relief='groove')
    lblTo1.grid(row=10, column=1, columnspan=2, sticky=W)
    lblTo1.configure(text=Des.get())


    lblD_Time = Label(mainframe, font=("arial", 15, 'bold'), text="Departure Time", width=20, bd=2, relief='groove')
    lblD_Time.grid(row=11, column=0, columnspan=2, sticky=W)
    lblD_Time1 = Label(mainframe, font=("arial", 15,'bold'), width=10, bd=2, relief='groove')
    lblD_Time1.grid(row=11, column=2, sticky=W, )
    lblD_Time1.configure(text=D_timing.get())

    lblD_Date = Label(mainframe, font=("arial", 15, 'bold'), text="Departure Date", width=20, bd=2, relief='groove')
    lblD_Date.grid(row=12, column=0, columnspan=2, sticky=W)
    lblD_Date1 = Label(mainframe, font=("arial", 15,'bold'), width=10, bd=2, relief='groove')
    lblD_Date1.grid(row=12, column=2, sticky=W)
    lblD_Date1.configure(text=D_Date.get())



    lblAmount = Label(mainframe, font=("arial", 15, 'bold'), text="Total Amount", width=20, bd=2,relief='groove')
    lblAmount.grid(row=14, column=0,columnspan=2, sticky=W)
    lblAmount1 = Label(mainframe, font=("arial", 15, 'bold'), width=10, bd=2, relief="sunken")
    lblAmount1.grid(row=14,column=2, sticky=W)
    lblAmount1.configure(text=Amount.get())

    separator = Frame(height=2)
    separator.pack(fill=X, padx=5, pady=20)

    def print_ticket():
        return

    def back():
        window3.destroy()
        import window2
        return

    printBtn = Button(window3, text="Print Ticket", font=('bold', 15), width=10, fg="white", bg="green")
    printBtn.place(x=350,y=615)
    backBtn = Button(window3, text="Back", font=('bold', 10), width=10, fg="white", bg="Blue",command=back)
    backBtn.place(x=250, y=620)


    window3.mainloop()


totBtn = Button(window2, text="Check Total", font=('bold', 15), fg='white', bg='blue', cursor="hand2",
                command=total, width=20)
totBtn.place(x=420, y=730)

resBtn = Button(window2, text="Reset", font=('bold', 15), fg='white', bg='blue', cursor="hand2",
                command=reset, width=20)
resBtn.place(x=170, y=730)





ticketBtn = Button(window2, text="Generate Ticket", font=('bold', 15), fg='white', bg='green', cursor="hand2", width=20,command=window3)
ticketBtn.place(x=670, y=730)
window2.mainloop()
