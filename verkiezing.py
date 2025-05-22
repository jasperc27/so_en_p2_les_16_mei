class Kandidaat:
    def __init__(self, naam):
        self._naam = naam
        self._stemmen = []

    @property
    def naam(self):
        return self._naam

    @property
    def stemmen(self):
        return self._stemmen

    def geef_stem(self, stem):
        self._stemmen.append(stem)

    def __str__(self):
        return f"{self.naam}"
    
class Stem:
    def __init__(self, kandidaat):
        self.kandidaat = kandidaat

    def __str__(self):
        return f"Stem op {self.kandidaat}"
    
class Kiezer:
    def __init__(self, naam):
        self.naam = naam


    def stem(self, kandidaat):
        stem = Stem(kandidaat)
        kandidaat.geef_stem(stem)
        print(f"{self.naam} heeft gestemd op {kandidaat}")