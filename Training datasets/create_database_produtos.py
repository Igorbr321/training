import mysql.connector

config = {
    'user': 'root',
    'password': 'Ifrb@3009',
    'host': 'localhost',
    'database': 'teste',
}

conn = None  # Inicializando a conexão como None

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    criar_tabela_produtos = """
    CREATE TABLE IF NOT EXISTS Produtos (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Nome VARCHAR(100) NOT NULL,
        Codigo_Barras VARCHAR(13) UNIQUE NOT NULL,
        Preco DECIMAL(10, 2) NOT NULL,
        Estoque INT DEFAULT 0,
        Data_Criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    cursor.execute(criar_tabela_produtos)
    print("Tabela 'Produtos' criada com sucesso.")
    
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close()


