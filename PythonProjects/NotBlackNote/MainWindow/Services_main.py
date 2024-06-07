from data import Repository
from customtkinter import *

class Resouces_MainWindow:
    def __init__(self, ui) -> None:
        self.data = Repository
        self.obj = ui
        self.menu_style_aberto = False
        self.cat_fav_aberto = False
        self.tema_atual: str = self.obj.tema_atual

    def new_file(self) -> None:
        ...
    
    def new_note(self) -> None:

        tet = CTkLabel(self.obj.center_frame, width=160, height=160, text='Eu sou uma label')
        tet.pack(side=TOP,  padx=25, pady=15)
    
    def abrir_fechar_dark_style(self) -> None:
        if self.menu_style_aberto: 
            self.obj.menu_style.place(x=334, y=300)
            self.menu_style_aberto = False
        else:
            self.obj.menu_style.place(x=634, y=600)
            self.menu_style_aberto = True
    
    def change_color(self, color):
        if self.tema_atual == 'escuro':
            self.obj.color = color
            self.obj.master._fg_color = self.obj.color[2]

            self.obj.master.configure(fg_color=self.obj.color[2])
            self.obj.top_frame.configure(fg_color=self.obj.color[2])
            self.obj.center_frame.configure(fg_color=self.obj.color[2])
            self.obj.bt_menu.configure(fg_color=self.obj.color[2], hover_color=self.obj.color[0])
            self.obj.bt_org_list.configure(hover_color=self.obj.color[0])
            self.obj.bt_theme.configure(fg_color=self.obj.color[2], hover_color=self.obj.color[0])
            self.obj.bottom_frame.configure(fg_color=self.obj.color[1])
            self.obj.bt_novo.configure(fg_color=self.obj.color[0], hover_color=self.obj.color[0])
            self.obj.bt_catalogo.configure(fg_color=self.obj.color[1], hover_color=self.obj.color[0])
            self.obj.bt_busca.configure(fg_color=self.obj.color[1], hover_color=self.obj.color[0])
            self.obj.bt_favorito.configure(fg_color='white', hover_color=self.obj.color[0])
            self.obj.bt_style.configure(fg_color=self.obj.color[0], hover_color=self.obj.color[0])

            if color == self.obj.dark_theme['verde'] or color == self.obj.dark_theme['roxo']:
                novo_img = self.obj.dark.get_img('new3_icon.png')
                style_img = self.obj.dark.get_img('newstyle2_icon.png')
                if self.cat_fav_aberto:
                    fav_img = self.obj.dark.get_img('fav4_icon.png')
                else:
                    fav_img = self.obj.dark.get_img('fav3_icon.png')

            elif color == self.obj.dark_theme['azul']:
                novo_img = self.obj.dark.get_img('newb_icon.png')
                style_img = self.obj.dark.get_img('newstyleb_icon.png')
                if self.cat_fav_aberto:
                    fav_img = self.obj.dark.get_img('fav4b_icon.png')
                else:
                    fav_img = self.obj.dark.get_img('fav3b_icon.png')
            else:
                novo_img = self.obj.dark.get_img('new_icon.png')
                style_img = self.obj.dark.get_img('newstyle_icon.png')
                if self.cat_fav_aberto:
                    fav_img = self.obj.dark.get_img('fav2_icon.png')
                else:
                    fav_img = self.obj.dark.get_img('fav1_black_icon.png')

        elif self.tema_atual == 'claro':
            pass
                
        self.obj.bt_novo.configure(
            image=CTkImage(
                dark_image=novo_img,
                light_image=novo_img,
                size=(90, 90)
            )
        )
        self.obj.bt_favorito.configure(
            image=CTkImage(
                light_image=fav_img,
                dark_image=fav_img,
                size=(50, 50)
            )
        )
        self.obj.bt_style.configure(
            image=CTkImage(
                dark_image=style_img,
                light_image=style_img,
                size=(70, 70)
            )
        )
        