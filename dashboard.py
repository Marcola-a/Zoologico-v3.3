import ttkbootstrap as ttk
from PIL import Image, ImageTk

from ttkbootstrap.widgets.tableview import Tableview
from animal import Animal
from database.conexao import conectar
from usuario import Usuario

import pywinstyles

def abrir(usuario, root):
    # print("ADMIN:", usuario.admin, type(usuario.admin))
    nome_usuario = usuario.nome
    admin = usuario.admin
    if admin:
        width = 1300
        titulo = "Dashboard de Animais"
    else:
        width = 670
        titulo = "Conheça os animais do Zoo!"
    
    tabela_animais = None

    janela = ttk.Toplevel(root)
    janela.title("Zoológico - Animais")
    # janela.geometry("700x500")
    janela.state('zoomed')  # Abre a janela maximizada
    janela.iconbitmap("img/zebra_icon.ico")
    janela.config(bg="white")

    pywinstyles.change_header_color(janela, "#f5f5f5") # Define a cor da barra de título da app
    def carregar_background():
        imagem = Image.open("img/#21dc00.png")
        janela.bg_image = ImageTk.PhotoImage(imagem)

        background = ttk.Label(janela, image=janela.bg_image) 
        background.place(x=0, y=0, relwidth=1, relheight=1)
        background.lower()

    janela.after(0, carregar_background)

    def recarregar():
        nonlocal tabela_animais
        if tabela_animais is not None:
            tabela_animais.destroy()
        tabela()
        return print('Recarregado')

    frame = ttk.Frame(janela, padding=20, width=width, height=700)
    frame.pack_propagate(0)
    frame.pack(expand=True)
    ttk.Label(frame, text=titulo, font=("Arial", 16, "bold")).pack(pady=(0, 40))
    a = "Administrador" if admin else ""
    ttk.Label(frame, text=f"Bem-vindo(a) {a} {nome_usuario}", font=("Arial", 12)).pack(pady=(0, 20))
    if admin:
        import add_animal
        from add_animal import adicionar_animal
        ttk.Button(frame, text="Adicionar Animal", bootstyle="success", command=lambda: add_animal.adicionar_animal(recarregar)).pack(pady=(0, 20))

    # Definir os cabeçalhos das colunas
    def definir_colunas(admin):
        if admin:
            return [
                {"text": "ID"},
                {"text": "Apelido"},
                {"text": "Espécie"},
                {"text": "Nome Científico"},
                {"text": "Peso"},
                {"text": "Nascimento"},
                {"text": "Chegada"},
                {"text": "Dieta"},
                {"text": "Rotina"},
                {"text": "Recinto"},
                {"text": "Ativo"},
            ]
        else:
            return [
                {"text": "Apelido"},
                {"text": "Espécie"},
                {"text": "Nome Científico"},
                {"text": "Recinto"},
            ]   

    def montar_linhas(animais, admin):
        linhas = []
        for a in animais:
            if admin:
                linhas.append([
                    a.animal_id,
                    a.apelido,
                    a.especie,
                    a.nome_cientifico,
                    a.peso,
                    a.data_nascimento,
                    a.data_chegada,
                    a.dieta,
                    a.rotina_limpeza,
                    a.recinto,
                    a.ativo
                ])
            else:
                linhas.append([
                    a.apelido,
                    a.especie,
                    a.nome_cientifico,
                    a.recinto
                ])

        return linhas
    
    def tabela():
        nonlocal tabela_animais

        rowdata = montar_linhas(Animal.listar_animais(), admin)
        coldata = definir_colunas(admin)

        # print(coldata)
        # print(rowdata[:2])

        tabela_animais = Tableview(
            master=frame,
            coldata=coldata,
            rowdata=rowdata,
            searchable=True,         # Adiciona um campo de pesquisa
            bootstyle="success",
        )
        tabela_animais.pack(fill="both", expand=True, padx=10, pady=10)
        tabela_animais.autofit_columns() # Ajusta automaticamente a largura das colunas
    
    # Feito com IA - apenas essa função, os de baixo estão "safe"
    def frame_com_scroll(pai):
        container = ttk.Frame(pai)
        container.pack(fill="both", expand=True)

        canvas = ttk.Canvas(container, highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1 * int(e.delta / 120), "units"))

        scroll = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scroll.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scroll.set)

        scrollable_frame = ttk.Frame(canvas)
        window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.bind("<Configure>", lambda e: canvas.itemconfig(window_id, width=e.width))

        return scrollable_frame

    def user():
        com_scroll = frame_com_scroll(frame)

        for animal in Animal.listar_animais():
            card = ttk.Frame(com_scroll, padding=10, bootstyle="light")
            card.pack(fill="x", pady=5,)

            ttk.Label(card,text=animal.apelido, font=("Arial", 14, "bold"), bootstyle="inverse-light").pack(anchor="w")
            ttk.Label(card, text=f"{animal.apelido} é um(a) {animal.especie}({animal.nome_cientifico}), que faz parte do zoológico desde {animal.data_chegada} e vive atualmente no recinto {animal.recinto}, seguindo uma dieta baseada em {animal.dieta}.", 
            font=("Arial", 11), wraplength=500, justify="left", bootstyle="inverse-light").pack(anchor="w")


    if admin:
        tabela()
    else:
        user()