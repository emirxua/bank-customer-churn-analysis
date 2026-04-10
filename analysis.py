import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/churn.csv")

print(df.head())
print(df["churn"].value_counts())

print("\nAverage churn by country:")
print(df.groupby("country")["churn"].mean())

print("\nAverage churn by gender:")
print(df.groupby("gender")["churn"].mean())

print("\nAverage churn by products_number:")
print(df.groupby("products_number")["churn"].mean())


plt.figure(figsize=(6,4))
df["churn"].value_counts().plot(kind="bar")
plt.title("Churn Distribution")
plt.tight_layout()
plt.savefig("outputs/churn_distribution.png")
plt.close()


plt.figure(figsize=(6,4))
df.groupby("age")["churn"].mean().plot()
plt.title("Churn by Age")
plt.tight_layout()
plt.savefig("outputs/churn_by_age.png")
plt.close()