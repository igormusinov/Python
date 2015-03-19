import matplotlib.pyplot as plt

import numpy as nump

def main():
    data = nump.loadtxt('data/populations.txt')
    year, hares, lynxes, carrots = data.T
    year = year.astype(int)
    population = data[:, 1:]    
    species = np.array(['H', 'L', 'C'])
    
    print '1.The mean and std of the populations of each species for the years in the period.', dict(zip(species, population.mean(axis = 0)))    
    print '2.Which year each species had the largest population:', dict(zip(animals, year[population.argmax(axis=0)]))   
    print '3.Which species has the largest population for each year:', dict(zip(year, species[population.argmax(axis=1)]))    
    print '4.Which years any of the populations is above 50000:', year[[nump.any(population > 50000, axis=1)]]    
    print '5.The top 2 years for each species when they had the lowest populations:', dict(zip(species, year[populations.argsort(axis=0)[:2]].T))    
    gradient = nump.gradient(hares)
    print '6.Compare the change in hare population and the number of lynxes. Check correlation:'     
    print " Lynxes vs. Gradient Hares correlation", np.corrcoef(lynxes, gradient)[0,1]
    plt.plot(year, lynxes, year, gradient)
    plt.legend(('Lynxes', 'Gradient Hares'), loc='upper center')
    plt.show()
    
if __name__ == '__main__':
    main()
