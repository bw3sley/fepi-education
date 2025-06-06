-- CREATE

DROP DATABASE IF EXISTS db_supermercado
GO

CREATE DATABASE db_supermercado
GO

USE db_supermercado
GO

CREATE TABLE produtos (
    cod_produto INT PRIMARY KEY IDENTITY,
    nome VARCHAR(50) NOT NULL,
    preco DECIMAL(10,2),
    estoque INT,
	criado_em DATETIME DEFAULT(GETDATE())
)
GO

CREATE TABLE fornecedores (
    cnpj VARCHAR(18) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(30),
    tipo INT,
	criado_em DATETIME DEFAULT(GETDATE())
)
GO

CREATE TABLE clientes (
    cod_cliente INT PRIMARY KEY IDENTITY,
    nome VARCHAR(30) NOT NULL,
    endereco VARCHAR(30),
    desde DATETIME
)
GO

CREATE TABLE deliveries (
    cod_entregador INT PRIMARY KEY IDENTITY,
    nome_moto VARCHAR(30) NOT NULL,
    tipo INT
)
GO

CREATE TABLE controle_entregas (
    cod_cliente INT,
    cod_entregador INT,

    descritivo VARCHAR(100),

    PRIMARY KEY (cod_cliente, cod_entregador),

    FOREIGN KEY (cod_cliente) REFERENCES clientes(cod_cliente),
    FOREIGN KEY (cod_entregador) REFERENCES deliveries(cod_entregador)
)
GO

-- SEED

INSERT INTO produtos (nome, preco, estoque) VALUES
  ('Arroz',      5.99, 100),
  ('Feijão',     7.49,  80),
  ('Açúcar',     4.50, 120),
  ('Macarrão',   3.75, 150);
GO

INSERT INTO fornecedores (cnpj, nome, endereco, tipo) VALUES
  ('01.234.567/0001-89', 'Fornecedor Exemplo', 'Rua das Flores, 123', 1),
  ('98.765.432/0001-10', 'Alimentos LTDA',     'Av. Brasil, 456',    2);
GO

INSERT INTO clientes (nome, endereco, desde) VALUES
  ('Ana Souza',       'Rua das Palmeiras, 123', '2015-06-01'),
  ('Carlos Mendes',   'Avenida Brasil, 456',    '2018-09-15'),
  ('Fernanda Oliveira','Praça Central, 789',    '2022-02-20');
GO

INSERT INTO deliveries (nome_moto, tipo) VALUES
  ('Speed Racer', 1),
  ('Vento Forte', 2),
  ('Relâmpago Azul', 1);
GO

INSERT INTO controle_entregas (cod_cliente, cod_entregador, descritivo) VALUES
  (1, 1, 'Entrega rápida realizada com sucesso.'),
  (2, 2, 'Cliente pediu entrega expressa para endereço comercial.'),
  (3, 3, 'Pedido entregue no condomínio, sem complicações.');
GO

-- PROCEDURES

CREATE PROCEDURE _sp_inserir_produto
    @p_nome    VARCHAR(50),
    @p_preco   DECIMAL(10,2),
    @p_estoque INT
AS
BEGIN
    INSERT INTO produtos (nome, preco, estoque)
    VALUES (@p_nome, @p_preco, @p_estoque);
END;
GO

EXEC _sp_inserir_produto 'Batata', 2.99, 200;
SELECT * FROM produtos WHERE nome = 'Batata';
GO

CREATE PROCEDURE _sp_atualizar_nome_fornecedor
    @p_cnpj      VARCHAR(18),
    @p_novo_nome VARCHAR(50)
AS
BEGIN
    UPDATE fornecedores
    SET nome = @p_novo_nome
    WHERE cnpj = @p_cnpj;
END
GO

EXEC _sp_atualizar_nome_fornecedor 
     @p_cnpj      = '98.765.432/0001-10',
     @p_novo_nome = 'Alimentos e Bebidas LTDA';
SELECT * FROM fornecedores WHERE cnpj = '98.765.432/0001-10';
GO

CREATE PROCEDURE _sp_obter_entregador_por_cliente
    @p_cod_cliente INT
AS
BEGIN
    SELECT
        d.nome_moto AS nome_entregador
    FROM controle_entregas ce
    JOIN deliveries d
      ON ce.cod_entregador = d.cod_entregador
    WHERE ce.cod_cliente = @p_cod_cliente;
END
GO

EXEC _sp_obter_entregador_por_cliente @p_cod_cliente = 1;
EXEC _sp_obter_entregador_por_cliente @p_cod_cliente = 2;
EXEC _sp_obter_entregador_por_cliente @p_cod_cliente = 3;
GO