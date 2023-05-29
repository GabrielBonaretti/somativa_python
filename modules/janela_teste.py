import tkinter
from operator import itemgetter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from modules.banco import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from modules.extrair import Extrair

janela = Tk()


class Aplicacao:
    def __init__(self):
        self.lista_celulares = []
        self.lista_filtrada = []
        self.janela = janela

        # variaveis
        self.color_gray_dark = "#9c9a92"
        self.color_gray_light = "#bdbcb3"

        self.ordem_escolhida = ""
        self.loja_escolhida = ""
        self.modelo_escolhido = ""
        self.preco_max = 0

        self.lista_sites = ["Todos", "kalunga", "kabum"]
        self.lista_arquivos = ["", "xlsx", "csv"]
        self.lista_marcas = ["Todos", "Multi", "Nokia", "Samsung", "LG", "Apple", "Xiaomi", "Motorola"]
        self.lista_ordem = ["Nenhuma", "cres. ID", "decres. ID", "cres. Nome", "decres. Nome", "cres. Modelo",
                            "decres. Modelo", "cres. Preço", "decres. Preço"]

        # criando frames
        self.frame0 = Frame(self.janela, background=self.color_gray_dark)
        self.frame1 = Frame(self.janela, background=self.color_gray_dark)
        self.frame2 = Frame(self.janela, background=self.color_gray_dark)
        self.frame3 = Frame(self.janela, background=self.color_gray_dark)

        # criando botões
        self.btScraping = Button(self.frame1, text="Web Scraping no site", command=self.web_scraping)
        self.btBaixar = Button(self.frame1, text="Exportar aquivo", command=self.baixar)

        # criando combobox(dropbox)
        self.dropBoxModelo = ttk.Combobox(self.frame0, state="readonly", values=self.lista_marcas)
        self.dropBoxOrdenar = ttk.Combobox(self.frame0, state="readonly", values=self.lista_ordem)
        self.dropBoxLoja = ttk.Combobox(self.frame0, state="readonly", values=self.lista_sites)
        self.dropBoxArquivo = ttk.Combobox(self.frame1, state="readonly", values=self.lista_arquivos)

        # Escala
        def print_value(val):
            self.preco_max = val
            self.insert_tabela()

        self.escala = Scale(self.frame0, from_=0, to=5000, orient="horizontal", command=print_value)
        self.escala.set(5000)

        # Textos
        self.filtros = Label(self.frame0, text="Filtros: ", background=self.color_gray_dark, anchor="w")
        self.lojas = Label(self.frame0, text="Loja  ->", background=self.color_gray_dark, anchor="w")
        self.marca = Label(self.frame0, text="Marca ->", background=self.color_gray_dark, anchor="w")
        self.ordem = Label(self.frame0, text="Ordem ->", background=self.color_gray_dark, anchor="w")
        self.preco = Label(self.frame0, text="Preço Máx ->", background=self.color_gray_dark, anchor="w")
        self.grafico = Label(self.frame3, text="Sem dados para o gráfico", background=self.color_gray_dark, anchor="w")

        # criando tabela
        self.tabelaJanela = ttk.Treeview(self.frame2, height=3,
                                         columns=(
                                             "coluna1",
                                             "coluna2",
                                             "coluna3",
                                             "coluna4"))

        # criando scrollbar
        self.scrollLista = Scrollbar(self.frame2, orient="vertical")

        self.tela()
        self.frames()
        self.botoes()
        self.comboBox()
        self.scale()
        self.textos()
        self.lista_frame2()
        self.grafic()
        mainloop()

    def tela(self):
        self.janela.title("NETFLIX")
        self.janela.configure(background=self.color_gray_light)
        self.janela.geometry("700x750")
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=500)

    def frames(self):
        self.frame0.place(relheight=0.15, relwidth=0.58, relx=0.03, rely=0.03)
        self.frame1.place(relheight=0.15, relwidth=0.35, relx=0.62, rely=0.03)
        self.frame2.place(relheight=0.30, relwidth=0.94, relx=0.03, rely=0.22)
        self.frame3.place(relheight=0.415, relwidth=0.94, relx=0.03, rely=0.56)

    def botoes(self):
        self.btScraping.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.375)
        self.btBaixar.place(relx=0.05, rely=0.525, relwidth=0.5, relheight=0.375)

    def comboBox(self):
        # DropBox da loja, junto com o get do valor quando há um evento (alteração)
        self.dropBoxLoja.place(relx=0.2, rely=0.35, relheight=0.2, relwidth=0.25)

        def value_change_loja(event):
            self.loja_escolhida = self.dropBoxLoja.get()
            self.insert_tabela()

        self.dropBoxLoja.bind('<<ComboboxSelected>>', value_change_loja)

        # DropBox do modelo dos celulares, junto com o get do valor quando há um evento (alteração)
        self.dropBoxModelo.place(relx=0.2, rely=0.7, relheight=0.2, relwidth=0.25)

        def value_change_modelo(event):
            self.modelo_escolhido = self.dropBoxModelo.get()
            self.insert_tabela()

        self.dropBoxModelo.bind('<<ComboboxSelected>>', value_change_modelo)

        # DropBox da loja, junto com o get do valor quando há um evento (alteração)
        self.dropBoxOrdenar.place(relx=0.7, rely=0.7, relheight=0.2, relwidth=0.25)

        def value_change_ordem(event):
            self.ordem_escolhida = self.dropBoxOrdenar.get()
            self.insert_tabela()

        self.dropBoxOrdenar.bind('<<ComboboxSelected>>', value_change_ordem)

        # DropBox da loja, junto com o get do valor quando há um evento (alteração)
        self.dropBoxArquivo.place(relx=0.6, rely=0.525, relheight=0.375, relwidth=0.35)


    def scale(self):
        self.escala.place(relx=0.7, rely=0.275, relheight=0.35, relwidth=0.25)

    def textos(self):
        self.filtros.place(relx=0.05, rely=0.1, relheight=0.2, relwidth=0.2)

        self.lojas.place(relx=0.05, rely=0.35, relheight=0.2, relwidth=0.15)
        self.preco.place(relx=0.50, rely=0.35, relheight=0.2, relwidth=0.20)

        self.marca.place(relx=0.05, rely=0.7, relheight=0.2, relwidth=0.15)
        self.ordem.place(relx=0.55, rely=0.7, relheight=0.2, relwidth=0.15)

        self.grafico.place(relx=0.4, rely=0.35, relheight=0.3, relwidth=0.25)

    def lista_frame2(self):
        self.tabelaJanela.heading("#0", text="ID")
        self.tabelaJanela.heading("#1", text="Nome")
        self.tabelaJanela.heading("#2", text="Modelo")
        self.tabelaJanela.heading("#3", text="Preço")
        self.tabelaJanela.heading("#4", text="Loja")

        self.tabelaJanela.column("#0", width=60)
        self.tabelaJanela.column("#1", width=370)
        self.tabelaJanela.column("#2", width=60)
        self.tabelaJanela.column("#3", width=60)
        self.tabelaJanela.column("#4", width=60)

        self.tabelaJanela.place(relx=0.025, rely=0.097, relwidth=0.927, relheight=0.809)

        self.tabelaJanela.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.95, rely=0.1, relwidth=0.025, relheight=0.8)
        self.scrollLista.config(command=self.tabelaJanela.yview)

    def web_scraping(self):
        try:
            self.escala.set(5000)
            self.dropBoxOrdenar.set("")
            self.dropBoxLoja.set("")
            self.dropBoxModelo.set("")
            self.dropBoxArquivo.set("")
            deletar_tabela(self.loja_escolhida)
            criar_tabela(self.loja_escolhida)
            self.tabelaJanela.delete(*self.tabelaJanela.get_children())
            self.ordem_escolhida = ""
            self.loja_escolhida = ""
            self.modelo_escolhido = ""
        except:
            showinfo(title='Error', message='Preencha o campo da loja.')

    def insert_tabela(self):
        self.lista_celulares.clear()

        if self.loja_escolhida == "Todos":
            try:
                lista_kalunga = ler_lista("kalunga")
                for i in lista_kalunga:
                    self.lista_celulares.append(i)
            except:
                pass

            try:
                lista_kabum = ler_lista("kabum")
                for j in lista_kabum:
                    self.lista_celulares.append(j)
            except:
                pass
        elif self.loja_escolhida == "kalunga":
            self.lista_celulares = ler_lista("kalunga")
        elif self.loja_escolhida == "kabum":
            self.lista_celulares = ler_lista("kabum")
        else:
            pass

        lista_ordenada = self.ordenar_lista()
        self.tabelaJanela.delete(*self.tabelaJanela.get_children())

        for i in lista_ordenada:
            if (self.modelo_escolhido in i or self.modelo_escolhido == "Todos") and (float(self.preco_max) >= float(i[3])):
                self.tabelaJanela.insert('', tkinter.END, values=[i[1], i[2], i[3], i[4]], text=i[0])
                self.lista_filtrada.append(i)

        self.grafic()

    def ordenar_lista(self):
        try:
            index = self.lista_ordem.index(self.ordem_escolhida)
        except:
            index = 0

        if index == 0:
            return self.lista_celulares
        elif index == 1:
            return sorted(self.lista_celulares[0:], key=itemgetter(0))
        elif index == 2:
            return sorted(self.lista_celulares[0:], key=itemgetter(0), reverse=True)
        elif index == 3:
            return sorted(self.lista_celulares[0:], key=itemgetter(1))
        elif index == 4:
            return sorted(self.lista_celulares[0:], key=itemgetter(1), reverse=True)
        elif index == 5:
            return sorted(self.lista_celulares[0:], key=itemgetter(2))
        elif index == 6:
            return sorted(self.lista_celulares[0:], key=itemgetter(2), reverse=True)
        elif index == 7:
            return sorted(self.lista_celulares[0:], key=itemgetter(3))
        elif index == 8:
            return sorted(self.lista_celulares[0:], key=itemgetter(3), reverse=True)
        else:
            print("erro")

    def grafic(self):
        precos = []
        celulares = []

        fig = plt.figure(figsize=(11, 4), dpi=50)
        ax = fig.add_subplot(111)

        canva = FigureCanvasTkAgg(fig, self.janela)
        canva.get_tk_widget().place(relheight=0.415, relwidth=0.94, relx=0.03, rely=0.56)
        for i in self.lista_filtrada:
            precos.append(i[3])
            celulares.append(i[1])
        ax.bar(celulares, precos)

        ax.set_ylabel('quantidade')
        ax.set_title('números')
        self.lista_filtrada.clear()

    def baixar(self):
        lista_ids = []
        lista_nomes = []
        lista_marcas = []
        lista_precos = []
        lista_lojas = []

        for i in self.lista_filtrada:
            lista_ids.append(i[0])
            lista_nomes.append(i[1])
            lista_marcas.append(i[2])
            lista_precos.append(i[3])
            lista_lojas.append(i[4])

        pd = Extrair(lista_ids=lista_ids,
                    lista_nomes=lista_nomes,
                    lista_marcas=lista_marcas,
                    lista_precos=lista_precos,
                    lista_lojas=lista_lojas)
        
        if self.dropBoxArquivo.get() == "xlsx":
            pd.criar_excel()
        else:
            pd.criar_csv()



