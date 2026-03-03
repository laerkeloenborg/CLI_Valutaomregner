import argparse, requests

parser = argparse.ArgumentParser()
parser.add_argument("--key")
args = parser.parse_args()
api_key = None

if args.key:
    with open(".env", "w") as file:
        file.write("API_KEY=" + args.key)
    print("API key: ", args.key, " er gemt")
    api_key = args.key
else:
    try:
        with open(".env", "r") as file:
            line = file.readline()
            
            if line and "=" in line:
                api_key = line.split("=")[1]
                print("API key fundet:", api_key)
            else:
                print("Ingen API key fundet.")

    except FileNotFoundError:
        print("Ingen API key fundet.")


def get_api_data(api_key, base_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    
    response = requests.get(url)
    if response.status_code != 200:
        print("Fejl ved hentning af data")
        return None
    
    data = response.json()
    if data["result"] != "success":
        print("API fejl: ", data["error-type"])
        return None
    
    return data["conversion_rates"]

def convert_currency(amount, rate):
    return amount * rate

def main():
    print("========== VALUTA OMREGNER ===========")
    base_currency = input("Fra valuta (f.eks. DKK)").upper()
    target_currency = input("Til valuta (f.eks. USD)").upper()
    
    try:
        amount = float(input("Beløbet der omregnes: "))
    except ValueError:
        print("Beløbet er ugyldigt")
        return
    
    rates = get_api_data(api_key,base_currency)
    if rates is None:
        return
    
    if target_currency not in rates:
        print("Valutaen findes ikke")
        return
    
    rate = rates[target_currency]
    converted_amount = convert_currency(amount, rate)

    print(f"\n{amount} {base_currency} = {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    if api_key:
        main()
    else:
        print("Programmet kan ikke starte uden en API key -  Brug --key første gang.")
