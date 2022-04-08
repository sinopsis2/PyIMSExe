from tkinter import*
from PIL import Image, ImageTk
import datetime as dt
from modes.users import UsersClass
from modes.categories import CategorieClass
from modes.products import ProductsClass
from modes.mediafiles import MediaFileClass
from modes.sales import SalesClass



class IMS:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1350x700+0+0")
		self.root.title("Inventory Management System | Devoloped by Shurid")
		logo=PhotoImage(file ="images/logo.png")
		self.root.slogo=PhotoImage(file="Images/32x32.png")
		self.root.iconphoto(False, logo)

#== Title ==#
		self.root.slogo=PhotoImage(file="Images/32x32.png")
		title=Label(self.root,text="Inventory Management System",image=self.root.slogo, compound=LEFT, font=("times new roman",24,"bold"),bg="#010c48", fg="white").place(x=0,y=0,relwidth=1,height=50)

#== Logout Button ==#
		logoutbtn=Button(self.root,text="Logout",command=self.lgout,font=("times new roman",14,"bold"),bg="yellow", cursor="hand2").place(x=1120,y=10,height=30, width=120)

#== Greetings & Clock ==#
		date = dt.datetime.now()
		self.greetclk=Label(self.root,text="Welcome to Inventory Management System\t\t"f"{date:%A, %B %d, %Y}", font=("times new roman",12),bg="#4d636d", fg="white")
		self.greetclk.place(x=0,y=50,relwidth=1,height=30)

#== Left Menu ==#
		self.LeftMenuLogo=Image.open("Images/company-image.png")
		self.LeftMenuLogo=self.LeftMenuLogo.resize((200,200), Image.ANTIALIAS)
		self.LeftMenuLogo=ImageTk.PhotoImage(self.LeftMenuLogo)

		LeftMenu=Frame(self.root, bd=2, relief=RIDGE,bg="#808080")
		LeftMenu.place(x=0,y=80,width=200,height=615)

		LeftMenuLogoImg=Label(LeftMenu, image=self.LeftMenuLogo)
		LeftMenuLogoImg.pack(side=TOP,fill=X)

#== Menu ==#
		lblMenu=Label(LeftMenu,text="Menu", font=("times new roman",26,"bold"), bg="#009688").pack(side=TOP, fill=X)

#== Menu Button ==#
		Dashboardbtn=Button(LeftMenu,text="Dashboard",font=("times new roman",14,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
		UserMgmtbtn=Button(LeftMenu,text="Users",command=self.users, font=("times new roman",14,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
		Categoriesbtn=Button(LeftMenu,text="Categories",command=self.categorie,font=("times new roman",14,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
		Productsbtn=Button(LeftMenu,text="Products",command=self.prod,font=("times new roman",14,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
		MediaFilesbtn=Button(LeftMenu,text="Media Files",command=self.mediafile,font=("times new roman",14,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
		Salesbtn=Button(LeftMenu,text="Sales",command=self.sale,font=("times new roman",14,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
		SalesReportsbtn=Button(LeftMenu,text="Sales Reports", font=("times new roman",14,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
		Accountsbtn=Button(LeftMenu,text="Accounts", font=("times new roman",14,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)

		self.prodlbl=Label(self.root,text="Total Products\n[0]",bd=5,relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20,"bold"))
		self.prodlbl.place(x=300,y=100,height=250,width=400)

		self.usrlbl=Label(self.root,text="Total Products\n[0]",bd=5,relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20,"bold"))
		self.usrlbl.place(x=800,y=100,height=250,width=400)

		self.slslbl=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20,"bold"))
		self.slslbl.place(x=300,y=400,height=250,width=400)

		self.ctglbl=Label(self.root,text="Total Categories\n[0]",bd=5,relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20,"bold"))
		self.ctglbl.place(x=800,y=400,height=250,width=400)



#== Footer ==#
		lblFooter=Label(self.root,text=f"Inventory Management System | Copyright @ BitSoft From 2021 to {date.year}",font=("times new roman",14,"bold"), bg="#31906E", fg="#800000").pack(side=BOTTOM, fill=X)

#== Contents Functions==#
	def lgout(self):
		self.root.destroy()

	def exit(self):
		self.new_win=Toplevel(self.root)
		self.new_win.destroy()

	def users(self):
			self.new_win=Toplevel(self.root)
			self.usr_win=UsersClass(self.new_win)

	def categorie(self):
			self.new_win=Toplevel(self.root)
			self.ctg_win=CategorieClass(self.new_win)

	def prod(self):
			self.new_win=Toplevel(self.root)
			self.prod_win=ProductsClass(self.new_win)

	def mediafile(self):
			self.new_win=Toplevel(self.root)
			self.mf_win=MediaFileClass(self.new_win)

	def sale(self):
			self.new_win=Toplevel(self.root)
			self.sel_win=SalesClass(self.new_win)


if __name__=="__main__":

#== Viewer ==#
	root=Tk()
	obj=IMS(root)
	root.mainloop()
