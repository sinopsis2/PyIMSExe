from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class UsersClass:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1145x558+202+112")
		self.root.title("Users")
		logo=PhotoImage(file="images/company-image.png")
		self.root.iconphoto(False, logo)
		self.root.config(bg="#5E7D7E")
		self.root.focus()
#======= All Variables ===========
		self.var_searchby=StringVar()
		self.var_searchtxt=StringVar()

		self.var_usr_id=StringVar()
		self.var_gender=StringVar()
		self.var_contact=StringVar()
		self.var_name=StringVar()
		self.var_dob=StringVar()
		self.var_doj=StringVar()
		self.var_email=StringVar()
		self.var_passwd=StringVar()
		self.var_utype=StringVar()
		self.var_salary=StringVar()


#== Search Frame==#
		SearchFrame=LabelFrame(self.root,text="Search User",bg="white", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
		SearchFrame.place(x=300,y=20,width=600,height=70)

#== Options ==#
		cmb_SearchBox=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Name","Email","Phone"),state="readonly",justify=CENTER, font=("goudy old style",12,"bold"))
		cmb_SearchBox.place(x=10,y=10,width=180)
		cmb_SearchBox.current(0)

		txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=10)
		btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",bd=2, cursor="hand2").place(x=430,y=10,width="150",height=28)

		title=Label(self.root,text="User Details", font=("goudy old style",20,"bold"),bg="#0f4d7d", fg="white").place(x=50,y=100,width=1050)

#== Contents ==#
	#== Row1 ==#
		lbl_usr_id=Label(self.root,text="User ID", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=150)
		lbl_gender=Label(self.root,text="Gender", font=("goudy old style",15,"bold"),bg="white").place(x=400,y=150)
		lbl_contact=Label(self.root,text="Contact", font=("goudy old style",15,"bold"),bg="white").place(x=750,y=150)

		lbl_usr_id=Entry(self.root,text="User ID",textvariable=self.var_usr_id, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=150,width=200)
		cmb_genderBox=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state="readonly",justify=CENTER, font=("goudy old style",15,"bold"))
		cmb_genderBox.place(x=500,y=150,width=200)
		cmb_genderBox.current(0)
		lbl_contact=Entry(self.root,text="Contact",textvariable=self.var_contact, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=850,y=150,width=200)

	#== Row2 ==#
		lbl_name=Label(self.root,text="Name", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=200)
		lbl_dob=Label(self.root,text="D.O.B", font=("goudy old style",15,"bold"),bg="white").place(x=400,y=200)
		lbl_doj=Label(self.root,text="D.O.J", font=("goudy old style",15,"bold"),bg="white").place(x=750,y=200)

		lbl_name=Entry(self.root,textvariable=self.var_name, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=200,width=200)
		lbl_dob=Entry(self.root,textvariable=self.var_dob, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=500,y=200,width=200)
		lbl_contact=Entry(self.root,textvariable=self.var_doj, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=850,y=200,width=200)

	#== Row3 ==#
		lbl_email=Label(self.root,text="Email", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=250)
		lbl_passwd=Label(self.root,text="Passwd", font=("goudy old style",15,"bold"),bg="white").place(x=400,y=250)
		lbl_utype=Label(self.root,text="U.Type", font=("goudy old style",15,"bold"),bg="white").place(x=750,y=250)

		lbl_email=Entry(self.root,textvariable=self.var_email, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=250,width=200)
		lbl_passwd=Entry(self.root,textvariable=self.var_passwd, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=500,y=250,width=200)
		cmb_utypeBox=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Customer","Employee","Admin"),state="readonly",justify=CENTER, font=("goudy old style",15,"bold"))
		cmb_utypeBox.place(x=850,y=250,width=200)
		cmb_utypeBox.current(0)

		lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=300)
		lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15,"bold"),bg="white").place(x=520,y=300)

		self.txt_address=Text(self.root, font=("goudy old style",15,"bold"),bg="lightyellow")
		self.txt_address.place(x=150,y=300,width=350,height=80)
		lbl_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=600,y=300,width=200)

		#== Buttons ==#
		btn_add=Button(self.root,text="Add",command=self.add,font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",bd=2, cursor="hand2").place(x=600,y=350,width="110",height=28)
		btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",bd=2, cursor="hand2").place(x=720,y=350,width="110",height=28)
		btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15,"bold"),bg="#f44336",fg="white",bd=2, cursor="hand2").place(x=840,y=350,width="110",height=28)
		btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",bd=2, cursor="hand2").place(x=960,y=350,width="110",height=28)

		#== User Details Viewer ==#
		usr_frame=Frame(self.root, bd=3, relief=RIDGE)
		usr_frame.place(x=0,y=400,relwidth=1,height=160)

		scrolly=Scrollbar(usr_frame,orient=VERTICAL)
		scrollx=Scrollbar(usr_frame,orient=HORIZONTAL)

		self.UsersTable=ttk.Treeview(usr_frame,columns=("uid","name","email","gender","contact","dob","doj","passwd","utype","salary","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
		scrollx.pack(side=BOTTOM,fill=X)
		scrolly.pack(side=RIGHT,fill=Y)
		scrollx.config(command=self.UsersTable.xview)
		scrolly.config(command=self.UsersTable.yview)

		self.UsersTable.heading("uid",text="User ID")
		self.UsersTable.heading("name",text="Name")
		self.UsersTable.heading("email",text="Email")
		self.UsersTable.heading("gender",text="Gender")
		self.UsersTable.heading("contact",text="Contact")
		self.UsersTable.heading("dob",text="D.O.B")
		self.UsersTable.heading("doj",text="D.O.J")
		self.UsersTable.heading("passwd",text="Passwd")
		self.UsersTable.heading("utype",text="U.Type")
		self.UsersTable.heading("salary",text="Salary")
		self.UsersTable.heading("address",text="Address")
		self.UsersTable["show"]="headings"

		self.UsersTable.column("uid",width=50)
		self.UsersTable.column("name",width=100)
		self.UsersTable.column("email",width=150)
		self.UsersTable.column("gender",width=100)
		self.UsersTable.column("contact",width=100)
		self.UsersTable.column("dob",width=100)
		self.UsersTable.column("doj",width=100)
		self.UsersTable.column("passwd",width=100)
		self.UsersTable.column("utype",width=100)
		self.UsersTable.column("salary",width=100)
		self.UsersTable.column("address",width=200)
		self.UsersTable.pack(fill=BOTH,expand=1)
		self.UsersTable.bind("<ButtonRelease-1>",self.get_data)

		self.show()

#== Contents Functions==#
	#=============== Add Button ==============#
	def add(self):
		con=sqlite3.connect(database=r'databases/system.db')
		cur=con.cursor()
		try:
			if self.var_usr_id.get()=="":
				messagebox.showerror("Error","User ID Requird",parent=self.root)
			else:
				cur.execute("Select * from users where uid=?",(self.var_usr_id.get(),))
				row=cur.fetchone()
				if row!=None:
					messagebox.showerror("Error","This User ID Already Exists Try Different",parent=self.root)
				else:
					cur.execute("Insert into users (uid,name,email,gender,contact,dob,doj,passwd,utype,salary,address) values (?,?,?,?,?,?,?,?,?,?,?)",(
									self.var_usr_id.get(),
									self.var_name.get(),
									self.var_email.get(),
									self.var_gender.get(),
									self.var_contact.get(),
									self.var_dob.get(),
									self.var_doj.get(),
									self.var_passwd.get(),
									self.var_utype.get(),
									self.var_salary.get(),
									self.txt_address.get('1.0',END)		
					))
					con.commit()
					self.show()
					messagebox.showinfo("Success", "User Added Successfully.",parent=self.root)
#
		except Exception as ex:
			messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root)
	#=============== Show ==============#
	def show(self):
		con=sqlite3.connect(database=r'databases/system.db')
		cur=con.cursor()
		try:
			cur.execute("Select * from users")
			rows=cur.fetchall()
			self.UsersTable.delete(*self.UsersTable.get_children())
			for row in rows:
				self.UsersTable.insert('',END,values=row)
#
		except Exception as ex:
			messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root)

	#=============== Get Data ==============#
	def get_data(self,ev):
		f=self.UsersTable.focus()
		content=(self.UsersTable.item(f))
		row=content['values']
#		print(row)
		self.var_usr_id.set(row[0]),
		self.var_name.set(row[1]),
		self.var_email.set(row[2]),
		self.var_gender.set(row[3]),
		self.var_contact.set(row[4]),
		self.var_dob.set(row[5]),
		self.var_doj.set(row[6]),
		self.var_passwd.set(row[7]),
		self.var_utype.set(row[8]),
		self.var_salary.set(row[9]),
		self.txt_address.delete('1.0',END)
		self.txt_address.insert(END,row[10])
	#-------------------------------------------------------#

	#=============== Update Button ==============#
	def update(self):
		con=sqlite3.connect(database=r'databases/system.db')
		cur=con.cursor()
		try:
			if self.var_usr_id.get()=="":
				messagebox.showerror("Error","User ID Requird",parent=self.root)
			else:
				cur.execute("Select * from users where uid=?",(self.var_usr_id.get(),))
				row=cur.fetchone()
				if row==None:
					messagebox.showerror("Error","Invalid User ID",parent=self.root)
				else:
					cur.execute("Update users set name=?,email=?,gender=?,contact=?,dob=?,doj=?,passwd=?,utype=?,salary=?,address=? where uid=?",(
									self.var_name.get(),
									self.var_email.get(),
									self.var_gender.get(),
									self.var_contact.get(),
									self.var_dob.get(),
									self.var_doj.get(),
									self.var_passwd.get(),
									self.var_utype.get(),
									self.var_salary.get(),
									self.txt_address.get('1.0',END),
									self.var_usr_id.get(),
					))
					con.commit()
					self.show()
					messagebox.showinfo("Success", "User Updated Successfully.",parent=self.root)
#
		except Exception as ex:
			messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root)
	#-------------------------------------------------------#

	#=============== Delete Button ==============#
	def delete(self):
		con=sqlite3.connect(database=r'databases/system.db')
		cur=con.cursor()
		try:
			if self.var_usr_id.get()=="":
				messagebox.showerror("Error","User ID Requird",parent=self.root)
			else:
				cur.execute("Select * from users where uid=?",(self.var_usr_id.get(),))
				row=cur.fetchone()
				if row==None:
					messagebox.showerror("Error","Invalid User ID",parent=self.root)
				else:
					op=messagebox.askyesno("Confirm", "Do You Really Want To Delete?",parent=self.root)
					if op==True:
						cur.execute("delete from users where uid=?",(self.var_usr_id.get(),))
						con.commit()
						messagebox.showinfo("Delete", "Deleted Successfully.",parent=self.root)
						self.clear()
#
		except Exception as ex:
			messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root)
	#-------------------------------------------------------#

	#=============== Clear Button ==============#
	def clear(self):
		self.var_usr_id.set(""),
		self.var_name.set(""),
		self.var_email.set(""),
		self.var_gender.set("Select"),
		self.var_contact.set(""),
		self.var_dob.set(""),
		self.var_doj.set(""),
		self.var_passwd.set(""),
		self.var_utype.set("Admin"),
		self.var_salary.set(""),
		self.txt_address.delete('1.0',END)
		self.var_searchby.set("select")
		self.var_searchtxt.set("")

		self.show()
	#-------------------------------------------------------#
	#=============== Search Button Function ==============#
	def search(self):
		con=sqlite3.connect(database=r'databases/system.db')
		cur=con.cursor()
		try:
			if self.var_searchby.get()=="Select":
				messagebox.showerror("Error","Select Search Option",parent=self.root)
			elif self.var_searchtxt.get()=="":
				messagebox.showerror("Error","Search Input Is Empty",parent=self.root)
			else:
				cur.execute("Select * from users where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
				rows=cur.fetchall()
				if len(rows)!=0:
					self.UsersTable.delete(*self.UsersTable.get_children())
					for row in rows:
						self.UsersTable.insert('',END,values=row)
				else:
					messagebox.showerror("Error","No Record Found!",parent=self.root)
#
		except Exception as ex:
			messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root)
#----------------------------------------------------

#== Viewer ==#
if __name__=="__main__":
	root=Tk()
	obj=UsersClass(root)
	root.mainloop()
