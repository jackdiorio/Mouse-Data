import datetime
from typing import Type

# Define mouse class
class Mouse():

    # Class constructor
    def __init__(self, name :str=None, birthday :datetime=None, 
                 father :Type["Mouse"]=None, mother :Type["Mouse"]=None, 
                 agouti_pheno :str=None, agouti_a1 :str=None, agouti_a2 :str=None):
        
        self.name = name
        self.birthday = birthday
        self.father = father
        self.mother = mother

        # Phenotype for A (agouti) locus
        self.agouti_pheno = agouti_pheno

        # Genotypes for A (agouti) locus
        self.agouti_a1 = agouti_a1
        self.agouti_a2 = agouti_a2

    # Method to mate self with 'mate' and return list of hypothetical offspring
    def mate(self, mate: Type["Mouse"]) -> list:

        # 1?. get_punnett for each locus
        # 2?. process_punnet to get possible phenotypes per locus
        # 3?. somehow get possible phenotypes for all locuses

        possible_mice = [Mouse(), Mouse(), Mouse(), Mouse()]
        return possible_mice

    # Method to get punnett square for locus returned as a list with pattern:
    # [self mate]: [ a1 a1, a1 a2, a2 a1, a2 a2 ]
    def get_punnett(self, mate: Type["Mouse"], locus: str) -> list:
        punnett = []

        # Set gene list and relevant alleles based on locus
        if (locus == "A"):
            self_a1, self_a2 = self.agouti_a1, self.agouti_a2
            mate_a1, mate_a2 = mate.agouti_a1, mate.agouti_a2
        else:
            print("ERROR: A (Agouti) is the only locus currently supported")
            return punnett

        # List shows punnett square by [a1xa1, a1xa2, a2xa1, a2xa2]
        punnett.append(f"{self_a1} {mate_a1}")
        punnett.append(f"{self_a1} {mate_a2}")
        punnett.append(f"{self_a2} {mate_a1}")
        punnett.append(f"{self_a2} {mate_a2}")

        return punnett
    
    # Method to process output from get_punnett and returns phenotype
    # possibilites for a specific locus
    def process_punnett(self, punnett: list, locus: str) -> str:

        # TODO: MAKE THIS SHIT!!

        return "?"
    
    # This is called when the object is printed
    def __str__(self):
        return f"{self.name} - {self.birthday} - {self.agouti_pheno}"