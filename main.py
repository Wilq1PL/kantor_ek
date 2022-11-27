
import time
import requests

URL = 'https://api.nbp.pl/api/exchangerates/tables/A/?format=json'




# zamiana
def zamiana(zl, waluta):


    wyn = round(zl / waluta["mid"], 2)


    time.sleep(0.25)
    print(f'Za {zl}zł możesz mieć {wyn} {waluta["currency"]}\n')

# wczytanie ilości zł
def zapytaj_o_budzet():
    zl = float(input("Podaj ile masz złotych(Pln): "))
    return zl

# menu
def zapytaj_o_walute_docelowa():
    global URL
    rezultat = requests.get(URL)

    dane = rezultat.json()
    slownik_kodow = {}
    for i, el in enumerate(dane[0]['rates']):
        print(f'{i+1}. {el["currency"]}: {el["code"]}')
        slownik_kodow[el['code']] = el
        time.sleep(0.10)
    odp = input("Wybierz walutę jaką chcesz otrzymać: ")
    odp2 = int(odp)
    odp2 = odp2 - 1
    print(f'Wybrano walutę {dane[0]["rates"][odp2]["currency"]}: {dane[0]["rates"][odp2]["code"]}')
    return dane[0]["rates"][odp2]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    zamiana(zapytaj_o_budzet(), zapytaj_o_walute_docelowa())

