from tkinter import *
import csv
from tkinter import messagebox

phonelist = []
def ProcitajCSVFile():
	global header
	with open('StudentData.csv') as csvfile:
		csv_reader = csv.reader(csvfile,delimiter=',')
		header = next(csv_reader)
		for row in csv_reader:
			phonelist.append(row)
	set_select()		
	print(phonelist)

def UpisiUCSVFile(phonelist):
	with open('StudentData.csv','w',newline='') as csv_file:
		writeobj = csv.writer(csv_file,delimiter=',')
		writeobj.writerow(header)
		for row in phonelist:
			writeobj.writerow(row)


def Odabrani():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Molimo odaberite ime")
	else:
		return int(select.curselection()[0])
		


def DodajKontakt():
	if E_name.get()!="" and E_last_name.get()!="" and E_contact.get()!="":
		phonelist.append([E_name.get()+' '+E_last_name.get(),E_contact.get()])
		print(phonelist)
		UpisiUCSVFile(phonelist)
		set_select()
		Reset()
		messagebox.showinfo("Confermation", "Kontakt dodan")
		
	else:
		messagebox.showerror("Error", "Molimo ispunite informacije")

def AzurirajKontakt():
	if E_name.get() and E_last_name.get() and E_contact.get():
		phonelist[Odabrani()] = [ E_name.get()+' '+E_last_name.get(), E_contact.get()]
		UpisiUCSVFile(phonelist)
		messagebox.showinfo("Confirmation", "Kontakt azuriran")
		Reset()
		set_select()

	elif not(E_name.get()) and not(E_last_name.get()) and not(E_contact.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Molimo ispunite informacije")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Odaberite ime i  \n pritisnite Azuriraj dugme")
		else:
			message1 = """Da biste ucitali sve informacije \n 
						  odabranog retka pritisnite dugme Ucitaj\n.
						  """
			messagebox.showerror("Error", message1)

def Reset():
	E_name_var.set('')
	E_last_name_var.set('')
	E_contact_var.set('')


def IzbrisiKontakt():
	if len(select.curselection())!=0:
		result=messagebox.askyesno('Confirmation','Zelite li obrisati\n odabrani kontakt?')
		if result==True:
			del phonelist[Odabrani()]
			UpisiUCSVFile(phonelist)
			set_select()
	else:
		messagebox.showerror("Error", 'Molimo odaberite kontakt')

def UcitajKontakt():
    name, phone = phonelist[Odabrani()]
    print(name.split(' '))
    E_name_var.set(name.split()[0])
    E_last_name_var.set(name.split()[1])
    E_contact_var.set(phone)


def set_select():
    phonelist.sort(key=lambda record: record[1])
    select.delete(0, END)
    i=0
    for name, phone in phonelist:
    	i+=1
    	select.insert(END, f"{i}  |    {name}   |   {phone}")


prozor = Tk()

Frame1 = LabelFrame(prozor,text="Unesite Kontakt")
Frame1.grid(padx=15,pady=15)


Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0,column=0,padx=15,pady=15)
#---------------------------------------------
l_name = Label(Inside_Frame1,text="Ime")
l_name.grid(row=0,column=0,padx=5,pady=5)
E_name_var = StringVar()

E_name = Entry(Inside_Frame1,width=30, textvariable=E_name_var)
E_name.grid(row=0,column=1,padx=5,pady=5)
#-----------------------------------------------
l_last_name= Label(Inside_Frame1,text="Prezime")
l_last_name.grid(row=1,column=0,padx=5,pady=5)
E_last_name_var= StringVar()
E_last_name = Entry(Inside_Frame1,width=30,textvariable=E_last_name_var)
E_last_name.grid(row=1,column=1,padx=5,pady=5)
#---------------------------------------------------
l_contact= Label(Inside_Frame1,text="Kontakt")
l_contact.grid(row=2,column=0,padx=5,pady=5)
E_contact_var = StringVar()
E_contact = Entry(Inside_Frame1,width=30,textvariable=E_contact_var)
E_contact.grid(row=2,column=1,padx=5,pady=5)
#---------------------------------------------------
Frame2 = Frame(prozor)
Frame2.grid(row=0,column=1,padx=15,pady=15,sticky=E)
#<><><><><><><><><><><><><><<><<<><><<<><><><><><><><><><>
Add_button = Button(Frame2,text="Dodaj Kontakt",width=15,bg="#F7120B",fg="#FFFFFF",command=DodajKontakt)
Add_button.grid(row=0,column=0,padx=8,pady=8)

Update_button = Button(Frame2,text="Azuriraj",width=15,bg="#F7120B",fg="#FFFFFF",command=AzurirajKontakt)
Update_button.grid(row=1,column=0,padx=8,pady=8)


Reset_button = Button(Frame2,text="Reset",width=15,bg="#F7120B",fg="#FFFFFF",command=Reset)
Reset_button.grid(row=2,column=0,padx=8,pady=8)
#----------------------------------------------------------------------------

DisplayFrame = Frame(prozor)
DisplayFrame.grid(row=1,column=0,padx=15,pady=15)

scroll = Scrollbar(DisplayFrame, orient=VERTICAL)
select = Listbox(DisplayFrame, yscrollcommand=scroll.set,font=("Arial Bold",10),bg="#2316EC",fg="#F5F5F5",width=40,height=10,borderwidth=3,relief="groove")
scroll.config(command=select.yview)
select.grid(row=0,column=0,sticky=W)
scroll.grid(row=0,column=1,sticky=N+S)



#-----------------------------------------------------------------------------------
ActionFrame = Frame(prozor)
ActionFrame.grid(row=1,column=1,padx=15,pady=15,sticky=E)

Delete_button = Button(ActionFrame,text="Izbrisi",width=15,bg="#D20000",fg="#FFFFFF",command=IzbrisiKontakt)
Delete_button.grid(row=0,column=0,padx=5,pady=5,sticky=S)

Loadbutton = Button(ActionFrame,text="Ucitaj",width=15,bg="#6B69D6",fg="#FFFFFF",command=UcitajKontakt)
Loadbutton.grid(row=1,column=0,padx=5,pady=5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx





ProcitajCSVFile()


	

prozor.mainloop()
