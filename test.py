from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.firefox import GeckoDriverManager

def get_html_from_url(url):
    # Configuration des options de Firefox
    options = Options()
    options.headless = True  # Mode sans tête

    # Utiliser WebDriver Manager pour gérer GeckoDriver
    service = Service(GeckoDriverManager().install())

    # Initialisation de Firefox avec Selenium
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(url)
    driver.implicitly_wait(10)  # Attendre 10 secondes pour le chargement complet

    # Obtenir le code source et fermer le navigateur
    html = driver.page_source
    driver.quit()

    return html

def parse_prayer_times(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Supposons que les horaires soient dans une table avec id='priere_hours'
    prayer_table = soup.find('table', id='horaires_table')
    if not prayer_table:
        return {"Erreur": "Table des horaires introuvable."}  # Retourner un dictionnaire avec un message d'erreur
    
    prayer_times = {}

    # Exemple d'extraction basée sur la structure HTML fournie précédemment
    for row in prayer_table.find_all('tr')[1:]:
        cells = row.find_all('td')
        if len(cells) == 6:
            # Remplacer 'span' par la balise appropriée si nécessaire
            fajr, shuruk, dhuhr, asr, maghrib, isha = [cell.find('span').text for cell in cells]
            prayer_times[row.find('td', id='priere_date').text] = {
                'Fajr': fajr, 
                'Shuruk': shuruk, 
                'Dhuhr': dhuhr, 
                'Asr': asr, 
                'Maghrib': maghrib, 
                'Isha': isha
            }
    
    return prayer_times
