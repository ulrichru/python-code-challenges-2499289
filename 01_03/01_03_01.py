# Rekursiver Ansatz als Muster, welche Zahlen ermittelt werden sollen
#def fibonacciZahlen(n):
#    if n > 1:
 #       return fibonacciZahlen(n-1) + fibonacciZahlen(n-2)
  #  return n


# for i in range(10):
  #  print(fibonacciZahlen(i))
def fibonacciZahlen(n):
    fibonacciListe=[0,1]
    i=0
    while i < n:
        fZahl=fibonacciListe[len(fibonacciListe)-2]+fibonacciListe[len(fibonacciListe)-1]
        fibonacciListe.append(fZahl)
        i = i + 1
    print(fibonacciListe)

fibonacciZahlen(20)