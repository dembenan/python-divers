

# Programme Python pour l'implémentation du tri par insertion
def tri_insertion(tab): 
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k
    return tab


# Programme Python pour l'implémentation du tri par selection
def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp

   return tab

# Programme Python pour l'implémentation du Tri à bulle
def tri_bulle(tab):
    n = len(tab)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]
print ("Le tableau initial est:")
print(tab)

tab_tri = tri_insertion(tab)
print ("Le tableau trié par insertion est:")
print(tab_tri)

tab_tri = tri_selection(tab)
print ("Le tableau trié  par selection est:")
print(tab_tri)

tab_tri = tri_bulle(tab)
print ("Le tableau trié par bulles est:")
print(tab_tri)