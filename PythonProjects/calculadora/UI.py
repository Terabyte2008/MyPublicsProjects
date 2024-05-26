from customtkinter import *


class Gui:
    def __init__(self, ) -> None:
        self.master = CTk()
        self.conta = StringVar()
        self.conta.set('0')
        self.top_layer()
        self.label_conta()
        self.label_botoes()
        self.botoes()
        self.master.mainloop()
    
    def top_layer(self) -> None:
        self.master.title("Calculadora")
        self.master.geometry("420x600")
        self.master.configure(background='#1A1A1A')
        self.master.resizable(True, True)
    
    def label_conta(self) -> None:
        self.frame1 = CTkFrame(self.master, fg_color='#000000')
        self.frame1.place(relx=0, rely=0, relwidth=1, relheight=0.23)

        self.interface = CTkEntry(self.frame1, textvariable=self.conta, font=('Arial', 60))
        self.interface.place(relx=0, rely=0, relwidth=1, relheight=1)

    def label_botoes(self) -> None:
        self.frame2 = CTkFrame(self.master, fg_color='#000000')
        self.frame2.place(relx=0, rely=0.230001, relwidth=1, relheight=1 )

    def botoes(self) -> None:
        buttons = [
            #('AC', 0.04, 0.04, 0.155), ('+/-', 0., 0.04, 0.155)
            ('C', 0, 1, 'C'), ('+/-', 1, 1, '*-1'), (' % ', 2, 1, '/100*'), (' / ', 3, 1, '/'),
            (' 7 ', 0, 2, '7' ), (' 8 ', 1, 2, '8'), (' 9 ', 2, 2, '9'), (' X ', 3, 2, '*'),
            (' 4 ', 0, 3, '4'), (' 5 ', 1, 3, '5'), (' 6 ', 2, 3, '6'), (' - ', 3, 3, '-'),
            (' 1 ', 0, 4, '1'), (' 2 ', 1, 4, '2'), (' 3 ', 2, 4, '3'), (' + ', 3, 4, '+'),
            (' 0 ', 0, 5, '0'), (' , ', 1, 5, '.'), (' = ', 3, 5, '=')

        ]
        cont = 1
        for (text, column, row, comm) in buttons:
            if cont % 4 == 0 or comm == '=':
                self.bt = CTkButton(self.frame2, text=text, fg_color='#FF7F00', hover_color='#8B4500', text_color='#F0FFFF', font=('Arial', 20), corner_radius=10000, width=40, height=60, command=lambda t=comm: self.on_click(t))
            else:
                self.bt = CTkButton(self.frame2, text=text, fg_color='#808080', hover_color='#2B2B2B', text_color='#000000', font=('Arial', 20), corner_radius=10000, width=40, height=60, command=lambda t=comm: self.on_click(t))
            #self.bt.place(relx=relx, rely=rely, relwidth=size, relheight=size)
            if column == 1:
                self.bt.grid(column=column, row=row, padx=(8), pady=(8))  # Adiciona uma margem à esquerda para a primeira coluna
            else:
                self.bt.grid(column=column, row=row, padx=5, pady=5)
            cont += 1

    def on_click(self, char: str) -> str:
        if char == 'C':
            self.conta.set("0")
        
        elif char == '=':
            result = eval(self.conta.get())
            self.conta.set(str(result))
        else:
            if self.conta.get() == "0":
                self.conta.set(char)
            else:
                self.conta.set(self.conta.get() + char)
        


