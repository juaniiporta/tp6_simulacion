import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fitter import Fitter
from scipy.stats import pareto

distributions = ['pareto']

datasetArriboSemana = pd.read_csv('./#1_arribos_semana.csv', header=0)
# datasetPartidaSemana = pd.read_csv('./#2_partidas_semana.csv', header=0)
# datasetArriboFinde = pd.read_csv('./#3_arribos_finde.csv', header=0)
# datasetPartidaFinde = pd.read_csv('./#4_partidas_finde.csv', header=0)

filteredDatasetArriboSemana = datasetArriboSemana[(datasetArriboSemana.diferencia >= 0.25) & (datasetArriboSemana.diferencia <= 40)]
# filteredDatasetPartidaSemana = datasetPartidaSemana[(datasetPartidaSemana.diferencia >= 0.25) & (datasetPartidaSemana.diferencia <= 40)]
# filteredDatasetArriboFinde = datasetArriboFinde[(datasetArriboFinde.diferencia >= 0.25) & (datasetArriboFinde.diferencia <= 40)]
# filteredDatasetPartidaFinde = datasetPartidaFinde[(datasetPartidaFinde.diferencia >= 0.25) & (datasetPartidaFinde.diferencia <= 40)]

fdp_arribo_semana = Fitter(filteredDatasetArriboSemana.diferencia, distributions=distributions)
# fdp_partida_semana = Fitter(filteredDatasetPartidaSemana.diferencia, distributions=distributions)
# fdp_arribo_finde = Fitter(filteredDatasetArriboFinde.diferencia, distributions=distributions)
# fdp_partida_finde = Fitter(filteredDatasetPartidaFinde.diferencia, distributions=distributions)

fdp_arribo_semana.fit()
# fdp_partida_semana.fit()
# fdp_partida_finde.fit()
# fdp_arribo_finde.fit()

b, loc, scale = fdp_arribo_semana.fitted_param["pareto"]
# b, loc, scale = fdp_partida_semana.fitted_param["pareto"]
# b, loc, scale = fdp_arribo_finde.fitted_param["pareto"]
# b, loc, scale = fdp_partida_finde.fitted_param["pareto"]
print('\n')
print('b: ' + str(b))
print('loc: ' + str(loc))
print('scale: ' + str(scale))
print('\n')

# fdp_arribo_semana.plot_pdf(names=['pareto'], Nbest=5, lw=1, method='sumsquare_error')
# fdp_arribo_semana.hist()
# fdp_partida_semana.plot_pdf(names=['pareto'], Nbest=5, lw=2, method='sumsquare_error')
# fdp_partida_semana.hist()
# fdp_partida_finde.plot_pdf(names=['pareto'], Nbest=5, lw=3, method='sumsquare_error')
# fdp_partida_finde.hist()
# fdp_arribo_finde.plot_pdf(names=['pareto'], Nbest=5, lw=4, method='sumsquare_error')
# fdp_arribo_finde.hist()

print(fdp_arribo_semana.summary())
# print(fdp_partida_semana.summary())
# print(fdp_arribo_finde.summary())
# print(fdp_partida_finde.summary())
print('\n')

fig, ax = plt.subplots(1, 1)
x = np.linspace(0, 40)

# y = (b * (scale)**b) / ((x-loc)**(b+1))
j = 1 - ((scale/(x-loc)) ** b)

ax.set_xlim([0, 40])

# ax.plot(x, y, linewidth=2.0,marker='o')
ax.plot(x, j, linewidth=1)
# ax.plot(x, pareto.pdf(x, b, loc, scale), 'r-', lw=3, alpha=0.8, label='pareto pdf')

plt.show()
