from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import sqlite3


class employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")

        
        self.var_name=StringVar()
        self.var_desig=StringVar()
        self.var_addr=StringVar()
        self.var_dob=StringVar()
        self.var_id=StringVar()
        self.var_dept=StringVar()
        self.var_email=StringVar()
        self.var_salary=StringVar()
        
               
        lbl_title=Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),fg="white",bg="black")
        lbl_title.place(x=0,y=0,width=1530,height=50)
        
        
        img_logo=Image.open("images/appleinc.png")
        img_logo=img_logo.resize((80,80))
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=230,y=0,width=50,height=50)
        
        
        img_frm1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        img_frm1.place(x=0,y=50,width=1530,height=160)
        
        
        img_logo1=Image.open("images/apple1.webp")
        img_logo1=img_logo1.resize((340,160))
        self.photo_logo1=ImageTk.PhotoImage(img_logo1)
        self.logo1=Label(img_frm1,image=self.photo_logo1)
        self.logo1.place(x=0,y=0,width=340,height=160)
        
        lbl_title1=Label(img_frm1,text="Apple.Inc Database Access Granted",font=("times new roman",30,"bold"),fg="black")
        lbl_title1.place(x=340,y=0,width=1300,height=200)
        
        req_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        req_frame.place(x=10,y=220,width=1500,height=560)
        
        req_frame1=Frame(req_frame,bd=2,relief=RIDGE,bg="white")
        req_frame1.place(x=10,y=10,width=1480,height=260)
        
        req_frame2=Frame(req_frame,bd=2,relief=RIDGE,bg="white")
        req_frame2.place(x=10,y=280,width=1480,height=260)
        
        dept=Label(req_frame,text="Department",font=("arial",15,"bold"),bg="white")
        dept.grid(row=1,column=2,padx=20,pady=20)
        
        dept_det=ttk.Combobox(req_frame,textvariable=self.var_dept,font=("arial",13,"bold"),width=26,state="readonly")
        dept_det["value"]=("Select Department","HR","Manager","Software Engineer","Non Techincal")
        dept_det.current(0)
        dept_det.grid(row=1,column=3,padx=2,pady=10)
        
        name=Label(req_frame,text="Name",font=("arial",15,"bold"),bg="white")
        name.grid(row=0,column=0,padx=20,pady=20)
        
        name_det=ttk.Entry(req_frame,width=22,textvariable=self.var_name,font=("arial",15,"bold"))
        name_det.grid(row=0,column=1,padx=2,pady=10)
        
        desig=Label(req_frame,text="designation",font=("arial",15,"bold"),bg="white")
        desig.grid(row=1,column=0,padx=20,pady=20)
        
        desig_det=ttk.Entry(req_frame,textvariable=self.var_desig,width=22,font=("arial",15,"bold"))
        desig_det.grid(row=1,column=1,padx=2,pady=10)
        
        email=Label(req_frame,text="E-Mail",font=("arial",15,"bold"),bg="white")
        email.grid(row=2,column=2,padx=20,pady=20)
        
        email_det=ttk.Entry(req_frame,textvariable=self.var_email,width=22,font=("arial",15,"bold"))
        email_det.grid(row=2,column=3,padx=2,pady=10)
        
        addr=Label(req_frame,text="Address",font=("arial",15,"bold"),bg="white")
        addr.grid(row=2,column=0,padx=20,pady=20)
        
        addr_det=ttk.Entry(req_frame,textvariable=self.var_addr,width=22,font=("arial",15,"bold"))
        addr_det.grid(row=2,column=1,padx=2,pady=10)
        
        salary=Label(req_frame,text="Salary",font=("arial",15,"bold"),bg="white")
        salary.grid(row=3,column=2,padx=20,pady=20)
        
        salary_det=ttk.Entry(req_frame,textvariable=self.var_salary,width=22,font=("arial",15,"bold"))
        salary_det.grid(row=3,column=3,padx=2,pady=10)
        
        DOB=Label(req_frame,text="D.O.B",font=("arial",15,"bold"),bg="white")
        DOB.grid(row=3,column=0,padx=10,pady=10)
        
        DOB_det=ttk.Entry(req_frame,textvariable=self.var_dob,width=22,font=("arial",15,"bold"))
        DOB_det.grid(row=3,column=1,padx=2,pady=10)
        
        id=Label(req_frame,text="ID Proof",font=("arial",15,"bold"),bg="white")
        id.grid(row=0,column=2,padx=20,pady=20)
        
        id_det=ttk.Combobox(req_frame,textvariable=self.var_id,font=("arial",13,"bold"),width=26,state="readonly")
        id_det["value"]=("Passport","Liscense","Aadhar","PAN Card")
        id_det.current(0)
        id_det.grid(row=0,column=3,padx=2,pady=10)
        
        img_emp=Image.open("images/OIP.jpeg")
        img_emp=img_emp.resize((220,220))
        self.photo_logo2=ImageTk.PhotoImage(img_emp)
        self.logo2=Label(req_frame,image=self.photo_logo2)
        self.logo2.place(x=850,y=25,width=220,height=220)
        
        img_frm5=Frame(req_frame,bd=2,relief=RIDGE,bg="white")
        img_frm5.place(x=1100,y=25,width=370,height=230)
        
        btn1=Button(img_frm5,text="Save",command=self.add_data,font=("arial",13,"bold"),width=13,bg="gray",fg="black")
        btn1.grid(row=0,column=3,padx=10,pady=17 )
        
        btn2=Button(img_frm5,text="Update",font=("arial",13,"bold"),width=13,bg="gray",fg="black")
        btn2.grid(row=1,column=3,padx=10,pady=17)
        
        btn3=Button(img_frm5,text="Delete",font=("arial",13,"bold"),width=13,bg="gray",fg="black")
        btn3.grid(row=2,column=3,padx=10,pady=17)
        
        
        srch_frm1=Frame(req_frame2,bd=2,relief=RIDGE,bg="white")
        srch_frm1.place(x=0,y=0,width=1475,height=50)
        
        search1=ttk.Combobox(srch_frm1,state="readonly",font=("arial",13,"bold"),width=18)
        search1["value"]=("select option","Name","designation")
        search1.current(0)
        search1.place(x=110,y=10)
        
        butn1=Button(srch_frm1,text="Search",font=("arial",13,"bold"),width=13,bg="gray",fg="black")
        butn1.place(x=460,y=4)
        
        lbl_srch=Label(srch_frm1,text="Search By",font=("arial",13,"bold"),bg="gray",fg="black")
        lbl_srch.place(x=0,y=7,width=100,height=30)
        
        txt_ent=ttk.Entry(srch_frm1,width=13,font=("arial",15,"bold"))
        txt_ent.place(x=300,y=7)
        
        butn2=Button(srch_frm1,text="Show All",font=("arial",13,"bold"),width=13,bg="gray",fg="black")
        butn2.place(x=610,y=4)
        
        
        dispfrm=Frame(req_frame2,bd=2,relief=RIDGE)
        dispfrm.place(x=10,y=60,width=1460,height=170)
        
        scroll_x=ttk.Scrollbar(dispfrm,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(dispfrm,orient=VERTICAL)
        
        self.tree=ttk.Treeview(dispfrm,column=("name","desig","addr","dob","id","dept","email","salary"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)   
        
        scroll_x.config(command=self.tree.xview)
        scroll_y.config(command=self.tree.yview)
        
        self.tree.heading("name",text="Name")
        self.tree.heading("desig",text="Designation")
        self.tree.heading("addr",text="Address")
        self.tree.heading("dob",text="D.O.B")
        self.tree.heading("id",text="ID Proof")
        self.tree.heading("dept",text="Department")
        self.tree.heading("email",text="E-mail")
        self.tree.heading("salary",text="Salary")
        
        self.tree["show"]="headings"

        
        self.tree.column("name",width=100)
        self.tree.column("desig",width=100)
        self.tree.column("addr",width=100)
        self.tree.column("dob",width=100)
        self.tree.column("id",width=100)
        self.tree.column("dept",width=100)
        self.tree.column("email",width=100)
        self.tree.column("salary",width=100)
        
        
        self.tree.pack(fill=BOTH,expand=1)
        self.tree.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
        
    def add_data(self):
        if self.var_name.get()=="":
            messagebox.showerror("error","All Fields are Required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="violetriolet",database="python")
                cur=conn.cursor()
                sql='Insert into employee (name,desig,addr,dob,id,dept,email,salary) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
                val=[(                                                     self.var_name.get(),
                                                                            self.var_desig.get(),
                                                                            self.var_addr.get(),
                                                                            self.var_dob.get(),
                                                                            self.var_id.get(),
                                                                            self.var_dept.get(),
                                                                            self.var_email.get(),
                                                                            self.var_salary.get(),)]
                cur.executemany(sql,val)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Employee has been added",parent= self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="violetriolet",database="python")
        cur=conn.cursor()
        cur.execute("select * from employee")
        data=cur.fetchall()
        for i in data:
            self.tree.insert("",END,values=i)
        conn.commit()
        conn.close()
    

    def get_cursor(self,event=""):
        cursor_row=self.tree.focus()
        content=self.tree.item(cursor_row)
        
        data=content["values"]
        self.var_name.set(value=data[0])
        self.var_desig.set(value=data[1])
        self.var_addr.set(value=data[2])
        self.var_dob.set(value=data[3])
        self.var_id.set(value=data[4])
        self.var_dept.set(value=data[5])
        self.var_email.set(value=data[6])
        self.var_salary.set(value=data[7])
        
        
        

root=Tk()
obj=employee(root)
root.mainloop()