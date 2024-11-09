from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

from PIL import Image, ImageTk

import addbook,addmember,borrowbook,returnbook

con=sqlite3.connect('library.db')
cur=con.cursor()

class Main(object):
    def __init__(self, main) -> None:
        self.main = main

        def displayStatistics(evt):
            count_books = cur.execute("SELECT count(livro_id) FROM livros").fetchall()
            count_members = cur.execute("SELECT count(membro_id) FROM membros").fetchall()
            taken_books = cur.execute("SELECT count(livro_status) FROM livros WHERE livro_status=1").fetchall()

            self.lbl_book_count.config(text='Total: '+ str(count_books[0][0])+' Livros na biblioteca')
            self.lbl_member_count.config(text='Total usuarios: '+ str(count_members[0][0]))
            self.lbl_taken_count.config(text="Livros emprestados: "+str(taken_books[0][0]))
            displayBooks(self)

        def displayBooks(self):
            books = cur.execute("SELECT * FROM livros").fetchall()
            count = 0

            self.list_books.delete(0,'end')
            for book in books:
                self.list_books.insert(count, str(book[0])+ "-" +book[1])
                count += 1

            def bookInfo(evt):
                value=str(self.list_books.get(self.list_books.curselection()))
                id = value.split('-')[0]
                book = cur.execute("SELECT * FROM livros WHERE livro_id=?",(id,))
                book_info = book.fetchall()

                self.list_details.delete(0,'end')

                self.list_details.insert(0,"Nome do Livro: "+book_info[0][1])
                self.list_details.insert(1,"Autor: "+book_info[0][2])
                self.list_details.insert(2,"Páginas: "+book_info[0][3])
                self.list_details.insert(3,"Idioma: "+book_info[0][4])
                if book_info[0][5] == 0:
                    self.list_details.insert(4,"Status: Disponível")
                else:
                    self.list_details.insert(4,"Status: Emprestado")
            
            def doubleClick(evt):
                global borrown_id
                value = str(self.list_books.get(self.list_books.curselection()))
                borrown_id = value.split('-')[0]
                borrow_book = BorrowBook()
            # Adiciona duplo clique para que o livro seja emprestado.
            self.list_books.bind('<Double-Button-1>', doubleClick)
            # Faz com que atualize qualquer informação modificada.
            self.list_books.bind('<<ListboxSelect>>',bookInfo)
            self.tabs.bind('<<NotebookTabChanged>>', displayStatistics)

        #frames
        mainFrame = Frame(self.main)
        mainFrame.pack()
        #top frames
        topFrame = Frame(mainFrame, width=1350, height=70,bg='#f8f8f8',padx=20, relief=SUNKEN, borderwidth=2)
        topFrame.pack(side=TOP, fill=X)
        #center frame
        centerFrame = Frame(mainFrame, width=1350,relief=RIDGE,bg='#e0f0f0',height=680)
        centerFrame.pack(side=TOP)
        #center left frame
        centerLeftFrame = Frame(centerFrame, width=900, height=700, bg='#e0f0f0', borderwidth=2, relief=SUNKEN)
        centerLeftFrame.pack(side=LEFT)
        #ceter right frame
        centerRightFrame = Frame(centerFrame, width=450, height=700, bg='#e0f0f0', borderwidth=2, relief=SUNKEN)
        centerRightFrame.pack()

        #search bar
        search_bar = LabelFrame(centerRightFrame,width=440, height=75, text='Pesquisa', bg='#9bc9ff')
        search_bar.pack(fill=BOTH)
        self.lbl_search=Label(search_bar, text='Procurar: ',font='arial 12 bold', bg='#9bc9ff', fg='white')
        self.lbl_search.grid(row=0,column=0,padx=10,pady=10)
        self.ent_search=Entry(search_bar, width=30,bd=2)
        self.ent_search.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
        self.btn_search=Button(search_bar,text='Procurar', font='arial 12', bg='#fcc324',fg='white', command=self.searchBooks)
        self.btn_search.grid(row=0,column=4,padx=10,pady=10)
        #list bar
        list_bar =LabelFrame(centerRightFrame,width=440,height=175, text="List Box",bg='#fcc324')
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar,text='Ordernar por', font='times 16 bold', fg='#2488ff', bg='#fcc324')
        lbl_list.grid(row=0,column=2)
        self.listChoice=IntVar()
        rb1 = Radiobutton(list_bar,text='Todos os Livros', var=self.listChoice, value=1,bg='#fcc324')
        rb2 = Radiobutton(list_bar,text='Na Biblioteca', var=self.listChoice, value=2,bg='#fcc324')
        rb3 = Radiobutton(list_bar,text='Livros emprestados', var=self.listChoice, value=3,bg='#fcc324')
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btn_list = Button(list_bar,text='Listar livros', bg='#2488ff', fg='white', font='arial 12', command=self.listBooks)
        btn_list.grid(row=1, column=3, padx=10,pady=10)

        #Imagem e Título
        image_bar = Frame(centerRightFrame, width=440, height=350)
        image_bar.pack(fill=BOTH)
        self.title_right=Label(image_bar, text='Bem vindo!', font='arial 16 bold')
        self.title_right.grid(row=0)
        self.img_library = ImageTk.PhotoImage(Image.open('icons/bookshelf.jpg'))
        self.lblImg=Label(image_bar,image=self.img_library)
        self.lblImg.grid(row=1)


        ##############################################################################################
        #add book
        self.iconbook=PhotoImage(file="icons/add-book.png")
        self.btnbook=Button(topFrame, text='Novo Livro', image=self.iconbook, compound=LEFT,font='arial 12 bold',command=self.addBook)
        self.btnbook.pack(side=LEFT, padx=10)
        #add member button
        self.iconmember=PhotoImage(file='icons/user.png')
        self.btnmember=Button(topFrame, text='Novo Membro', font='arial 12 bold', padx=10, command=self.addMember)
        self.btnmember.configure(image=self.iconmember,compound=LEFT)
        self.btnmember.pack(side=LEFT)
        #borrow-book
        self.iconborrow=PhotoImage(file='icons/borrow-book.png')
        self.btnborrow=Button(topFrame,text='Emprestar Livro', font='arial 12 bold',padx=10, image=self.iconborrow, compound=LEFT, command=self.borrowBook)
        self.btnborrow.pack(side=LEFT)
        #return-book
        self.iconreturn=PhotoImage(file='icons/return-book.png')
        self.btnreturn=Button(topFrame,text='Devolver Livro', font='arial 12 bold',padx=10, image=self.iconreturn, compound=LEFT, command=self.returnBook)
        self.btnreturn.pack(side=LEFT)
        ###########################################################################################################

        # Abas
        self.tabs = ttk.Notebook(centerLeftFrame,width=900,height=660)
        self.tabs.pack()
        self.tab1_icon=PhotoImage(file='icons/stack-book.png')
        self.tab2_icon=PhotoImage(file='icons/books-2.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='Gerenciamento de biblioteca', image=self.tab1_icon, compound=LEFT)
        self.tabs.add(self.tab2, text='Estatísticas',image=self.tab2_icon,compound=LEFT)

        # Lista de Livros
        self.list_books = Listbox(self.tab1, width=40, height=30, bd=2, font='times 12 bold')
        self.sb=Scrollbar(self.tab1, orient=VERTICAL)
        self.list_books.grid(row=0,column=0,padx=(10,0),pady=10, sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=0,sticky=N+S+E)
        # Detalhes
        self. list_details = Listbox(self.tab1, width=80, height=30, bd=2, font='times 12 bold')
        self.list_details.grid(row=0,column=1,padx=(10,0), pady=10, sticky=N)

        # Estatistícas
        self.lbl_book_count = Label(self.tab2, text="test1", pady=20, font='verdanan 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count=Label(self.tab2, text="test2", pady=20, font='verdana 14 bold')
        self.lbl_member_count.grid(row=1,sticky=W)
        self.lbl_taken_count=Label(self.tab2,text="test3",pady=20,font='verdana 14 bold')
        self.lbl_taken_count.grid(row=2,sticky=W)
        
        # Funções
        displayBooks(self)
        displayStatistics(self)
    

    def searchBooks(self):
        value = self.ent_search.get()
        search = cur.execute("SELECT * FROM livros WHERE livro_name LIKE ?", ('%'+ value + '%',)).fetchall()
        self.list_books.delete(0,'end')
        count = 0
        for book in search:
            self.list_books.insert(count, str(book[0])+"-"+book[1])
            count += 1

    def listBooks(self):
        value = self.listChoice.get()
        if value == 1:
            allbooks = cur.execute("SELECT * FROM livros").fetchall()
            self.list_books.delete(0,"end")

            count = 0
            for book in allbooks:
                self.list_books.insert(count,str(book[0])+ "-"+book[1])
                count += 1
        elif value == 2:
            books_in_library = cur.execute("SELECT * FROM livros WHERE livro_status =?", (0,)).fetchall()
            self.list_books.delete(0,"end")

            count = 0
            for book in books_in_library:
                self.list_books.insert(count,str(book[0])+ "-"+book[1])
                count += 1
        else:
            taken_books= cur.execute("SELECT * FROM livros WHERE livro_status=?",(1,)).fetchall()
            self.list_books.delete(0,"end")

            count = 0
            for book in taken_books:
                self.list_books.insert(count,str(book[0])+ "-"+book[1])
                count += 1

    def addBook(self):
        add=addbook.AddBook()
    def addMember(self):
        member = addmember.AddMember()
    def borrowBook(self):
        borrow_book = borrowbook.BorrowBook()
    def returnBook(self):
        return_book = returnbook.ReturnBook()

class BorrowBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Emprestar Livro")
        self.resizable(False,False)

        global borrown_id
        self.book_id=int(borrown_id)
        query = "SELECT * FROM livros WHERE livro_status=0"
        books = cur.execute(query).fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0])+"-"+book[1])
        
        query2 = "SELECT * FROM membros"
        members = cur.execute(query2).fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0])+"-"+member[1])

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
        heading= Label(self.topFrame,text='Empréstimo de livro', font='arial 22 bold', fg='#033f8a',bg='white')
        heading.place(x=290,y=60)

        ########################################################################################################
        # Entradas 

        # Livro
        self.book_name = StringVar()
        self.lbl_book = Label(self.bottomFrame, text='Livro: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_book.place(x=40,y=40)
        self.combo_book = ttk.Combobox(self.bottomFrame,textvariable=self.book_name)
        self.combo_book['values']=book_list
        self.combo_book.current(self.book_id-1)
        self.combo_book.place(x=150, y=45)

        # Membro
        self.member_name = StringVar()
        self.lbl_member = Label(self.bottomFrame, text='Usuario: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_member.place(x=40,y=80)
        self.combo_membro = ttk.Combobox(self.bottomFrame,textvariable=self.member_name)
        self.combo_membro['values'] = member_list
        self.combo_membro.place(x=150, y=85)
        
        # Botão
        button = Button(self.bottomFrame, text='Emprestar', command=self.lendBook)
        button.place(x=270,y=120)
    def lendBook(self):
        book_name = self.book_name.get()
        member_name = self.member_name.get()

        if (book_name and member_name !=""):
            try:
                query="INSERT INTO 'emprestados' (blivro_id,bmembro_id) VALUES(?,?)"
                cur.execute(query,(book_name,member_name))
                con.commit()
                messagebox.showinfo("Sucesso!","Adcionado com sucesso a base de dados!", icon='info')
                cur.execute("UPDATE livros SET livro_status =? WHERE livro_id=?", (1,self.book_id))
                con.commit()
            except:
                messagebox.showerror("Error", "Não foi possível adicionar a base de dados!", icon='warning')
        else:
            messagebox.showerror("Error", "Todos os campos precisam estar preenchidos", icon='warning')
            
def main():
    root = Tk()
    app = Main(root)
    root.title("Sistema de gerenciamento de Bibliotecas")
    root.geometry("1450x750+350+200")
    # Colocando um icone na janela
    im = Image.open('icons/logo.png')
    photo = ImageTk.PhotoImage(im)
    root.wm_iconphoto(True, photo)
 
    root.mainloop()

if __name__ == '__main__':
    main()