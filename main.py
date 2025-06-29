from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import openpyxl 
# from mySQLi_helper import MySQLI_helper 
from sqlite_helper import SQLite_helper 

root = Tk()
root.geometry('800x600')
root.title('ATM')
root.configure(bg='#232946') 

color_root = '#232946'
color_child = '#b8c1ec'
color_child2 = '#eebbc3'

# db_helper = MySQLI_helper(host='localhost', port=3306, user='root', password='password', database='BANK_MANAGEMENT')
db_helper = SQLite_helper('bank_management.db')

def clearEntryFields(*fields):
    for field in fields:
        field.delete(0,END)
    

def forgetPlace(*widgets):
    pass
    for widget in widgets:
        widget.place_forget()

def forgetPack(*widgets):
    pass
    for widget in widgets:
        widget.pack_forget()


def createAcc():
    new_userName= StringVar()
    new_password = StringVar()
    confirm_password = StringVar()
    newAcFrame = Frame(root,background=color_child)
    newAcFrame.place(width=500,height=420,x=145,y=110)
    createAcHeading = Label(newAcFrame, text='New Account Registration',font='Helvetica 20 underline',fg=color_root,bg=color_child).pack(side='top',pady=5)
    
    new_uName_Lbl = Label(newAcFrame, text='User Name:',font='Helvetica 14 underline',justify='left',bg=color_child, fg=color_root)
    new_uName_Lbl.place(relx='0.017',rely='0.23')
    new_uName_in = Entry(newAcFrame, textvariable=new_userName, font='Helvetica 14')
    new_uName_in.place(relx='0.5',rely='0.23')
    new_uName_in.focus_set()

    new_Pass_Lbl = Label(newAcFrame, text="Passwword:",font='Helvetica 14 underline',justify='left',bg=color_child, fg=color_root)
    new_Pass_Lbl.place(relx='0.017',rely='0.33')
    new_password_in = Entry(newAcFrame, textvariable=new_password, font='Helvetica 14',show='*')
    new_password_in.place(relx='0.5',rely='0.33')
    
    confirm_Pass_Lbl = Label(newAcFrame, text="Confirm Passwword:",font='Helvetica 14 underline',justify='left',bg=color_child, fg=color_root)
    confirm_Pass_Lbl.place(relx='0.017',rely='0.43')
    confirm_pass_in = Entry(newAcFrame, textvariable=confirm_password, font='Helvetica 14',show='*')
    confirm_pass_in.place(relx='0.5',rely='0.43')

    def newAccCreate_sbmt():
        if not new_uName_in.get() == '' and not new_password_in.get() == '' and not confirm_pass_in.get() == '':
            if new_password_in.get() != confirm_pass_in.get():
                messagebox.showerror("ERROR !" ,"Password and Confirm Password is not same!")
                return
            else:
                # save2Xlsx(new_UID,new_pass)
                db_helper.register_user(new_userName.get(), new_password.get())
                clearEntryFields(new_uName_in,new_password_in,confirm_pass_in)
                messagebox.showinfo("Sucess","Your account has been registered sucessfully !")
                closeBtnAct_1()
        else:
            messagebox.showerror("ERROR !" ,"There is some problem, please try again later !")
            
    createAccBtn = Button(newAcFrame, text='Submit', font='Arial 14',command=newAccCreate_sbmt)
    createAccBtn.place(relx=0.35,rely=0.7,relwidth=0.3)

    def closeBtnAct_1():
        newAcFrame.place_forget()
        newAccBtn.pack(fill=X,padx=300,pady=20)
        loginBtn.pack(fill=X,padx=300,pady=20)

    closeBtn_1 = Button(newAcFrame,text='X',fg='red',font='Helvetica 12',bg='grey',command=closeBtnAct_1)
    closeBtn_1.place(relx=0.93,rely=0.02)

    # newAccBtn.pack_forget()
    # loginBtn.pack_forget()
    forgetPack(newAccBtn,loginBtn)

def loginAcc():
    uid = StringVar()
    pasw = StringVar()
    loginFrame = Frame(root,background=color_child)
    loginFrame.place(width=500,height=380,x=150,y=110)
    loginHeading = Label(loginFrame, text='Login with your User Name',font='Helvetica 20 underline',fg=color_root,bg=color_child)
    loginHeading.pack(side='top',pady=5)
    
    uid_Lbl = Label(loginFrame, text='Enter User Name:',font='Helvetica 14 underline',justify='left',bg=color_child, fg=color_root)
    uid_Lbl.place(relx='0.017',rely='0.23')
    uid_in = Entry(loginFrame, textvariable=uid, font='Helvetica 14',)
    uid_in.place(relx='0.5',rely='0.23')
    uid_in.focus_set()
    pass_Lbl = Label(loginFrame, text="Enter Passwword:",font='Helvetica 14 underline',justify='left',bg=color_child, fg=color_root)
    pass_Lbl.place(relx='0.017',rely='0.33')
    pass_in = Entry(loginFrame, textvariable=pasw, font='Helvetica 14',show='*')
    pass_in.place(relx='0.5',rely='0.33')

    def login_validate():
        if not uid_in.get() == '' and not pass_in.get() == '' :
            # uid len 15, pas len 10 
            # useAcc('abc')
            user_data = db_helper.login_user(uid_in.get(),pass_in.get())
            if user_data:
                useAcc(uid_in.get(), pass_in.get())
                forgetPack(newAccBtn,loginBtn)
                loginFrame.place_forget()
            else:
                pass 
                messagebox.showerror("ERROR !" ,"User not found !\nRegister and try again")
                closeBtnAct_1()
        else:
            messagebox.showerror("ERROR !" ,"User Id and Password field must not be empty !")

    _login = Button(loginFrame, text='Login', font='Arial 14',command=login_validate)
    _login.place(relx=0.35,rely=0.7,relwidth=0.3)

    def closeBtnAct_1():
        loginFrame.place_forget()
        newAccBtn.pack(fill=X,padx=300,pady=20)
        loginBtn.pack(fill=X,padx=300,pady=20)

    closeBtn = Button(loginFrame,text='X',fg='red',font='Helvetica 12',bg='grey',command=closeBtnAct_1)
    closeBtn.place(relx=0.93,rely=0.02)

def changePasw(user):
    chPassFrame = Frame(root,relief='raised', borderwidth=1,bg=color_child2)
    chPassFrame.place(width=350,height=220,x=235,y=210)
    Label(chPassFrame,text='Change Password', font='Arial 14 underline', fg=color_root,bg=color_child2).pack(pady=15)
    pas_label = Label(chPassFrame, text='Enter New Password:',font='Arial 12',fg=color_root,bg=color_child2).place(rely=0.3,relx=0.005)
    newPas = StringVar()
    newPasIn = Entry(chPassFrame,font='Arial 14',bg='skyblue',textvariable=newPas)
    newPasIn.place(rely=0.3,relx=0.45,width=180)
    newPasIn.focus_set()

    confirm_pas_label = Label(chPassFrame, text='Confirm Password:',font='Arial 12',bg=color_child2,fg=color_root).place(rely=0.5,relx=0.005)
    c_newPas = StringVar()
    c_newPasIn = Entry(chPassFrame,font='Arial 14',bg='skyblue',textvariable=c_newPas).place(rely=0.5,relx=0.45,width=180)

    def validate_updatePas():
        if not newPas.get() == '' and not c_newPas.get() == '':
            if newPas.get() == c_newPas.get():
                # updatePass(user,newPas.get())
                db_helper.update_password(user, newPas.get())
                messagebox.showinfo("Sucess","Your password has been changed sucessfully !")
                chPassFrame.place_forget()
            else:
                messagebox.showerror("ERROR !" ,"New Password and Confirm Password is not same!")
        else:
            messagebox.showerror("ERROR !" ,"New Password field and Confirm Password field must not be empty !")

    chngPasBtn = Button(chPassFrame,text='OK',command=validate_updatePas).place(relx=0.4,rely=0.7,width=100)

    def closeBtnAct():
        chPassFrame.place_forget()

    closeBtn = Button(chPassFrame,text='X',fg='red',font='Helvetica 12',bg='grey',command=closeBtnAct)
    closeBtn.place(relx=0.93,rely=0.02)

def depositAcc(user, password):
    depositFrame = Frame(root,relief='raised', borderwidth=1,bg=color_child2)
    depositFrame.place(width=350,height=220,x=235,y=210)
    Label(depositFrame,text='Deposit Balance', font='Arial 14 underline', fg=color_root,bg=color_child2).pack(pady=15)
    d_amount = Label(depositFrame, text='Enter Amount:',font='Arial 12',bg=color_child2,fg=color_root).place(rely=0.45,relx=0.005)
    dAmount = IntVar()
    d_amountIn = Entry(depositFrame,font='Arial 14',bg='skyblue',textvariable=dAmount)
    d_amountIn.place(rely=0.45,relx=0.45,width=180)
    d_amountIn.focus_set()

    okBtn = Button(depositFrame,text='OK',command=db_helper.deposit).place(relx=0.4,rely=0.7,width=100)

    def validate_deposit():
        if dAmount.get() <= 0:
            messagebox.showerror("ERROR !", "Amount must be greater than zero!")
            return
        balance = db_helper.get_balance(user, password)
        if balance is not None:
            db_helper.deposit(user,password, balance + dAmount.get())
            messagebox.showinfo("Sucess", f"Your account has been credited with amount of ₹{dAmount.get()} successfully!\nYour new balance is ₹{balance + dAmount.get()}.")
            depositFrame.place_forget()
        else:
            messagebox.showerror("ERROR !", "Error fetching balance!")

    def closeBtnAct():
        depositFrame.place_forget()

    closeBtn = Button(depositFrame,text='X',fg='red',font='Helvetica 12',bg='grey',command=closeBtnAct)
    closeBtn.place(relx=0.93,rely=0.02)
    
def changeUserName(user, password):
    chUserIdFrame = Frame(root,relief='raised', borderwidth=1,bg=color_child2)
    chUserIdFrame.place(width=350,height=220,x=235,y=210)
    Label(chUserIdFrame,text='Change User Id', font='Arial 14 underline', fg=color_root,bg=color_child2).pack(pady=15)
    new_uNamelabel = Label(chUserIdFrame, text='New User Id:',font='Arial 12',bg=color_child2,fg=color_root).place(rely=0.45,relx=0.005)
    new_Uname = StringVar()
    new_uName_in = Entry(chUserIdFrame,font='Arial 14',bg='skyblue',textvariable=new_Uname)
    new_uName_in.place(rely=0.45,relx=0.45,width=180)
    new_uName_in.focus_set()

    def change_uName():
        db_helper.update_username(user, password, new_Uname.get())
        messagebox.showinfo("Sucess","Your User Id has been changed sucessfully !")
        chUserIdFrame.place_forget()
        useAccFrame.place_forget()
        useAcc(new_Uname, password)

    okBtn = Button(chUserIdFrame,text='OK',command=change_uName).place(relx=0.4,rely=0.7,width=100)

    def closeBtnAct():
        chUserIdFrame.place_forget()

    closeBtn = Button(chUserIdFrame,text='X',fg='red',font='Helvetica 12',bg='grey',command=closeBtnAct)
    closeBtn.place(relx=0.93,rely=0.02)

def withdrawAcc(user, password):
    withdrawFrame = Frame(root,relief='raised', borderwidth=1,bg=color_child2)
    withdrawFrame.place(width=350,height=220,x=235,y=210)
    Label(withdrawFrame,text='Withdraw Balance', font='Arial 14 underline', fg=color_root,bg=color_child2).pack(pady=15)
    w_amount = Label(withdrawFrame, text='Enter Amount:',font='Arial 12',bg='skyblue').place(rely=0.45,relx=0.005)
    wAmount = IntVar()
    w_amountIn = Entry(withdrawFrame,font='Arial 14',bg='skyblue',textvariable=wAmount)
    w_amountIn.place(rely=0.45,relx=0.45,width=180)
    w_amountIn.focus_set()

    def validate_withdraw():
        if wAmount.get() <= 0:
            messagebox.showerror("ERROR !", "Amount must be greater than zero!")
            return
        balance = db_helper.get_balance(user, password)
        if balance is not None and wAmount.get() <= balance:
            db_helper.withdraw(user, password, balance - wAmount.get())
            messagebox.showinfo("Sucess", f"Your account has been debited with amount of ₹{wAmount.get()} successfully!\nYour new balance is ₹{balance - wAmount.get()}.")
            withdrawFrame.place_forget()
        else:
            messagebox.showerror("ERROR !", "Insufficient balance or error fetching balance!")

    okBtn = Button(withdrawFrame,text='OK',command=validate_withdraw).place(relx=0.4,rely=0.7,width=100)

    def closeBtnAct():
        withdrawFrame.place_forget()

    closeBtn = Button(withdrawFrame,text='X',fg='red',font='Helvetica 12',bg='grey',command=closeBtnAct)
    closeBtn.place(relx=0.93,rely=0.02)

def checkBalance(user, password):
    balanceFrame = Frame(root,relief='raised', borderwidth=1,bg=color_child2)
    balanceFrame.place(width=350,height=220,x=235,y=210)
    Label(balanceFrame,text='Check Balance', font='Arial 14 underline', fg=color_root,bg=color_child2).pack(pady=15)
    
    balance = db_helper.get_balance(user, password)
    if balance is not None:
        balanceLabel = Label(balanceFrame, text=f'Your current balance is: ₹{balance}', font='Arial 12', bg=color_child2, fg=color_root)
        balanceLabel.place(rely=0.4, relx=0.1)
    else:
        balanceLabel = Label(balanceFrame, text='Error fetching balance!', font='Arial 12', bg=color_child2,fg='red')
        balanceLabel.place(rely=0.4, relx=0.1)

    okBtn = Button(balanceFrame,text='OK',command=lambda: [balanceFrame.place_forget()]).place(relx=0.4,rely=0.7,width=100)

    def closeBtnAct():
        balanceFrame.place_forget()

    closeBtn = Button(balanceFrame,text='X',fg='red',font='Helvetica 12',bg='grey',command=closeBtnAct)
    closeBtn.place(relx=0.93,rely=0.02)

def useAcc(usrName, password):
    user = usrName
    useAccFrame.place(x=0,rely=0.1,relwidth=1.0,relheight=0.9)
    useAccFrame.configure(bg=color_child)

    def changePasAct():
        changePasw(user)

    def depositAct():
        depositAcc(user, password)

    def changeUnameAct():
        changeUserName(user, password)

    def withdrawAct():
        withdrawAcc(user, password)

    def checkBalanceAct():
        checkBalance(user, password)
    
    def deleteAccAct():
        if messagebox.askyesno("Delete Account", "Are you sure you want to delete your account? This action cannot be undone."):
            db_helper.delete_user(user, password)
            messagebox.showinfo("Deleted", "Your account has been deleted successfully!")
            useAccFrame.place_forget()
            newAccBtn.pack(fill=X, padx=300, pady=20)
            loginBtn.pack(fill=X, padx=300, pady=20)

    userInfo = Label(useAccFrame,text='User: '+user, font='Helvetica 18 underline',fg=color_root,bg=color_child,border=2,padx=10,pady=5)
    userInfo.place(relx=0.05,rely=0.02)

    changePasBtn = Button(useAccFrame, text='Change Password',font='Arial 14',fg=color_root,bg=color_child,command=changePasAct).place(relx=0.08,rely=0.4,width=180)
    updateUsrtBtn = Button(useAccFrame, text='Edit User Name',font='Arial 14',fg=color_root,bg=color_child,command=changeUnameAct).place(relx=0.7,rely=0.4,width=180)
    depositBtn = Button(useAccFrame, text='Deposit Amount',font='Arial 14',fg=color_root,bg=color_child,command=depositAct).place(relx=0.08,rely=0.5,width=180)
    withdrawBtn = Button(useAccFrame, text='Withdraw Amount',font='Arial 14',fg=color_root,bg=color_child, command=withdrawAct).place(relx=0.7,rely=0.5,width=180)
    checkBalanceBtn = Button(useAccFrame, text='Check Balance',font='Arial 14',fg=color_root,bg=color_child, command=checkBalanceAct).place(relx=0.08,rely=0.6,width=180)

    logoutBtn = Button(useAccFrame, text='Logout',font='Arial 14',fg='red',bg=color_child,command=lambda: [useAccFrame.place_forget(), newAccBtn.pack(fill=X,padx=300,pady=20), loginBtn.pack(fill=X,padx=300,pady=20)]).place(relx=0.7,rely=0.6,width=180)

    deleteAccBtn = Button(useAccFrame, text='Delete Account',font='Arial 14',fg='red',bg=color_child,command=deleteAccAct).place(relx=0.4,rely=0.78,width=180)


heading = Label(root, text='Welcome to Pyhton ATM',font='Helvetica 20 underline',fg=color_child2, bg=color_root).pack(side='top',pady=5)

newAccBtn = Button(root,text='Create Account',font='18',command=createAcc,bg=color_child2,fg=color_root)
newAccBtn.pack(fill=X,padx=300,pady=20)

loginBtn = Button(root,text='Login',font='18',command=loginAcc,bg=color_child2,fg=color_root)
loginBtn.pack(fill=X,padx=300,pady=20)

useAccFrame = Frame(root,bg='grey',relief='raised')

root.mainloop()