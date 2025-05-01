import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")

largura_janela = 300
altura_janela = 400
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = (largura_tela // 2) - (largura_janela // 2)
y = (altura_tela // 2) - (altura_janela // 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

def clicar(botao):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + str(botao))

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

def limpar():
    entrada.delete(0, tk.END)

entrada = tk.Entry(janela, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4)

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        botao = tk.Button(janela, text=texto, width=5, height=2, command=calcular)
    else:
        botao = tk.Button(janela, text=texto, width=5, height=2, command=lambda t=texto: clicar(t))
    botao.grid(row=linha, column=coluna)

botao_limpar = tk.Button(janela, text="C", width=5, height=2, command=limpar)
botao_limpar.grid(row=5, column=0, columnspan=4, sticky="we")

janela.mainloop()
