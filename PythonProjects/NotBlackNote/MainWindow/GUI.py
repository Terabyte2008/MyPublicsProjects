from customtkinter import *
from MainWindow.Services_main import Resouces_MainWindow as rm
from MainWindow.images import DarkTheme, LightTheme



class MainWindow:
    
    def __init__(self, master) -> None:

        self.dark_theme = {
            'azul': ('#2507B3', '#0D0D0D', '#1A1A1A', '#0D0D0D'),
            'verde': ('chartreuse2', '#333333', '#242424', '#292421'),
            'roxo':  ('darkorchid', '#333333', '#242424', '#292421'),
            'aqua': ('springgreen2', 'black', '#0D0D0D', '#1A1A1A')
        }

        
        self.color = self.dark_theme["aqua"]
        self.tema_atual: str = 'escuro'
        
        self.master = master
        self.svc = rm(self)
        self.dark = DarkTheme()
        self.light = LightTheme()
        self.loading_screen()
        self.master.mainloop()

    def main_window(self) -> None:
        self.master.geometry('400x620')
        self.master.resizable(False, False)
        self.master.title("BlackNote Remake")
        self.master.anchor('center')
        self.frames_main_window()
    
    def loading_screen(self) -> None:
        self.splash = CTk()
        self.splash.geometry('500x500')
        self.splash.anchor('center')
        self.splash.after(50, self.main_window)

    def frames_main_window(self) -> None:
        self.top_frame = CTkFrame(self.master, fg_color=self.color[2], corner_radius=0)
        self.top_frame.place(relx=0, rely=0, relwidth=1, relheight=0.06)

        self.center_frame = CTkScrollableFrame(self.master, fg_color=self.color[2], corner_radius=0)
        self.center_frame.place(relx=0, rely=0.05, relwidth=1, relheight=0.98)

        self.bottom_frame = CTkFrame(self.master, fg_color=self.color[1], corner_radius=0)
        self.bottom_frame.place(relx=0, rely=0.92, relwidth=1, relheight=0.08)

        self.theme_frame = CTkFrame(self.master, fg_color='transparent', bg_color='transparent')
        self.theme_frame.place(relx=0.855, rely=0.85, relwidth=0.1, relheight=0.06)

        self.widgets_top()
        self.widgets_bottom()
        self.menu_troca_style()
    
    def widgets_top(self) -> None:
       
       org_list_dark_img = self.dark.get_img('org_icon.png')
       self.bt_org_list = CTkButton(
           master=self.top_frame,
           text='',
           fg_color='#1E1E1E',
           border_width=-80,
           border_spacing=0,
           corner_radius=0,
           round_height_to_even_numbers=False,
           round_width_to_even_numbers=False,
           image=CTkImage(
               light_image=org_list_dark_img, 
               dark_image=org_list_dark_img, 
               size=(30, 30)
               ),
           width=30,
           height=30,
           hover_color=self.color[0]
       )
       self.bt_org_list.place(relx=0.03, rely=0, relwidth=0.1, relheight=1)

       menu_img = self.dark.get_img('menusimples_icon.png')
       self.bt_menu = CTkButton(
           master=self.top_frame,
           text='',
           fg_color='transparent',
           border_width=-80,
           border_spacing=0,
           corner_radius=0,
           round_height_to_even_numbers=False,
           round_width_to_even_numbers=False,
           image=CTkImage(
               light_image=menu_img, 
               dark_image=menu_img, 
               size=(25, 25),
               ),
           width=25,
           height=25,
           hover_color=self.color[0]
       )
       self.bt_menu.place(relx=0.87, rely=0, relwidth=0.1, relheight=1)

       titulo_app = CTkLabel(
           master=self.top_frame,
           text='NotBlackNote',
           font=('Verdana', 20),
           text_color='white',

       )
       titulo_app.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.9)

    def widgets_bottom(self) -> None:
       novo_dark_img = self.dark.get_img('new_icon.png')
       self.bt_novo = CTkButton(
           master=self.bottom_frame,
           text='',
           fg_color=self.color[0],
           border_width=-80,
           border_spacing=0,
           corner_radius=0,
           round_height_to_even_numbers=False,
           round_width_to_even_numbers=False,
           image=CTkImage(
               light_image=novo_dark_img, 
               dark_image=novo_dark_img, 
               size=(90, 90)
               ),
           width=60,
           height=60,
           hover_color=self.color[0]
       )
       self.bt_novo.place(relx=0.432, rely=0, relwidth=0.14, relheight=1)

       catalogo_dark_img = self.dark.get_img('cat_icon.png')
       self.bt_catalogo = CTkButton(
           master=self.bottom_frame,
           text='',
           fg_color=self.color[1],
           border_width=-80,
           border_spacing=0,
           corner_radius=0,
           round_height_to_even_numbers=False,
           round_width_to_even_numbers=False,
           image=CTkImage(
               light_image=catalogo_dark_img, 
               dark_image=catalogo_dark_img, 
               size=(30, 30)
            ),
           width=30,
           height=30, 
           hover_color=self.color[0]
        )
       self.bt_catalogo.place(relx=0.02, rely=0.1, relwidth=0.1, relheight=0.8)

       busca_dark_img = self.dark.get_img('busca_icon.png')
       self.bt_busca = CTkButton(
           master=self.bottom_frame,
           text='',
           fg_color='transparent',
           border_width=-80,
           border_spacing=0,
           corner_radius=0,
           round_height_to_even_numbers=False,
           round_width_to_even_numbers=False,
           image=CTkImage(
               light_image=busca_dark_img, 
               dark_image=busca_dark_img, 
               size=(30, 30)
            ),
           width=30,
           height=30,
           hover_color=self.color[0]
        )
       self.bt_busca.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.8)

       favorito_dark_img = self.dark.get_img('fav1_black_icon.png')
       self.bt_favorito = CTkButton(
           master=self.bottom_frame,
           text='',
           fg_color='white',
           border_width=-80,
           border_spacing=0,
           corner_radius=0,
           round_height_to_even_numbers=False,
           round_width_to_even_numbers=False,
           image=CTkImage(
               light_image=favorito_dark_img, 
               dark_image=favorito_dark_img, 
               size=(50, 50)
            ),
           width=30,
           height=30,
           hover_color=self.color[0]
        )
       self.bt_favorito.place(relx=0.7, rely=0.1, relwidth=0.11, relheight=0.8)

       style_dark_img = self.dark.get_img('newstyle_icon.png')
       self.bt_style = CTkButton(
           master=self.bottom_frame,
           text='',
           fg_color=self.color[0],
           border_width=-80,
           border_spacing=0,
           corner_radius=0,
           round_height_to_even_numbers=False,
           round_width_to_even_numbers=False,
           image=CTkImage(
               light_image=style_dark_img, 
               dark_image=style_dark_img, 
               size=(70, 70)
            ),
           width=70,
           height=70,
           hover_color=self.color[0],
           command=self.svc.abrir_fechar_dark_style
        )
       self.bt_style.place(relx=0.85, rely=0.1, relwidth=0.11, relheight=0.8)
       

       theme_img = self.dark.get_img('theme_dark.png')
       self.bt_theme = CTkButton(
            master=self.theme_frame,
            text='',
            round_height_to_even_numbers=False,
            round_width_to_even_numbers=False,
            corner_radius=0,
            border_width=-80,
            border_spacing=0,
            fg_color='transparent',
            bg_color='transparent',
            image=CTkImage(
                light_image=theme_img,
                dark_image=theme_img,
                size=(60, 60)
            ),
            width=30,
            height=30,
           hover_color=self.color[0]
       )
       self.bt_theme.place(relx=0, rely=0, relwidth=1, relheight=1)

    def menu_troca_style(self)  -> None:
        
        self.menu_style = CTkFrame(
            master=self.master,
            bg_color='transparent',
            fg_color='black',
            corner_radius=10000,
            width=50,
            height=220,
        )
        self.menu_style.place(x=634, y=600)

       

        azul_img = self.dark.get_img('style_icon.png')
        bt_azul = CTkButton(
            master=self.menu_style,
            text='',
            image=CTkImage(
                dark_image=azul_img,
                light_image=azul_img,
                size=(60, 60),
            ),
            width=30,
            height=30,
            round_height_to_even_numbers=False,
            round_width_to_even_numbers=False,
            fg_color=self.dark_theme['azul'][0],
            border_spacing=0,
            border_width=-800,
            corner_radius=0,
            command=lambda: self.svc.change_color(self.dark_theme['azul'])
        )
        bt_azul.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.16)

        verde_img = self.dark.get_img('style_icon.png')
        bt_verde = CTkButton(
            master=self.menu_style,
            text='',
            image=CTkImage(
                dark_image=verde_img,
                light_image=verde_img,
                size=(60, 60),
            ),
            width=30,
            height=30,
            round_height_to_even_numbers=False,
            round_width_to_even_numbers=False,
            fg_color=self.dark_theme['verde'][0],
            border_spacing=0,
            border_width=-800,
            corner_radius=0,
            command=lambda: self.svc.change_color(self.dark_theme['verde'])
        )
        bt_verde.place(relx=0.15, rely=0.28, relwidth=0.7, relheight=0.16)

        roxo_img = self.dark.get_img('style_icon.png')
        bt_roxo = CTkButton(
            master=self.menu_style,
            text='',
            image=CTkImage(
                dark_image=roxo_img,
                light_image=roxo_img,
                size=(60, 60),
            ),
            width=30,
            height=30,
            round_height_to_even_numbers=False,
            round_width_to_even_numbers=False,
            fg_color=self.dark_theme['roxo'][0],
            border_spacing=0,
            border_width=-800,
            corner_radius=0,
            command=lambda: self.svc.change_color(self.dark_theme['roxo'])
        )
        bt_roxo.place(relx=0.15, rely=0.52, relwidth=0.7, relheight=0.16)

        aqua_img = self.dark.get_img('style_icon.png')
        bt_aqua = CTkButton(
            master=self.menu_style,
            text='',
            image=CTkImage(
                dark_image=aqua_img,
                light_image=aqua_img,
                size=(60, 60),
            ),
            width=30,
            height=30,
            round_height_to_even_numbers=False,
            round_width_to_even_numbers=False,
            fg_color=self.dark_theme['aqua'][0],
            border_spacing=0,
            border_width=-800,
            corner_radius=0,
            command=lambda: self.svc.change_color(self.dark_theme['aqua'])
        )
        bt_aqua.place(relx=0.15, rely=0.75, relwidth=0.7, relheight=0.16)

    

