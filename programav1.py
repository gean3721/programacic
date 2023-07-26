import tkinter as tk
from datetime import datetime
import webbrowser

# Função para abrir o link ao clicar no rótulo
def abrir_link(event):
    webbrowser.open("https://www.sistemafiep.org.br")

# Função para atualizar o rótulo do rodapé com a data e hora atual
def atualizar_data_hora():
    agora = datetime.now()
    data_hora_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
    label_data_hora.config(text=data_hora_formatada)
    root.after(1000, atualizar_data_hora)  # Atualizar a cada 1000 milissegundos (1 segundo)

def gerar_texto1():
    texto_box.delete(1.0, tk.END)
    texto_box.insert(tk.END, """\
Olá, [Nome do Responsável]!

Gostaria de solicitar a gentileza de efetuar a reserva do Laboratório [N° do Laboratório] pelo período mínimo de [Quantidade] dias, para que possamos realizar a formatação e configuração dos computadores.

O motivo da reserva é executar uma manutenção completa em todos os computadores do laboratório, a fim de otimizar o desempenho e garantir que estejam em plenas condições de uso para os nossos professores e alunos.

Durante esse período, a equipe de T.I. estará trabalhando no local para realizar as seguintes atividades:

    1. Formatação dos computadores para garantir um sistema operacional limpo e atualizado.
    2. Instalação e configuração dos softwares necessários para as atividades do laboratório.
    3. Verificação e correção de eventuais problemas de hardware ou software que possam afetar o desempenho das máquinas.

Essas ações visam melhorar a eficiência e a segurança dos computadores, garantindo que estejam em conformidade com os padrões da empresa.

Caso a reserva de três dias não seja possível, solicitamos que nos informe a disponibilidade de datas para que possamos ajustar o planejamento da manutenção.

Agradecemos antecipadamente pela sua colaboração e compreensão. Se houver qualquer questão ou necessidade de ajuste, por favor, entre em contato conosco.""")

def gerar_texto2():
    texto_box.delete(1.0, tk.END)
    texto_box.insert(tk.END, "Texto gerado pelo Botão 2\n")

def gerar_texto3():
    texto_box.delete(1.0, tk.END)
    texto_box.insert(tk.END, """\
Olá, [Nome do Responsável]!

Gostaríamos de solicitar aprovação para conserto de equipamento [Descrever o equipamento]. Identificamos que uma falha [Descrevre a falha] e não é possível realizar a manutenção para corrigir o problema.

Abaixo, fornecemos as informações detalhadas sobre o orçamento para a troca do teclado:

Custo da peça: R$[Especificar o valor]
Mão de obra: R$[Especificar o valor]
Deslocamento: R$[Especificar o valor]
Total do orçamento: R$[Especificar o valor]

Orçamento em anexo!

Se aprovado precisamos também da CASA, UNIDADE e CR para lançamento das despesas.

Qualquer dúvida estamos a disposição.""")

def gerar_texto4():
    texto_box.delete(1.0, tk.END)
    texto_box.insert(tk.END, "Texto gerado pelo Botão 4\n")

def gerar_texto5():
    texto_box.delete(1.0, tk.END)
    texto_box.insert(tk.END, "Texto gerado pelo Botão 5\n")

def gerar_texto6():
    texto_box.delete(1.0, tk.END)
    texto_box.insert(tk.END, "Texto gerado pelo Botão 6\n")

def gerar_texto7():
    texto_box.delete(1.0, tk.END)
    texto_box.insert(tk.END, "Texto gerado pelo Botão 7\n")

def gerar_texto8():
    texto_box.delete(1.0, tk.END)
    texto_box.insert(tk.END, "Texto gerado pelo Botão 8\n")

# Texto da tela inicial
texto_inicial = """\
Com um simples clique, você terá acesso a respostas personalizadas
e prontas para serem compartilhadas com sua equipe no Teams, Outlook
ou qualquer outra plataforma que você preferir.
BASTA COPIAR E COLAR!
"""

# Criação da janela principal em tela cheia
root = tk.Tk()
root.title("Gerador de respostas SENAI CIC")
root.attributes("-fullscreen", True)  # Abre em tela cheia

# Função para alternar entre o modo janela e tela cheia
def alternar_modo():
    if root.attributes("-fullscreen"):
        root.attributes("-fullscreen", False)
        botao_modo.config(text="Modo Tela Cheia")
    else:
        root.attributes("-fullscreen", True)
        botao_modo.config(text="Modo Janela")

# Botão para alternar o modo janela/tela cheia
botao_modo = tk.Button(root, text="Modo Janela", command=alternar_modo)
botao_modo.pack(side=tk.TOP, padx=5, pady=5)

# Criação dos frames para as duas colunas
frame_coluna_esquerda = tk.Frame(root)
frame_coluna_direita = tk.Frame(root)

# Criação dos botões
botao1 = tk.Button(frame_coluna_esquerda, text="Agendamento de Laboratório", command=gerar_texto1)
botao2 = tk.Button(frame_coluna_esquerda, text="Gerar Texto 2", command=gerar_texto2)
botao3 = tk.Button(frame_coluna_direita, text="Aprovação de Orçamento", command=gerar_texto3)
botao4 = tk.Button(frame_coluna_direita, text="Gerar Texto 4", command=gerar_texto4)
botao5 = tk.Button(frame_coluna_direita, text="Gerar Texto 5", command=gerar_texto5)
botao6 = tk.Button(frame_coluna_direita, text="Gerar Texto 6", command=gerar_texto6)
botao7 = tk.Button(frame_coluna_esquerda, text="Gerar Texto 7", command=gerar_texto7)
botao8 = tk.Button(frame_coluna_esquerda, text="Gerar Texto 8", command=gerar_texto8)

# Criação do rótulo para exibir o texto inicial
label_texto_inicial = tk.Label(root, text=texto_inicial, justify=tk.CENTER)

# Criação da caixa de texto
texto_box = tk.Text(root, width=40, height=10)

# Criação da barra de rolagem vertical
scrollbar = tk.Scrollbar(root, command=texto_box.yview)
texto_box.config(yscrollcommand=scrollbar.set)

# Empacotamento dos botões, rótulo e caixa de texto
label_texto_inicial.pack(pady=10, padx=10)
botao1.pack(fill=tk.BOTH, padx=5, pady=5)
botao2.pack(fill=tk.BOTH, padx=5, pady=5)
botao3.pack(fill=tk.BOTH, padx=5, pady=5)
botao4.pack(fill=tk.BOTH, padx=5, pady=5)
botao5.pack(fill=tk.BOTH, padx=5, pady=5)
botao6.pack(fill=tk.BOTH, padx=5, pady=5)
botao7.pack(fill=tk.BOTH, padx=5, pady=5)
botao8.pack(fill=tk.BOTH, padx=5, pady=5)

texto_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

texto_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Criação do rótulo para exibir a barra de copyright
texto_copyright = "© 2023 - Coordenação de Serviços e Suporte TI"
label_copyright = tk.Label(root, text=texto_copyright)
label_copyright.pack(side=tk.BOTTOM)

# Criação do rótulo para exibir a barra de data e hora
label_data_hora = tk.Label(root, text="", font=("Arial", 10))
label_data_hora.pack(side=tk.BOTTOM)

# Iniciar a atualização da data e hora
atualizar_data_hora()

# Criação do rótulo para exibir o link
texto_link = "www.sistemafiep.org.br"
label_link = tk.Label(root, text=texto_link, fg="blue", cursor="hand2", font=("Arial", 10))
label_link.pack(side=tk.BOTTOM)

# Vincular o evento de clique ao rótulo
label_link.bind("<Button-1>", abrir_link)

# Criação do rótulo para exibir a imagem no rodapé
imagem = tk.PhotoImage(file="fieplogo.png")
label_imagem = tk.Label(root, image=imagem)
label_imagem.pack(side=tk.BOTTOM, pady=5)

# Empacotar os frames na janela principal
frame_coluna_esquerda.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame_coluna_direita.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Iniciar o loop principal
root.mainloop()