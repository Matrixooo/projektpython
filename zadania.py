#zad1
rok_urodzenia = int(input("Podaj rok urodzenia: "))
obecny_rok = 2025
wiek = obecny_rok - rok_urodzenia

print(f"Masz {wiek} lat.")
if wiek >= 18:
    print("Jesteś pełnoletni.")
else:
    print("Jesteś niepełnoletni.")
#zad2
km = float(input("Ile kilometrów zamierzasz przejechać "))
spalanie = float(input("Podaj średnie spalanie : "))
cena_paliwa = float(input("Podaj cenę paliwa za litr: "))

paliwo = (km / 100) * spalanie
koszt = paliwo * cena_paliwa

print(f"Zużyjesz {paliwo:.2f} litrów paliwa.")
print(f"Koszt podróży: {koszt:.2f} zł")

pasazerowie = int(input("Podaj liczbę pasażerów (włącznie z Tobą): "))
cena_na_osobe = koszt / pasazerowie
print(f"Koszt na osobę: {cena_na_osobe:.2f} zł")

if km > 500:
    print("Długa trasa – zaplanuj przerwy na odpoczynek!")
    #zad3
wyniki = (45, 67, 82, 90, 55, 74, 100, 61)
srednia = sum(wyniki) / len(wyniki)
print(f"Średnia ocen: {srednia:.2f}")

powyzej_sredniej = [w for w in wyniki if w > srednia]
print("Wyniki powyżej średniej:", powyzej_sredniej)

zdali = len([w for w in wyniki if w >= 60])
print(f"Liczba osób, które zdały test: {zdali}")

if 100 in wyniki:
    print("Gratulacje dla najlepszego uczestnika!")
#zad4
produkty = ("mleko", "chleb", "masło", "ser", "jabłka", "banany", "woda", "cukier", "ryż", "kawa")

koszyk = []

for i in range(3):
    produkt = input(f"Podaj nazwę produktu nr {i+1}: ").lower().strip()
    if produkt in produkty:
        koszyk.append(produkt)
    else:
        print(f"Produkt {produkt} jest niedostępny.")

print("\nTwój koszyk (alfabetycznie):")
for p in sorted(koszyk):
    print("-", p)
    
#zad5
def analizuj_tekst(tekst):
    tekst_sformatowany = tekst.strip().lower().replace("python", "PYTHON")
    slowa = tekst_sformatowany.split()
    tekst_odwrocony = " ".join([s[::-1] for s in slowa])
    licznik = {}
    for znak in tekst_sformatowany:
        if znak.isalpha():
            licznik[znak] = licznik.get(znak, 0) + 1
    wynik = {
        "tekst_sformatowany": tekst_sformatowany,
        "tekst_odwrocony": tekst_odwrocony,
        "licznik_liter": licznik
    }
    return wynik

tekst_uzytkownika = input("Podaj tekst do analizy: ")
wynik = analizuj_tekst(tekst_uzytkownika)

print("\n--- WYNIK ANALIZY ---")
print("Sformatowany tekst:", wynik["tekst_sformatowany"])
print("Tekst z odwróconymi słowami:", wynik["tekst_odwrocony"])
print("Licznik liter:")
for litera, liczba in wynik["licznik_liter"].items():
    print(f"{litera}: {liczba}")
    
#zad6
def student_info():
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    rok = int(input("Rok studiów: "))
    kierunek = input("Kierunek studiów: ")
    oceny = input("Podaj oceny oddzielone spacją: ").split()
    oceny = [float(o) for o in oceny]
    srednia = sum(oceny) / len(oceny)
    a = float(input("Podaj długość pierwszego boku prostokąta: "))
    b = float(input("Podaj długość drugiego boku prostokąta: "))
    pole = a * b
    obwod = 2 * (a + b)
    student = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok": rok,
        "kierunek": kierunek,
        "oceny": oceny,
        "srednia_ocen": round(srednia, 2),
        "pole_prostokata": pole,
        "obwod_prostokata": obwod
    }
    return student

raport = student_info()
print("\n--- RAPORT STUDENTA ---")
for klucz, wartosc in raport.items():
    print(f"{klucz}: {wartosc}")