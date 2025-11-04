# Relatório de Limpeza de Dados – Netflix 🎬

**Integrantes:**  

- Wesley Bernardes (020321)  
- Lucas Faria (020321)  


## 📌 Introdução

Este projeto apresenta o processo de limpeza de dados realizado no dataset [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows), disponível na plataforma Kaggle.  

O objetivo foi organizar e padronizar a base de dados para permitir análises mais consistentes, identificando padrões e gerando insights sobre o catálogo de filmes e séries da Netflix.  

## ⚙️ Como Rodar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/bw3sley/fepi-education.git
cd fepi-education/semesters/semester-8/course-special-topics/assignments/exercise-1
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar

Você pode rodar o script Python diretamente:

## Como foi feita a limpeza

A base de dados original apresentava os seguintes problemas:

- Valores nulos em colunas como director, cast e country.
- Registros duplicados.
- Coluna `date_added` armazenada como texto.
- Inconsistências em campos de texto.

As etapas de limpeza realizadas foram:

- Remoção de duplicatas.
- Preenchimento de valores nulos com termos genéricos.
- Conversão da coluna date_added para tipo datetime.
- Padronização dos países.

## 📊 Resultados

O catálogo é predominantemente composto por filmes em comparação às séries.

Estados Unidos, Índia e Reino Unido são os países que mais contribuem com títulos na plataforma.

## ✅ Conclusão

A Netflix possui um catálogo majoritariamente de filmes, com forte concentração de produções nos Estados Unidos, Índia e Reino Unido.
O processo de limpeza foi essencial para corrigir inconsistências e permitir análises confiáveis.