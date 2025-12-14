import tkinter as tk
from tkinter import messagebox


def validar_campos(entry_nome, entry_idade, sexo_var):
    nome_raw = entry_nome.get().strip()
    idade_raw = entry_idade.get().strip()
    sexo = sexo_var.get().strip()

    # Tratar placeholders como vazios
    nome = "" if (hasattr(entry_nome, "placeholder") and nome_raw == entry_nome.placeholder) else nome_raw
    idade_str = "" if (hasattr(entry_idade, "placeholder") and idade_raw == entry_idade.placeholder) else idade_raw

    ok, err_msg, idade = validate_inputs(nome, idade_str, sexo)
    if not ok:
        if "Idade" in err_msg:
            messagebox.showerror("Idade inválida", err_msg)
        else:
            messagebox.showwarning("Campos vazios", err_msg)
        return

    messagebox.showinfo("Sucesso", f"Nome: {nome}\nIdade: {idade}\nSexo: {sexo}")


def validate_inputs(nome, idade_str, sexo):
    """Valida valores e retorna (ok, mensagem_erro, idade_int)."""
    nome = nome.strip()
    idade_str = idade_str.strip()
    sexo = sexo.strip()

    if not nome or not idade_str or not sexo or sexo == "Selecione":
        return False, "Por favor, preencha todos os campos!", None

    try:
        idade = int(idade_str)
        if idade <= 0:
            raise ValueError
    except ValueError:
        return False, "Informe uma idade válida (número inteiro positivo).", None

    return True, None, idade


def main():
    print("Alô mundo")
    janela = tk.Tk()
    janela.title("Formulário")
    janela.geometry("500x500")
    janela.resizable(False, False)

    # Helper para placeholder em Entry
    def add_placeholder(entry, text):
        entry.placeholder = text
        entry.insert(0, text)
        entry.config(fg="grey")

        def on_focus_in(event):
            if entry.get() == entry.placeholder:
                entry.delete(0, tk.END)
                entry.config(fg="black")

        def on_focus_out(event):
            if not entry.get():
                entry.insert(0, entry.placeholder)
                entry.config(fg="grey")

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

    tk.Label(janela, text="Nome completo:").grid(row=0, column=0, sticky="e", padx=10, pady=6)
    entry_nome = tk.Entry(janela, width=40)
    entry_nome.grid(row=0, column=1, padx=10, pady=6)
    add_placeholder(entry_nome, "Ex: João Silva")

    tk.Label(janela, text="Idade (anos):").grid(row=1, column=0, sticky="e", padx=10, pady=6)
    entry_idade = tk.Entry(janela, width=40)
    entry_idade.grid(row=1, column=1, padx=10, pady=6)
    add_placeholder(entry_idade, "Ex: 30")

    tk.Label(janela, text="Sexo:").grid(row=2, column=0, sticky="e", padx=10, pady=6)
    sexo_var = tk.StringVar(value="Selecione")
    sexo_opcoes = ["Selecione", "Masculino", "Feminino", "Outro", "Prefiro não dizer"]
    sexo_menu = tk.OptionMenu(janela, sexo_var, *sexo_opcoes)
    sexo_menu.config(width=30)
    sexo_menu.grid(row=2, column=1, sticky="w", padx=10, pady=6)

    botao = tk.Button(janela, text="Confirmar", command=lambda: validar_campos(entry_nome, entry_idade, sexo_var))
    botao.grid(row=3, column=0, columnspan=2, pady=(10, 6))

    janela.mainloop()


if __name__ == "__main__":
    main()