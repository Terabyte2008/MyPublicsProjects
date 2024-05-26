from customtkinter import CTk
from interface import Janela
from functions import Services

class Application:
    def __init__(self, root) -> None:
        self.root = root
        self.gui = Janela(self.root)  # Inicializa a interface gráfica
        self.data = Services(self.gui.frames)  # Inicializa as funcionalidades

        # Cria a janela e realiza as operações necessárias
        self.gui.janela_configs()
        self.data.monta_tabela()  # Cria a tabela no banco de dados, se necessário
        self.data.select_lista()  # Atualiza a lista de clientes na interface
        self.root.mainloop()

# Cria a instância da janela principal e executa o programa
if __name__ == "__main__":
    root = CTk()
    app = Application(root)
