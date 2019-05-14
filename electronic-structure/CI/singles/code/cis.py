import numpy as np
import sys
sys.path.insert(0,"/Users/avery/git/summer-program/5/aewiens")
from uhf import UHF


class CIS:
    """
    CIS (closed-shell) computations using a UHF reference
    """

    def __init__(self,mol,mints):
        """
        Initialize cis class
        :param mol: a psi4 molecule object
        :param mints: a molecular integrals object (from psi4 MintsHelper)
        """

        uhf = UHF(mol,mints)
        uhf.get_energy()

        nbf = uhf.nbf
        self.nocc = uhf.nocc
        self.nvirt = 2*nbf - self.nocc
        #self.ndet = self.nvirt*self.nocc

        self.E0 = uhf.E
        self.e = uhf.e
        self.C = uhf.C
        self.g = uhf.g 
        self.Fmo = uhf.Fmo

    def transform_integrals(self,g,C):
        """
        :param g: 4D array of 2-electron integrals in AO basis
        :param C: 2D array of MO expansion coefficients for AO basis functions
        Return: a 4D array (same as g.size) of 2-electron integrals in MO basis
        """
        return np.einsum('Pp,Pqrs->pqrs', C,
                    np.einsum('Qq,PQrs->Pqrs', C,
                        np.einsum('Rr,PQRs->PQrs', C,
                            np.einsum('Ss,PQRS->PQRs', C, g))))

    def get_singles(self):
        """
        return a list of all possible (i,a) single excitations
        """
        return [(i,a) for i in range(self.nocc) for a in range(self.nocc,self.nocc+self.nvirt)]


    def get_energies(self):
        """ 
        Return and print an ordered list of CIS excitation energies
        """

        ## rename class variables
        E0, e, g, C, = self.E0, self.e, self.g, self.C
        Fmo = self.Fmo

        Gmo = self.transform_integrals(g,C)
        singles = self.get_singles()
        ndet = len(singles)

        ## initialize eigenvalue-shifted CIS Hamiltonian tH
        tH = np.zeros((ndet,ndet))

        ## build tH
        for P, (i,a) in enumerate(singles):
            for Q, (j,b) in enumerate(singles):
                tH[P,Q] += Gmo[a,j,i,b] + (e[a] - e[i])*(a==b)*(i==j)    # fock matrix is diagonal in MO basis
#                tH[P,Q] += Gmo[a,j,i,b] + (Fmo[a,b]*(i==j) - Fmo[i,j]*(a==b))

        ## diagonalize tH
        E, C = np.linalg.eigh(tH)

        print(C.round(4))

        print( "{:>6s}{:>15s}".format("State","Energy") )
        for i, en in enumerate(E):
            print("{:6d}  {: >16.11f}".format(i,en) )

        self.E = E
        return E
    
