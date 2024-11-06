from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()

class ReturnBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Devolução de Livro")
        self.resizable(False,False)

        query = "SELECT borrow_id FROM emprestados"
        books = cur.execute(query).fetchall()
        borrow_list = []
        for book in books:
            borrow_list.append(str(book[0]))
        
        query2 = "SELECT DISTINCT bmembro_id FROM emprestados"
        members = cur.execute(query2).fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0]))
        

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
        heading= Label(self.topFrame,text='Devolução de livro', font='arial 22 bold', fg='#033f8a',bg='white')
        heading.place(x=290,y=60)

        ########################################################################################################
        # Entradas 

        # Livro
        self.book_name = StringVar()
        self.lbl_book = Label(self.bottomFrame, text='Livro: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_book.place(x=40,y=80)
        self.combo_book = ttk.Combobox(self.bottomFrame,textvariable=self.book_name)
        self.combo_book['values']=borrow_list
        self.combo_book.place(x=150, y=85)

        # Membro
        self.member_name = StringVar()
        self.lbl_member = Label(self.bottomFrame, text='Usuario: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_member.place(x=40,y=40)
        self.combo_membro = ttk.Combobox(self.bottomFrame,textvariable=self.member_name)
        self.combo_membro['values'] = member_list
        self.combo_membro.place(x=150, y=45)
        
        # Botão
        button = Button(self.bottomFrame, text='Devolver', command=self.returnBook)
        button.place(x=270,y=120)
    def returnBook(self):
        book_name = self.book_name.get()
        self.book_id=int(book_name.split('-')[0])

        member_name = self.member_name.get()

        if (book_name and member_name !=""):
            try:
                query="DELETE FROM 'emprestados' WHERE borrow_id=?"
                cur.execute(query,(book_name,member_name))
                con.commit()
                messagebox.showinfo("Sucesso!","Adcionado com sucesso a base de dados!", icon='info')
                cur.execute("UPDATE livros SET livro_status =? WHERE livro_id=?", (0,self.book_id))
                con.commit()
            except:
                messagebox.showerror("Error", "Não foi possível adicionar a base de dados!", icon='warning')
        else:
            messagebox.showerror("Error", "Todos os campos precisam estar preenchidos", icon='warning')