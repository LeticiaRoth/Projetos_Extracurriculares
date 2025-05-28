import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode('dark')

system = ctk.CTk()
system.title("Sistema de gerenciamento do WorldGame")
system.geometry("400x450")

#Listas que irão armazenar aquilo que for adicionado, já vi isso
jogos_disponiveis = []
preco_jogo = []
quantidade_loja = []
preco_fabrica = []

#Vão adicionar a venda e compra
registro_vendas = []
registro_compra = []


resultado = ctk.CTkLabel(system, text="", wraplength=380, justify="left")
resultado.pack(pady=20)


#Usamos função para facilitar, aqui usei para cadastrar novo jogo
def cadastrar_jogos():
    parte_cadastro = ctk.CTkToplevel(system)
    #Titulo que fica na página,t ipo o html
    parte_cadastro.title("Cadastre um novo jogo")
    #Determinei o tamanho
    parte_cadastro.geometry("400x420")

    #ctk.CTkLabel - uso para escrever em determinada parte
    ctk.CTkLabel(parte_cadastro, text="Nome do Jogo").pack(pady=0)
    nome = ctk.CTkEntry(parte_cadastro, placeholder_text="Insira o nome")
    nome.pack(pady=5)

    ctk.CTkLabel(parte_cadastro, text="Preço de Venda").pack(pady=5)
    preco = ctk.CTkEntry(parte_cadastro, placeholder_text="Insira o valor")
    preco.pack(pady=5)

    ctk.CTkLabel(parte_cadastro, text="Quantidade em Estoque").pack(pady=5)
    quantidade = ctk.CTkEntry(parte_cadastro, placeholder_text="Insira a quantidade no estoque")
    quantidade.pack(pady=5)

    ctk.CTkLabel(parte_cadastro, text="Preço de Fábrica").pack(pady=5)
    preco_fabrica_entry = ctk.CTkEntry(parte_cadastro, placeholder_text="Insira o preço de fábrica")
    preco_fabrica_entry.pack(pady=5)

#Aprimorei para que verificasse se o jogo esta no sistema
    def jogo_no_sistema():
        nome_jogo = nome.get()
        if nome_jogo in jogos_disponiveis:
            resultado.configure(text="Jogo já cadastrado no sistema", text_color="orange", font=("Arial", 15)) #Configure, preciso determinar qula fonte e tamanho
        else:
            try:
                jogos_disponiveis.append(nome_jogo)
                preco_jogo.append(float(preco.get()))
                quantidade_loja.append(int(quantidade.get()))
                preco_fabrica.append(float(preco_fabrica_entry.get()))
                resultado.configure(text=f"Jogo {nome_jogo} cadastrado com sucesso!", text_color="green")
                parte_cadastro.destroy()
            except ValueError:
                resultado.configure(text="Valores inválidos. Tente novamente.", text_color="red")

    ctk.CTkButton(parte_cadastro, text="Salvar", command=jogo_no_sistema).pack(pady=10)

#Função para registrar a venda no sistema
def registrar_venda():
    if not jogos_disponiveis:
        resultado.configure(text="Nenhum jogo cadastrado para venda.", text_color="red", font=("Arial", 15))
        return

    parte_venda = ctk.CTkToplevel(system)
    parte_venda.title("Registrar Venda")
    parte_venda.geometry("350x250")

    ctk.CTkLabel(parte_venda, text="Selecione o jogo").pack(pady=5)
    jogo_var = ctk.StringVar(value=jogos_disponiveis[0])
    jogo_dropdown = ctk.CTkOptionMenu(parte_venda, values=jogos_disponiveis, variable=jogo_var)
    jogo_dropdown.pack(pady=5)

    ctk.CTkLabel(parte_venda, text="Quantidade").pack(pady=5)
    #Para personalizar é como um css so que do Python
    quantidade_entry = ctk.CTkEntry(parte_venda, placeholder_text="Insira a quantidade", width=200, height=30)
    quantidade_entry.pack(pady=5)

    def confirmar_venda():
        #Aqui o get serve para pegar o nome do jogo, no menu suspenso;
        #Variavel com o nome do jogo que foi puxado do get
        nome_jogo = jogo_var.get()
        try:
            #Transformo em inteiro, get mais uma vez pegando o que foi digitado
            quantidade_venda = int(quantidade_entry.get())

            #Mesmo índice para todas as listas;
            #IDX = novo comando que ajuda a saber qual a posição do indice, nesse caso do preço, estoque e fábrica
            idx = jogos_disponiveis.index(nome_jogo)

            estoque_atual = quantidade_loja[idx]

            #Verifico se não é menor que 0 e se não é maior que o estoque atual, pega o indice
            if quantidade_venda <= 0:
                resultado.configure(text="Quantidade deve ser maior que zero.", text_color="red")
                return

            if quantidade_venda > estoque_atual:
                resultado.configure(text=f"Estoque insuficiente! Estoque atual: {estoque_atual}", text_color="red")
                return

            #Atualizo o estoque, subtraindo a quantidade da loja pelas vendas, para ser precisso
            quantidade_loja[idx] -= quantidade_venda

            #Multiplicação simples, total da venda é o preço do jogo que puxa pelo indice mais a quantidade
            valor_venda = preco_jogo[idx] * quantidade_venda
            #Adicione na lista de resgistro de vendas
            registro_vendas.append((nome_jogo, quantidade_venda, valor_venda))

            #Mostra na tela
            resultado.configure(text=f"Venda registrada: {quantidade_venda} x {nome_jogo} por R${valor_venda:.2f}", text_color="green")
            parte_venda.destroy()

        #LEMBRAR: try e except, trabalham juntos um identifica outro avsa
        except ValueError:
            resultado.configure(text="Quantidade inválida.", text_color="red")

    #Command chama a função quando clicado
    ctk.CTkButton(parte_venda, text="Confirmar Venda", command=confirmar_venda).pack(pady=10)

#Para realizar a compra no estoque
def compra_estoque():
    #Se não estiver, usa o configure para exibir a mensagem de erro
    if not jogos_disponiveis:
        resultado.configure(text="Nenhum jogo cadastrado para compra.", text_color="orange")
        return

    #Toplevel, cria um janela
    parte_compra = ctk.CTkToplevel(system)
    parte_compra.title("Compra de Estoque")
    parte_compra.geometry("350x250")

    #Cria o label padrão como título para a Janela
    ctk.CTkLabel(parte_compra, text="Selecione o jogo").pack(pady=5)


    #ESTUDAR MAIS DROPBOX
    #Contara os jogos que tem dentro do drop, atribui a uma varável
    jogo_var = ctk.StringVar(value=jogos_disponiveis[0])

    #Pega o valor e atribui a o jogo_dropbox
    jogo_dropdown = ctk.CTkOptionMenu(parte_compra, values=jogos_disponiveis, variable=jogo_var)
    jogo_dropdown.pack(pady=5)

    ctk.CTkLabel(parte_compra, text="Quantidade a comprar").pack(pady=5)
    quantidade_entry = ctk.CTkEntry(parte_compra, placeholder_text="Insira a quantidade")
    quantidade_entry.pack(pady=5)



    #Função dentro de comprar estoque
    def confirmar_compra():

        #Pega o valor de jogo var inserido no dropbox e coloca na variável nme_jogo
        nome_jogo = jogo_var.get()
        try:
            #Converte para inteiro pois entra como string
            quantidade_compra = int(quantidade_entry.get())

            if quantidade_compra <= 0:
                resultado.configure(text="Quantidade deve ser maior que zero.", text_color="red")
                return

            idx = jogos_disponiveis.index(nome_jogo)

            #Atualiza o estoque de acordo com a compra, adicionando!
            quantidade_loja[idx] += quantidade_compra

            #Calcula o valor da compra
            valor_compra = preco_fabrica[idx] * quantidade_compra

            #Coloca na lista de registro de compra
            registro_compra.append((nome_jogo, quantidade_compra, valor_compra))

            #Mensagem básica da confimação com o valor
            resultado.configure(text=f"Compra registrada: {quantidade_compra}x {nome_jogo} por R${valor_compra:.2f}", text_color="green")
            parte_compra.destroy()

        except ValueError:
            #Implementação se caso o usuário tentar digitar uma letra, por exemplos (EXPLICAR ISSO)
            resultado.configure(text="Quantidade inválida.", text_color="red")

    ctk.CTkButton(parte_compra, text="Confirmar Compra", command=confirmar_compra).pack(pady=10)



#Resumo da loja com as vendas, e totais
def resumo_loja():

    #TESTE
    #Com o [2] ele pega o valor total de cada venda
    #Soma os valores com o sum
    total_entrada = sum(venda[2] for venda in registro_vendas)  #total vendido
    total_saida = sum(compra[2] for compra in registro_compra)    #total gasto em compras

    #Saldo simples
    saldo = total_entrada - total_saida

    #Criação da tela separada, sem destroy para possuir uma volta
    parte_resumo = ctk.CTkToplevel(system)
    parte_resumo.title("Resumo da Loja")
    parte_resumo.geometry("400x400")

    #O mais adiicona ao texto, 2f para determinar as ccasas
    texto = f"Total de dinheiro que entrou (vendas): R$ {total_entrada:.2f}\n"
    texto += f"Total de dinheiro que saiu (compras): R$ {total_saida:.2f}\n"
    texto += f"Saldo atual: R$ {saldo:.2f}\n\n"
    texto += "Estoque atual:\n"

    #Busca o indice na lista jogos disponiveis e adiciona ao texto
    for i, jogo in enumerate(jogos_disponiveis):
        texto += f"{jogo}: {quantidade_loja[i]} unidades\n"

    label_resumo = ctk.CTkLabel(parte_resumo, text=texto, wraplength=380, justify="left")
    label_resumo.pack(padx=20, pady=20)


#Função para sair
def sair():
    #Importo a mensagem em box lá em cima e chamo aqui
    #Primeiro o title = Sistema, que aparece em cima
    #Segundo message = Que aparece no conteúdo
    messagebox.showinfo("Sistema", "Caixa fechado. Até logo DS18 e Luca!")
    #Destroe a tela atual, preciso colocar o nome na fresnte
    system.destroy()


#Botões do menu, poderia usar um while True
ctk.CTkButton(system, text="Cadastrar jogo", command=cadastrar_jogos).pack(pady=5)
ctk.CTkButton(system, text="Registrar venda", command=registrar_venda).pack(pady=5)
ctk.CTkButton(system, text="Compra de estoque", command=compra_estoque).pack(pady=5)
ctk.CTkButton(system, text="Resumo da loja", command=resumo_loja).pack(pady=5)
ctk.CTkButton(system, text="Sair", command=sair).pack(pady=5)

#Main sempre roda o sistema (LEMBRAR)
system.mainloop()
