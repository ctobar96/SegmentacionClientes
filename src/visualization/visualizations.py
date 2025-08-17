import matplotlib.pyplot as plt
import seaborn as sns

def matrizCorrelacion(df, columnas):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[columnas].corr(numeric_only=True), 
                annot=True,
                fmt=".2f",
                cmap="coolwarm",
                linewidths=0.5,
                vmin=-1,
                vmax=1)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.title("Matriz de Correlación")
    plt.tight_layout()
    return plt.show()


def graficoBoxplot(rfm, columnas):
    plt.figure(figsize=(15, 8))
    for i, col in enumerate(columnas, 1):
        plt.subplot(2, 2, i)
        sns.boxplot(x=rfm[col])
        plt.title(col)

    plt.tight_layout()
    return plt.show()
