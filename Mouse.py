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
    # [self x mate]: [ a1 x a1, a1 x a2, a2 x a1, a2 x a2 ]
    def get_punnett(self, mate: Type["Mouse"], locus: str) -> list:
        punnett = []
        genes = []  # Genes will always be least dom -> most dom
        first_dom = 0 # This variable is the first dominant index in 'genes'

        # Set above declarations (adhering to rules) based on locus
        if (locus == "A"):
            self_a1, self_a2 = self.agouti_a1, self.agouti_a2
            mate_a1, mate_a2 = mate.agouti_a1, mate.agouti_a2
            genes = ["ae","a","at","am","A","Aw","Ahvy","Avy","Ay"]
            first_dom = 4
        # TEMPORARY UNTIL OTHER LOCUS' IMPLEMENTED
        else:
            print("ERROR: A (Agouti) is the only locus currently supported")
            return punnett
        
        # Make punnett list, :<4 is extra formatting for parsing below
        punnett = [f"{self_a1:<4} {mate_a1:<4}", f"{self_a1:<4} {mate_a2:<4}", 
                   f"{self_a2:<4} {mate_a1:<4}", f"{self_a2:<4} {mate_a2:<4}"]

        # MASSIVE CODE BLOCK to verify the punnett sqaure
        for pair in punnett:
            result = ""
            self_a = pair[:4].strip() # This string parsing relies on the
            mate_a = pair[5:].strip() # spacial formatting above

            # If self_a and mate_a are dominant
            if (self_a in genes[first_dom:] and mate_a in genes[first_dom:]):
                self_a_dmnce = genes.index(self_a)
                mate_a_dmnce = genes.index(mate_a)
                # Remove less dominant one (relies on 'genes' being in order)
                if (self_a_dmnce > mate_a_dmnce):
                    result = f"{self_a}"
                else:
                    result = f"{mate_a}"
            # Both aren't dominant, if self_a is the dominant one
            elif (self_a in genes[first_dom:]):
                result = f"{self_a}"
            # If mate_a is the dominant one
            elif (mate_a in genes[first_dom:]):
                result = f"{mate_a}"
            # Ok then neither are dominant
            else:
                result = f"{self_a} {mate_a}"

            punnett[punnett.index(pair)] = result # Apply result

        return punnett
    

    
    # Method to process output from get_punnett and returns phenotype
    # possibilites for a specific locus
    def process_punnett(self, punnett: list, locus: str) -> str:

        # TODO: MAKE THIS SHIT!!

        return "?"
    
    
    
    # This is called when the object is printed
    def __str__(self):
        return f"{self.name} - {self.birthday} - {self.agouti_pheno}"