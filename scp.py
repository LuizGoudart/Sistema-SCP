import customtkinter as ctk
from tkinter import messagebox
import openpyxl
import os
from datetime import datetime

# Nome do arquivo onde salvaremos a presença
ARQUIVO_PRESENCA = "presenca.xlsx"


# Função para verificar e perguntar sobre o arquivo
def verificar_arquivo():
    if os.path.exists(ARQUIVO_PRESENCA):
        resposta = messagebox.askquestion(
            "Arquivo existente",
            f"O arquivo '{ARQUIVO_PRESENCA}' já existe. Deseja usar o arquivo existente?",
            icon="warning",
        )
        if (
            resposta == "no"
        ):  # Se o usuário não quiser usar o arquivo existente, criamos um novo
            criar_arquivo()
    else:
        resposta = messagebox.askquestion(
            "Arquivo não encontrado",
            f"O arquivo '{ARQUIVO_PRESENCA}' não foi encontrado. Deseja criar um novo arquivo?",
            icon="question",
        )
        if resposta == "yes":  # Se o usuário quiser criar um novo arquivo
            criar_arquivo()


# Função para criar um novo arquivo
def criar_arquivo():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Presencas"
    sheet.append(["Data", "Turma", "Aluno", "Presenca"])
    workbook.save(ARQUIVO_PRESENCA)


# Chama a função para verificar o arquivo logo ao iniciar
verificar_arquivo()


class AppPresenca:
    def __init__(self, master):
        self.master = master
        master.title("Controle de Presença")
        master.geometry("500x350")
        master.minsize(400, 300)

        # Frame principal
        frame = ctk.CTkFrame(master)
        frame.pack(padx=30, pady=30, expand=True, fill="both")

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=2)

        # Campo de data
        self.label_data = ctk.CTkLabel(
            frame, text="Data (dd/mm/aaaa) (Opcional):", font=ctk.CTkFont(weight="bold")
        )
        self.label_data.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_data = ctk.CTkEntry(
            frame, placeholder_text="Ex: 25/04/2025", width=200
        )
        self.entry_data.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Campo de turma
        self.label_turma = ctk.CTkLabel(
            frame, text="Turma:", font=ctk.CTkFont(weight="bold")
        )
        self.label_turma.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_turma = ctk.CTkEntry(frame, placeholder_text="Ex: 3A", width=200)
        self.entry_turma.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Campo de nome do aluno
        self.label_nome = ctk.CTkLabel(
            frame, text="Nome do Aluno:", font=ctk.CTkFont(weight="bold")
        )
        self.label_nome.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_nome = ctk.CTkEntry(
            frame, placeholder_text="Digite o nome completo", width=200
        )
        self.entry_nome.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Botões de Presente/Ausente
        self.botao_presente = ctk.CTkButton(
            frame,
            text="Presente",
            command=lambda: self.registrar_presenca("Presente"),
            fg_color="#006400",
            hover_color="#228B22",
            font=ctk.CTkFont(weight="bold"),
            width=150,
        )
        self.botao_presente.grid(row=3, column=0, padx=10, pady=20)

        self.botao_ausente = ctk.CTkButton(
            frame,
            text="Ausente",
            command=lambda: self.registrar_presenca("Ausente"),
            fg_color="#8B0000",
            hover_color="#B22222",
            font=ctk.CTkFont(weight="bold"),
            width=150,
        )
        self.botao_ausente.grid(row=3, column=1, padx=10, pady=20)

    def registrar_presenca(self, status):
        data = self.entry_data.get()
        turma = self.entry_turma.get()
        nome = self.entry_nome.get()

        if not turma or not nome:
            messagebox.showwarning(
                "\u26a0\ufe0f Aviso", "Preencha todos os campos obrigatórios!"
            )
            return

        if not data:
            data = datetime.now().strftime("%d/%m/%Y")

        workbook = openpyxl.load_workbook(ARQUIVO_PRESENCA)
        sheet = workbook.active
        sheet.append([data, turma, nome, status])
        workbook.save(ARQUIVO_PRESENCA)

        messagebox.showinfo(
            "\u2705 Sucesso",
            f"Presença de {nome} na turma {turma} registrada como {status}!",
        )
        self.entry_nome.delete(0, "end")


if __name__ == "__main__":
    ctk.set_appearance_mode("light")  # "dark" ou "system" também pode ser usado
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = AppPresenca(root)
    root.mainloop()
