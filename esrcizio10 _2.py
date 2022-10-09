'''Esercizio 2: Un supermercato vuole ricompensare i suoi clienti giornalieri,
 mostrando il loro nome su uno schermo all'interno del supermercato.
  A tal fine, l'importo degli acquisti del cliente è memorizzato in una prima lista
  e il nome del cliente in una seconda lista corrispondente. Scrivi quindi un programma
  che chiede al cassiere di inserire tutti gli acquisti dei clienti e i nomi dei clienti,
  da inserire in due liste. Implementa la funzionalità che visualizza il nome e l'importo del cliente
  che ha speso di più, il nome e l'importo del cliente che ha speso di meno, la media e la mediana della spesa
  di tutti i clienti e visualizza il risultato quando il cassiere immette prezzo O (valore usato come sentinella) '''
import numpy as np
prezzo = ''
clienti = []
acquisti = []
i=1
while prezzo !=0:
    prezzo = float(input('Inserire importo speso dal cliente {}: '.format(i)))
    if prezzo !=0:
        acquisti.append(prezzo)
        nome = input('Inserire nome cliente {}: '.format(i))
        clienti.append(nome)
        i+=1
#cliente che ha speso di più
print('Il cliente che ha speso di più è {} con un importo di {}€'.format(clienti[acquisti.index(max(acquisti))],max(acquisti)))
print(acquisti.index(max(acquisti)))
print(clienti[acquisti.index(max(acquisti))])
#cliente che ha speso di meno
print('Il cliente che ha speso di meno è {} con un importo di {}€'.format(clienti[acquisti.index(min(acquisti))],min(acquisti)))
#media
print('L\'importo medio speso è {} €'.format(np.mean(acquisti)))
#mediana
print('La mediana dell\'importo speso è {} €'.format(np.median(acquisti)))