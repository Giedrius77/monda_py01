
#kodas pagal pavyzdi 





def income():
    pajamu_saltinis = input("Prasome ivesti pajamu saltini: ")
    suma = float(input("Iveskite suma: "))
    if pajamu_saltinis in biudzetas:
        biudzetas[pajamu_saltinis] = biudzetas[pajamu_saltinis] + suma
    else:
        biudzetas[pajamu_saltinis] = suma

def expenses():
    islaidu_pavadinimas = input("Prasome ivesti islaidu pavadinima: ")
    suma = float(input("Iveskite suma: "))
    if islaidu_pavadinimas in biudzetas:
        biudzetas[islaidu_pavadinimas] = biudzetas[islaidu_pavadinimas] - suma
    else:
        biudzetas[islaidu_pavadinimas] = -suma
    
def spausdinti_zurnala ():
    print("Biudzetao zurnalas:")
    for paskirtis, suma in biudzetas.items():
        print(f"{paskirtis}: {suma}")

def skaiciuoti_balansa():
    balansas = sum(biudzetas.values())
    print(f"Biudzeto balansas: {balansas}") 

biudzetas = {}

income()
income()
expenses()
expenses()

spausdinti_zurnala()
skaiciuoti_balansa() 