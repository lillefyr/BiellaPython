#!/usr/bin/env python3

def search(wordict, lookup):
    for key, value in wordict.items():
        if lookup.lower() == key.lower():
            return value
    return 0

wordict = {
    "purtroppo" : 2,
    "anomalia" : 1,
    "errore" : 1,
    "lamentele" : 2,
    "rimborsi" : 1,
    "disservizi" : 1,
    "ritardi" : 2,
    "problema" : 1,
    "grande": 4,
    "ringraziare": 4,
    "eccellente": 5,
    "bravissimi": 5
}

#il Punteggio dovrà considerare: 2 di “purtroppo” e 1 di “anomalia”. La media finale sarà: 1,5 quindi

Messagio1 = "Buongiorno, purtroppo si tratta della stampante principale, alla quale fano riferimento 5 colleghi per le stampe quotidiane Stiamo sollecitando la sistemazione da oltre un mese con esito vano, Vi chiedo cortesemente d'intervenire per la sistemazione dell'anomalia"

Messagio2 = "Purtroppo il dispositivo è quasi sempre in queste condizioni..se ne richiede pertanto, ASSISTENZA RISOLUTIVA, per via anche, delle continue lamentele e dei continui rimborsi ai clienti.  Cordiali Saluti"

Messagio3 = "con la presente segnaliamo numerosi disservizi alla Clientela, nelle ultime settimane, derivanti dai ritardi nella generazione/spedizione dei documenti che si aspettano.  Abbiamo difficoltà a tranquillizzare i Clienti in quanto il problema e’ diffuso e si protrae da molto tempo. Sapete dirci se e’ stata analizzata la questione e se e’ gia’ stata individuata una data potenziale di risoluzione dell’anomalia?"

Messagio4 = "Ciao, mi prendo un momento per ringraziare te e tutta la squadra per il grande lavoro che state facendo in queste settimane. Avete consentito in modo eccellente di continuare a lavorare, funzionare, servire i clienti.  Un grazie sincero.  Siete stati bravissimi. Davvero! Non ci sono tante aziende in Italia che hanno avuto la stessa continuità"

# range does NOT include the last value
for counter  in range(1, 5):
    if   counter == 1:
        Messagio = Messagio1;
    elif counter == 2:
        Messagio = Messagio2;
    elif counter == 3:
        Messagio = Messagio3;
    elif counter == 4:
        Messagio = Messagio4;
    else:
        print("go home")

    # remove chars causing trouble for split
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~’'''
    for char in Messagio:
        if char in punctuations:
           Messagio = Messagio.replace(char," ");

    # Split string into a list
    x = Messagio.split()

    # check the words from the string against the dict
    # count how many are found
    # calculate the average 
    cnt = 0
    Punteggio = 0
    for word in x:
        retval = wordict.get(word, 0)
        if retval > 0:
            cnt = cnt + 1
            Punteggio = Punteggio + retval
            print(word, " points=", Punteggio)

    if ( cnt > 0 ):
        print ("Messagio numero ", counter, " Punteggio=", Punteggio/cnt, " ", sep=" ")

        if Punteggio/cnt == 5:
             print ( "positivo" )
        elif Punteggio/cnt >= 4:
             print ( "parzialmente positivo" )
        elif Punteggio/cnt >= 3:
             print ( "neutro" )
        elif Punteggio/cnt >= 2:
             print ( "parzialmente negativo" )
        elif Punteggio/cnt >= 1:
             print ( "negativo" )
        print()
