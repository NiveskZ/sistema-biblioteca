from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import pandas as pd
import sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()

# query = """SELECT * FROM emprestados """
# df = pd.read_sql(query,con)


class ReturnBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        query = """SELECT * FROM emprestados """
        global df
        df = pd.read_sql(query,con)
        

        self.geometry("650x750+550+200")
        self.title("Devolução de Livro")
        self.resizable(False,False)
        
        books = df["blivro_id"]
        book_list = []
        for book in books:
            book_list.append(book)
        print(book_list)

        #####################################################################################

        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        # Bottom Frame
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)
        # Cabeçalho e imagem
        self.top_image = PhotoImage(file='icons/return-book.png')
        top_image_lbl = Label(self.topFrame,image=self.top_image, bg='white')
        top_image_lbl.place(x=120,y=10)
        heading= Label(self.topFrame,text='Devolução de livro', font='arial 22 bold', fg='#033f8a',bg='white')
        heading.place(x=290,y=60)

        ########################################################################################################
        # Entradas 

        # Livro
        self.borrow_name = StringVar()
        self.lbl_borrow = Label(self.bottomFrame, text='Livro: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_borrow.place(x=40,y=40)
        self.combo_borrow = ttk.Combobox(self.bottomFrame,textvariable=self.borrow_name)
        self.combo_borrow['values']=book_list
        self.combo_borrow.place(x=150, y=45)

        # Botão
        button = Button(self.bottomFrame, text='Devolver', command=self.returnBook)
        button.place(x=270,y=160)

    def returnBook(self):
        
        borrow_name = self.borrow_name.get()
        df2 = df.loc[df.blivro_id == borrow_name]['borrow_id']
        b_id = df2[0]
        
        borrow_id = int(borrow_name[0])       

        if (borrow_name !=""):
            try:
                query="DELETE FROM emprestados WHERE borrow_id={0}"
                cur.execute(query.format(b_id))
                con.commit()
                query2 = "UPDATE livros SET livro_status =? WHERE livro_id=?"
                cur.execute(query2, (0,borrow_id))
                con.commit()
                messagebox.showinfo("Sucesso!","O livro foi devolvido!", icon='info')
            except:
                messagebox.showerror("Error", "Não foi possível devolver o livro!", icon='warning')
        else:
            messagebox.showerror("Error", "Todos os campos precisam estar preenchidos", icon='warning')
        