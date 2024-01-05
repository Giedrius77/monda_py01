""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas
* Spausdinti pajamų/išlaidų žurnalą
* Suskaičiuoti biudžeto balansą

"""
# Mano pagal Ellie su lietuviskais terminais

def income(pajamos, suma):
    biudzetas[pajamos] = float(suma)
    return biudzetas

def expenses(islaidos, suma):
    biudzetas[islaidos] = -abs(float(suma))
    return biudzetas

biudzetas = {}

while True:
    print("""
    ---Sveiki, pasirinkite jums norima operacija---

1 - Pridekite savo pajamu saltinius ir sumas
2 - Pridekite savo islaidu apibudinimus ir sumas
3 - Parodykite visus mano pavedimus
4 - Noreciau suzinoti savo likuti

0 = Baigti apziura     
""")

    pasirinkti = input( "Iveskite skaiciu is meniu: ")
    if pasirinkti.startswith('0'):
        print("Biudzeto patikrinimas baigtas")
        break
    elif pasirinkti.startswith('1'):
        pajamos = input("Prasome ivesti pajamu saltini: ")
        suma = input("Iveskite suma: ")
        biudzetas = income(pajamos, suma)
    elif pasirinkti.startswith('2'):
        islaidos = input("Prasome ivesti islaidu pavadinima: ")
        suma = input("Iveskite suma: ")
        biudzetas = expenses(islaidos, suma)
    elif pasirinkti.startswith('3'):
        print("Tavo visi pavedimai: ")
        for key, value in biudzetas.items():
            print(f"""{key}  {value}""")
    elif pasirinkti.startswith('4'):
        print("Jusu likutis: ", sum(biudzetas.values()))
