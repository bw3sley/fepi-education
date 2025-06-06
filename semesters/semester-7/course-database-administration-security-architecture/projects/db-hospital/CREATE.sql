DROP DATABASE IF EXISTS db_hospital
GO

CREATE DATABASE db_hospital
GO

USE db_hospital
GO

CREATE TABLE hospitais (
	id INT PRIMARY KEY IDENTITY,
	nome VARCHAR(100) NOT NULL,
	cpnj VARCHAR(18) NOT NULL UNIQUE
)

CREATE TABLE alas (
	id INT PRIMARY KEY IDENTITY,
	especialidade VARCHAR(100) NOT NULL,

	id_hospital INT,

	FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
)

CREATE TABLE enfermeiras (
	id INT PRIMARY KEY IDENTITY,
	cre VARCHAR(25) NOT NULL,
	nome VARCHAR(100) NOT NULL,

	id_ala INT,

	FOREIGN KEY (id_ala) REFERENCES alas(id)
)

ALTER TABLE alas ADD id_enfermeira INT NULL;
GO

ALTER TABLE alas ADD CONSTRAINT fk_alas_chefe
FOREIGN KEY (id_enfermeira) REFERENCES enfermeiras(id);
GO

CREATE TABLE planos_saude (
	id INT PRIMARY KEY IDENTITY,
	nome VARCHAR(100) NOT NULL UNIQUE,
	tipo VARCHAR(25) NOT NULL,
	telefone VARCHAR(25),

	CONSTRAINT tipo_plano_saude CHECK (tipo IN ('particular', 'convenio_empresa'))
)

CREATE TABLE pacientes (
	id INT PRIMARY KEY IDENTITY,
	nome VARCHAR(100) NOT NULL,

	id_plano INT NOT NULL

	FOREIGN KEY (id_plano) REFERENCES planos_saude(id)
)

CREATE TABLE medicos (
	id INT PRIMARY KEY IDENTITY,

	crm INT UNIQUE,

	nome VARCHAR(100) NOT NULL,
	especialidade VARCHAR(100) NOT NULL,
)

CREATE TABLE atendimentos (
	id INT PRIMARY KEY IDENTITY,

	id_medico INT NOT NULL,
	id_paciente INT NOT NULL,

	data_hora DATETIME NOT NULL,

	FOREIGN KEY (id_medico) REFERENCES medicos(id),
	FOREIGN KEY (id_paciente) REFERENCES pacientes(id)
)

CREATE TABLE medicos_planos (
	id INT PRIMARY KEY IDENTITY,
	
	id_plano INT NOT NULL,
	id_medico INT NOT NULL,

	FOREIGN KEY (id_plano) REFERENCES planos_saude(id),
	FOREIGN KEY (id_medico) REFERENCES medicos(id)
)