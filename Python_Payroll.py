import tkinter as tk #import tkinter
from PIL import Image, ImageTk #import pillow
import os #os module for operating system functions
current_dir = os.getcwd() #get the current directory
file_dir = '\\default_pfp.png' #relative directory
full_path = current_dir + file_dir #the full directory to the file
print(full_path) #print the full path for debugging

WN_W = 668 #window width
WN_H = 864 #window height

class PayrollGui:
    #constructor
     def __init__(self):
         self.root = tk.Tk() #construct a window object
         self.root.title("Payroll") #set title
         self.root.geometry(str(WN_W)+'x'+str(WN_H)) #set window size
         
         self.lblHeader = tk.Label(self.root, text='SE-RI\'S CHOICE PAYROLL', font=('Algerian', 18,'bold'))
         self.lblHeader.place(relx = 0.5,y=50, anchor='center') #center

         self.lbl1 = tk.Label(self.root, text='EMPLOYEE BASIC INFO:', font=('Arial',9,'bold'))
         self.lbl1.place(x=20, y=80)

         #picture
         image = Image.open(full_path) #load the image
         render = ImageTk.PhotoImage(image.resize((120,120))) #render the image in tkinter
         self.lblImg = tk.Label(self.root, image=render) #set the label image param to render
         self.lblImg.place(x=20,y=100) #place the banner object in the window

         #employee basic info
         self.lblEmpno = tk.Label(self.root,text="Employee Number: ", font=('Arial',7)).place(x=25,y=230)
         self.txtEmpno = tk.Text(self.root,height=1,width = 20).place(x=140, y=230)

         self.lblSearch = tk.Label(self.root,text="Search Employee: ", font=('Arial',7)).place(x=25,y=270)
         self.btnSearch = tk.Button(self.root, text="SEARCH", bg='red', fg='white', font=('Arial',8), width=10, height=1).place(x=140, y=260)

         self.lblDept = tk.Label(self.root,text="Department: ", font=('Arial',7)).place(x=25,y=300)
         self.txtDept = tk.Text(self.root,height=1,width = 20).place(x=140, y=300)

         #basic income
         self.lblIncomeHeader = tk.Label(self.root, text='BASIC INCOME:', font=('Arial',9,'bold')).place(x=20, y=325)

         self.lblRate1 = tk.Label(self.root,text="Rate / Hour: ", font=('Arial',7)).place(x=25,y=365)
         self.txtRate1 = tk.Text(self.root,height=1,width = 20).place(x=140, y=365)

         self.lblHours1 = tk.Label(self.root,text="No. of Hours / Cut Off: ", font=('Arial',7)).place(x=25,y=390)
         self.txtHours1 = tk.Text(self.root,height=1,width = 20).place(x=140, y=390)

         self.lblIncome1 = tk.Label(self.root,text="Income / Cut Off: ", font=('Arial',8)).place(x=25,y=415)
         self.txtIncome1 = tk.Text(self.root,height=1,width = 20).place(x=140, y=415)

         #honorarium income
         self.lblHonorariumHeader = tk.Label(self.root, text='HONORARIUM INCOME:', font=('Arial',9,'bold')).place(x=20, y=440)

         self.lblRate2 = tk.Label(self.root,text="Rate / Hour: ", font=('Arial',7)).place(x=25,y=480)
         self.txtRate2 = tk.Text(self.root,height=1,width = 20).place(x=140, y=480)

         self.lblHours2 = tk.Label(self.root,text="No. of Hours / Cut Off: ", font=('Arial',7)).place(x=25,y=505)
         self.txtHours2 = tk.Text(self.root,height=1,width = 20).place(x=140, y=505)

         self.lblIncome2 = tk.Label(self.root,text="Income / Cut Off: ", font=('Arial',7)).place(x=25,y=530)
         self.txtIncome2 = tk.Text(self.root,height=1,width = 20).place(x=140, y=530)

         #other income
         self.lblOtherHeader = tk.Label(self.root, text='OTHER INCOME:', font=('Arial',9,'bold')).place(x=20, y=555)

         self.lblRate3 = tk.Label(self.root,text="Rate / Hour: ", font=('Arial',7)).place(x=25,y=595)
         self.txtRate3 = tk.Text(self.root,height=1,width = 20).place(x=140, y=595)

         self.lblHours3 = tk.Label(self.root,text="No. of Hours / Cut Off: ", font=('Arial',7)).place(x=25,y=620)
         self.txtHours3 = tk.Text(self.root,height=1,width = 20).place(x=140, y=620)

         self.lblIncome3 = tk.Label(self.root,text="Income / Cut Off: ", font=('Arial',7)).place(x=25,y=645)
         self.txtIncome3 = tk.Text(self.root,height=1,width = 20).place(x=140, y=645)

         #summary income
         self.lblOtherHeader = tk.Label(self.root, text='SUMMARY INCOME:', font=('Arial',9,'bold')).place(x=20, y=670)

         self.lblGrossIncome = tk.Label(self.root,text="GROSS INCOME: ", font=('Arial',7)).place(x=25,y=710)
         self.txtGrossIncome = tk.Text(self.root,height=1,width = 20).place(x=140, y=710)

         self.lblNetIncome = tk.Label(self.root,text="NET INCOME: ", font=('Arial',7)).place(x=25,y=735)
         self.txtNetIncome = tk.Text(self.root,height=1,width = 20).place(x=140, y=735)


         #basic info
         self.lblFirstname = tk.Label(self.root,text="Firstname: ", font=('Arial',7)).place(x=359,y=100)
         self.txtFirstname = tk.Text(self.root,height=1,width = 20).place(x=479, y=100)

         self.lblMiddlename = tk.Label(self.root,text="Middle Name: ", font=('Arial',7)).place(x=359,y=125)
         self.txtMiddlename = tk.Text(self.root,height=1,width = 20).place(x=479, y=125)

         self.lblSurname = tk.Label(self.root,text="Surname: ", font=('Arial',7)).place(x=359,y=150)
         self.txtSurname = tk.Text(self.root,height=1,width = 20).place(x=479, y=150)

         self.lblCivilStatus = tk.Label(self.root,text="Civil Status: ", font=('Arial',7)).place(x=359,y=175)
         self.txtCivilStatus = tk.Text(self.root,height=1,width = 20).place(x=479, y=175)

         self.lblQualifDep = tk.Label(self.root,text="Qualified Dependents \nStatus: ", font=('Arial',7)).place(x=359,y=200)
         self.txtQualifDep = tk.Text(self.root,height=1,width = 20).place(x=479, y=200)

         self.lblPaydate = tk.Label(self.root,text="Paydate: ", font=('Arial',7)).place(x=359,y=225)
         self.txtPaydate = tk.Text(self.root,height=1,width = 20).place(x=479, y=225)

         self.lblEmpStatus = tk.Label(self.root,text="Employee Status: ", font=('Arial',7)).place(x=359,y=250)
         self.txtEmpStatus = tk.Text(self.root,height=1,width = 20).place(x=479, y=250)

         self.lblDesignation = tk.Label(self.root,text="Designation: ", font=('Arial',8)).place(x=359,y=275)
         self.txtDesignation = tk.Text(self.root,height=1,width = 20).place(x=479, y=275)

         #regular deductions
         self.lblOtherDeductionsHeader = tk.Label(self.root, text='REGULAR DEDUCTIONS:', font=('Arial',9,'bold')).place(x=359, y=340)

         self.lblSssCon = tk.Label(self.root,text="SSS Contribution: ", font=('Arial',7)).place(x=359,y=380)
         self.txtSssCon = tk.Text(self.root,height=1,width = 20).place(x=479, y=380)

         self.lblPhilCon = tk.Label(self.root,text="PhilHealth Contribution: ", font=('Arial',7)).place(x=359,y=405)
         self.txtPhilCon = tk.Text(self.root,height=1,width = 20).place(x=479, y=405)

         self.lblPagibigCon = tk.Label(self.root,text="Pagibig Contribution: ", font=('Arial',7)).place(x=359,y=430)
         self.txtPagibigCon = tk.Text(self.root,height=1,width = 20).place(x=479, y=430)

         self.lblIncomeTaxCon = tk.Label(self.root,text="Income Tax Contribution: ", font=('Arial',7)).place(x=359,y=455)
         self.txtIncomeTaxCon = tk.Text(self.root,height=1,width = 20).place(x=479, y=455)

         #other deductions
         self.lblOtherDeductionsHeader = tk.Label(self.root, text='OTHER DEDUCTIONS:', font=('Arial',9,'bold')).place(x=359, y=480)

         self.lblSssLoan = tk.Label(self.root,text="SSS Loan: ", font=('Arial',7)).place(x=359,y=520)
         self.txtSssLoan = tk.Text(self.root,height=1,width = 20).place(x=479, y=520)

         self.lblPagibigLoan = tk.Label(self.root,text="Pagibig Loan: ", font=('Arial',7)).place(x=359,y=545)
         self.txtPagibigLoan = tk.Text(self.root,height=1,width = 20).place(x=479, y=545)

         self.lblFacultyDeposit = tk.Label(self.root,text="Faculty Savings Deposit: ", font=('Arial',7)).place(x=359,y=570)
         self.txtFacultyDeposit = tk.Text(self.root,height=1,width = 20).place(x=479, y=570)

         self.lblFacultyLoan = tk.Label(self.root,text="Faculty Savings Loan: ", font=('Arial',7)).place(x=359,y=595)
         self.txtFacultyLoan = tk.Text(self.root,height=1,width = 20).place(x=479, y=595)

         self.lblSalaryLoan = tk.Label(self.root,text="Salary Loan: ", font=('Arial',7)).place(x=359,y=620)
         self.txtSalaryLoan = tk.Text(self.root,height=1,width = 20).place(x=479, y=620)

         self.lblOtherLoan = tk.Label(self.root,text="Other Loan: ", font=('Arial',7)).place(x=359,y=645)
         self.txtOtherLoan = tk.Text(self.root,height=1,width = 20).place(x=479, y=645)

         #deduction summary
         self.lblOtherHeader = tk.Label(self.root, text='DEDUCTION SUMMARY:', font=('Arial',9,'bold')).place(x=354, y=670)

         self.lblTotalDeductions = tk.Label(self.root,text="GROSS INCOME: ", font=('Arial',7)).place(x=359,y=700)
         self.txtTotalDeductions = tk.Text(self.root,height=1,width = 20).place(x=479, y=700)

         self.btnGross = tk.Button(self.root, text="GROSS INCOME", bg='blue', fg='white', font=('Arial',7), width=12).place(x=354, y=735)
         self.btnNet = tk.Button(self.root, text="NET INCOME", bg='blue', fg='white', font=('Arial',7), width=11).place(x=440, y=735)
         self.btnSave = tk.Button(self.root, text="SAVE", bg='dark turquoise', fg='white', font=('Arial',7), width=5).place(x=520, y=735)
         self.btnUpdate = tk.Button(self.root, text="UPDATE", bg='dark turquoise', fg='white', font=('Arial',7), width=7).place(x=563, y=735)
         self.btnSave = tk.Button(self.root, text="NEW", bg='yellow', fg='black', font=('Arial',7), width=5).place(x=620, y=735)

         self.root.mainloop() #execute GUI

PayrollGui() #call the constructor