from tkinter import *
from tkinter import messagebox
import csv

window = Tk()
window.geometry("700x700")
window.resizable(0, 0)
window.title("Create an account")


def create():
    username = unameEnt.get()
    phone = phoneEnt.get()
    cnic = cnicEnt.get()
    password = pwdEnt.get()

    csv_file = csv.reader(open("Add user.csv", 'r'))

    xNoError = True
    if username == "" and password == "" and phone == "" and cnic == "":
        messagebox.showerror("Alert", "Please Fill the Required Fields")
        xNoError = True

    elif len(phone) != 12:
        messagebox.showerror("Alert", "Incorrect Phone No is required")
        xNoError = False

    elif len(cnic) != 13:
        messagebox.showerror("Alert", "Incorrect CNIC No is required")
        xNoError = False

    if (xNoError):
        xUsernameStatus=True
        for row in csv_file:
            if username == row[0]:
                messagebox.showerror("Error","This Username is already taken")
                xUsernameStatus=False
                break
        if xUsernameStatus:
            data_list = [username, phone, cnic, password]
            with open('Add user.csv', 'a', newline='') as writefile:
                the_writer = csv.writer(writefile)
                the_writer.writerow(data_list)
            messagebox.showinfo("Information", "Your account has been created")
            window.destroy()
            import Login







def back():
    window.destroy()
    import Login


icon = PhotoImage(file="image1.png")
logo = Label(window, image=icon)
logo.pack()
# Heading
heading = Label(window, text="Create An Account", font=("century gothic", 30, "bold"))
heading.place(x=180, y=240)

icon2 = PhotoImage(file="image2.png")
logo2 = Label(window, image=icon2, width=200 )
logo2.place(x=80, y=380)

# labels
namelbl = Label(window, text="Uername:", fg="black", font=("Arial", 15, "bold",))
namelbl.place(x=295, y=400)
phonelbl = Label(window, text="Phone No:", fg="black", font=("Arial", 15, "bold",))
phonelbl.place(x=295, y=450)
cniclbl = Label(window, text="CNIC:", fg="black", font=("Arial", 15, "bold",))
cniclbl.place(x=295, y=500)
pwdlbl = Label(window, text="Password:", fg="black", font=("Arial", 15, "bold",))
pwdlbl.place(x=295, y=550)

# Buttons
unameEnt = Entry(window, width=20, font=('bold', 17))
unameEnt.place(x=400, y=402)
phoneEnt = Entry(window, width=20, font=('bold', 17))
phoneEnt.place(x=400, y=450)
phoneEnt.insert(0,"92")
cnicEnt = Entry(window, width=20, font=('bold', 17))
cnicEnt.place(x=400, y=500)
pwdEnt = Entry(window, width=20, font=('bold', 17))
pwdEnt.place(x=400, y=550)

b3 = Button(window, text="Sign Up", fg="white", bg="green", font=("Arial", 15, "bold"), width=15, command=create)
b3.place(x=425, y=600)
b3 = Button(window, text="Back", fg="white", bg="blue", font=("Arial", 13, "bold"), command=back)
b3.place(x=490, y=650)
window.mainloop()
