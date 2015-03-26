from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = numpy.genfromtxt("https://raw.githubusercontent.com/anaderi/lhcb_trigger_ml/master/hep_ml/datasets/dalitzplot/bkgd.csv", skip_header=1, delimiter="\t")
    ox = data.T[0]; oy = data.T[1]
    fig = plt.figure()
    axes = Axes3D(fig)
    
    hist, x, y = np.histogram2d(ox, oy, bins = 42, range = [[0, 0.8], [0, 0.8]])
    x, y = np.meshgrid(x[:42], y[:42])
    surf = axes.plot_surface(x[:42], y[:42], hist, rstride=1, cstride=1, cmap='Blues', linewidth = 0)
    fig.colorbar(surf, shrink = 0.8, aspect = 6)
    axes.invert_yaxis()
    axes.invert_xaxis()
    axes.view_init(elev = 60, azim = -120)
    
    plt.show()
    
if __name__ == "__main__":
    main()
