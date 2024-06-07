from customtkinter import CTk
from MainWindow import GUI


class Application:

    def __init__(self, root) -> None:
        self.mainwindow = GUI.MainWindow
        self.mainwindow(root)


NotBlackNote = Application
master = CTk(fg_color='#0D0D0D')
if __name__ == '__main__':
    NotBlackNote(master)