from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()

class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Novo Livro")
        self.resizable(False, False)

        #####################################################################################

        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        # Bottom Frame
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)
        # Cabeçalho e imagem
        self.top_image = PhotoImage(file='icons/add-book.png')
        top_image_lbl = Label(self.topFrame,image=self.top_image, bg='white')
        top_image_lbl.place(x=120,y=10)
        heading= Label(self.topFrame,text='Adicionar Livro', font='arial 22 bold', fg='#033f8a',bg='white')
        heading.place(x=290,y=60)

        ########################################################################################################
        # Entradas 

        # Nome
        self.lbl_name = Label(self.bottomFrame, text='Nome: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40,y=40)
        self.ent_name=Entry(self.bottomFrame, width=30, bd=2)
        self.ent_name.insert(0, 'Digite o título do livro')
        self.ent_name.place(x=150,y=45)
        # Autor
        self.lbl_author = Label(self.bottomFrame, text='Autor: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_author.place(x=40,y=80)
        self.ent_author=Entry(self.bottomFrame, width=30, bd=2)
        self.ent_author.insert(0, 'Digite o autor do livro')
        self.ent_author.place(x=150,y=85)
        # Pages
        self.lbl_page = Label(self.bottomFrame, text='Paginas: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_page.place(x=40,y=120)
        self.ent_page=Entry(self.bottomFrame, width=30, bd=2)
        self.ent_page.insert(0, 'Digite quantas paginas tem o livro')
        self.ent_page.place(x=150,y=125)
        # Idioma
        self.lbl_language = Label(self.bottomFrame, text='Idioma: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_language.place(x=40,y=160)
        self.ent_language=Entry(self.bottomFrame, width=30, bd=2)
        self.ent_language.insert(0, 'Digite o idioma do livro')
        self.ent_language.place(x=150,y=165)
        # Botão
        button = Button(self.bottomFrame, text='Novo Livro', command=self.addBook)
        button.place(x=270,y=200)

    def addBook(self):
        name = self.ent_name.get()
        author = self.ent_author.get()
        page = self.ent_page.get()
        language = self.ent_language.get()

        if (name and author and page and language != ""):
            try:
                query="INSERT INTO 'livros' (livro_name, livro_author, livro_page, livro_language) VALUES(?,?,?,?)"
                cur.execute(query, (name, author, page, language))
                con.commit()
                messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!", icon='info')
            except:
                messagebox.showerror("Error","Não foi possível adicionar o livro", icon='warning')
        else:
            messagebox.showerror("Error", "Preencha todos os campos!", icon='warning')