from tkinter .ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
from os.path import exists

from PIL import Image, ImageTk
import pandas as pd

# Cores
co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # Azul-bg
co4 = "#87CEEB" # Azul claro

# Criando janela

janela = Tk()
janela.title("")
janela.geometry('770x330')
janela.configure(background='')
janela.resizable(width=False,height=False)

style = Style(janela)
style.theme_use("clam")

#
# Criando arquivo csv
list_header = ['Nome','Apelido','Endereço','Email','Telefone']
if exists("./projeto_integrado/usuarios.csv") == False:
        with open('./projeto_integrado/usuarios.csv', 'w',newline="", encoding='utf-8') as csvfile:   
            # creating a csv writer object   
            csvwriter = csv.writer(csvfile)   
                
            # writing the fields   
            csvwriter.writerow(list_header)
    

# Frames
#Posição do Header do programa.
frameTopo = Frame(janela,width=770, height=50,bg=co2,relief='flat')
frameTopo.grid(row=0, column=0, columnspan=2, sticky='NSEW')

#Posição do Menu.
frameEsquerda = Frame(janela,width=150, height=265,bg=co3,relief='solid')
frameEsquerda.grid(row=1, column=0, sticky='NSEW')

#Posição das informações gerais do programa.
frameDireita = Frame(janela,width=600, height=265,bg=co1,relief='raised')
frameDireita.grid(row=1, column=1, sticky='NSEW')

# Logo <a target="_blank" href="https://icons8.com/icon/43130/book-shelf">Book Shelf</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>

# Logo do aplicativo.
app_img = Image.open('./projeto_integrado/icons/logo.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

# Posicionando o logo.
app_logo = Label(frameTopo, image=app_img, width=50, compound=LEFT, padx=5, anchor=NW,bg=co2)
app_logo.place(x=5, y=0)

# Posicioando o título.
app_ = Label(frameTopo, text="Sistema de Gerenciamento de Biblioteca", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'),bg=co2, fg=co0)
app_.place(x=50, y=7)

# Novo usuario
def novo_usuario():
    global img_salvar

    def add():
        # Entrada de informações novo usuario
        name = _nome_entry.get()
        apelido = _apelido_entry.get()
        email = _email_entry.get()
        telefone = _telefone_entry.get()
        endereco = _endereco_entry.get()
        
        # Armazena os dados em uma lista temporária
        Lista = [name, apelido, email, telefone, endereco]

        # Exibe um erro caso o usuario não preencha todos os campos.
        for i in Lista:
            if i == '':
                messagebox.showerror("Erro", "Preencha todos os campos")
                break
        # Mostra sucesso caso o usuário consiga se cadastrar.
        messagebox.showinfo("Sucesso", "Usuario cadastrado com sucesso!")

        # Impede que um usuário seja cadastrado duas vezes.
        df = pd.read_csv("./projeto_integrado/usuarios.csv", encoding='utf-8')
        if (df == name).any().any():
            print("Usuário já cadastrado.")
        # Cadastro do usuario no arquivo csv.
        else:
            with open('./projeto_integrado/usuarios.csv', 'a',newline="", encoding='utf-8') as csvfile:   
                # creating a csv writer object
                dict = {}
                for i,j in enumerate(list_header):
                    dict.update({j:Lista[i]})
                    print(dict)   
                print(dict) 
                csvwriter = csv.DictWriter(csvfile, fieldnames=list_header)
                csvwriter.writerow(dict)

        _nome_entry.delete(0,END)
        _apelido_entry.delete(0,END)
        _email_entry.delete(0,END)
        _telefone_entry.delete(0, END)
        _endereco_entry.delete(0, END)

    # Grid de entradas 
    app_ = Label(frameDireita, text="Cadastro Novo Usuário", width=50, compound=LEFT,padx=5,pady=10,font=('Verdana 12'),bg=co1,fg=co0)
    app_.grid(row=0, column=0 , columnspan=4, sticky=NSEW)

    app_linha = Label(frameDireita, width=600,height=1, anchor=NW,font=('Verdana 1'), bg=co3,fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    _nome_label = Label(frameDireita, text="Nome", anchor=NW, font=("Ivy 10"), bg=co1, fg=co0)
    _nome_label.grid(row=2,column=0,padx=5,pady=5,sticky=NSEW)
    _nome_entry = Entry(frameDireita, width=25,justify="left", relief='solid')
    _nome_entry.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    _apelido_label = Label(frameDireita, text="Apelido", anchor=NW, font=("Ivy 10"), bg=co1, fg=co0)
    _apelido_label.grid(row=3,column=0,padx=5,pady=5,sticky=NSEW)
    _apelido_entry = Entry(frameDireita, width=25,justify="left", relief='solid')
    _apelido_entry.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)
        
    _email_label = Label(frameDireita, text="Email", anchor=NW, font=("Ivy 10"), bg=co1, fg=co0)
    _email_label.grid(row=4,column=0,padx=5,pady=5,sticky=NSEW)
    _email_entry = Entry(frameDireita, width=25,justify="left", relief='solid')
    _email_entry.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    _telefone_label = Label(frameDireita, text="Telefone", anchor=NW, font=("Ivy 10"), bg=co1, fg=co0)
    _telefone_label.grid(row=5,column=0,padx=5,pady=5,sticky=NSEW)
    _telefone_entry = Entry(frameDireita, width=25,justify="left", relief='solid')
    _telefone_entry.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    _endereco_label = Label(frameDireita, text="Endereço", anchor=NW, font=("Ivy 10"), bg=co1, fg=co0)
    _endereco_label.grid(row=6,column=0,padx=5,pady=5,sticky=NSEW)
    _endereco_entry = Entry(frameDireita, width=25,justify="left", relief='solid')
    _endereco_entry.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

        # Botão para salvar
    img_salvar = Image.open('./projeto_integrado/icons/add-book.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    botao_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT,width=100, anchor=NW, text='    Salvar', bg=co4,fg=co0, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    botao_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

def ver_usuarios():

    global treeview

    app_ = Label(frameDireita,text="Todos os usuários do banco de dados",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=co1, fg=co0)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=600, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)
        
    df = pd.read_csv("./projeto_integrado/usuarios.csv").transpose()

    mydict = {}
    
    for column in df:
        mydict[column] = [i for i in df[column]]

    treeview = ttk.Treeview(frameDireita, selectmode='extended', columns=list_header, show='headings')

    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=treeview.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=treeview.xview)

    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    treeview.grid(column=0, row=2, sticky='nsew')
    

    for col in list_header:
        treeview.heading(col, text=col, anchor='nw')
        treeview.column(col,width=80,anchor='nw')

    for i in range(len(df.columns)):
        treeview.insert(
            "",
            END,
            text=df.columns[i],
            values=(mydict[df.columns[i]])
        )


# Funções Menu

def control(i):
    # novo usuario
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        novo_usuario()

    # ver usuarios
    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_usuarios()

# Menu

# Novo Usuario
usuario_img = Image.open('./projeto_integrado/icons/user.png')
usuario_img = usuario_img.resize((18,18))
usuario_img = ImageTk.PhotoImage(usuario_img)
botao_usuario = Button(frameEsquerda, command=lambda: control('novo_usuario'), image=usuario_img, compound=LEFT, anchor=NW, text='Novo Usuario', bg=co4,fg=co0, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# Novo Livro
novo_livro_img = Image.open('./projeto_integrado/icons/add-book.png')
novo_livro_img = novo_livro_img.resize((18,18))
novo_livro_img = ImageTk.PhotoImage(novo_livro_img)
botao_novo_livro = Button(frameEsquerda, image=novo_livro_img, compound=LEFT, anchor=NW, text='Novo Livro', bg=co4,fg=co0, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Ver Livros
ver_livros_img = Image.open('./projeto_integrado/icons/stack-book.png')
ver_livros_img = ver_livros_img.resize((18,18))
ver_livros_img = ImageTk.PhotoImage(ver_livros_img)
botao_ver_livro = Button(frameEsquerda, image=ver_livros_img, compound=LEFT, anchor=NW, text='Livros Disponiveis', bg=co4,fg=co0, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# Ver Usuarios
ver_usuarios_img = Image.open('./projeto_integrado/icons/find-users.png')
ver_usuarios_img = ver_usuarios_img.resize((18,18))
ver_usuarios_img = ImageTk.PhotoImage(ver_usuarios_img)
botao_ver_usuario = Button(frameEsquerda, command=lambda: control('ver_usuarios'), image=ver_usuarios_img, compound=LEFT, anchor=NW, text='Usuarios cadastrados', bg=co4,fg=co0, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

# Fazer um Emprestimo
emprestimo_img = Image.open('./projeto_integrado/icons/borrow-book.png')
emprestimo_img = emprestimo_img.resize((18,18))
emprestimo_img = ImageTk.PhotoImage(emprestimo_img)
botao_emprestimo = Button(frameEsquerda, image=emprestimo_img, compound=LEFT, anchor=NW, text='Emprestar um livro', bg=co4,fg=co0, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Devolver um livro Emprestado
devolver_img = Image.open('./projeto_integrado/icons/return-book.png')
devolver_img = devolver_img.resize((18,18))
devolver_img = ImageTk.PhotoImage(devolver_img)
botao_devolver = Button(frameEsquerda, image=devolver_img, compound=LEFT, anchor=NW, text='Devolver um livro', bg=co4,fg=co0, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_devolver.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# Livros emprestados
emprestado_img = Image.open('./projeto_integrado/icons/books-2.png')
emprestado_img = emprestado_img.resize((18,18))
emprestado_img = ImageTk.PhotoImage(emprestado_img)
botao_emprestado = Button(frameEsquerda, image=emprestado_img, compound=LEFT, anchor=NW, text='Livros emprestados', bg=co4,fg=co0, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_emprestado.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

janela.mainloop()