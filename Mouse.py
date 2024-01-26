import datetime
from typing import Type

# Define mouse class
class Mouse():

    # Class constructor
    def __init__(self, name: str, birthday: datetime, father: Type["Mouse"], mother: Type["Mouse"], 
                 agouti_pheno, agouti_a1: str, agouti_a2: str):
        
        self.name = name
        self.birthday = birthday
        self.father = father
        self.mother = mother

        # Phenotype for A (agouti) locus
        self.agouti_pheno = agouti_pheno

        # Genotypes for A (agouti) locus
        self.agouti_a1 = agouti_a1
        self.agouti_a2 = agouti_a2

    # Method to mate self with 'mate' by punnet square under 'locus'
    def mate(self, mate: Type["Mouse"], locus: str):
        punnet = []

        # Set gene list and relevant alleles based on locus
        if (locus == "A"):
            self_a1, self_a2 = self.agouti_a1, self.agouti_a2
            mate_a1, mate_a2 = mate.agouti_a1, mate.agouti_a2
        else:
            print("ERROR: A (Agouti) is the only locus currently supported")
            return punnet

        # List shows punnet square by [a1xa1, a1xa2, a2xa1, a2xa2]
        punnet.append(f"{self_a1} {mate_a1}")
        punnet.append(f"{self_a1} {mate_a2}")
        punnet.append(f"{self_a2} {mate_a1}")
        punnet.append(f"{self_a2} {mate_a2}")

        return punnet