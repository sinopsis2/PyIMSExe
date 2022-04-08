from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox

class MediaFileClass:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1145x558+202+112")
		self.root.title("Users")
		logo=PhotoImage(file="images/company-image.png")
		self.root.iconphoto(False, logo)
		self.root.config(bg="black")
		self.root.focus()
#======= All Variables ===========

		title=Label(self.root,text="Media File Details", font=("goudy old style",20,"bold"),bg="#0f4d7d", fg="white").place(x=50,y=100,width=1050)


#== Viewer ==#
if __name__=="__main__":
	root=Tk()
	obj=MediaFileClass(root)
	root.mainloop()