import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox as messagebox
from ttkbootstrap.widgets import DateEntry

import pywinstyles
from animal import Animal
import dashboard

from PIL import Image, ImageTk

recarregar = None

def adicionar_animal(recarregar_callback = None):
    # Criação da janela
    pop_up = ttk.Toplevel()
    pop_up.title("Zoológico - Adicionar Animal")
    pop_up.geometry("600x900")
    pop_up.resizable(True, True)

    pywinstyles.change_header_color(pop_up, "#f5f5f5") # Define a cor da barra de título da app

    # Define o ícone da janela
    pop_up.iconbitmap("img/zebra_icon.ico")
    pop_up.grab_set() # Torna o pop-up modal (impede interação com a janela principal)

    # Definir a imagem de fundo
    imagem = Image.open("img/#21dc00.png")
    bg_image = ImageTk.PhotoImage(imagem) 
    background = ttk.Label(pop_up, image=bg_image) 
    background.image = bg_image
    background.place(x=0, y=0, relwidth=1, relheight=1)
    background.lower()

    # Criar o frame principal dentro do pop-up
    frame = ttk.Frame(pop_up, padding=20, width=500, height=840)
    frame.pack(expand=True)
    frame.pack_propagate(0)

    cadastro = ["Apelido", "Espécie", "Nome Científico", "Peso", "Data de Nascimento", "Data de Chegada", "Dieta", "Rotina de Limpeza", "Recinto"]
    entrada = {}

    global recarregar
    recarregar = recarregar_callback

    ttk.Label(frame, text="Cadastro de Animais", font=("Arial", 16, "bold")).pack(pady=(0, 40))

    for i in cadastro:
        ttk.Label(frame, text=i).pack(anchor="w")
        if "Data" in i:
            entrada[i] = DateEntry(frame)
        else:
            entrada[i] = ttk.Entry(frame)
        entrada[i].pack(fill=X, pady=5)
    
    confirmar = ttk.Button(frame, text="Adicionar Animal", bootstyle="success", command=lambda: salvar_animal(entrada, pop_up))
    confirmar.pack(pady=20)

    def salvar_animal(entrada, pop_up):
        upload = []
        for i in cadastro:
            if "Data" in i:
                if not entrada[i].entry.get():
                    ttk.Label(frame, text=f"Preencha o campo: {i}", font=("Arial", 10),foreground="red")
                    return
            elif not entrada[i].get():
                ttk.Label(frame, text=f"Preencha o campo: {i}", font=("Arial", 10),foreground="red")
                return

            if "Data" in i:
                upload.append(entrada[i].get_date())
            elif "Peso" == i:
                try:
                    upload.append(float(entrada[i].get()))
                except ValueError:
                    print("")
            else:
                upload.append(entrada[i].get())
        
        upload = Animal.salvar_animal(upload[0], upload[1], upload[2], upload[3], upload[4], upload[5], upload[6], upload[7], upload[8])
        if upload == True:
            pop_up.destroy()
            if recarregar is not None:
                recarregar()
            else:
                print("Erro no Recarregamento automatico")