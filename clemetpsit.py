#Creare nel linguaggio di programmazione che preferisci (PHP, C#, Java, ...) una classe (ad es. EsprReg) che data una espressione regolare e una stringa valida quest'ultima, ovvero restituisce a video il testo "match" oppure "mismatch".
#In particolare si vogliono vedere:
#1. attributi e metodi con gli opportuni modificatori di classe
#2. almeno due metodi di cui uno che riceve in input l'espressione regolare e l'altro che effettua il test per la validazione e restituisce l'output suddetto
#3a. il costruttore della vostra classe (potete anche estenderne una già prevista se preferite) e un'istanza della vostra classe nel main in cui vengono richiamati i metodi di cui sopra 
#3b. in alternativa potete anche creare una classe di utilità con metodi e proprietà statici e utilizzarla opportunamente nel main in cui vengono richiamati i metodi di cui sopra
#4. codice ben indentato, commentato e modulare (ovvero un file dedicato per ogni parte logica del programma). 

#N.B.: il tutto va versionato in un repository nel vostro GitHub.
#La consegna prevede il link al vostro repository!
#Non c'è tanto codice da scrivere, fatemi vedere che avete capito entrambi i concetti: versionamento (i vari comandi di git) e espressioni regolari.
#Per domande tecniche sul linguaggio di programmazione scelto chiedete al vostro docente di Informatica che sicuramente è più bravo di me :)


import re
class MichEsprReg:
    def __init__(self):
        self.pattern = ""

    def set_pattern(self, pattern: str):
        """Imposta l'espressione regolare."""
        self.pattern = pattern

    def validate(self, string: str) -> str:
        """Verifica se la stringa corrisponde all'espressione regolare."""
        if re.fullmatch(self.pattern, string):
            return "match"
        else:
            return "mismatch"
# Esempio di utilizzo
if __name__ == "__main__":
    espr = MichEsprReg()
    # Pattern per date nel formato gg/mm/yyyy dal 1900 al 2025
    espr.set_pattern(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19[0-9][0-9]|20[2][0-5])$')
    test_string = "12/12/2020" "34/56/7890"
    result = espr.validate(test_string)
    print(f"Test string: '{test_string}' => {result}")

#espr.set_pattern = metodo per impostare l'espressione regolare
#espr.validate = metodo per validare la stringa rispetto all'espressione regolare
#re.fullmatch = funzione della libreria re per verificare la corrispondenza completa tra la stringa e il pattern regex
#/d= cifra
#{n}= esattamente n occorrenze del carattere precedente
#( )= gruppo di caratteri
#|= operatore logico "o"    
#^= inizio della stringa
#$= fine della stringa
