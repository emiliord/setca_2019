"""
Tests for geom_analysis.py
"""

#Install pytest: conda install pytest-cov

import geom_analysis as ga

def test_calculate_distance():
    coord1 = [0, 0, 2]
    coord2 = [0, 0, 0]

    observed = ga.calculate_distance(coord1, coord2)

    assert observed == 2

def test_bond_check_false():
    """A test for the bond_check function"""
    bond_length = 3
    observed = ga.bond_check(bond_length)
    assert observed == False

def test_bond_check_true():
    """A test for the bond_check function"""
    bond_length = 1.4
    observed = ga.bond_check(bond_length)
    assert observed == True
