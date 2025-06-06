DROP DATABASE IF EXISTS exercicio_8;

CREATE DATABASE exercicio_8;
GO

USE exercicio_8;
GO

CREATE TABLE fornecedores (
    cnpj CHAR(14) NOT NULL PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    endereco VARCHAR(30) NULL,
    tipo VARCHAR(20) NULL
);
GO

CREATE TABLE entregadores (
    cod_entregador INT PRIMARY KEY IDENTITY(1,1),
    nome VARCHAR(30) NOT NULL,
    endereco VARCHAR(30) NULL,
    tipo VARCHAR(20) NULL
);
GO

CREATE TABLE caixas (
    cpf CHAR(11) NOT NULL PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    endereco VARCHAR(30) NULL,
    salario DECIMAL(18,2) NULL
);
GO

CREATE TABLE controle_entregas (
    id INT PRIMARY KEY IDENTITY(1,1),
    cpf CHAR(11) NOT NULL,
    cnpj CHAR(14) NOT NULL,
    cod_entregador INT NOT NULL,
    destino VARCHAR(30) NULL,
    FOREIGN KEY (cpf) REFERENCES caixas(cpf),
    FOREIGN KEY (cnpj) REFERENCES fornecedores(cnpj),
    FOREIGN KEY (cod_entregador) REFERENCES entregadores(cod_entregador)
);
GO

CREATE TABLE clientes (
    id_cli INT PRIMARY KEY IDENTITY(1,1),
    nome VARCHAR(30) NOT NULL,
    endereco VARCHAR(30) NULL,
    desde DATE NULL
);
GO

CREATE TABLE produtos (
    cod INT PRIMARY KEY IDENTITY(1,1),
    nome VARCHAR(30) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NULL
);
GO

CREATE TABLE fornecimentos (
    cod INT PRIMARY KEY IDENTITY(1,1),
    cnpj CHAR(14) NOT NULL,
    cod_produto INT NOT NULL,
    entrega DATE NULL,
    FOREIGN KEY (cnpj) REFERENCES fornecedores(cnpj),
    FOREIGN KEY (cod_produto) REFERENCES produtos(cod)
);
GO

CREATE TABLE vendidos (
    id INT PRIMARY KEY IDENTITY(1,1),
    cod INT NOT NULL,
    cpf CHAR(11) NOT NULL,
    data_venda DATE NULL,
    nome VARCHAR(30) NULL,
    FOREIGN KEY (cod) REFERENCES produtos(cod),
    FOREIGN KEY (cpf) REFERENCES caixas(cpf)
);
GO
