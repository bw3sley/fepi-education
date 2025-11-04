import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")

#print(df.head())

print(f"Média do valor da conta {df['total_bill'].mean()}")
print(f"\nMédia do valor das gorjetas {df['tip'].mean()}")

print(f"\nMediana do valor da conta {df['total_bill'].median()}")
print(f"\nMediana do valor das gorjetas {df['tip'].median()}")

print(f"\nModa do valor da conta {df['total_bill'].mode()[0]}")
print(f"\nModa do valor das gorjetas {df['tip'].mode()[0]}")

print(f"\nDesvio padrão do valor da conta {df['total_bill'].std()}")
print(f"\nDesvio padrão do valor das gorjetas {df['tip'].std()}")

print(f"\nValor mínimo da conta {df['total_bill'].min()}")
print(f"\nValor mínimo das gorjetas {df['tip'].min()}")

print(f"\nValor máximo da conta {df['total_bill'].max()}")
print(f"\nValor máximo das gorjetas {df['tip'].max()}")

print(f"\nAssimetria da conta {df['total_bill'].skew()}")
print(f"\nAssimetria das gorjetas {df['tip'].skew()}")

print(f"\nCurtose da conta {df['total_bill'].kurt()}")
print(f"\nCurtose das gorjetas {df['tip'].kurt()}")

sns.histplot(df["total_bill"], kde=True, bins=30, color="skyblue")
plt.show()

sns.histplot(df["tip"], kde=True, bins=30, color="skyblue")
plt.show()

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

sns.regplot(x="total_bill", y="tip", data=df)
plt.show()

sns.regplot(x="tip", y="size", data=df)
plt.show()

#> 46,48 outlier valor da conta (média + 3*desvio-padrão)
df = df[df["total_bill"] <= 46.48]

#> 7,2 outlier gorjeta (média + 3*desvio-padrão)
df = df[df["tip"] <= 7.2]

print(f"Média do valor da conta {df['total_bill'].mean()}")
print(f"\nMédia do valor das gorjetas {df['tip'].mean()}")

print(f"\nMediana do valor da conta {df['total_bill'].median()}")
print(f"\nMediana do valor das gorjetas {df['tip'].median()}")

print(f"\nModa do valor da conta {df['total_bill'].mode()[0]}")
print(f"\nModa do valor das gorjetas {df['tip'].mode()[0]}")

print(f"\nDesvio padrão do valor da conta {df['total_bill'].std()}")
print(f"\nDesvio padrão do valor das gorjetas {df['tip'].std()}")

print(f"\nValor mínimo da conta {df['total_bill'].min()}")
print(f"\nValor mínimo das gorjetas {df['tip'].min()}")

print(f"\nValor máximo da conta {df['total_bill'].max()}")
print(f"\nValor máximo das gorjetas {df['tip'].max()}")

print(f"\nAssimetria da conta {df['total_bill'].skew()}")
print(f"\nAssimetria das gorjetas {df['tip'].skew()}")

print(f"\nCurtose da conta {df['total_bill'].kurt()}")
print(f"\nCurtose das gorjetas {df['tip'].kurt()}")

sns.histplot(df["total_bill"], kde=True, bins=30, color="skyblue")
plt.show()

sns.histplot(df["tip"], kde=True, bins=30, color="skyblue")
plt.show()

'''sns.boxplot(x=df['total_bill'])
plt.show()

sns.boxplot(x=df['tip'])
plt.show()'''


corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

sns.scatterplot(x="total_bill", y="tip", data=df)
plt.show()

sns.scatterplot(x="tip", y="size", data=df)
plt.show()

#sns.pairplot(df[['total_bill', 'tip', 'size']])
#plt.show()

'''sns.regplot(x="total_bill", y="total_bill", data=df)
plt.show()

sns.regplot(x="total_bill", y="tip", data=df)
plt.show()

sns.regplot(x="size", y="tip", data=df)
plt.show()'''

from sklearn.preprocessing import StandardScaler

'''num_cols = df.select_dtypes(include=['float64', 'int64'])

scaler = StandardScaler()
zscore_data = scaler.fit_transform(num_cols)

df_zscore = pd.DataFrame(zscore_data, columns=num_cols.columns)

print(df_zscore.head())'''


num_cols = df[["total_bill", "tip"]]

scaler = StandardScaler()
zscore_data = scaler.fit_transform(num_cols)
df_zscore = pd.DataFrame(zscore_data, columns=["total_bill_z", "tip_z"])

sns.regplot(x="total_bill_z", y="tip_z", data=df_zscore)
plt.title("Scatterplot - Dados Padronizados (Z-score)")
plt.show()

