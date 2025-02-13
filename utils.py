import matplotlib.pyplot as plt

def get_model():
    with open('model.txt', 'r') as f:
        theta_0 = float(f.readline())
        theta_1 = float(f.readline())

    return theta_0, theta_1


def plot_data(ax, x, y, title):
    # Plota o gráfico dentro do eixo fornecido
    ax.scatter(x, y, color="orange")
    ax.ticklabel_format(style='plain')
    ax.set_xlabel('KM')
    ax.set_ylabel('Preço')
    ax.set_title(title)

def plot_function(ax, x, y, intercept, slope, title):
    # Plota a função linear dentro do eixo fornecido
    ax.scatter(x, y)
    ax.plot(x, slope * x + intercept, color='red')
    ax.ticklabel_format(style='sci', axis='both', scilimits=(10, 10))
    ax.set_xlabel('KM')
    ax.set_ylabel('Preço')
    ax.set_title(title)


def plot_all(x, y, n_x, n_y, intercept, slope, n_intercept, n_slope):
    fig, axs = plt.subplots(2, 2, figsize=(10, 8), num='HEY TEAM, ENJOY THE AMPLIFIER!')

    # Plotando cada gráfico no seu respectivo eixo
    plot_data(axs[0, 0], x, y, 'Dados')
    plot_data(axs[0, 1], n_x, n_y, 'Dados normalizados')
    plot_function(axs[1, 1], n_x, n_y, n_intercept, n_slope, 'Função Linear Normalizada')
    plot_function(axs[1, 0], x, y, intercept, slope, 'Função Linear')

    # Ajustando o layout para evitar sobreposição
    plt.tight_layout()
    plt.show()