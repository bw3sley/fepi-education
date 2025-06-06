USE db_supermercado;
GO

CREATE TABLE contas (
    id_conta INT PRIMARY KEY IDENTITY,
    nome    VARCHAR(45)    NOT NULL,
    agencia INT            NULL,
    desde   DATETIME       NULL,
    cnpj    VARCHAR(18)         NULL,

    FOREIGN KEY (cnpj) REFERENCES fornecedores(cnpj)
)
GO

INSERT INTO contas (nome, agencia, desde, cnpj)
VALUES
    ('Loja Alpha',        1001, '20180510 14:30:00', '01.234.567/0001-89'),
    ('Supermercado Beta', 1002, '20190722 09:15:00', '01.234.567/0001-89'),
    ('Mercado Gamma',     1003, '20200115 11:00:00', '01.234.567/0001-89'),
    ('Comércio Delta',    1004, '20210301 08:45:00', '98.765.432/0001-10'),
    ('Padaria Épsilon',   1005, '20221112 16:20:00', '98.765.432/0001-10');
GO

-- 1) Mostrar nome do entregador, nome do cliente e descritivo da entrega
CREATE PROCEDURE _sp_mostrar_entregas
AS
BEGIN
    SELECT 
        d.nome_moto    AS nome_entregador,
        c.nome         AS nome_cliente,
        ce.descritivo  AS descritivo
    
	FROM controle_entregas AS ce

    INNER JOIN deliveries AS d  
      ON ce.cod_entregador = d.cod_entregador
    
	INNER JOIN clientes AS c  
      ON ce.cod_cliente = c.cod_cliente;
END
GO

EXEC _sp_mostrar_entregas;
GO

-- 2) Cadastrar novos fornecedores
CREATE PROCEDURE _sp_cadastrar_fornecedor
    @p_cnpj     VARCHAR(18),
    @p_nome     VARCHAR(50),
    @p_endereco VARCHAR(30),
    @p_tipo     INT
AS
BEGIN
    INSERT INTO fornecedores (cnpj, nome, endereco, tipo)
    VALUES (@p_cnpj, @p_nome, @p_endereco, @p_tipo);
END
GO

EXEC _sp_cadastrar_fornecedor 
     @p_cnpj     = '12.345.678/0001-99',
     @p_nome     = 'Fornecedor Novo',
     @p_endereco = 'Rua Inovação, 100',
     @p_tipo     = 3;
SELECT * FROM fornecedores;
GO

-- 3) Inserir e listar todos os fornecedores
CREATE PROCEDURE _sp_cadastrar_e_listar_fornecedores
    @p_cnpj     VARCHAR(18),
    @p_nome     VARCHAR(50),
    @p_endereco VARCHAR(30),
    @p_tipo     INT
AS
BEGIN
    INSERT INTO fornecedores (cnpj, nome, endereco, tipo)
    VALUES (@p_cnpj, @p_nome, @p_endereco, @p_tipo);

    SELECT * FROM fornecedores;z
END
GO

EXEC _sp_cadastrar_e_listar_fornecedores 
     @p_cnpj     = '22.333.444/0001-55',
     @p_nome     = 'Fornecedor X',
     @p_endereco = 'Av. Central, 200',
     @p_tipo     = 1;
GO

-- 4) Idade do cliente mais antigo e nome (OUT parameters)
CREATE PROCEDURE _sp_idade_conta_mais_velha
    @p_idade    INT            ,
    @p_nome_dono VARCHAR(30)   
AS
BEGIN
    SELECT TOP 1
        @p_idade = DATEDIFF(YEAR, desde, GETDATE()),
        @p_nome_dono = nome
    FROM clientes
    ORDER BY desde ASC;
END
GO

DECLARE @idade INT, @nome_dono VARCHAR(30);
EXEC _sp_idade_conta_mais_velha 
     @p_idade     = @idade     OUTPUT,
     @p_nome_dono = @nome_dono OUTPUT;
SELECT 
    @idade     AS idade_do_cliente_mais_antigo,
    @nome_dono AS nome_do_cliente;
GO

-- 5) Somar um valor decimal com uma variável (IN e)
CREATE PROCEDURE _sp_somar_decimal
    @p_entrada     DECIMAL(10,2),
    @p_acumulador  DECIMAL(10,2) OUTPUT
AS
BEGIN
    DECLARE @soma DECIMAL(10,2);
    SET @soma = @p_acumulador + @p_entrada;
    SET @p_acumulador = @soma;
END;
GO

DECLARE @total DECIMAL(10,2) = 100;

EXEC _sp_somar_decimal 
     @p_entrada    = 25,
     @p_acumulador = @total OUTPUT;

SELECT @total AS resultado_soma;
GO

-- 6) Multiplicar inteiro e atualizar estoque de produto
CREATE PROCEDURE _sp_multiplicar_e_atualizar_estoque
    @p_multiplicando INT,
    @p_cod_produto   INT
AS
BEGIN
    DECLARE @novo_estoque INT;
    SET @novo_estoque = @p_multiplicando * 2;  
    UPDATE produtos
    SET estoque = @novo_estoque
    WHERE cod_produto = @p_cod_produto;
END;
GO

SELECT cod_produto, nome, estoque FROM produtos WHERE cod_produto = 1;

EXEC _sp_multiplicar_e_atualizar_estoque 
     @p_multiplicando = 5, 
     @p_cod_produto   = 1;

SELECT cod_produto, nome, estoque FROM produtos WHERE cod_produto = 1;
GO

-- 7) Remover quantidade de produtos cujo nome começa com “a” (antes/depois)
CREATE PROCEDURE _sp_remover_produtos_a
    @p_quantidade INT
AS
BEGIN
    SELECT 
        'ANTES'    AS momento, 
        cod_produto, nome, preco, estoque
    FROM produtos
    WHERE LOWER(nome) LIKE 'a%';

    UPDATE produtos SET estoque = estoque - @p_quantidade
    WHERE LOWER(nome) LIKE 'a%';

    SELECT 
        'DEPOIS'   AS momento, 
        cod_produto, nome, preco, estoque
    FROM produtos
    WHERE LOWER(nome) LIKE 'a%';
END
GO

EXEC _sp_remover_produtos_a @p_quantidade = 10;
GO

-- 8) Receita geral comentada
CREATE PROCEDURE _sp_receita_geral
    @total DECIMAL(18,2) OUTPUT
AS
BEGIN
    -- contador: itera sobre cada produto (inicia em 1)
    DECLARE @contador    INT = 1;
    -- estoque atual do produto
    DECLARE @estoque     INT;
    -- preço unitário do produto
    DECLARE @valor_unit  DECIMAL(10,2);
    -- total de produtos na tabela
    DECLARE @total_itens INT;
    -- acumulador do valor total de todas as vendas
    DECLARE @soma        DECIMAL(18,2) = 0;

    -- obtém a quantidade de registros em produtos
    SET @total_itens = (SELECT COUNT(*) FROM produtos);

    -- enquanto não percorrer todos os produtos
    WHILE @contador <= @total_itens
    BEGIN
        -- busca estoque do produto de código = contador
        SET @estoque = (
            SELECT estoque 
            FROM produtos 
            WHERE cod_produto = @contador
        );
        -- busca preço unitário do mesmo produto
        SET @valor_unit = (
            SELECT preco 
            FROM produtos 
            WHERE cod_produto = @contador
        );
        -- acumula: soma += estoque * preço
        SET @soma = @soma + (@estoque * @valor_unit);
        -- próximo produto
        SET @contador = @contador + 1;
    END

    -- retorna o valor total
    SET @total = @soma;
END;
GO

DECLARE @receita DECIMAL(18,2);
EXEC _sp_receita_geral @receita OUTPUT;
SELECT @receita AS receita_total;
GO