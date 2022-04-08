from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox

class ProductsClass:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1145x558+202+112")
		self.root.title("Products")
		logo=PhotoImage(file="images/logo.png")
		self.root.iconphoto(False, logo)
		self.root.config(bg="white")
		self.root.focus()
#======= All Variables ===========
		self.var_searchby=StringVar()
		self.var_searchtxt=StringVar()

		self.var_prod_sku=StringVar()
		self.var_prod_title=StringVar()
		self.var_ctgo=StringVar()
		self.var_in_stk=StringVar()
		self.var_prod_buy_pric=StringVar()
		self.var_prod_sell_pric=StringVar()
		self.var_prod_img=StringVar()







#======= Fields ===========

#== Search Frame==#
		SearchFrame=LabelFrame(self.root,text="Product Search",bg="white", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
		SearchFrame.place(x=300,y=20,width=600,height=70)

#== Options ==#
		cmb_SearchBox=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Product SKU","Product Title","Categories"),state="readonly",justify=CENTER, font=("goudy old style",12,"bold"))
		cmb_SearchBox.place(x=10,y=10,width=180)
		cmb_SearchBox.current(0)

		txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=10)
		btn_search=Button(SearchFrame,text="Search",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",bd=2, cursor="hand2").place(x=430,y=10,width="150",height=28)

#======= Title ===========
		title=Label(self.root,text="Product Details", font=("goudy old style",20,"bold"),bg="#0f4d7d", fg="white").place(x=0,y=100,width=1145)

#-------------------------------------------------------#
#== Contents ==#
	#== Row1 ==#
		lbl_prod_sku=Label(self.root,text="Product SKU	:", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=150)
		lbl_prod_title=Label(self.root,text="Product Name	:", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=200)
		lbl_categorie=Label(self.root,text="Categorie	:", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=250)
		lbl_in_stk=Label(self.root,text="Quantity		:", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=300)

		lbl_buy_pric=Label(self.root,text="Buying Price	:", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=350)
		lbl_sell_pric=Label(self.root,text="Selling Price	:", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=400)
		lbl_prod_img=Label(self.root,text="Product Image	:", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=450)

		lbl_usr_id=Entry(self.root,text="User ID",textvariable=self.var_prod_sku, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=238,y=150,width=300)
		lbl_contact=Entry(self.root,text="Contact",textvariable=self.var_prod_title, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=238,y=200,width=300)	
		cmb_genderBox=ttk.Combobox(self.root,textvariable=self.var_ctgo,values=("Select","Solid","Liquid","Other"),state="readonly",justify=CENTER, font=("goudy old style",15,"bold"))
		cmb_genderBox.place(x=238,y=250,width=300)
		cmb_genderBox.current(0)

		lbl_in_stk=Entry(self.root,text="In-Stock:",textvariable=self.var_prod_sku, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=238,y=300,width=300)

		lbl_in_stk=Entry(self.root,text="In-Stock:",textvariable=self.var_prod_sku, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=238,y=350,width=300)
		lbl_in_stk=Entry(self.root,text="In-Stock:",textvariable=self.var_prod_sku, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=238,y=400,width=300)
		lbl_in_stk=Entry(self.root,text="In-Stock:",textvariable=self.var_prod_sku, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=238,y=450,width=300)
	#== Row2 ==#










#---------------------------------------------------#


#== Buttons ==#
		btn_add=Button(self.root,text="Add",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",bd=2, cursor="hand2").place(x=200,y=500,width="90",height=28)
		btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",bd=2, cursor="hand2").place(x=300,y=500,width="90",height=28)
		btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",bd=2, cursor="hand2").place(x=400,y=500,width="90",height=28)
		btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",bd=2, cursor="hand2").place(x=500,y=500,width="90",height=28)


#== Products Details Viewer ==#
		usr_frame=Frame(self.root, bd=3, relief=RIDGE)
		usr_frame.place(x=600,y=138,relwidth=1,height=400)

		scrolly=Scrollbar(usr_frame,orient=VERTICAL)
		scrollx=Scrollbar(usr_frame,orient=HORIZONTAL)


		self.ProductTable=ttk.Treeview(usr_frame,columns=("sku","prod_name","ctgo","buy_pric","sell_pric","prod_img",),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
		scrollx.pack(side=BOTTOM,fill=X)
		scrolly.pack(side=RIGHT,fill=Y)
		scrollx.config(command=self.ProductTable.xview)
		scrolly.config(command=self.ProductTable.yview)

		self.ProductTable.heading("sku",text="SKU")
		self.ProductTable.heading("prod_name",text="Name")
		self.ProductTable.heading("ctgo",text="Category")
		self.ProductTable.heading("buy_pric",text="Buy")
		self.ProductTable.heading("sell_pric",text="Sell")
		self.ProductTable.heading("prod_img",text="Img")


		self.ProductTable.column("sku",width=50)
		self.ProductTable.column("prod_name",width=100)
		self.ProductTable.column("ctgo",width=100)
		self.ProductTable.column("buy_pric",width=100)
		self.ProductTable.column("sell_pric",width=100)
		self.ProductTable.column("prod_img",width=100)

		self.ProductTable.pack(fill=BOTH,expand=1)


	#=============== Show ==============#
	def show(self):
		con=sqlite3.connect(database=r'ims.db')
		cur=con.cursor()
		try:
			cur.execute("Select * from users")
			rows=cur.fetchall()
			self.ProductTable.delete(*self.ProductTable.get_children())
			for row in rows:
				self.ProductTable.insert('',END,values=row)
#
		except Exception as ex:
			messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root)
#--------------------------------------------------------------------------------------------#


#== Viewer ==#
if __name__=="__main__":
	root=Tk()
	obj=ProductsClass(root)
	root.mainloop()