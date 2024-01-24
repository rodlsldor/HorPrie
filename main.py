import ctypes
import sys
import test

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()
else:
    testpri = test
    url = 'https://www.mosquee-mirail-toulouse.fr/horaires-de-priere/'
    geckodriver_path = 'C:\\GeckoDriver\\geckodriver.exe'

    # Obtenir le HTML et analyser les horaires de prière
    html = testpri.get_html_from_url(url)
    prayer_times = testpri.parse_prayer_times(html)

    # Afficher les horaires récupérés
    for date, times in prayer_times.items():
        print(f"{date}: {times}")