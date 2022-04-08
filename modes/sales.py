from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import datetime as dt
import time

class SalesClass:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1145x558+202+112")
		self.root.title("Sales")
		logo=PhotoImage(file="images/logo.png")
		self.root.iconphoto(False, logo)
		self.root.config(bg="white")
		self.root.focus()
#======= All Variables ===========

#== Contents ==#
		title=Label(self.root,text="Sales Order Placement", font=("goudy old style",20,"bold"),bg="#0f4d7d", fg="white").place(x=0,y=10,width=1145)
	#== Row1 ==#
		lbl_cus_name=Label(self.root,text="Customer Name	:", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=100)
		lbl_cus_ph=Label(self.root,text="Customer Address:", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=140)
		lbl_cus_addr=Label(self.root,text="Customer Phone	:", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=180)

		lbl_cus_name=Entry(self.root, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=240,y=100,width=300)
		lbl_cus_ph=Entry(self.root, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=240,y=140,width=300)
		lbl_cus_addr=Entry(self.root, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=240,y=180,width=300)


#== Greetings & Clock ==#
		date = dt.datetime.now()
		lbl_date_clk=Label(self.root,text="Date	:", font=("goudy old style",15,"bold"),bg="white").place(x=700,y=100)
		self.greetclk=Label(self.root,text=f"{date:%A, %B %d, %Y}", font=("times new roman",15),bg="lightyellow").place(x=820,y=100)

		lbl_date_clk=Label(self.root,text="Time	:", font=("goudy old style",15,"bold"),bg="white").place(x=700,y=140)
		tim = time.strftime('%I:%M:%S %p')
		self.time_clk=Label(self.root,text=tim, font=("times new roman",15),bg="lightyellow").place(x=820,y=140)
#== Search Frame==#
		ProdFrame=LabelFrame(self.root,text="Product",bg="white", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
		ProdFrame.place(x=10,y=220,width=1125,height=100)

		lbl_prod_name=Label(ProdFrame,text="Name:", font=("goudy old style",15,"bold"),bg="white").place(x=80,y=0)
		lbl_prod_qty=Label(ProdFrame,text="Quantity:", font=("goudy old style",15,"bold"),bg="white").place(x=550,y=0)
		lbl_prod_pric=Label(ProdFrame,text="Price:", font=("goudy old style",15,"bold"),bg="white").place(x=700,y=0)

		lbl_prod_name=Entry(ProdFrame, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=80,y=30,width=400)
		lbl_prod_qty=Entry(ProdFrame, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=550,y=30,width=100)
		lbl_prod_pric=Entry(ProdFrame, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=700,y=30,width=100)

		btn_add_prod=Button(ProdFrame,text="Add",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",bd=2, cursor="hand2").place(x=890,y=30,width="100",height=28)
		btn_delete=Button(ProdFrame,text="Remove",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",bd=2, cursor="hand2").place(x=1000,y=30,width="100",height=28)




#== Viewer ==#
if __name__=="__main__":
	root=Tk()
	obj=SalesClass(root)
	root.mainloop()