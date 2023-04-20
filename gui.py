import PySimpleGUI as sg
import b_and as be
# test com
program = False
menu_def = [["Setari", ["Inscrie_Membru","membru 2",["meniu3"]]]]

autentificare = sg.Tab("Autentificare", [
    #[sg.Menu(menu_def)],
    [sg.Text("Utilizator", size = (9, 1), font = 10), sg.InputText(key = 'A_utilizator', font = 10)],
    [sg.Text("Parola", size = (9, 1), font = 10), sg.InputText(key = 'A_parola', password_char = '*', font = 10)],
    [sg.Button('Ok'), sg.Button('Inchide')]])



Inscrie_Membru = sg.Tab("Adeziuni", [
    [sg.Menu(menu_def)],
    [sg.Text(" ", size=(1, 2))],
    
    [sg.Text("Numar inregistrare", size=(15, 1), font=16), sg.Input(size=(16, 1), key="IN_numar_inregistrare")],
    [sg.Text(" ", size=(1, 2))],
    [sg.Text(" ", size=(50, 2)),
     sg.Text("Adeziune", size=(8, 1), font=16)],
    [sg.Text(" ", size=(1, 2))],
    [sg.Text("Subsemnatul ", size = (10, 1), font=16),
     sg.Text("Nume", size=(5, 1), font=16), sg.Input(size=(16, 1), key="IN_Nume"),
     sg.Text("Prenume", size=(8, 1), font=16), sg.Input(size=(16, 1), key="IN_prenume"),
     sg.Text("nascut la data de zi", size=(16, 1), font=16),
     sg.Input(size=(2, 1), key="IN_Zi_nastere", font=16),
     sg.Text("ll/", font=16),
     sg.Input(size=(2, 1), key="IN_Luna_nastere", font=16),
     sg.Text("aaaa/", font=16),
     sg.Input(size=(4, 1), key="IN_An_nastere", font=16)
    ],              
    [sg.Text("în localitatea", size = (9, 1), font = 16), sg.Input(size = (16, 1),key = "IN_localitatea_nasteri"),
     sg.Text("jud", size = (3, 1), font = 16), sg.Input(size = (16, 1),key = "IN_judet_nasteri"),
     sg.Text("domiciliat în localitatea", size=(18, 1), font=16), sg.Input(size=(16, 1), key='IN_localitatea_domiciliului'),
     sg.Text("jud", size = (3, 1), font = 16), sg.Input(size = (16, 1),key = "IN_judet_domiciliu")
    ],
     [
     sg.Text("strada", size = (5, 1), font = 16), sg.Input(size = (16, 1),key = "IN_strada_domiciliu"),
     sg.Text("nr", size = (2, 1), font = 16), sg.Input(size = (3, 1),key = "IN_nr_domiciliu"),
     sg.Text("bl", size = (2, 1), font = 16), sg.Input(size = (3, 1),key = "IN_bl_domiciliu"),
     sg.Text("sc", size = (2, 1), font = 16), sg.Input(size = (3, 1),key = "IN_sc_domiciliu"),
     sg.Text("et", size = (2, 1), font = 16), sg.Input(size = (3, 1),key = "IN_et_domiciliu"),
     sg.Text("ap", size = (2, 1), font = 16), sg.Input(size = (3, 1),key = "IN_ap_domiciliu"),
     sg.Text("posesor al BI/CI", size = (13, 1), font = 16), sg.Combo(['BI', 'CI'],key='IN_bi/ci_domicilui',default_value="CI"),         
     sg.Text("serie", size = (4, 1), font = 16), sg.Input(size = (2, 1),key = "IN_serie_id"),
     sg.Text("numar", size = (5, 1), font = 16), sg.Input(size = (6, 1),key = "IN_numar_id")
     ],
     [
     sg.Text("cnp", size = (4, 1), font = 16), sg.Input(size = (13, 1),key = "IN_cnp"),
     sg.Text("profesie", size = (9, 1), font = 16), sg.Input(size = (13, 1),key = "IN_profesie"),
     sg.Text("ocupatie", size = (9, 1), font = 16), sg.Input(size = (13, 1),key = "IN_ocupatie")
     ],
    
    [sg.Text("Organizatie : ", size = (9, 1), font = 16), sg.Input(size = (16, 1),key = "IN_organizatie"),
     sg.Text("Nr telefon : ", size = (9, 1), font = 16), sg.Input(size = (16, 1),key = "IN_nr_telefon"),
     sg.Text("e-mail : ", size = (9, 1), font = 16), sg.Input(size = (16, 1),key = "IN_e_mail")],
    [
     sg.Text("Utilizator : ", size = (9, 1), font = 16), sg.InputText(size = (16, 1),key = 'IN_utilizator'),
     sg.Text("Parola : ", size = (9, 1), font = 16), sg.InputText(size = (16, 1),key = 'IN_parola', password_char = '*'),
     sg.Text("Pozitie : ", size = (9, 1), font = 16), sg.Combo(["Membru", "Presedinte", 'Administrator'],key="membru",default_value="Membru")],
    
    
     [sg.Text(" ", size=(100, 1)),  # linie goală de text pentru a ocupa spațiul din partea dreaptă
     sg.Button('Adauga', size=(8, 1))]  # butonul mutat în partea stângă
     ])
     
    
layout = [[sg.TabGroup([[autentificare]])]]
window = sg.Window('Per Membri DB', layout,finalize=True, resizable = True,button_color='#0047bb',background_color='#2e8b57')

event, values = window.read()

while True:
    
    if event == 'Ok':
        utilizator = values['A_utilizator']
        parola = values['A_parola']
        r_autentificate = be.autentificare(utilizator = utilizator, parola = parola)
        p_nume = (r_autentificate["nume"])
        prenume = (r_autentificate["prenume"])
        organizatie = (r_autentificate["organizatie"])
        nr_telefon = (r_autentificate["nr_telefon"])
        e_mail = (r_autentificate["e_mail"])
        utilizator = (r_autentificate["utilizator"])
        parola = (r_autentificate["parola"])
        referal =  (r_autentificate["_id"])
        pozitie=(r_autentificate["pozitie"])
        
        if r_autentificate is None or r_autentificate['utilizator'] == "" and r_autentificate['parola'] == "":
            sg.popup("Utilizator sau Parola incorecta")
            break

        elif r_autentificate['utilizator'] == utilizator and r_autentificate['parola'] == parola:
            window.close()
            program=True
            break             
    elif event in (sg.WIN_CLOSED, 'Exit') or event == 'Inchide':
        break  

Datele_Tale = sg.Tab("Datele Tale", [
    # [sg.Text("Datele mele")],
    [sg.Menu(menu_def)],
    # [sg.Output(size = (100, 10), key = "output")],
    # [sg.Text("Datele tale")],
    [sg.Text("Nume : ", size = (9, 1), font = 16), sg.Input(f"{p_nume}",key = "P_Nume")],
    [sg.Text("Prenume : ", size = (9, 1), font = 16), sg.Input(f"{prenume}",key = "prenume")],
    [sg.Text("Organizatie : ", size = (9, 1), font = 16), sg.Input(f"{organizatie}",key = "organizatie")],
    [sg.Text("Nr telefon : ", size = (9, 1), font = 16), sg.Input(f"{nr_telefon}",key = "nr_telefon")],
    [sg.Text("e-mail : ", size = (9, 1), font = 16), sg.Input(f"{e_mail}",key = "e_mail")],
    [sg.Text("Utilizator : ", size = (9, 1), font = 16), sg.InputText(f"{utilizator}",key = 'utilizator')],
    [sg.Text("Parola : ", size = (9, 1), font = 16), sg.InputText(f"{parola}",key = 'parola')],
    [
        sg.Button('Actualizeaza'),
    ]])


Organizatie = sg.Tab("Organizatie", [
    
    [sg.Menu(menu_def)],
    [sg.Output(size = (80, 10), key = "output")],    
    [sg.Text("Cauta dupa  : ", size = (10, 1), font = 6)],
    [sg.Combo(['Nume', "Prenume", 'Organizatie', 'Nr_telefon', 'E_mail', 'Utilizator'], size = (8, 1), font = 10,readonly=True,key="alegere", default_value ="Nume"),
     sg.Input(key = "cauta"),],
    [
        sg.Button('Cauta'),
        sg.Button('Sterge'),
    ]])
if pozitie == "Membru":
    membru=[[sg.TabGroup([[Datele_Tale ]])],
          [sg.Button('Inchide')]]
elif pozitie=="Presedinte":
    membru=[[sg.TabGroup([[Datele_Tale, Inscrie_Membru, Organizatie ]])],
              [sg.Button('Inchide')]]

elif pozitie== 'Administrator':
    membru=[[sg.TabGroup([[Datele_Tale, Inscrie_Membru, Organizatie]])],
              [sg.Button('Inchide')]]

else:
    sg.WIN_CLOSED

my_windows= sg.Window(f'Per DB {be.data}', membru,finalize=True, resizable = True,background_color='#2e8b57',button_color='#0047bb')


while program == True:
         
    event, values = my_windows.read()
       

    if event in (sg.WIN_CLOSED, 'Exit') or event == 'Inchide':
        break
    if event == 'Adauga':
        nume = values["IN_Nume"].title()
        prenume = values["IN_prenume"].title()
        organizatie = values["IN_organizatie"].title()
        nr_telefon = values["IN_nr_telefon"]
        e_mail = values["IN_e_mail"].lower()
        utilizator = values["IN_utilizator"]
        parola = values["IN_parola"]
        pozitie = values["membru"]
        IN_numar_inregistrare = values['IN_numar_inregistrare']
        IN_Zi_nastere = values["IN_Zi_nastere"]
        IN_Luna_nastere = values['IN_Luna_nastere']
        IN_An_nastere = values['IN_An_nastere']
        IN_localitatea_nasteri = values['IN_localitatea_nasteri']
        IN_judet_nasteri = values['IN_judet_nasteri']
        IN_judet_domiciliu = values['IN_judet_domiciliu']
        IN_nr_domiciliu = values['IN_nr_domiciliu']
        IN_bl_domiciliu = values['IN_bl_domiciliu']
        IN_sc_domiciliu = values['IN_sc_domiciliu']
        IN_et_domiciliu = values['IN_et_domiciliu']
        IN_ap_domiciliu = values['IN_ap_domiciliu']
        IN_serie_id = values['IN_serie_id']
        IN_numar_id = values['IN_numar_id']
        IN_cnp = values['IN_cnp']
        IN_profesie = values['IN_profesie']
        IN_ocupatie = values['IN_ocupatie']
        IN_strada_domiciliu = values['IN_strada_domiciliu']
        IN_localitatea_domiciliului= values['IN_localitatea_domiciliului']

        be.insert(nume=nume, prenume=prenume, organizatie=organizatie, nr_telefon=nr_telefon, e_mail=e_mail,
                  utilizator=utilizator, parola=parola, referal=referal, pozitie=pozitie,
                  IN_numar_inregistrare=IN_numar_inregistrare, IN_Zi_nastere=IN_Zi_nastere,
                  IN_Luna_nastere=IN_Luna_nastere, IN_An_nastere=IN_An_nastere,
                  IN_localitatea_nasteri=IN_localitatea_nasteri,
                  IN_judet_nasteri=IN_judet_nasteri, IN_judet_domiciliu=IN_judet_domiciliu,
                  IN_nr_domiciliu=IN_nr_domiciliu, IN_bl_domiciliu=IN_bl_domiciliu,
                  IN_sc_domiciliu=IN_sc_domiciliu, IN_et_domiciliu=IN_et_domiciliu,
                  IN_ap_domiciliu=IN_ap_domiciliu, IN_serie_id=IN_serie_id, IN_numar_id=IN_numar_id, IN_cnp=IN_cnp,
                  IN_profesie=IN_profesie, IN_ocupatie=IN_ocupatie, IN_strada_domiciliu=IN_strada_domiciliu,
                  IN_localitatea_domiciliului=IN_localitatea_domiciliului)


    elif event == 'Cauta':

        my_windows["output"].update(value='')
        alegere=(values["alegere"].lower())
        cauta =(values["cauta"])
        be.cauta(keie=alegere,valoare=cauta)
        
    elif event == 'Sterge':
      
        alegere1=(values["alegere"].lower())
        cauta1 =(values["cauta"])
         
        if alegere1 == "nr_telefon" :
            be.stergec(categorie=alegere1,colectie=cauta1)
            my_windows["output"].update(value='')
        else:
            my_windows["output"].update(value='')
            print ("Doar in optiunea 'NR Telefon'se poate sterge")    
            
        
    elif event == 'Actualizeaza':
        
        r_nume =(values["P_Nume"])
        r_prenume = (values["prenume"])
        r_organizatie = (values["organizatie"])
        r_nr_telefon = (values["nr_telefon"])
        r_e_mail = (values["e_mail"])
        r_utilizator = (values["utilizator"])
        r_parola = (values["parola"])


        be.modifica( nume_nou= r_nume, prenume_nou= r_prenume, organizatie_nou= r_organizatie, nr_telefon_nou= r_nr_telefon, e_mail_nou= r_e_mail, utilizator_nou= r_utilizator, parola_nou= r_parola,
                     nume_vechi= p_nume, prenume_vechi= prenume, organizatie_vechi= organizatie, nr_telefon_vechi= nr_telefon, e_mail_vechi= e_mail, utilizator_vechi= utilizator, parola_vechi= parola)
        
    elif event == "Setari":
        pass
    elif event == 'Inchide':
        break
           
window.close()