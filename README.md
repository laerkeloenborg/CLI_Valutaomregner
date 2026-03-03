# CLI Valutaomregner 

Dette er en Command Line Interface (CLI) applikation til valutaomregning.  
Programmet bruger ExchangeRate-API til at hente aktuelle valutakurser.

# Krav til programmet
- Python 3 installeret
- En (gratis) API key fra: https://www.exchangerate-api.com/

# Sådan henter du projektet
- Klon projektet fra GitHub
    (bash)
    git clone <repository_url>
    cd <projekt_mappe>

- Opret virtuelt miljø og aktivér det
    (bash)
    python -m venv venv

    Windows:
    venv\Scripts\activate

    Mac/Linux:
    source venv/bin/activate

- Installér nødvendige pakker
    (bash)
    pip install requests


# Spdan kører du projektet
- Første gang / Din API key skal gemmes 
    (bash)
    python program.py --key DIN_API_KEY

- Herefter kan programmet køres uden at angive ens API key
    (bash)
    python program.py


# Når du er færdig 
- Deaktiver det virtuelle miljø
    (bash)
    deactivate
