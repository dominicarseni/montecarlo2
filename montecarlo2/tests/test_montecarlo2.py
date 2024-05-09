"""
Unit and regression test for the montecarlo2 package.
"""

# Import package, test suite, and other packages as needed

import pytest
import sys
import montecarlo2
from montecarlo2.bitstring import BitString
from montecarlo2.isinghamiltonian import IsingHamiltonian
import numpy as np
import networkx as nx
G=nx.graph()

def test_bitstring():
    my_bs = BitString(20)
    my_bs.set_int_config(3221)
    print(my_bs)

    # Let's make sure this worked:
    tmp = np.array([0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1])
    assert((my_bs.config == tmp).all())

    # We can provide an even stronger test here:
    for i in range(1000):
        my_bs.set_int_config(i) # Converts from integer to binary
        assert(my_bs.int() == i) # Converts back from binary to integer and tests
'''
def test_ising_compute_average_values():
    conf = BitString(6)

    # Compute the average values for Temperature = 1
    E, M, HC, MS = IsingHamiltonian.compute_average_values(conf, G, 1)


    print(" E  = %12.8f" %E)
    print(" M  = %12.8f" %M)
    print(" HC = %12.8f" %HC)
    print(" MS = %12.8f" %MS)

    assert(np.isclose(E,  -11.95991923))
    assert(np.isclose(M,   -0.00000000))
    assert(np.isclose(HC,   0.31925472))
    assert(np.isclose(MS,   0.01202961))

def test_get_lowest_energy_config():
    N=10
    
    assert(abs(IsingHamiltonian.energy(my_bs, G) - -9) < 1e-12)
'''



