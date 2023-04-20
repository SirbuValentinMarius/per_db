import time  # importați modulul time pentru a aștepta un timp scurt între operații
import urllib.request  # importați modulul urllib.request pentru a efectua cereri HTTP
import requests  # importați modulul requests pentru a efectua cereri HTTP
import subprocess # Import the subprocess module

fisiere = ['gui.py', 'b_and.py', 'per_db.py']  # lista fișierelor care trebuie actualizate
branch = 'https://raw.githubusercontent.com/SirbuValentinMarius/per_db/master/'  # ramura unde se află noile fișiere
currentVersion = "1.0.3"  # versiunea curentă a aplicației

# efectuați o cerere GET pentru a obține versiunea curentă a aplicației de la un server web
URL = urllib.request.urlopen('https://perdb.000webhostapp.com/')
data = URL.read()
data = data.decode("utf-8")

# verificați dacă versiunea curentă a aplicației este actualizată
if (data == currentVersion):
    print("App is up to date!")
else:
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

