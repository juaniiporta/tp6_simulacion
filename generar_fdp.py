import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fitter import Fitter
from scipy.stats import pareto

print("\n////////////////////////////////////////////////// Inicio //////////////////////////////////////////////////\n")

distributions = ['pareto']

datasetArriboSemana = pd.read_csv('./#1_arribos_semana.csv', header=0)
datasetPartidaSemana = pd.read_csv('./#2_partidas_semana.csv', header=0)
datasetArriboFinde = pd.read_csv('./#3_arribos_finde.csv', header=0)
datasetPartidaFinde = pd.read_csv('./#4_partidas_finde.csv', header=0)

filteredDatasetArriboSemana = datasetArriboSemana[(datasetArriboSemana.diferencia >= 1) & (datasetArriboSemana.diferencia <= 50)]
filteredDatasetPartidaSemana = datasetPartidaSemana[(datasetPartidaSemana.diferencia >= 1) & (datasetPartidaSemana.diferencia <= 50)]
filteredDatasetArriboFinde = datasetArriboFinde[(datasetArriboFinde.diferencia >= 1) & (datasetArriboFinde.diferencia <= 50)]
filteredDatasetPartidaFinde = datasetPartidaFinde[(datasetPartidaFinde.diferencia >= 1) & (datasetPartidaFinde.diferencia <= 50)]

fdp_arribo_semana = Fitter(filteredDatasetArriboSemana.diferencia, distributions=distributions)
fdp_partida_semana = Fitter(filteredDatasetPartidaSemana.diferencia, distributions=distributions)
fdp_arribo_finde = Fitter(filteredDatasetArriboFinde.diferencia, distributions=distributions)
fdp_partida_finde = Fitter(filteredDatasetPartidaFinde.diferencia, distributions=distributions)

fdp_arribo_semana.fit()
fdp_partida_semana.fit()
fdp_partida_finde.fit()
fdp_arribo_finde.fit()

print("\n////////////////////////////////////////////////// Params //////////////////////////////////////////////////\n")

print( f'Arribo semana {fdp_arribo_semana.fitted_param["pareto"]}')
print( f'Partida semana {fdp_partida_semana.fitted_param["pareto"]}')
print("\n")
print( f'Arribo finde {fdp_arribo_finde.fitted_param["pareto"]}')
print( f'Partida finde {fdp_partida_finde.fitted_param["pareto"]}')
print("\n")


# fdp_arribo_semana.plot_pdf(names=['pareto'], Nbest=5, lw=1, method='sumsquare_error')
# fdp_arribo_semana.hist()
# fdp_partida_semana.plot_pdf(names=['pareto'], Nbest=5, lw=2, method='sumsquare_error')
# fdp_partida_semana.hist()
# fdp_partida_finde.plot_pdf(names=['pareto'], Nbest=5, lw=3, method='sumsquare_error')
# fdp_partida_finde.hist()
# fdp_arribo_finde.plot_pdf(names=['pareto'], Nbest=5, lw=4, method='sumsquare_error')
# fdp_arribo_finde.hist()

# print("\n/////////////////////////////////////////////////summary//////////////////////////////////////////////////\n")

# print(fdp_arribo_semana.summary())
# print(fdp_partida_semana.summary())
# print(fdp_arribo_finde.summary())
# print(fdp_partida_finde.summary())

b = 2.8082473740799703
loc = -11.509852649735958
scale= 12.509852652735956

fig, ax = plt.subplots(1, 1)
x = np.linspace(0, 50)

# y = (b * (scale)**b) / ((x-loc)**(b+1))
j = 1 - ((scale/(x-loc)) ** b)

ax.set_xlim([0, 50])
ax.set_title="Arribos semanales"

# ax.plot(x, y, linewidth=2.0,marker='o')
ax.plot(x, j, linewidth=1)
# ax.plot(x, pareto.pdf(x, b, loc, scale), 'r-', lw=3, alpha=0.8, label='pareto pdf')

plt.show()
