# Trabalho de Análise Estatística em Dados Históricos de Criptomoedas - Lucas Faria (019790) e Wesley Bernardes (020321)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

plt.style.use("ggplot")
sns.set_palette(["#1b4965", "#ca6702", "#2a9d8f", "#f4a261", "#e76f51"])

historical_df = pd.read_csv("crypto-historical-data.csv")
historical_df["Date"] = pd.to_datetime(historical_df["Date"])

doge_data = historical_df[historical_df["ticker"] == "DOGE-USD"].copy()
doge_data["Year"] = doge_data["Date"].dt.year
doge_data["Month"] = doge_data["Date"].dt.month
doge_data["Week"] = doge_data["Date"].dt.isocalendar().week
doge_data["Year_Month"] = doge_data["Date"].dt.to_period("M")

print(f"Total de linhas no dataset: {len(historical_df)}")
print(f"Registros focados em Dogecoin: {len(doge_data)}")
print(f"Janela temporal analisada: {doge_data['Date'].min()} ate {doge_data['Date'].max()}")

# Questão 1: Qual a media e a mediana dos preços de fechamento da moeda Dogecoin?

mean_close = doge_data["Close"].mean()
median_close = doge_data["Close"].median()

print("\nQuestão 1 - Fechamento médio do Dogecoin")
print(f"Media dos preços de fechamento: ${mean_close:.6f}")
print(f"Mediana dos preços de fechamento: ${median_close:.6f}")
print(f"Comentario: A media e {'maior' if mean_close > median_close else 'menor'} que a mediana, sinal de assimetria {'positiva' if mean_close > median_close else 'negativa'}.")

# Questão 2: Compare a media e mediana do volume de negociacao. Ha indicio de assimetria?

mean_volume = doge_data["Volume"].mean()
median_volume = doge_data["Volume"].median()

print("\nQuestão 2 - Volume negociado")
print(f"Volume médio: {mean_volume:,.0f}")
print(f"Volume mediano: {median_volume:,.0f}")
print(f"Diferenca percentual: {((mean_volume - median_volume) / median_volume * 100):.2f}%")
print(f"Indício de assimetria: {'SIM' if abs(mean_volume - median_volume) / median_volume > 0.1 else 'NãO'}")

if mean_volume > median_volume:
    print("A media e bem maior que a mediana, indicando assimetria positiva e presenca de dias com volumês extremos.")

# Questão 3: Calcule a assimetria (skewness) dos preços de fechamento.

skew_close = doge_data["Close"].skew()

print("\nQuestão 3 - Assimetria dos fechamentos")
print(f"Coeficiente de assimetria: {skew_close:.4f}")
print(f"Tipo de assimetria: {'POSITIVA' if skew_close > 0 else 'NEGATIVA'}")

if skew_close > 0:
    print("Análise: Distribuição com cauda a direita, com mais valores concentrados abaixo da media e poucos pontos altos puxando a media para cima.")
else:
    print("Análise: Distribuição com cauda a esquerda, com valores mais concentrados acima da media.")

# Questão 4: Calcule a curtose (kurtosis) dos preços de fechamento.

kurt_close = doge_data["Close"].kurtosis()

print("\nQuestão 4 - Curtose dos fechamentos")
print(f"Coeficiente de curtose: {kurt_close:.4f}")

if kurt_close > 0:
    print("Tipo: LEPTOCURTICA (concentrada)")
    print("Análise: Distribuição mais concentrada no centro e com caudas pesadas, indicando maior probabilidade de valores extremos.")
elif kurt_close < 0:
    print("Tipo: PLATICURTICA (achatada)")
    print("Análise: Distribuição mais achatada que a normal, com valores mais dispersos.")
else:
    print("Tipo: MÊSOCURTICA (similar a normal)")

# Questão 5: Calcule a media e o desvio-padrao de todos os valores de fechamento.

overall_mean = doge_data["Close"].mean()
overall_std = doge_data["Close"].std()
max_close = doge_data["Close"].max()
min_close = doge_data["Close"].min()

print("\nQuestão 5 - Estatisticas gerais de fechamento")
print(f"Media: ${overall_mean:.6f}")
print(f"Desvio-padrao: ${overall_std:.6f}")
print(f"Valor maximo: ${max_close:.6f}")
print(f"Valor minimo: ${min_close:.6f}")
print(f"Amplitude: ${max_close - min_close:.6f}")

q1_close = doge_data["Close"].quantile(0.25)
q3_close = doge_data["Close"].quantile(0.75)

iqr_close = q3_close - q1_close

lower_limit = q1_close - 1.5 * iqr_close
upper_limit = q3_close + 1.5 * iqr_close
iqr_outliers = doge_data[(doge_data["Close"] < lower_limit) | (doge_data["Close"] > upper_limit)]

print("\nAnálise de outliers (metodo IQR):")
print(f"Q1 (25%): ${q1_close:.6f}")
print(f"Q3 (75%): ${q3_close:.6f}")
print(f"IQR: ${iqr_close:.6f}")
print(f"Limite inferior: ${lower_limit:.6f}")
print(f"Limite superior: ${upper_limit:.6f}")
print(f"Número de outliers: {len(iqr_outliers)} ({len(iqr_outliers)/len(doge_data)*100:.2f}% dos dados)")
print("Presenca de outliers: SIM")
print("Análise: O mercado de criptomoedas e volatil e sujeito a picos de preço, o que gera valores extremos.")

# Questão 6: Análise a distribuição dos volumês de negociacao.

skew_volume = doge_data["Volume"].skew()
kurt_volume = doge_data["Volume"].kurtosis()

print("\nQuestão 6 - Perfil dos volumês")
print(f"Assimetria: {skew_volume:.4f}")
print(f"Curtose: {kurt_volume:.4f}")

if abs(skew_volume) < 0.5:
    distribution_profile = "SIMETRICA"
elif skew_volume > 0:
    distribution_profile = "ASSIMETRICA POSITIVA"
else:
    distribution_profile = "ASSIMETRICA NEGATIVA"

if kurt_volume > 0:
    concentration_profile = "CONCENTRADA (leptocurtica)"
else:
    concentration_profile = "ACHATADA (platicurtica)"

print(f"Tipo de distribuição: {distribution_profile}")
print(f"Concentracao: {concentration_profile}")

fig_rel, axes_rel = plt.subplots(2, 2, figsize=(15, 12))
fig_rel.suptitle("Correlacoes e Tendencias do Dogecoin", fontsize=16, fontweight="bold")

correlation_open_close = doge_data["Open"].corr(doge_data["Close"])
correlation_volume_close = doge_data["Volume"].corr(doge_data["Close"])
outliers_plot = doge_data[(doge_data["Close"] < lower_limit) | (doge_data["Close"] > upper_limit)]

# Questão 7: Grafico de dispersao entre Open e Close.

print("\nQuestão 7 - Relacao entre Open e Close")
print(f"Correlação: {correlation_open_close:.4f}")

if abs(correlation_open_close) > 0.9:
    print("Análise: Correlação muito forte e positiva.")
    print("Os preços de abertura e fechamento caminham juntos, sinalizando comportamento alinhado.")

axes_rel[0, 0].scatter(doge_data["Open"], doge_data["Close"], alpha=0.55, s=20, color="#1b4965")
axes_rel[0, 0].set_xlabel("Preço de abertura (Open)")
axes_rel[0, 0].set_ylabel("Preço de fechamento (Close)")
axes_rel[0, 0].set_title("Open x Close (dispersão)")
axes_rel[0, 0].text(0.05, 0.95, f"Correlação: {correlation_open_close:.4f}",
                    transform=axes_rel[0, 0].transAxes, verticalalignment="top",
                    bbox=dict(boxstyle="round", facecolor="#fdf0d5", alpha=0.6))

# Questão 8: Grafico de dispersao entre Volume e Close.

print("\nQuestão 8 - Volume x fechamento")
print(f"Correlação: {correlation_volume_close:.4f}")

if abs(correlation_volume_close) < 0.3:
    print("Análise: correlação fraca. O volume tem pouca ligacao linear com o fechamento.")
elif abs(correlation_volume_close) < 0.7:
    print("Análise: correlação moderada. Existe relacao, mas não e determinante.")
else:
    print("Análise: correlação forte. Volume tem influencia significativa no fechamento.")

axes_rel[0, 1].scatter(doge_data["Volume"], doge_data["Close"], alpha=0.5, s=20, color="#ca6702")
axes_rel[0, 1].set_xlabel("Volume negociado")
axes_rel[0, 1].set_ylabel("Preço de fechamento (Close)")
axes_rel[0, 1].set_title("Volume x Close (nuvem de pontos)")
axes_rel[0, 1].text(0.05, 0.95, f"Correlação: {correlation_volume_close:.4f}",
                    transform=axes_rel[0, 1].transAxes, verticalalignment="top",
                    bbox=dict(boxstyle="round", facecolor="#fdf0d5", alpha=0.6))

# Questão 9: Grafico de dispersao com regressao.

print("\nQuestão 9 - Tendencia linear Open - Close")
print(f"Correlação: {correlation_open_close:.4f}")
print("Análise: A linha de tendencia confirma uma relacao linear forte e positiva.")
print("E possivel prever o fechamento a partir do valor de abertura.")

sns.regplot(data=doge_data, x="Open", y="Close", ax=axes_rel[1, 0],
            scatter_kws={"alpha":0.35, "s":20, "color":"#2a9d8f"},
            line_kws={"color":"#e76f51", "linewidth":2})
axes_rel[1, 0].set_xlabel("Preço de abertura (Open)")
axes_rel[1, 0].set_ylabel("Preço de fechamento (Close)")
axes_rel[1, 0].set_title("Tendencia linear: Open x Close")

axes_rel[1, 0].text(0.05, 0.95, f"Correlação: {correlation_open_close:.4f}\nTendencia: linear positiva",
                    transform=axes_rel[1, 0].transAxes, verticalalignment="top",
                    bbox=dict(boxstyle="round", facecolor="#fdf0d5", alpha=0.6))

# Questão 11: Outliers de preço aparecem claramente no scatterplot?

print("\nQuestão 11 - Outliers no scatterplot de preço")
print(f"Número de outliers identificados: {len(outliers_plot)}")
print("Análise: Os outliers aparecem como pontos afastados do miolo da serie.")
print("Eles representam picos de valorização ou quedas abruptas, tipicos de momentos de alta volatilidade.")

axes_rel[1, 1].scatter(doge_data["Open"], doge_data["Close"], alpha=0.5, s=20, color="#1d3557")
axes_rel[1, 1].scatter(outliers_plot["Open"], outliers_plot["Close"],
                       color="#e63946", s=55, alpha=0.75, label="Outliers")
axes_rel[1, 1].set_xlabel("Preço de abertura (Open)")
axes_rel[1, 1].set_ylabel("Preço de fechamento (Close)")
axes_rel[1, 1].set_title("Outliers de preço (Close)")
axes_rel[1, 1].legend()

fig_barras, axes_bar = plt.subplots(2, 2, figsize=(15, 12))
fig_barras.suptitle("Panorama Temporal - Barras Dogecoin", fontsize=16, fontweight="bold")

# Questão 12: Grafico de barras mostrando o preço médio de fechamento por ano.

close_by_year = doge_data.groupby("Year")["Close"].mean().sort_index()

axes_bar[0, 0].bar(close_by_year.index, close_by_year.values, color="#4c956c", edgecolor="black")
axes_bar[0, 0].set_xlabel("Ano")
axes_bar[0, 0].set_ylabel("Preço médio de fechamento ($)")
axes_bar[0, 0].set_title("Fechamento médio por ano")
axes_bar[0, 0].tick_params(axis="x", rotation=45)

for i, value in enumerate(close_by_year.values):
    axes_bar[0, 0].text(close_by_year.index[i], value, f"${value:.4f}", ha="center", va="bottom", fontsize=8)

# Questão 13: Monte um grafico de barras comparando Open e Close por semana.

doge_sample = doge_data.head(140)

weekly_means = doge_sample.groupby("Week").agg({"Open": "mean", "Close": "mean"}).head(20)

x_positions = np.arange(len(weekly_means))

bar_width = 0.35

axes_bar[0, 1].bar(x_positions - bar_width/2, weekly_means["Open"], bar_width, label="Open", alpha=0.85, color="#1b4965")
axes_bar[0, 1].bar(x_positions + bar_width/2, weekly_means["Close"], bar_width, label="Close", alpha=0.85, color="#f4a261")
axes_bar[0, 1].set_xlabel("Semana")
axes_bar[0, 1].set_ylabel("Preço médio ($)")
axes_bar[0, 1].set_title("Open x Close por semana (amostra)")
axes_bar[0, 1].set_xticks(x_positions)
axes_bar[0, 1].set_xticklabels(weekly_means.index, rotation=45, ha="right")
axes_bar[0, 1].legend()

# Questão 14: Barras com as 5 maiores medias de fechamento mensais.

top_monthly_means = doge_data.groupby("Year_Month")["Close"].mean().sort_values(ascending=False).head(5)

axes_bar[1, 0].bar(range(len(top_monthly_means)), top_monthly_means.values, color="#2a9d8f", edgecolor="black")
axes_bar[1, 0].set_xlabel("Mês")
axes_bar[1, 0].set_ylabel("Preço médio de fechamento ($)")
axes_bar[1, 0].set_title("Top 5 médias mensais de fechamento")
axes_bar[1, 0].set_xticks(range(len(top_monthly_means)))
axes_bar[1, 0].set_xticklabels([str(x) for x in top_monthly_means.index], rotation=45, ha="right")

for i, value in enumerate(top_monthly_means.values):
    axes_bar[1, 0].text(i, value, f"${value:.4f}", ha="center", va="bottom", fontsize=9)

axes_bar[1, 1].axis("off")

fig_variab, axes_var = plt.subplots(2, 2, figsize=(15, 12))
fig_variab.suptitle("Correlações e Variabilidade", fontsize=16, fontweight="bold")

# Questão 15: Existe correlação forte ou fraca entre High e Low?

correlation_high_low = doge_data["High"].corr(doge_data["Low"])

print("\nQuestão 15 - Relacao High x Low")
print(f"Correlação: {correlation_high_low:.4f}")

if abs(correlation_high_low) > 0.7:
    print("Tipo: CORRELAÇÃO FORTE")
    print("Análise: Preços maximos e minimos caminham juntos; quando o minimo cresce, o maximo tambem sobe.")

axes_var[0, 0].scatter(doge_data["Low"], doge_data["High"], alpha=0.5, s=20, color="#2a9d8f")
axes_var[0, 0].set_xlabel("Preço minimo (Low)")
axes_var[0, 0].set_ylabel("Preço máximo (High)")
axes_var[0, 0].set_title("Correlação High x Low")
axes_var[0, 0].text(0.05, 0.95, f"Correlação: {correlation_high_low:.4f}\nTipo: {'FORTE' if abs(correlation_high_low) > 0.7 else 'FRACA'}",
                    transform=axes_var[0, 0].transAxes, verticalalignment="top",
                    bbox=dict(boxstyle="round", facecolor="#fdf0d5", alpha=0.6))

# Questão 16: Qual variável apresenta maior variabilidade (desvio padrão)?

price_columns = ["Open", "Close", "High", "Low"]
price_std = [doge_data[col].std() for col in price_columns]
most_variable = price_columns[price_std.index(max(price_std))]

for i, col in enumerate(price_columns):
    print(f"{col}: {price_std[i]:.6f}")

print(f"\nMaior variabilidade: {most_variable} (desvio = {max(price_std):.6f})")
print("Análise: Maior desvio-padrão indica volatilidade mais intensa nessa variável.")

std_colors = ["#1b4965", "#ca6702", "#2a9d8f", "#f4a261"]

axes_var[0, 1].bar(price_columns, price_std, color=std_colors, edgecolor="black")
axes_var[0, 1].set_ylabel("Desvio-padrão")
axes_var[0, 1].set_title("Variabilidade das variáveis de preço")

for i, value in enumerate(price_std):
    axes_var[0, 1].text(i, value, f"{value:.4f}", ha="center", va="bottom")
axes_var[0, 1].text(0.5, 0.95, f"Maior variabilidade: {most_variable}",
                    transform=axes_var[0, 1].transAxes, ha="center", verticalalignment="top",
                    bbox=dict(boxstyle="round", facecolor="#fdf0d5", alpha=0.6))

# Questão 17: Volume diario influencia o fechamento?

correlation_volume_close_q17 = doge_data["Volume"].corr(doge_data["Close"])

print("\nQuestão 17 - Volume diario influencia o fechamento?")
print(f"Correlação: {correlation_volume_close_q17:.4f}")

if abs(correlation_volume_close_q17) < 0.3:
    print("Conclusão: Volume diario tem pouca influencia direta no fechamento.")
    print("Correlação fraca sugere que outros fatores explicam o preço.")
else:
    print("Conclusão: Mudancas no volume impactam o fechamento de forma perceptivel.")

sns.regplot(data=doge_data, x="Volume", y="Close", ax=axes_var[1, 0],
            scatter_kws={"alpha":0.35, "s":20, "color":"#1b4965"},
            line_kws={"color":"#e76f51", "linewidth":2})
axes_var[1, 0].set_xlabel("Volume diario")
axes_var[1, 0].set_ylabel("Preço de fechamento (Close)")
axes_var[1, 0].set_title("Influencia do volume no fechamento")
axes_var[1, 0].text(0.05, 0.95, f"Correlação: {correlation_volume_close_q17:.4f}",
                    transform=axes_var[1, 0].transAxes, verticalalignment="top",
                    bbox=dict(boxstyle="round", facecolor="#fdf0d5", alpha=0.6))

# Questão 18: Ha sazonalidade mensal nos preços de fechamento?

monthly_close = doge_data.groupby("Month")["Close"].mean().sort_index()
months_labels = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

print("\nQuestão 18 - Sazonalidade mensal dos fechamentos")
print("Preços médios por mês:")

for month, price in monthly_close.items():
    print(f"  {months_labels[month-1]}: ${price:.6f}")

highest_month = monthly_close.idxmax()
lowest_month = monthly_close.idxmin()

print(f"\nMês com maior preço médio: {months_labels[highest_month-1]} (${monthly_close.max():.6f})")
print(f"Mês com menor preço médio: {months_labels[lowest_month-1]} (${monthly_close.min():.6f})")

variation_pct = (monthly_close.max() - monthly_close.min()) / monthly_close.min() * 100

if variation_pct > 20:
    print(f"Conclusão: Ha sazonalidade (variacao de {variation_pct:.2f}% entre mêses).")
    print("Os preços mudam de forma relevante ao longo do ano.")
else:
    print(f"Conclusão: Baixa sazonalidade (variacao de {variation_pct:.2f}% entre mêses).")
    print("Os preços sao relativamente estaveis ao longo do ano.")

fig_sazonal, ax_season = plt.subplots(figsize=(12, 6))

ax_season.plot(monthly_close.index, monthly_close.values, marker="o", linewidth=2, markersize=8, color="#1d3557")
ax_season.set_xlabel("Mês", fontsize=12)
ax_season.set_ylabel("Preço médio de fechamento ($)", fontsize=12)
ax_season.set_title("Sazonalidade mensal nos preços de fechamento", fontsize=14, fontweight="bold")
ax_season.set_xticks(range(1, 13))
ax_season.set_xticklabels(months_labels)
ax_season.grid(True, alpha=0.3)

for i, value in enumerate(monthly_close.values):
    ax_season.text(monthly_close.index[i], value, f"${value:.4f}", ha="center", va="bottom", fontsize=8)

# Questão 19: Análise dos outliers no boxplot de fechamento.

outliers_by_year = doge_data.groupby("Year").apply(
    lambda x: len(x[(x["Close"] < q1_close - 1.5 * iqr_close) | (x["Close"] > q3_close + 1.5 * iqr_close)])
).sort_values(ascending=False)

print("\nQuestão 19 - Outliers por ano")
print("Número de outliers por ano:")

for year, count in outliers_by_year.items():
    print(f"  {year}: {count} outliers")
year_with_most = outliers_by_year.idxmax()

print(f"\nAno com mais outliers: {year_with_most} ({outliers_by_year.max()} outliers)")
print("Conclusão: Outliers não aparecem de forma uniforme; alguns anos concentram eventos extremos de preço.")

doge_data.boxplot(column="Close", by="Year", ax=axes_var[1, 1])
axes_var[1, 1].set_xlabel("Ano")
axes_var[1, 1].set_ylabel("Preço de fechamento ($)")
axes_var[1, 1].set_title("Outliers no boxplot de fechamento por ano")
plt.sca(axes_var[1, 1])
plt.xticks(rotation=45)

plt.show()