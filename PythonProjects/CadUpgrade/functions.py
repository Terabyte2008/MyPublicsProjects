from PythonProjects.CadUpgrade.ApplicationProject.data import DataBase
from tkinter.constants import END

class Services(DataBase):

    def __init__(self, frames) -> None:
        super().__init__()
        self.frame = frames
    
    def variaveis(self):
        self.codigo = self.frame.codigo_entry.get()
        self.nascimento = self.frame.nascimento_entry.get()
        self.nome = self.frame.nome_entry.get()
        self.telefone = self.frame.fone_entry.get()
        self.endereco = self.frame.endereco_entry.get()
        self.banco = self.frame.banco_entry.get()
        self.agencia = self.frame.agencia_entry.get()
        self.rg_cnh = self.frame.rg_cnh_entry.get()
        self.conta = self.frame.conta_entry.get()
        self.ult_op = self.frame.ult_op_entry.get()

    def add_cliente(self):
        self.variaveis()
        self.connect()
        self.cursor.execute("""INSERT INTO cadastroclientes (nome_cliente, endereco, ult_op, telefone, 
                            nascimento, rg_cnh, banco, agencia, conta )
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
                            (self.nome, self.endereco, self.ult_op, self.telefone, self.nascimento, self.rg_cnh,
                             self.banco, self.agencia, self.conta))
        self.conn.commit()
        self.disconnect()
        self.select_lista()
        self.limpa_cliente()
        
    def select_lista(self):
        self.frame.lista_clientes.delete(*self.frame.lista_clientes.get_children())
        self.connect()
        lista = self.cursor.execute("""SELECT
                            cod, nome_cliente, endereco, ult_op, telefone,
                            nascimento, rg_cnh, banco, agencia, conta FROM cadastroclientes
                            ORDER BY nome_cliente ASC""")
        for row in lista:
            self.frame.lista_clientes.insert("", "end", values=row)
        self.disconnect()
        
    def limpa_cliente(self):
        self.frame.codigo_entry.delete(0, 'end')
        self.frame.nome_entry.delete(0, 'end')
        self.frame.fone_entry.delete(0, 'end')
        self.frame.endereco_entry.delete(0, 'end')
        self.frame.banco_entry.delete(0, 'end')
        self.frame.agencia_entry.delete(0, 'end')
        self.frame.conta_entry.delete(0, 'end')
        self.frame.rg_cnh_entry.delete(0, 'end')
        self.frame.nascimento_entry.delete(0, 'end')
        self.frame.ult_op_entry.delete(0, 'end')
        self.frame.criar_entries()

    def ondoubleclick(self, event):
        self.limpa_cliente()
        self.frame.lista_clientes.selection()

        for n in self.frame.lista_clientes.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = self.frame.lista_clientes.item(n, 'values')
            self.frame.codigo_entry.insert(END, col1)
            self.frame.nome_entry.insert(END, col2)
            self.frame.endereco_entry.insert(END, col3)
            self.frame.ult_op_entry.insert(END, col4)
            self.frame.fone_entry.insert(END, col5)
            self.frame.nascimento_entry.insert(END, col6)
            self.frame.rg_cnh_entry.insert(END, col7)
            self.frame.banco_entry.insert(END, col8)
            self.frame.agencia_entry.insert(END, col9)
            self.frame.conta_entry.insert(END, col10)

    def deleta_cliente(self):
        self.variaveis()
        self.connect()
        self.cursor.execute("""DELETE FROM cadastroclientes WHERE cod = ? """, (self.codigo,))
        self.conn.commit()
        self.disconnect()
        self.limpa_cliente()
        self.select_lista()

    def busca_cliente(self):
        self.connect()
        self.frame.lista_clientes.delete(*self.frame.lista_clientes.get_children())

        self.frame.nome_entry.insert(END, '%')
        nome = self.frame.nome_entry.get()
        self.cursor.execute("""SELECT cod, nome_cliente, 
                            telefone, nascimento, endereco, 
                            ult_op, banco, agencia, conta, rg_cnh
                            FROM cadastroclientes WHERE nome_cliente LIKE '%s'
                            ORDER BY nome_cliente ASC""" % nome)
        busca_nome = self.cursor.fetchall()
        for i in busca_nome:
            self.frame.lista_clientes.insert("", END, values=i)
        self.limpa_cliente()
        self.disconnect()
    
    def altera_cliente(self):
        self.variaveis()
        self.connect()
        self.cursor.execute(""" UPDATE cadastroclientes 
            SET nome_cliente = ?, telefone = ?, nascimento = ?, 
            endereco = ?, ult_op = ?, banco = ?, agencia = ?, 
            conta = ?, rg_cnh = ? WHERE cod = ?""", 
            (self.nome, self.telefone, self.nascimento, 
             self.endereco, self.ult_op, self.banco, self.agencia, 
             self.conta, self.rg_cnh, self.codigo))
        self.conn.commit()
        self.disconnect()
        self.select_lista()
        self.limpa_cliente()