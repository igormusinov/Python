import matplotlib.pyplot as plt
import numpy as np

def main():
    data = numpy.genfromtxt("https://raw.githubusercontent.com/anaderi/lhcb_trigger_ml/master/hep_ml/datasets/dalitzplot/bkgd.csv", skip_header=1, delimiter="\t")
    fig = plt.figure()
    fig.subplots_adjust(bottom=0.025, left=0.025, top = 0.975, right=1.75)
    
    plt.subplot(1, 2, 1)
    plt.hist(data.T[0], bins = 30, histtype = 'step')
        
    plt.subplot(1, 2, 2)
    n, bins, patches = plt.hist(data.T[0], bins = 29, range = (0, 0.5), histtype = 'step')
    plt.xlabel('M2AB')
    plt.ylabel('N')  
    x = np.linspace(0, 0.5, 29)
    plt.errorbar(x, n, yerr = sqrt(n), elinewidth = 2, barsabove = True, linestyle = 'None', capsize = 4, ecolor = "red")
    plt.show()
    
if __name__ == "__main__":
    main()
