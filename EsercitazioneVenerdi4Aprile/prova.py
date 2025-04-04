class Centro_Revisione_Auto:
    
    def __init__(self):
        self.clienti = []

    def inserimento_cliente(self, cliente):
        for i in self.clienti:
            if i.cf == cliente.cf:
                print("Impossibile aggiungere utente, già esistente.")
                return
        self.clienti.append(cliente)
        print("\nUtente aggiunto con successo.")
        self.menu_gestione_cliente(cliente)

    def elimina_cliente(self, cf):
        for i in self.clienti:
            if i.cf == cf:
                self.clienti.remove(i)
                print("\nUtente eliminato con successo.")
                return
        print("Impossibile eliminare utente, poiché non presente.")

    def modifica_cliente(self, cf):
        for i in self.clienti:
            if i.cf == cf:
                while True:
                    print("\n--- Menu Modifica Cliente ---")
                    try:
                        scelta = int(input(
                            "Inserisci il campo da modificare:\n"
                            "1. Cognome\n"
                            "2. Codice Fiscale\n"
                            "3. Numero Telefono\n"
                            "4. Data Scadenza\n"
                            "5. Nome\n"
                            "0. Esci\n> "
                        ))
                    except ValueError:
                        print("Inserisci un numero valido.")
                        continue

                    if scelta == 1:
                        i.cognome = input("Inserisci nuovo cognome: ")
                    elif scelta == 2:
                        i.cf = input("Inserisci nuovo codice fiscale: ")
                    elif scelta == 3:
                        i.numero = input("Inserisci nuovo numero: ")
                    elif scelta == 4:
                        i.data_scadenza = input("Inserisci nuova data scadenza: ")
                    elif scelta == 5:
                        i.nome = input("Inserisci nuovo nome: ")
                    elif scelta == 0:
                        break
                    else:
                        print("Scelta non valida.")
                    print("Modifica effettuata.\n")
                return
        print("Cliente non trovato.")

    def stampa_dati(self):
        if not self.clienti:
            print("Nessun cliente registrato.")
            return
        for c in self.clienti:
            print(f"\nCliente: {c.nome} {c.cognome}")
            print(f"Auto: {c.auto}, Revisione entro: {c.data_scadenza}")
            print(f"Stato: {c.stato}")
            print(f"Contatto: {c.numero}, CF: {c.cf}")

    def menu_gestione_cliente(self, cliente):
        print(f"\n--- Gestione Revisione per {cliente.nome} {cliente.cognome} ---")
        scelta = input("Vuoi procedere con la revisione? (s/n): ").strip().lower()
        if scelta == 's':
            print("Il costo della revisione è di 78.75€.")
            pagamento = input("Metodo di pagamento (bancomat/contanti): ").strip().lower()
            if pagamento in ['bancomat', 'contanti']:
                cliente.stato = "Revisione completata"
                print(f"Pagamento effettuato con {pagamento}. Revisione completata con successo.")
            else:
                print("Metodo di pagamento non valido. Revisione non completata.")
        else:
            print("Revisione non eseguita. Cliente in attesa.")

class Cliente:
    def __init__(self):
        self.nome = input("Inserisci il nome: ")
        self.cognome = input("Inserisci il cognome: ")
        self.numero = input("Inserisci il numero di telefono: ")
        self.cf = input("Inserisci il codice fiscale: ")
        self.data_scadenza = input("Inserisci la data di scadenza della revisione (gg/mm/aaaa): ")
        self.auto = input("Inserisci il modello dell'auto: ")
        self.stato = "In attesa di revisione"

def inserimento_cliente(centro):
    while True:
        nuovo_cliente = Cliente()
        centro.inserimento_cliente(nuovo_cliente)
        risp = input("Vuoi inserire ancora clienti? (s/n): ").strip().lower()
        if risp == "n":
            break

def modifica(centro):
    cf = input("Inserisci codice fiscale del cliente da modificare: ")
    centro.modifica_cliente(cf)

def elimina(centro):
    cf = input("Inserisci codice fiscale del cliente da eliminare: ")
    centro.elimina_cliente(cf)

# Creazione del centro revisioni
centro = Centro_Revisione_Auto()

# Menu principale
while True:
    try:
        scelta = int(input("\nCIAO, BENVENUTO! SCEGLI UN'OPZIONE:\n1. ADMIN\n2. CLIENTE\n3. ESCI\n> "))
    except ValueError:
        print("Inserisci un numero valido.")
        continue

    match scelta:
        case 1:  # ADMIN
            while True:
                try:
                    scelta_admin = int(input("\n--- Menu Admin ---\n1. Inserisci nuovo cliente\n2. Stampa clienti\n3. Esci\n> "))
                except ValueError:
                    print("Inserisci un numero valido.")
                    continue

                match scelta_admin:
                    case 1:
                        inserimento_cliente(centro)
                    case 2:
                        centro.stampa_dati()
                    case 3:
                        print("Tornando al menu principale...")
                        break
                    case _:
                        print("Scelta non valida.")

        case 2:  # CLIENTE
            while True:
                try:
                    scelta_cliente = int(input("\n--- Menu Cliente ---\n1. Inserimento Cliente\n2. Modifica Cliente\n3. Elimina Cliente\n4. Stampa Dati\n5. Esci\n> "))
                except ValueError:
                    print("Inserisci un numero valido.")
                    continue

                match scelta_cliente:
                    case 1:
                        inserimento_cliente(centro)
                    case 2:
                        modifica(centro)
                    case 3:
                        elimina(centro)
                    case 4:
                        centro.stampa_dati()
                    case 5:
                        print("Tornando al menu principale...")
                        break
                    case _:
                        print("Scelta non valida.")

        case 3:  # USCITA
            print("Chiusura programma. Arrivederci!")
            break

        case _:
            print("Scelta non valida. Riprova.")
                                        
        