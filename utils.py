import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def get_model():
    with open('model.txt', 'r') as f:
        theta_0 = float(f.readline())
        theta_1 = float(f.readline())

    return theta_0, theta_1


def plot_data(ax, x, y, title, normalizado):
    # Plota o gráfico dentro do eixo fornecido
    ax.scatter(x, y, color="orange")
    ax.ticklabel_format(style='plain')
    if normalizado:
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:,.0f}".replace(",", ".")))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f"{y:,.0f}".replace(",", ".")))
    ax.set_xlabel('KM')
    ax.set_ylabel('Preço')
    ax.set_title(title)

def plot_function(ax, x, y, intercept, slope, title, normalizado):
    # Plota a função linear dentro do eixo fornecido
    ax.scatter(x, y)
    ax.plot(x, slope * x + intercept, color='red')
    if normalizado:
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:,.0f}".replace(",", ".")))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f"{y:,.0f}".replace(",", ".")))
    ax.set_xlabel('KM')
    ax.set_ylabel('Preço')
    ax.set_title(title)


def plot_all(x, y, n_x, n_y, intercept, slope, n_intercept, n_slope):
    fig, axs = plt.subplots(2, 2, figsize=(10, 8), num='HEY TEAM, ENJOY THE AMPLIFIER!')

    # Plotando cada gráfico no seu respectivo eixo
    plot_data(axs[0, 0], x, y, 'Dados', True)
    plot_data(axs[0, 1], n_x, n_y, 'Dados normalizados', False)
    plot_function(axs[1, 1], n_x, n_y, n_intercept, n_slope, 'Função Linear Normalizada', False)
    plot_function(axs[1, 0], x, y, intercept, slope, 'Função Linear', True)

    # Ajustando o layout para evitar sobreposição
    plt.tight_layout()
    plt.show()