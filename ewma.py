"""
Anomaly detection using EWMA and Shewhart control charts
to analyse residuals

From the paper Automating Anomaly Detection by Dongyu Zheng
"""
import math

ALPHA = 0.6
LMBDA = 0.05
K = 3.


time_series = [0, 1, 2, 3, 4, 5]
final_point = time_series.pop()

y_bar = time_series[0]
s = 0
e_bar = 0

for y in time_series:
    y_hat = y_bar
    y_bar = ALPHA * y + (1 - ALPHA) * y

    e = y - y_hat
    s = (1 - LMBDA) * (s + LMBDA * (e - e_bar) ** 2)
    e_bar = (1 - LMBDA) * e + (LMBDA * e_bar)

y_hat = y_bar
e = final_point - y_hat
sigma = math.sqrt(s)
lcl = e_bar - K * sigma
ucl = e_bar + K * sigma

anaomaly = (e < lcl) or (e > ucl)
