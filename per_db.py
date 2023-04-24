import time  # importați modulul time pentru a aștepta un timp scurt între operații
import urllib.request  # importați modulul urllib.request pentru a efectua cereri HTTP
import requests
import subprocess  # Import the subprocess module
import os
import re
versiune='1.0.6'
def auto_instal_python():
    # Descărcarea paginii cu lista de versiuni Python disponibile
    url = "https://www.python.org/downloads/"
    response = urllib.request.urlopen(url)
    html = response.read().decode()

    # Căutarea celei mai recente versiuni Python
    version_pattern = r'href="/downloads/release/python-([\d.]+)">Python [\d.]+</a>'
    versions = re.findall(version_pattern, html)

    if not versions:
        print("Nu s-a găsit nicio versiune validă a Python.")
    else:
        latest_version = versions[0]

        # URL-ul de descărcare al fișierului de instalare Python
        python_url = f"https://www.python.org/ftp/python/{latest_version}/python-{latest_version}-amd64.exe"

        # Numele fișierului de instalare
        python_installer = "python_installer.exe"

        # Descărcarea fișierului de instalare
        print(f"Descărcare Python {latest_version}...")
        urllib.request.urlretrieve(python_url, python_installer)

        # Instalarea Python automat
        print(f"Instalare Python {latest_version}...")
        subprocess.run([python_installer, "/quiet", "InstallAllUsers=1", "PrependPath=1"])

        # Ștergerea fișierului de instalare
        print("Ștergere fișier de instalare...")
        os.remove(python_installer)

        # Ștergerea versiunilor vechi de Python
        print("Ștergere versiuni vechi de Python...")
        python_dir_pattern = r'C:\\Python[\d.]+'
        dirs_to_remove = [d for d in os.listdir("C:\\") if re.match(python_dir_pattern, d)]

        for d in dirs_to_remove:
            print(f"Ștergere {d}...")
            os.system(f"rd /s /q C:\\{d}")


def pip ():
    # Verificarea versiunii instalate de pip
    subprocess.check_call(['python', '-m', 'pip', '--version'])
    # Instalarea ultimei versiuni de pip
    subprocess.check_call(['python', '-m', 'ensurepip', '--upgrade'])

pip ()

fisiere = ['gui.py', 'b_and.py','per_db.py']  # lista fișierelor care trebuie actualizate
branch = 'https://raw.githubusercontent.com/SirbuValentinMarius/per_db/master/'  # ramura unde se află noile fișiere

currentVersion = versiune # versiunea curentă a aplicației

# efectuați o cerere GET pentru a obține versiunea curentă a aplicației de la un server web
URL = urllib.request.urlopen('https://perdb.000webhostapp.com/')
data = URL.read()
data = data.decode("utf-8")

# verificați dacă versiunea curentă a aplicației este actualizată
if (data == currentVersion):
    print("App is up to date!")
else:

    auto_instal_python()
    # dacă nu este actualizată, descărcați și instalați noile fișiere
    print(f'App is not up to date! App is on version  {currentVersion}   but could be on version  {data}  !')
    print("Downloading new version now!")
    for fisier in fisiere:
        newVersion = requests.get(f"{branch}{fisier}")  # descărcați noua versiune a fișierului
        open(fisier , "wb").write(newVersion.content)  # salvați noua versiune a fișierului
        print(fisier)
    time.sleep(1)  # așteptați un timp scurt pentru a permite descărcarea să se finalizeze
# Deschideți un nou proces și rulați fișierul „gui.py” folosind comanda „python”.
# „creationflags” este folosit pentru a transmite un steag procesului care indică faptul că noua fereastră ar trebui să fie ascunsă
subprocess.Popen(["python", "gui.py"], creationflags=subprocess.CREATE_NO_WINDOW)

