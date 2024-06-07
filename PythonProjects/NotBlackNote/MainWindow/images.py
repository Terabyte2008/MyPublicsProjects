from PIL import Image

class DarkTheme:

    def __init__(self) -> None:
        self.base_path = 'C:/Users/luizf/OneDrive/Anexos/Documentos/MeuProjetos/Python/Python/MeusProjetos/NotBlackNote/images/DarkTheme'
    
    def get_img(self, img_name: str) -> Image:
        final_path = str(self.base_path + '/' + img_name)
        image = Image.open(final_path)
        return image

class LightTheme:

    def __init__(self) -> None:
        self.base_path = 'C:/Users/luizf/OneDrive/Anexos/Documentos/MeuProjetos/Python/Python/MeusProjetos/NotBlackNote/images/LightTheme'
    
    def get_img(self, img_name: str) -> Image:
        final_path = str(self.base_path + '/' + img_name)
        image = Image.open(final_path)
        return image
