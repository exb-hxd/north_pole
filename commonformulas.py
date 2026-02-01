import numpy as np
import sympy as sy

from scipy.constants import c, hbar, electron_volt, e, epsilon_0

# eV = 1
# keV = 1e3
# MeV = 1e6
# GeV = 1e9
# TeV = 1e12


# kV = 1e3
# MV = 1e6
# GV = 1e9


energy_units = {
    "eV": 1,
    "keV":1e3,
    "MeV":1e6,
    "GeV":1e9,
    "TeV":1e12,
    "PeV":1e15
}

voltage_units={
    "V":1,
    "kV":1e3,
    "MV":1e6,
    "GV":1e9,
    "TV":1e12
}

current_units={
    "A":1,
    "mA":1e-3,
    "uA":1e-6,
    "nA":1e-9,
    "pA":1e-12
}


length_units = {
    "km":1e3,
    "m":1,
    "cm":1e-2,
    "mm":1e-3,
    "um":1e-6,
    "nm":1e-9,
    "Ang":1e-10,
    "pm":1e-12

}

# def get_units(energy_unit_key="eV", voltage_unit_key="V"):
#     energy_unit = energy_units[energy_unit_key]
#     voltage_unit = voltage_units[voltage_unit_key]
#     for key, value in energy_units.items():
#         energy_units[key] = value / energy_unit
#     for key, value in voltage_units.items():
#         voltage_units[key] = value / voltage_unit

#     constants = {
#         f"hbar_{energy_unit_key}s": hbar / electron_volt / energy_unit,
#         f"epsilon_0_e_{energy_unit_key}m": epsilon_0 / e * energy_unit
#     }

#     return energy_units, voltage_units, current_units ,constants

def get_units():
    constants = {
        f"hbar_eVs": hbar / electron_volt,
        f"epsilon_0_e_eVm": epsilon_0 / e
    }
    return energy_units, voltage_units, current_units , length_units ,constants





_2pi = np.pi*2

class beam_rigidity:
    def By(self, p, rho, q=1): #p in ev/c, q in multiples of e
        return p/(q*rho) / c
    
    def rho(self, p, By, q=1): #p in ev/c, q in multiples of e
        return p/(q*By) / c
    
    def p(self, rho, By, q=1): #p in ev/c, q in multiples of e
        return q * rho * By * c 
