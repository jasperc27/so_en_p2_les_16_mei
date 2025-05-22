from verkiezing import Kandidaat, Stem, Kiezer

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self.faculteit = faculteit

    def __str__(self):
        return f"{self.naam} (Rector: {self.faculteit})"
    
class RectorStem(Stem):
    def __init__(self, kandidaat, faculteit):
        super().__init__(kandidaat)
        self.faculteit = faculteit

    def __str__(self):
        return f"Stem op {self.kandidaat} (Rector: {self.faculteit})"

if __name__ == "__main__":
    # Lijst van kandidaten
    kandidaten = [
        RectorKandidaat("Tine Baelmans", "Ingenieurswetenschappen"),
        RectorKandidaat("Peter Lievens", "Wetenschappen"),
        RectorKandidaat("Séverine Vermeire", "Geneeskunde"),
    ]

    # Lijst van kiezers
    kiezers = [
        Kiezer("Jasper"),
        Kiezer("Johannes"),
        Kiezer("Ward"),
        Kiezer("Pauline"),
    ]

    # Stemmen
    kiezers[0].stem(kandidaten[0])
    kiezers[1].stem(kandidaten[1])
    kiezers[2].stem(kandidaten[1])
    kiezers[3].stem(kandidaten[0])

    print("\nStemresultaten:")
    for kandidaat in kandidaten:
        print(f"{kandidaat}: {len(kandidaat.stemmen)} stemmen")
