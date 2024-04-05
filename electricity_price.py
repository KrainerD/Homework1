# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 23:04:26 2024

@author: KrainerD
"""

import numpy as np


def CRF(n, r):
    return ((1 + r) ** n * r) / ((1 + r) ** n - 1)


def fuel_costs(fuel_price, efficiency):
    return fuel_price / efficiency


def CO2_costs(CO2_price, emission_factor, efficiency):
    return (CO2_price * emission_factor) / efficiency


def electricity_prices(
        I, 
        Power, 
        operational_costs, 
        fix_costs,  
        fuel_price, 
        CO2_price, 
        emission_factor, 
        efficiency, 
        n, 
        r, 
        T,
):
    return (
        (CRF(n, r) * I / Power + fix_costs) / T 
        + operational_costs 
        + CO2_costs(CO2_price, emission_factor, efficiency) 
        + fuel_costs(fuel_price, efficiency)
    )


def Bezugsgroessen(U_N_eff, I_Str_N, f_N, T_R):
    U_bez = np.sqrt(2 / 3) * U_N_eff
    I_bez = np.sqrt(2) * I_Str_N
    Z_bez = U_bez / I_bez
    omega_el_bez = 2 * np.pi * f_N
    T_bez = 1 / omega_el_bez
    psi_bez = U_bez / omega_el_bez
    tau_R = T_R / T_bez
    return U_bez, I_bez, Z_bez, omega_el_bez, psi_bez, tau_R


print(
      round(electricity_prices(1000000, 10, 1, 1, 50 , 50, 1.5 , 0.75, 15, 0.06, 3000), 3)
)
