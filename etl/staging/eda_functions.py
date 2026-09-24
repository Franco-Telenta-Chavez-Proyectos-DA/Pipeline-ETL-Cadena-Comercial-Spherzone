import matplotlib.pyplot as plt
import seaborn as sns


def graficar_categoricas(df):
    columnas = df.select_dtypes(include=["object", "category"]).columns

    for columna in columnas:
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df, x=columna)
        plt.title(f"Distribución de {columna}")
        plt.xlabel(columna)
        plt.ylabel("Frecuencia")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()


def graficar_numericas(df):
    columnas = df.select_dtypes(include=["int", "float"]).columns

    for columna in columnas:
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        sns.histplot(data=df, x=columna, ax=axes[0])
        axes[0].set_title(f"Distribución de {columna}")

        sns.boxplot(data=df, x=columna, ax=axes[1])
        axes[1].set_title(f"Boxplot de {columna}")

        plt.tight_layout()
        plt.show()
