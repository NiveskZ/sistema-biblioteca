from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()

class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Novo Usuario")
        self.resizable(False, False)


        #####################################################################################

        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        # Bottom Frame
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)
        # Cabeçalho e imagem
        self.top_image = PhotoImage(file='icons/add-person.png')
        top_image_lbl = Label(self.topFrame,image=self.top_image, bg='white')
        top_image_lbl.place(x=120,y=10)
        heading= Label(self.topFrame,text='    Adicionar Novo Usuario     ', font='arial 22 bold', fg='#033f8a',bg='white')
        heading.place(x=290,y=60)

        ########################################################################################################
        # Entradas 

        # Nome
        self.lbl_name = Label(self.bottomFrame, text='Nome: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40,y=40)
        self.ent_name=Entry(self.bottomFrame, width=30, bd=2)
        self.ent_name.insert(0, 'Digite seu nome de usuario')
        self.ent_name.place(x=150,y=45)
        # Número
        self.lbl_phone = Label(self.bottomFrame, text='Telefone: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40,y=80)
        self.ent_phone=Entry(self.bottomFrame, width=30, bd=2)
        self.ent_phone.insert(0, 'Digite seu número de celular')
        self.ent_phone.place(x=150,y=85)
        
        # Botão
        button = Button(self.bottomFrame, text='Novo Usuario', command=self.addMember)
        button.place(x=270,y=120)

    def addMember(self):
        name = self.ent_name.get()
        phone = self.ent_phone.get()
        

        if (name and phone != ""):
            try:
                query="INSERT INTO 'membros' (membro_name, membro_phone) VALUES(?,?)"
                cur.execute(query, (name, phone))
                con.commit()
                messagebox.showinfo("Sucesso", "Usuario adicionado com sucesso!", icon='info')
            except:
                messagebox.showerror("Error","Não foi possível adicionar o membro", icon='warning')
        else:
            messagebox.showerror("Error", "Preencha todos os campos!", icon='warning')