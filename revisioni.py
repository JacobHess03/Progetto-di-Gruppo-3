# Creare un gestionale di revisioni per auto:

import datetime
from datetime import datetime, timedelta

# Classe Cliente rappresenta un cliente con i suoi dati personali e le auto associate
class Cliente:
    def __init__(self, nome, cognome, codice_fiscale):
        self.nome = nome  # Nome del cliente
        self.cognome = cognome  # Cognome del cliente
        self.codice_fiscale = codice_fiscale  # Codice fiscale del cliente
        self.auto = []  # Lista delle auto associate al cliente

    # Metodo per aggiungere un'auto alla lista del cliente
    def aggiungi_auto(self, nome_auto, marca_auto, targa_auto, anno_immatricolazione, codice_fiscale):
        auto = Auto(nome_auto, marca_auto, targa_auto, anno_immatricolazione, codice_fiscale)
        self.auto.append(auto)  # Aggiunge l'auto alla lista

    # Metodo per stampare i dati del cliente
    def stampa_cliente(self):
        return f"{self.nome} {self.cognome} ({self.codice_fiscale})"

# Classe Auto rappresenta un'auto con i suoi dati e le revisioni associate
class Auto:
    def __init__(self, marca, modello, targa, anno_immatricolazione, cf):
        self.marca = marca  # Marca dell'auto
        self.modello = modello  # Modello dell'auto
        self.targa = targa  # Targa dell'auto
        self.anno_immatricolazione = anno_immatricolazione  # Anno di immatricolazione
        self.revisioni = []  # Lista di revisioni associate all'auto
        self.cf = cf  # Codice fiscale del proprietario

    # Metodo per aggiungere una revisione all'auto
    def aggiungi_revisione(self):
        costo = float(input("Inserisci il costo della revisione: "))  # Costo della revisione
        esito = input("Inserisci l'esito della revisione (ok, da rifare): ")  # Esito della revisione
        data_revisione = input("Inserisci la data della revisione (YYYY-MM-DD): ")  # Data della revisione
        self.revisioni.append({"data_revisione": data_revisione, "esito": esito, "costo": costo})  # Aggiunge la revisione alla lista

    # Metodo per visualizzare tutte le revisioni dell'auto
    def visualizza_revisioni(self):
        for revisione in self.revisioni:
            print(revisione)

    # Metodo per calcolare la scadenza della revisione (1 anno dopo la data della revisione)
    def scadenza_revisione(self):
        return self.data_revisione + timedelta(days=365)

    # Metodo per stampare i dati dell'auto
    def stampa_auto(self):
        return f"{self.marca} {self.modello} ({self.targa}, {self.anno_immatricolazione})"

# Classe GestioneRevisioni gestisce clienti, auto e revisioni
class GestioneRevisioni:
    def __init__(self):
        self.clienti = []  # Lista dei clienti
        self.revisioni = []  # Lista delle revisioni

    # Metodo per aggiungere un cliente alla lista
    def aggiungi_cliente(self, nome, cognome, codice_fiscale):
        cliente = Cliente(nome, cognome, codice_fiscale)
        self.clienti.append(cliente)

    # Metodo per aggiungere un'auto a un cliente
    def aggiungi_auto(self, auto):
        for cliente in self.clienti:
            if cliente.codice_fiscale == auto.cf:  # Verifica il codice fiscale
                cliente.aggiungi_auto(auto.marca, auto.modello, auto.targa, auto.anno_immatricolazione, auto.cf)

    # Metodo per visualizzare le auto di un cliente specifico
    def visualizza_auto_cliente(self):
        codice_fiscale = input("Inserisci il codice fiscale del cliente: ")  # Codice fiscale del cliente
        for cliente in self.clienti:
            if cliente.codice_fiscale == codice_fiscale:  # Trova il cliente
                for auto in cliente.auto:
                    print(auto.stampa_auto())  # Stampa i dati delle auto

    # Metodo per cercare un cliente tramite codice fiscale
    def ricerca_cliente(self, codice_fiscale):
        for cliente in self.clienti:
            if cliente.codice_fiscale == codice_fiscale:  # Trova il cliente
                print(cliente.stampa_cliente())
                return cliente
        return None

    # Metodo per cercare un'auto tramite targa
    def ricerca_auto(self, targa):
        for auto in self.auto:
            if auto.targa == targa:  # Trova l'auto
                return auto
        return None

    # Metodo per cercare una revisione tramite data
    def ricerca_revisione(self, data):
        for revisione in self.revisioni:
            if revisione.data_revisione == data:  # Trova la revisione
                return revisione
        return None

    # Metodo per aggiungere una revisione alla lista e associarla all'auto
    def aggiungi_revisione(self, revisione):
        self.revisioni.append(revisione)  # Aggiunge la revisione alla lista
        for auto in self.auto:
            if auto.targa == revisione.auto.targa:  # Trova l'auto associata
                auto.aggiungi_revisione(revisione)

# Creazione di un'istanza di GestioneRevisioni
G1 = GestioneRevisioni()

# Ciclo principale per interagire con l'utente
flag = True
while flag:
    scelta = int(input("Cosa vuoi scegliere: \n1.Aggiungi Cliente \n2.Aggiungi Auto per il Cliente \n3.Stampa report Clienti \n4.Uscita"))
    match scelta:
        case 1:
            # Aggiunta di un nuovo cliente
            nome = input("Inserisci il nome del cliente: ")
            cognome = input("Inserisci cognome del cliente: ")
            cf = input("Inserisci il cf: ")
            G1.aggiungi_cliente(nome, cognome, cf)

        case 2:
            # Aggiunta di un'auto per un cliente
            cf = input("Inserisci il cf: ")
            marca = input("Inserisci la marca dell'auto: ")
            modello = input("Inserisci il modello: ")
            targa = input("Targa: ")
            imma = input("Immatricolazione: ")
            A1 = Auto(marca, modello, targa, imma, cf)
            G1.aggiungi_auto(A1)

        case 3:
            # Stampa del report dei clienti e delle loro auto
            for cliente in G1.clienti:
                print(f'Nome: {cliente.nome}')
                id = 0
                for auto in cliente.auto:
                    id = id + 1
                    print(f'Auto {id}: {auto.marca}')

        case 4:
            # Uscita dal programma
            break