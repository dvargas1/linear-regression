#!/usr/bin/env python3

import pandas as pd

from utils import plot_all


def z_score_normalization(x):
    return (x - x.mean()) / x.std()


def gradient_descent(x, y, learning_rate, max_iterations):
    theta_0 = 0
    theta_1 = 0
    m = len(y)

    for _ in range(max_iterations):
        y_pred = theta_0 + (theta_1 * x)

        tmp_theta_0 = learning_rate * (1/m) * sum(y_pred - y)
        tmp_theta_1 = learning_rate * (1/m) * sum((y_pred - y) * x)

        theta_0 -= tmp_theta_0
        theta_1 -= tmp_theta_1

    return theta_0, theta_1


if __name__ == '__main__':
    df = pd.read_csv('dataset.csv')

    x = df['km']
    y = df['price']

    n_x = z_score_normalization(x)
    n_y = z_score_normalization(y)

    n_intercept, n_slope = gradient_descent(n_x, n_y, 0.01, 1000)

    slope = n_slope * y.std() / x.std()
    intercept = y.mean() - (slope * x.mean())

    plot_all(x, y, n_x, n_y, intercept, slope, n_intercept, n_slope)

    with open('model.txt', 'w') as f:
        f.write(f'{intercept}\n{slope}\n')