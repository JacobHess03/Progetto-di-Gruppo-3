
class Centro_Revisione_Auto:
    
    def __init__(self):
        self.clienti = []

    def inserimento_cliente(self,cliente):
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
                    scelta = int(input(
                        "Inserisci il campo da modificare:\n"
                        "1. Cognome\n"
                        "2. Codice Fiscale\n"
                        "3. Numero Telefono\n"
                        "4. Data Scadenza\n"
                        "5. Nome\n"
                        "0. Esci\n> "
                    ))

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



def inserimento_cliente(Revisione):
    
    c=True
    while(c):
        
        Cliente1=Cliente()
        Revisione.inserimento_cliente(Cliente1)
        
        risp=input("vuoi inserire ancora clienti")
        if(risp.upper()=="NO"):
            
            c=False
            
            
def modifica(Revisione):
    
    cf=input("inserisci codice fiscale")
    Revisione.modifica_cliente(cf)
    
    
    

def elimina(Revisione):
    
    cf=input("inserisci codice fiscale ")
    Revisione.elimina_cliente(cf)
    
    









        
             
            

        
        
    
   








# Test semplice




centro=Centro_Revisione_Auto()

flag1=True
while(flag1):
    
    scelta=int(input("CIAO,BENVENUTO,SCEGLI UN OPZIONE :\n1.ADMIN:\2cliente"))
    
    match scelta:
        
        
        case 1:
        
                        
                while True:
                    print("\n--- Menu Principale ---")
                    print("1. Inserisci nuovo cliente")
                    print("2. Stampa clienti")
                    print("3. Esci")
                    scelta = input("Scegli un'opzione: ")

                    if scelta == "1":
                        nuovo_cliente = Cliente()
                        centro.inserimento_cliente(nuovo_cliente)
                    elif scelta == "2":
                        centro.stampa_dati()
                    elif scelta == "3":
                        print("Chiusura programma.")
                        break
                    else:
                        print("Scelta non valida.")
        
        
        case 2:
                flag=True
                clienti=[]
                C1=Centro_Revisione_Auto()
                while(flag):
                    
                    scelta=int(input("CIAO, SCEGLI UN OPZIONE: \n1Inserimento cliente\n2MODIFICA\n3ELIMINA\n4STAMPA."))
                    
                    match scelta:
                        
                        case 1:
                            
                            inserimento_cliente(C1)
                            
                        case 2:
                            
                            modifica(C1)
                            
                        case 3:
                            
                            elimina(C1)
                            
                        case 4:
                            C1.stampa_dati()
                        
                        case _:
                            
                            print("esci")
                            flag=False
                            
        case _:
            
            print("ESCI DAL SISTEMA")
            flag1=False
                
                                        
        