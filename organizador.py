import os
from tkinter.filedialog import askdirectory
from tkinter import messagebox

try:
    messagebox.showinfo("Bem-vindo!", "Este programa irá ajudá-lo a organizar uma pasta. Clique em OK para continuar.")

    caminho = askdirectory(title="Selecione uma Pasta")

    lista_arquvios = os.listdir(caminho)

    locais = {
        "imagens": [".png", ".jpg", "jpeg"],
        "Gifs": [".gif"],
        "Planilhas": [".xlsx", ".xml", ".csv", ".xls"],
        "Pdfs": [".pdf"],
        "Word": [".docx", ".doc"],
        "Programas": [".exe"],
        "Torrents": [".torrent"],
        "Winrar": [".zip"],
        "Anotações": [".txt"],
    }

    for arquivo in lista_arquvios:
        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
        for pasta in locais:
            if  extensao in locais[pasta]:
                if not  os.path.exists(f"{caminho}/{pasta}"):
                    os.mkdir(f"{caminho}/{pasta}")
                os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")    

    messagebox.showinfo("Conclusão", "Organização concluída com sucesso!")
except:
    pass