from pymongo import MongoClient
import urllib.request

URL = urllib.request.urlopen('https://perdb.000webhostapp.com/')
data = URL.read()

r=open("mongo.txt","r")
client = r.read()
r.close()

client_db = MongoClient(client)

def connect(per='user', pas='pass'):
    
    client_db = MongoClient(client)
    client_db.list_database_names()
    print("Conectare baza de date reusita")

def insert(nume: 'nume', prenume: 'prenume', organizatie: 'organizatie', nr_telefon: 'nr_telefon', e_mail: 'e_mail', utilizator: 'utilizator',  parola: 'parola', referal: "referal", pozitie:"pozitie",
           IN_numar_inregistrare :'IN_numar_inregistrare', IN_Zi_nastere:'IN_Zi_nastere',IN_Luna_nastere:'IN_Luna_nastere',IN_An_nastere:'IN_An_nastere',IN_localitatea_nasteri:'IN_localitatea_nasteri',
           IN_judet_nasteri:'IN_judet_nasteri',IN_judet_domiciliu:'IN_judet_domiciliu',IN_nr_domiciliu:'IN_nr_domiciliu', IN_bl_domiciliu:'IN_bl_domiciliu',IN_sc_domiciliu:'IN_sc_domiciliu',
           IN_et_domiciliu:'IN_et_domiciliu',IN_ap_domiciliu:'IN_ap_domiciliu',IN_serie_id:'IN_serie_id',IN_numar_id:'IN_numar_id',IN_cnp:'IN_cnp',IN_profesie:'IN_profesie',IN_ocupatie:'IN_ocupatie',
           IN_strada_domiciliu:'IN_strada_domiciliu',IN_localitatea_domiciliului:'IN_localitatea_domiciliului'
           ):
                    
    # creare baza de date care ne eintereseza
    per_db = client_db["per_db"]
    # creare colectie care ne intereseaza
    membri = per_db["membri"]
    mydict = {
        'nume': nume,
        'prenume': prenume,
        'organizatie': organizatie,
        'nr_telefon': nr_telefon,
        'e_mail': e_mail,
        'utilizator': utilizator,
        'parola': parola,
        'referal': referal,
        'pozitie': pozitie,
        'IN_numar_inregistrare': IN_numar_inregistrare,
        'IN_Luna_nastere': IN_Luna_nastere,
        'IN_Zi_nastere': IN_Zi_nastere,
        'IN_An_nastere': IN_An_nastere,
        'IN_localitatea_nasteri':IN_localitatea_nasteri,        
        'IN_judet_nasteri':IN_judet_nasteri,
        'IN_judet_domiciliu':IN_judet_domiciliu,
        'IN_nr_domiciliu':IN_nr_domiciliu,
        'IN_bl_domiciliu':IN_bl_domiciliu,
        'IN_sc_domiciliu':IN_sc_domiciliu,
        'IN_et_domiciliu':IN_et_domiciliu,
        'IN_ap_domiciliu':IN_ap_domiciliu,
        'IN_serie_id':IN_serie_id,
        'IN_numar_id':IN_numar_id,
        'IN_cnp':IN_cnp,
        'IN_profesie':IN_profesie,
        'IN_ocupatie':IN_ocupatie,
        'IN_strada_domiciliu':IN_strada_domiciliu,
        'IN_localitatea_domiciliului':IN_localitatea_domiciliului
    }
   
    x = membri.insert_one(mydict)
    


def autentificare (utilizator: 'utilizator', parola: 'parola'):
    
  
    
    # creare baza de date care ne eintereseza
    per_db = client_db["per_db"]
    # creare colectie care ne intereseza
    membri = per_db["membri"]
    myquery = {"utilizator": utilizator, "parola": parola}
    mydoc = membri.find(myquery)
    for z in mydoc:
        return z
    
    
def modifica (nume_nou : "nume_nou", prenume_nou: "prenume_nou", organizatie_nou: "organizatie_nou", nr_telefon_nou: "nr_telefon_nou", e_mail_nou: "e_mail_nou", utilizator_nou: "utilizator_nou", parola_nou: "parola_nou",
            nume_vechi: "nume_vechi", prenume_vechi: "prenume_vechi", organizatie_vechi: "organizatie_vechi", nr_telefon_vechi: "nr_telefon_vechi", e_mail_vechi: "e_mail_vechi", utilizator_vechi: "utilizator_vechi", parola_vechi: "parola_vechi"):
  
   
    # creare baza de date care ne eintereseza
    per_db = client_db["per_db"]
    # creare colectie care ne intereseza

    membri = per_db["membri"]       
   
    myquery = { 'nume': nume_vechi, "prenume": prenume_vechi, 'organizatie': organizatie_vechi, 'nr_telefon': nr_telefon_vechi, 'e_mail': e_mail_vechi, 'utilizator': utilizator_vechi, 'parola': parola_vechi}
    newvalues = { "$set": { 'nume': nume_nou, "prenume": prenume_nou,'organizatie': organizatie_nou, 'nr_telefon': nr_telefon_nou,'e_mail': e_mail_nou, 'utilizator': utilizator_nou, 'parola': parola_nou }}

    membri.update_one(myquery, newvalues)

    
def stergec (categorie:'categorie',colectie:"colectie"):
    
    # creare baza de date care ne eintereseza
    per_db = client_db["per_db"]
    # creare colectie care ne intereseza

    membri = per_db["membri"]    
        
    myquery = { categorie: {"$regex":"^"+colectie} }

    x = membri.delete_many(myquery)
    

def cauta(keie:"keie",valoare:"valoare"):
    
    # creare baza de date care ne eintereseza
    per_db = client_db["per_db"]
    # creare colectie care ne intereseza

    membri = per_db["membri"]       
    y= membri.find({keie:valoare},{"_id": 0, 'nume': 1, "prenume": 1, 'organizatie':1, 'nr_telefon': 1, 'e_mail':1, 'utilizator': 1 })
    
    for x in y :
        print(x.get("nume"),",",x.get("prenume"),",", x.get('organizatie'),",",x.get('nr_telefon'),',', x.get('e_mail'),',', x.get('utilizator'))
        

'''insert(nume= 'testB2', prenume= 'testB2', organizatie= 'organizatie', nr_telefon= 'nr_telefon', e_mail='e_mail', utilizator= 'utilizator',  parola= 'parola',referal= "referal",pozitie="pozitie")'''