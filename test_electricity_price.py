# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 00:01:46 2024

@author: KrainerD
"""

from electricity_price import (
    CRF, 
    fuel_costs, 
    CO2_costs, 
    electricity_prices, 
    Bezugsgroessen,
)


def test_CRF():
    assert round(CRF(15, 0.06), 3) == 0.103


def test_fuel_costs():
    assert round(fuel_costs(50, 0.75), 3) == 66.667


def test_CO2_costs():
    assert CO2_costs(50, 1.5, 0.75) == 100


def test_electricity_prices():
    assert (
        round(
            electricity_prices(1000000, 10, 1, 1, 50 , 50, 1.5 , 0.75, 15, 0.06, 3000), 3
        ) 
        == 171.099
    )

def test_Bezugsgroessen():
    assert round(Bezugsgroessen(460, 18, 60, 212.2 * 10 ** (-3))[0], 2) == 375.59
    assert round(Bezugsgroessen(460, 18, 60, 212.2 * 10 ** (-3))[1], 2) == 25.46
    assert round(Bezugsgroessen(460, 18, 60, 212.2 * 10 ** (-3))[2], 2) == 14.75
    assert round(Bezugsgroessen(460, 18, 60, 212.2 * 10 ** (-3))[3], 2) == 376.99
    assert round(Bezugsgroessen(460, 18, 60, 212.2 * 10 ** (-3))[4], 2) == 1
    assert round(Bezugsgroessen(460, 18, 60, 212.2 * 10 ** (-3))[5], 2) == 80
    