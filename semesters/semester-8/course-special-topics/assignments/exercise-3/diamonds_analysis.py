# Análise diamantes - Lucas Faria (019790) e Wesley Bernardes (020321)

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

sns.set_theme()

# Carregar e filtrar fisicamente
df_raw = sns.load_dataset("diamonds").copy()
n_raw = len(df_raw)
df = df_raw[(df_raw["x"] > 0) & (df_raw["y"] > 0) & (df_raw["z"] > 0)].copy()
print(f"Removidos inválidos (x|y|z <= 0): {n_raw - len(df)} de {n_raw}")

# Ordinais → numéricos
cut_map = {"Fair":1, "Good":2, "Very Good":3, "Premium":4, "Ideal":5}
color_order = list("JIHGFED")
color_map = {c:i+1 for i,c in enumerate(color_order)}
clarity_order = ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"]
clarity_map  = {c:i+1 for i,c in enumerate(clarity_order)}
df["cut_num"] = df["cut"].map(cut_map).astype(int)
df["color_num"] = df["color"].map(color_map).astype(int)
df["clarity_num"] = df["clarity"].map(clarity_map).astype(int)

# Descritivas + outliers (±3*DP)
def desc_shape(s: pd.Series):
    return pd.Series({
        "count": s.count(), "mean": s.mean(), "median": s.median(),
        "std": s.std(ddof=1), "min": s.min(), "max": s.max(),
        "skew": s.skew(), "kurtosis_excess": s.kurt()
    })

d_price = desc_shape(df["price"]); d_carat = desc_shape(df["carat"])
p_mu, p_sd = d_price["mean"], d_price["std"]; p_lo, p_hi = p_mu - 3*p_sd, p_mu + 3*p_sd
c_mu, c_sd = d_carat["mean"], d_carat["std"]; c_lo, c_hi = c_mu - 3*c_sd, c_mu + 3*c_sd
price_out = ((df["price"] < p_lo) | (df["price"] > p_hi))
carat_out = ((df["carat"] < c_lo) | (df["carat"] > c_hi))
print("\n=== DESCRITIVAS price ===\n", d_price.round(3))
print("\n=== DESCRITIVAS carat ===\n", d_carat.round(3))
print(f"\nOutliers price (3*DP): {int(price_out.sum())} ({price_out.mean()*100:.2f}%) | lims [{p_lo:.2f}, {p_hi:.2f}]")
print(f"Outliers carat (3*DP): {int(carat_out.sum())} ({carat_out.mean()*100:.2f}%) | lims [{c_lo:.3f}, {c_hi:.3f}]")

# Histogramas (base cheia)
plt.figure(); sns.histplot(df, x="price", bins=60, kde=True)
plt.axvline(p_lo, ls="--"); plt.axvline(p_hi, ls="--")
plt.title("Figura 1 — Distribuição de Price (limites 3·DP)"); plt.tight_layout(); plt.show()

plt.figure(); sns.histplot(df, x="carat", bins=60, kde=True)
plt.axvline(c_lo, ls="--"); plt.axvline(c_hi, ls="--")
plt.title("Figura 2 — Distribuição de Carat (limites 3·DP)"); plt.tight_layout(); plt.show()

# Remover outliers de price p/ comparação e estatísticas pós-remoção
df_no_pout = df[~price_out].copy()
d_price_no = desc_shape(df_no_pout["price"]).round(3)
print("\n=== DESCRITIVAS price (sem outliers) ===\n", d_price_no)

# Histogramas (sem outliers de price)
plt.figure(); sns.histplot(df_no_pout, x="price", bins=60, kde=True)
plt.title("Figura 3 — Price sem Outliers (3·DP)"); plt.tight_layout(); plt.show()

plt.figure(); sns.histplot(df_no_pout, x="carat", bins=60, kde=True)
plt.title("Figura 4 — Carat (após remover outliers de price)"); plt.tight_layout(); plt.show()

# Figuras de outliers (boxplots, base cheia)
plt.figure(); sns.boxplot(y="price", data=df)
plt.title("Figura 5 — Outliers de Price (boxplot)"); plt.tight_layout(); plt.show()

plt.figure(); sns.boxplot(y="carat", data=df)
plt.title("Figura 6 — Outliers de Carat (boxplot)"); plt.tight_layout(); plt.show()

# price × carat
plt.figure()
sns.regplot(data=df, x="carat", y="price", scatter_kws={"alpha":0.2}, line_kws={"linewidth":2})
plt.title("Figura 7 — Preço × Quilates (carat)"); plt.tight_layout(); plt.show()

# price × cut
plt.figure()
sns.boxplot(data=df, x="cut", y="price", order=["Fair","Good","Very Good","Premium","Ideal"])
plt.title("Figura 8 — Preço por Cut"); plt.tight_layout(); plt.show()

# price × color
plt.figure()
sns.boxplot(data=df, x="color", y="price", order=color_order)
plt.title("Figura 9 — Preço por Color (J→D)"); plt.tight_layout(); plt.show()

# price × clarity
plt.figure()
sns.violinplot(data=df, x="clarity", y="price", order=clarity_order, cut=0, inner="quartile")
plt.title("Figura 10 — Preço por Clarity (I1→IF)"); plt.tight_layout(); plt.show()

# depth × table
plt.figure()
sns.scatterplot(data=df, x="depth", y="table", alpha=0.2)
plt.title("Figura 11 — Depth × Table"); plt.tight_layout(); plt.show()

# Correlações + Heatmaps
num_cols = ["price","carat","x","y","z","depth","table","cut_num","color_num","clarity_num"]
corr_p = df[num_cols].corr(method="pearson").round(3)
corr_s = df[num_cols].corr(method="spearman").round(3)
print("\nCorrelação (Pearson):\n", corr_p)
print("\nCorrelação (Spearman):\n", corr_s)

plt.figure(); sns.heatmap(corr_p, annot=True, fmt=".2f", square=True, cbar=True)
plt.title("Figura 12 — Heatmap de Correlação (Pearson)"); plt.tight_layout(); plt.show()

plt.figure(); sns.heatmap(corr_s, annot=True, fmt=".2f", square=True, cbar=True)
plt.title("Figura 13 — Heatmap de Correlação (Spearman)"); plt.tight_layout(); plt.show()

# Top correlações com price (para citar no texto)
print("\nTop correlações com price (Pearson):\n", corr_p["price"].drop("price").sort_values(ascending=False))
print("\nTop correlações com price (Spearman):\n", corr_s["price"].drop("price").sort_values(ascending=False))

# Medianas por categoria (apoia as conclusões dos box/violin)
print("\nMediana de price por CUT:\n", df.groupby("cut")["price"].median().reindex(["Fair","Good","Very Good","Premium","Ideal"]).round(0))
print("\nMediana de price por COLOR:\n", df.groupby("color")["price"].median().reindex(color_order).round(0))
print("\nMediana de price por CLARITY:\n", df.groupby("clarity")["price"].median().reindex(clarity_order).round(0))

# OLS simples (price ~ carat) para slope e R² fáceis de citar
ols_simple = sm.OLS(df["price"], sm.add_constant(df["carat"])).fit()
print("\n=== OLS price ~ carat ===")
print(f"R2: {ols_simple.rsquared:.3f} | slope(carat): {ols_simple.params['carat']:.2f} | intercept: {ols_simple.params['const']:.2f}")

# OLS múltipla (diagnóstico resumido)
X = sm.add_constant(df[["carat","cut_num","color_num","clarity_num","depth","table"]])
ols_multi = sm.OLS(df["price"], X).fit()
print("\n=== OLS price ~ carat + qualidade + geom ===")
print(f"R2: {ols_multi.rsquared:.3f}")
print(ols_multi.summary())