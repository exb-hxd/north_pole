import numpy as np

def relativistics_Ekin(Ekin, E0):
    E = Ekin + E0 # [E]
    p = np.sqrt(E**2 - E0**2) # [E/c]
    beta = p/E
    gamma = 1/np.sqrt(1-beta**2)

    return {"Ekin": Ekin, "E": E, "p":p, "beta":beta, "gamma":gamma}

def relativistics_E(E, E0):
    Ekin = E - E0 # [E]
    p = np.sqrt(E**2 - E0**2) # [E/c]
    beta = p/E
    gamma = 1/np.sqrt(1-beta**2)

    return {"Ekin": Ekin, "E": E, "p":p, "beta":beta, "gamma":gamma}


def relativistics_p(p, E0):
    E = np.sqrt(p**2 + E0**2) 
    Ekin = E - E0
    beta = p/E
    gamma = 1/np.sqrt(1-beta**2)

    return {"E": E, "Ekin": Ekin, "p" :p, "beta":beta, "gamma":gamma}

def relativistics_beta(beta, E0):
    gamma = 1/np.sqrt(1-beta**2)
    p = E0 * gamma * beta
    E = E0 * gamma
    Ekin = E - E0

    return {"E": E, "Ekin": Ekin, "p" :p, "beta":beta, "gamma":gamma}

def relativistics_gamma(gamma, E0):
    beta = np.sqrt(1-1/gamma**2)
    p = E0 * gamma * beta
    E = E0 * gamma
    Ekin = E - E0

    return {"E": E, "Ekin": Ekin, "p" :p, "beta":beta, "gamma":gamma}


class relativistics:
    def __init__(self, E0):
        self.E0 = E0


    def given_E(self, E):
        return relativistics_E(E, self.E0)
    def given_Ekin(self, Ekin):
        return relativistics_Ekin(Ekin, self.E0)
    def given_p(self, p):
        return relativistics_p(p, self.E0)
    def given_beta(self, beta):
        return relativistics_beta(beta, self.E0)
    def given_gamma(self, gamma):
        return relativistics_gamma(gamma, self.E0)
    


def Deltap_p(deltaE_E, beta):
    return 1/beta**2 * deltaE_E

def DeltaE_E(deltap_p, beta):
    return beta**2 * deltap_p