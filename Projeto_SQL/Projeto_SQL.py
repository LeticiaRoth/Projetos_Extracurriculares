import sqlite3 #Usado para mexer com o banco
import pandas as pd #Usado para analisar os dados dentro do banco, ele permite visualizar pelo terminal


conn = sqlite3.connect("teste.db") #Conecta a tabela ao banco, conn conecta com a tabela do teste
cursor = conn.cursor() #Executa os comandos do SQL dentro do Python

#Insere os dados pedidos
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade"))

#Insere os valores dentro da tabela
cursor.execute(
f'''INSERT INTO teste (nome,idade) VALUES('{nome}',{idade})''')


#Cria uma variável para ler a tabela com o pandas
resultados = pd.read_sql("SELECT * FROM teste", conn)

#Mostra quantas linhas eu determinar
print(resultados.head(10))

"""
cursor.execute(f"DELETE FROM teste")
Posso colocar o where para determinar qual valor desejo deleter
"""
conn.commit() #Salva as alterações
conn.close()  #Fecha as conexões