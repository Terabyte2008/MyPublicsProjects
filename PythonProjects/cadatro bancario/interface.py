from tkinter import ttk
from customtkinter import *
from functions import Services


class Frames:
    def __init__(self, root) -> None:
        self.root = root
        self.services = Services(self)
        self.criar_frame1()
        self.criar_botoes()
        self.criar_entries()
        self.criar_frame2()
        self.criar_lista()

    def criar_frame1(self) -> None:
        self.frame1 = CTkFrame(self.root,bg_color='#545454', border_color='#98F5FF', border_width=2)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.956, relheight=0.5)
    
    def criar_frame2(self) -> None:
        self.frame2 = CTkFrame(self.root,bg_color='#545454', border_color='#98F5FF', border_width=2)
        self.frame2.place(relx=0.02, rely=0.54, relwidth=0.956, relheight=0.44)

    def criar_botoes(self) ->None:
        self.bt_limpar = CTkButton(self.frame1, text="Limpar", corner_radius=10,
                                 border_color='#104E8B', border_width=2, command=self.services.limpa_cliente)
        self.bt_limpar.place(relx=0.05, rely=0.1, relwidth=0.1, relheight=0.1)

        self.bt_novo = CTkButton(self.frame1, text="Novo", corner_radius=10, 
                                 border_color='#104E8B', border_width=2, command=self.services.add_cliente)
        self.bt_novo.place(relx=0.15, rely=0.1, relwidth=0.1, relheight=0.1)

        self.bt_apagar = CTkButton(self.frame1, text="Apagar", corner_radius=10, 
                                 border_color='#104E8B', border_width=2, command=self.services.deleta_cliente)
        self.bt_apagar.place(relx=0.65, rely=0.1, relwidth=0.1, relheight=0.1)

        self.bt_buscar = CTkButton(self.frame1, text="Buscar", corner_radius=10, 
                                 border_color='#104E8B', border_width=2, command=self.services.busca_cliente)
        self.bt_buscar.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.1)

        self.bt_alterar = CTkButton(self.frame1, text="Alterar", corner_radius=10, 
                                 border_color='#104E8B', border_width=2, command=self.services.altera_cliente)
        self.bt_alterar.place(relx=0.85, rely=0.1, relwidth=0.1, relheight=0.1)

    def criar_entries(self) -> None:
        # Criação das entrys
        self.nome_entry = CTkEntry(self.frame1, placeholder_text="Nome...")
        self.nome_entry.place(relx=0.05, rely=0.29, relwidth=0.4, relheight=0.082)

        self.fone_entry = CTkEntry(self.frame1, placeholder_text="Telefone...")
        self.fone_entry.place(relx=0.05, rely=0.51, relwidth=0.14, relheight=0.082)

        self.nascimento_entry = CTkEntry(self.frame1, placeholder_text="Nascimento...")
        self.nascimento_entry.place(relx=0.25, rely=0.51, relwidth=0.14, relheight=0.082)

        self.rg_cnh_entry = CTkEntry(self.frame1, placeholder_text="RG ou CNH...")
        self.rg_cnh_entry.place(relx=0.72, rely=0.4, relwidth=0.16, relheight=0.082)

        self.endereco_entry = CTkEntry(self.frame1, placeholder_text="Endereço...")
        self.endereco_entry.place(relx=0.05, rely=0.4, relwidth=0.37, relheight=0.082)

        self.banco_entry = CTkEntry(self.frame1, placeholder_text="Banco...")
        self.banco_entry.place(relx=0.48, rely=0.29, relwidth=0.2, relheight=0.082)

        self.agencia_entry = CTkEntry(self.frame1, placeholder_text="Agência...")
        self.agencia_entry.place(relx=0.71, rely=0.29, relwidth=0.17, relheight=0.082)

        self.conta_entry = CTkEntry(self.frame1, placeholder_text="Conta...")
        self.conta_entry.place(relx=0.48, rely=0.51, relwidth=0.14, relheight=0.082)

        self.codigo_entry = CTkEntry(self.frame1, placeholder_text="codigo...")
        self.codigo_entry.place(relx=0.27, rely=0.105, relwidth=0.16, relheight=0.082)

        self.ult_op_entry = CTkEntry(self.frame1, placeholder_text="Ultima Operação...")
        self.ult_op_entry.place(relx=0.72, rely=0.51, relwidth=0.16, relheight=0.082)

        self.cpf_entry = CTkEntry(self.frame1, placeholder_text="CPF...")
        self.cpf_entry.place(relx=0.48, rely=0.4, relwidth=0.16, relheight=0.082)
    
    def criar_lista(self) -> None:
        self.lista_clientes = ttk.Treeview(self.frame2,
                                           columns=('col0', 'col1', 'col2', 'col3', 
                                                    'col5', 'col6', 'col7', 
                                                    'col8', 'col9', 'col10', 'col11'))
        self.lista_clientes.heading('#0', text='')
        self.lista_clientes.heading("#1", text='Código')
        self.lista_clientes.heading("#2", text='Nome')
        self.lista_clientes.heading("#3", text='Endereço')
        self.lista_clientes.heading('#4', text='Ultima Operação')
        self.lista_clientes.heading("#5", text='Telefone')
        self.lista_clientes.heading("#6", text='Nascimento')
        self.lista_clientes.heading("#7", text='RG / CNH')
        self.lista_clientes.heading('#8', text='CPF')
        self.lista_clientes.heading("#9", text='Banco')
        self.lista_clientes.heading("#10", text='Agencia')
        self.lista_clientes.heading("#11", text='Conta')

        self.lista_clientes.column('#0', width=0)
        self.lista_clientes.column("#1", width=10)
        self.lista_clientes.column("#2", width=160)
        self.lista_clientes.column("#3", width=120)
        self.lista_clientes.column("#4", width=40)
        self.lista_clientes.column("#5", width=35)
        self.lista_clientes.column("#6", width=25)
        self.lista_clientes.column("#7", width=35)
        self.lista_clientes.column("#8", width=45)
        self.lista_clientes.column("#9", width=41)
        self.lista_clientes.column("#10", width=41)
        self.lista_clientes.column("#11", width=41)
        self.lista_clientes.place(relx=0.01, rely=0.05, relwidth=0.97, relheight=0.85)

        self.scroll_lista = CTkScrollbar(self.frame2, orientation='vertical')
        self.scroll_lista.configure(command=self.lista_clientes.yview)
        self.lista_clientes.configure(yscrollcommand=self.scroll_lista.set)
        self.scroll_lista.place(relx=0.98, rely=0.1, relwidth=0.02, relheight=0.85)
        self.lista_clientes.bind("<Double-1>", self.services.ondoubleclick)

class Janela:

    def __init__(self, root) -> None:
        self.root = root
        self.frames = Frames(self.root)
        self.janela_configs()
        

    def janela_configs(self) -> None:
        self.root.title("Cadastro de Pessoas")
        self.root.geometry("1200x630")
        self.root.configure(background='#1A1A1A')
        self.root.resizable(True, True)
        self.root.maxsize(width=1400, height=700)
        self.root.minsize(width=800, height=400)
    
    


