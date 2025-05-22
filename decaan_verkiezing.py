from verkiezing import Kandidaat, Stem, Kiezer

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def __str__(self):
        return f"{self.naam} ({self.opleiding})"
    
class DecaanStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self.opleiding = opleiding

    def __str__(self):
        return f"Stem op {self.kandidaat} ({self.opleiding})"
    
class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def stem(self, kandidaat):
        if kandidaat.opleiding == self.opleiding:
            stem = DecaanStem(kandidaat, self.opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self.naam} heeft gestemd op {kandidaat} ({self.opleiding})")
        else:
            print(f"{self.naam} kan niet stemmen op {kandidaat} ({kandidaat.opleiding})")

if __name__ == "__main__":
    # Lijst van kandidaten
    kandidaten = [
        DecaanKandidaat("Prof. Peeters", "Informatica"),
        DecaanKandidaat("Dr. Claes", "Biologie"),
    ]

    # Lijst van kiezers
    kiezers = [
        DecaanKiezer("Emma", "Informatica"),
        DecaanKiezer("Noah", "Biologie"),
        DecaanKiezer("Liam", "Informatica"),
        DecaanKiezer("Olivia", "Geschiedenis"),  # Kan op niemand stemmen
    ]

    # Stemmen
    for kiezer in kiezers:
        for kandidaat in kandidaten:
            kiezer.stem(kandidaat)

    print("\nStemresultaten:")
    for kandidaat in kandidaten:
        print(f"{kandidaat}: {len(kandidaat.stemmen)} stemmen")
