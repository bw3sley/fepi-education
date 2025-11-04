# Integrantes: Wesley Bernardes (020321)

# 1) Fazendo import e carregando o dataset

import pandas as pd
import matplotlib.pyplot as plt

with open("multipleChoiceResponses.csv", "r", encoding="utf-8", errors="replace") as f:
    df = pd.read_csv(f)

# 2) Visualizando a base de dados

print("Base original:")
print(df.head())
print(df.info())

# 3.1) Removendo as duplicadas

df = df.drop_duplicates()

# 3.2) Padronizando os empregos

df['CurrentJobTitleSelect'] = df['CurrentJobTitleSelect'].str.strip().str.title()

df = df[df["CurrentJobTitleSelect"] != "Other"]

# 3.3) Padronizando os países

df["Country"] = (df["Country"].fillna("Indefinido").astype(str).str.split(",").str[0].str.strip())

df = df[df["Country"] != "Other"]

# 3.4) Padronizando as idades

df["Age_num"] = pd.to_numeric(df["Age"].astype(str).str.extract(r"(\d+)")[0], errors="coerce")

df = df[(df['Age_num'].isna()) | (df['Age_num'].between(16, 50, inclusive='both'))]

age_nonnull = df["Age_num"].dropna()

# 4) Analisando os dados

country_counts = df["Country"].value_counts()
top_country = country_counts.idxmax()
top_count = int(country_counts.max())

print(f'País que mais teve respondentes: {top_country} com {top_count} respondentes'.format(top_country, top_count))

youngest = int(age_nonnull.min())
oldest = int(age_nonnull.max())


print(f'Respondente mais novo: {youngest} Respondente mais velho: {oldest}'.format(youngest, oldest))

job_counts = df["CurrentJobTitleSelect"].dropna().value_counts()
top_job = job_counts.index[0]
top_job_count = int(job_counts.values[0])

print(f'O emprego mais comum: {top_job} com {top_job_count} respondentes'.format(top_job, top_job_count))

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

top10_countries = country_counts.head(10)
ax1 = top10_countries.plot(kind="bar")
ax1.set_title("Top 10 países com mais respondentes")
ax1.set_xlabel("País")
ax1.set_ylabel("Respondentes")
plt.xticks(rotation=30, ha="right")
add_value_labels(ax1)
plt.tight_layout()
plt.show()

top10_jobs = df["CurrentJobTitleSelect"].dropna().value_counts().head(10)
ax3 = top10_jobs.plot(kind="bar")
ax3.set_title("Top 10 cargos mais comuns")
ax3.set_xlabel("Cargo")
ax3.set_ylabel("Respondentes")
plt.xticks(rotation=30, ha="right")
add_value_labels(ax3)
plt.tight_layout()
plt.show()
