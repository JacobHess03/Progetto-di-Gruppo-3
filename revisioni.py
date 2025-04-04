# Creare un gestionale di revisioni per auto:
#1. Creare classe Cliente con i seguenti attributi:
#   - nome
#   - cognome
#   - codice fiscale
#2. Creare classe Auto con i seguenti attributi:
#   - marca
#   - modello
#   - targa
#   - anno immatricolazione
#3. Creare classe Revisione con i seguenti attributi:
#   - data revisione
#   - esito (ok, da rifare)
#   - costo
#4. Creare classe Officina con i seguenti attributi:
#   - nome
#   - indirizzo
#   - telefono
#   - email
#5. Creare classe GestioneRevisioni con i seguenti metodi:
#   - aggiungi_cliente(cliente: Cliente)
#   - aggiungi_auto(auto: Auto)
#   - aggiungi_revisione(revisione: Revisione)
#   - visualizza_clienti()
#   - visualizza_auto()
#   - visualizza_revisioni()
#   - visualizza_officina()
#   - ricerca_cliente(codice_fiscale: str)
#   - ricerca_auto(targa: str)
#   - ricerca_revisione(data: str)
#   - ricerca_officina(nome: str)
#   - modifica_cliente(codice_fiscale: str, cliente: Cliente)
#   - modifica_auto(targa: str, auto: Auto)
#   - modifica_revisione(data: str, revisione: Revisione)
#   - modifica_officina(nome: str, officina: Officina)
#   - elimina_cliente(codice_fiscale: str)
#   - elimina_auto(targa: str)
import datetime
from datetime import datetime, timedelta

class Cliente:
    def __init__(self, nome, cognome, codice_fiscale):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.auto = []
    # Aggiunge un'auto alla lista del cliente
    def aggiungi_auto(self, nome_auto, marca_auto, targa_auto, anno_immatricolazione):
        auto = Auto(nome_auto, marca_auto, targa_auto, anno_immatricolazione)
        self.auto.append(auto)
    

    def stampa_cliente(self):
        return f"{self.nome} {self.cognome} ({self.codice_fiscale})"
    
class Auto:
    
    def __init__(self, marca, modello, targa, anno_immatricolazione):
        self.marca = marca
        self.modello = modello
        self.targa = targa
        self.anno_immatricolazione = anno_immatricolazione
        self.revisioni = []  # Lista di revisioni associate all'auto
        
    def aggiungi_revisione(self):
        # Aggiunge una revisione alla lista delle revisioni dell'auto
        costo = float(input("Inserisci il costo della revisione: "))
        esito = input("Inserisci l'esito della revisione (ok, da rifare): ")
        data_revisione = input("Inserisci la data della revisione (YYYY-MM-DD): ")    
        self.revisioni.append({"data_revisione": data_revisione, "esito": esito, "costo": costo})
        
    def visualizza_revisioni(self):
        for revisione in self.revisioni:
            print(revisione)
    
    # Scadenza revisione
    def scadenza_revisione(self):
        return self.data_revisione + timedelta(days=365)  # Aggiunge un anno alla data di revisione

    def stampa_auto(self):
        return f"{self.marca} {self.modello} ({self.targa}, {self.anno_immatricolazione})"



class GestioneRevisioni:
    # Inizializza le liste per clienti, auto, revisioni e officine
    def __init__(self):
        
        self.clienti = []
        self.revisioni = []
       
    # Aggiunge un cliente alla lista
    def aggiungi_cliente(self, nome, cognome, codice_fiscale):
        cliente = Cliente(nome, cognome, codice_fiscale)
        self.clienti.append(cliente)
    
    # Aggiungere un auto ad un cliente
    def aggiungi_auto(self, auto):
        
        for cliente in self.clienti:
            if cliente.codice_fiscale == codice_fiscale:
                cliente.aggiungi_auto(auto.marca, auto.modello, auto.targa, auto.anno_immatricolazione)
        
    # Stampa le auto del cliente
    def visualizza_auto_cliente(self):
        # Trova il cliente con il codice fiscale specificato
        codice_fiscale = input("Inserisci il codice fiscale del cliente: ")
        for cliente in self.clienti:
            if cliente.codice_fiscale == codice_fiscale:
                for auto in cliente.auto:
                    print(auto.stampa_auto())
                    
    # Ricerca un cliente per codice fiscale
    def ricerca_cliente(self, codice_fiscale):
        for cliente in self.clienti:
            if cliente.codice_fiscale == codice_fiscale:
                print(cliente.stampa_cliente())
                return cliente
        return None
    # Ricerca un'auto per targa
    def ricerca_auto(self, targa):
        for auto in self.auto:
            if auto.targa == targa:
                return auto
        return None
    # Ricerca una revisione per data
    def ricerca_revisione(self, data):
        for revisione in self.revisioni:
            if revisione.data_revisione == data:
                return revisione
        return None
    # Aggiunge una revisione ad un'auto con self.revisioni essendo una lista di revisioni
    def aggiungi_revisione(self, revisione):
        self.revisioni.append(revisione)
        for auto in self.auto:
            if auto.targa == revisione.auto.targa:
                auto.aggiungi_revisione(revisione)
    
    
    
    
    

G1 = GestioneRevisioni()



flag = True
while flag:
    print("1. Aggiungi cliente")
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    codice_fiscale = input("Codice Fiscale: ")
    G1.aggiungi_cliente(nome, cognome, codice_fiscale)
    if input("Vuoi continuare? (s/n): ") == 'n':
        flag = False
print("Clienti aggiunti:")
for cliente in G1.clienti:
    print(cliente.stampa_cliente())
    
# aggiungi auto per cliente
flag = True
while flag:
    print("1. Aggiungi auto")
    marca = input("Marca: ")
    modello = input("Modello: ")
    targa = input("Targa: ")
    anno_immatricolazione = input("Anno immatricolazione: ")
    auto = Auto(marca, modello, targa, anno_immatricolazione)
    G1.aggiungi_auto(auto)
    if input("Vuoi continuare? (s/n): ") == 'n':
        flag = False

# Stampa auto aggiunte relative al cliente
print("Auto aggiunte:")
for cliente in G1.clienti:
    for auto in cliente.auto:
        print(auto.stampa_auto())
        print(cliente.stampa_cliente())



