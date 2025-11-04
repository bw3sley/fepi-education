# Limpeza de dados

# Integrantes: Wesley Bernardes (020321) e Lucas Faria (019790)

# 1) Fazendo import e carregando o dataset

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

# 2) Visualizando a base de dados

print("Base original:")
print(df.head())
print(df.info())

# 3.1) Removendo as duplicadas

df = df.drop_duplicates()

# 3.2) Tratando os valores nulos

df["director"] = df["director"].fillna("Desconhecido")
df["cast"] = df["cast"].fillna("Não informado")
df["country"] = df["country"].fillna("Indefinido")

# 3.3) Convertendo a coluna `date_added` para datetime

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# 3.4) Padronizando os países

df["country"] = df["country"].str.strip()
df = df[df["country"] != "Indefinido"]
df["country"] = df["country"].apply(lambda x: x.split(",")[0].strip())

# 4) Analisando os dados

conteudo = df["type"].value_counts()

paises = df["country"].value_counts().head(10)

# 5) Criando os gráficos

plt.rcParams["figure.figsize"] = (9, 5)
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.linestyle"] = ":"
plt.rcParams["grid.alpha"] = 0.4

def add_value_labels(ax):
    for p in ax.patches:
        valor = int(p.get_height())
        ax.annotate(
            f"{valor}",
            (p.get_x() + p.get_width() / 2, p.get_height()),
            ha="center", va="bottom",
            xytext=(0, 3), textcoords="offset points"
        )

ax1 = conteudo.plot(kind="bar", color=["red", "blue"])
ax1.set_title("Distribuição de Filmes e Séries na Netflix")
ax1.set_xlabel("Tipo")
ax1.set_ylabel("Quantidade")
add_value_labels(ax1)
plt.tight_layout()
plt.show()

ax2 = paises.plot(kind="bar", color="green")
ax2.set_title("Top 10 Países com Mais Títulos na Netflix")
ax2.set_xlabel("País")
ax2.set_ylabel("Quantidade")
plt.xticks(rotation=30, ha="right")
add_value_labels(ax2)
plt.tight_layout()
plt.show()