# Tenta importar o módulo ttkbootstrap para criar a interface
try: 
    import ttkbootstrap as ttk
    from ttkbootstrap.constants import *
except Exception: # Se não conseguir, avisa o usuário para instalar as dependências
    print("Módulo 'ttkbootstrap' não encontrado. Execute: pip install -r requisitos.txt")
    raise # Levanta o erro novamente para mostrar a mensagem completa

# Tenta importar o módulo Pillow para manipulação de imagens
try:
    from PIL import Image, ImageTk
except Exception:
    print("Pillow (PIL) não encontrado. Execute: pip install -r requisitos.txt")
    raise

import pywinstyles # Esse aq é para mudar a cor da barra de título no Windows
from ttkbootstrap.dialogs import Messagebox as messagebox # Para exibir as mensagens de alerta

from usuario import Usuario # Importa a classe Usuario do arquivo usuario.py
import dashboard


ent_nome = None
ent_senha = None
ent_email = None

# 1. Abrir a app e definir as propriedades
app = ttk.Window(themename="litera", resizable=(True, True)) # Escolha um tema, ex: 'cosmo', 'darkly', 'superhero'
app.title("Zoológico - Login")
app.geometry("700x500") # Largura x Altura

imagem = Image.open("img/#21dc00.png")
# converte imagem para um formato que o Tkinter usa
app.bg_image = ImageTk.PhotoImage(imagem) 

background = ttk.Label(app, image=app.bg_image)
background.place(x=0, y=0, relwidth=1, relheight=1) # Relwidth e relheight fazem a imagem preencher toda a janela
background.lower()
# app.config(bg="#21dc00") #Cor Background

pywinstyles.change_header_color(app, "#f5f5f5") # Define a cor da barra de título da app
app.iconbitmap("img/zebra_icon.ico") # Define o ícone da janela

# Ajuste de acordo com o tamanho da janela

frame = ttk.Frame(app, padding=30)
frame.pack(expand=True) # Centraliza o frame na janela

def fazer_login():
    nome = ent_nome.get() # Pega o valor do campo nome e senha
    senha = ent_senha.get()

    usuario = Usuario.autenticar(nome, senha)   

    if not nome or not senha:
        messagebox.show_warning("Preencha todos os campos", "Aviso", parent=app, alert=True)
        return

    if usuario:
        messagebox.show_info("Login realizado com sucesso!", "Sucesso", parent=app, alert=True)
        app.withdraw() # Fecha a janela de login

        dashboard.abrir(usuario, app) # Passa a janela principal como parâmetro
        
    else:
        messagebox.show_error("Usuário ou senha inválidos", "Erro", parent=app, alert=True)

def limpar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

tela = "login"

def tela_login():
    global ent_nome, ent_senha, ent_email, tela
    def novo_cadastro():
        global tela
        tela = "cadastro"
        limpar_frame(frame) 
        tela_login()

    def voltar_login():
        global tela
        tela = "login"
        tela_login()

    def cadastrar():
        nome = ent_nome.get()
        email = ent_email.get()
        senha = ent_senha.get()

        if not nome or not email or not senha:
            messagebox.show_warning("Preencha todos os campos", "Aviso",  parent=app, alert=True)
            return

        messagebox.show_info("Cadastro realizado com sucesso!", "Cadastro", parent=app, alert=True)
        Usuario.novo_usuario(nome, senha, email)
        voltar_login()
    

    limpar_frame(frame) # Limpa o frame antes de adicionar novos widgets

    ttk.Label(frame, text="Sistema do Zoológico", font=("Arial", 16, "bold")).pack(pady=(0, 35))
    ttk.Label(frame, text=tela.upper(), font=("Arial", 12, "bold")).pack(pady=(0, 1))

    # Campo nome
    ttk.Label(frame, text="Nome").pack(anchor="w")
    ent_nome = ttk.Entry(frame)
    ent_nome.pack(fill=X, pady=5)

    if tela == "cadastro":
        # Campo email
        ttk.Label(frame, text="Email").pack(anchor="w")
        ent_email = ttk.Entry(frame)
        ent_email.pack(fill=X, pady=5)

    # Campo senha
    ttk.Label(frame, text="Senha").pack(anchor="w")
    ent_senha = ttk.Entry(frame, show="*") # O parâmetro show="*" oculta os caracteres digitados
    ent_senha.pack(fill=X, pady=5)

    texto_botao = "Cadastrar" if tela == "cadastro" else "Entrar"
    comando_botao = cadastrar if tela == "cadastro" else fazer_login

    # Botão de login
    ttk.Button(frame, text=texto_botao, bootstyle=SUCCESS, command=comando_botao, cursor="hand2").pack(fill=X, pady=15)
    app.bind("<Return>", comando_botao)

    if texto_botao == "Entrar":
        cadastro = ttk.Label(frame, text="Não possui uma conta? Cadastrar!", foreground="#1E90FF", cursor="hand2", font=("Arial", 8),)
        cadastro.pack()
        cadastro.bind("<Button-1>", lambda e: novo_cadastro()) # Link para a tela de cadastro
    else:
        voltar = ttk.Label(frame, text="Já possui uma conta? Login!", foreground="#1E90FF", cursor="hand2", font=("Arial", 8),)
        voltar.pack()
        voltar.bind("<Button-1>", lambda e: voltar_login())
tela_login()

# 4. Iniciar o loop principal da aplicação
app.mainloop()