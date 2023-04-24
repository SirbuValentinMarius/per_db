import time  # importați modulul time pentru a aștepta un timp scurt între operații
import urllib.request  # importați modulul urllib.request pentru a efectua cereri HTTP
import requests  # importați modulul requests pentru a efectua cereri HTTP
import subprocess  # Import the subprocess module
import os
import re
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
        return

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
    subprocess.run(["del", python_installer])

def pip ():
    # Adresa URL pentru fișierul get-pip.py
    url = "https://bootstrap.pypa.io/get-pip.py"

    # Numele fișierului local pentru descărcare
    filename = "get-pip.py"

    # Descărcarea fișierului get-pip.py
    urllib.request.urlretrieve(url, filename)

    # Rularea fișierului get-pip.py pentru instalarea pip
    subprocess.call(["python", filename])
    # Ștergerea fișierului get-pip.py
    os.remove("get-pip.py")

fisiere = ['gui.py', 'b_and.py','per_db.py']  # lista fișierelor care trebuie actualizate
branch = 'https://raw.githubusercontent.com/SirbuValentinMarius/per_db/master/'  # ramura unde se află noile fișiere

currentVersion = "1.0.5"  # versiunea curentă a aplicației

# efectuați o cerere GET pentru a obține versiunea curentă a aplicației de la un server web
URL = urllib.request.urlopen('https://perdb.000webhostapp.com/')
data = URL.read()
data = data.decode("utf-8")

# verificați dacă versiunea curentă a aplicației este actualizată
if (data == currentVersion):
    print("App is up to date!")
else:
    pip()
    auto_instal_python()
    #Crează fișierul requirements.txt
    os.system('pip freeze > requirements.txt')
    # Instalează modulele lipsă din requirements.txt
    os.system('pip install -r requirements.txt')


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

