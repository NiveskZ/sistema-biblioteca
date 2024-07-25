import tkinter as tk

import pandas as pd
import numpy as np

class EstanteLivros():

    def __init__(self, nome_livro: str, isbn: str,):
        self.nome_livro = nome_livro
        self.isbn = isbn

    def cadastro_livro(self):
        if self in self.livros:
            raise Exception("Livro ja está cadastrado")
        self.append(self)
    
    def remove_livros(self,nome_livro: str):
        self.nome_livro = self.remove(nome_livro)

    
class Usuario:

    def _init_(self, nome, identificacao, contato):

        self.nome = nome

        self.identificacao = identificacao

        self.contato = contato

    def cadastrar_usuario(biblioteca):

        nome = input("Digite o nome do usuário: ")

        identificacao = input("Digite o número de identificação do usuário: ")

        contato = input("Digite o contato do usuário: ")

        usuario = Usuario(nome, identificacao, contato)

        biblioteca.cadastrar_usuario(usuario)

        print("Usuário cadastrado com sucesso.")

class Biblioteca:

    def _init_(self):

        self.livros = []

        self.usuario = []

        self.emprestimo = []

Usuario.cadastrar_usuario(Biblioteca)