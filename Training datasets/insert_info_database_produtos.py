import mysql.connector

# Configurações de conexão com o banco de dados
config = {
    'user': 'root',
    'password': 'Ifrb@3009',
    'host': 'localhost',
    'database': 'teste',
}

try:
    # Conectando ao banco de dados
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    while True:
        # Coletando informações do usuário
        nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break

        codigo_barras = input("Digite o código de barras: ")
        preco = float(input("Digite o preço: "))
        estoque = int(input("Digite a quantidade em estoque: "))

        # Comando SQL para inserir os dados
        inserir_produto = """
        INSERT INTO Produtos (Nome, Codigo_Barras, Preco, Estoque)
        VALUES (%s, %s, %s, %s)
        """
        dados_produto = (nome, codigo_barras, preco, estoque)

        # Executando o comando de inserção
        cursor.execute(inserir_produto, dados_produto)

        # Confirmando a transação
        conn.commit()

        print(f"Produto '{nome}' inserido com sucesso!")

except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
