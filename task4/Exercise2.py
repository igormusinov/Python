import numpy as np
import matplotlib.pyplot as plt

data = numpy.genfromtxt("https://raw.githubusercontent.com/anaderi/lhcb_trigger_ml/master/hep_ml/datasets/dalitzplot/bkgd.csv", skip_header=1, delimiter="\t")

plt.hist2d(data.T[0], data.T[1], bins = 42, range = [[0, 0.8], [0, 0.8]], cmap = plt.cm.Blues)
plt.colorbar()
plt.xlabel("M2AB")
plt.ylabel("M2AC")

plt.show()
