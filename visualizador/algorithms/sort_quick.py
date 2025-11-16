items = []
n = 0


pila = []

fase = "buscar_tarea"  
inicio = 0
fin = 0
valor_pivote = 0     
i = 0                
j = 0               

def init(vals):
    global items, n, pila, fase, inicio, fin, i, j, valor_pivote
    items = list(vals)
    n = len(items)
    
  
    pila = []
    
    if n > 1:
        pila.append((0, n - 1))
        
    fase = "buscar_tarea"
    inicio = 0
    fin = 0
    i = 0
    j = 0
    valor_pivote = 0

def step():
    global items, n, pila, fase, inicio, fin, i, j, valor_pivote

    if fase == "buscar_tarea":
        if not pila:
            return {"done": True}
            
        inicio, fin = pila.pop()


        if inicio >= fin:
            fase = "buscar_tarea" 
            return {"a": inicio, "b": fin, "swap": False, "done": False}

        
        valor_pivote = items[fin] 
        i = inicio - 1            
        j = inicio                
        fase = "escanear"        
        
        return {"a": j, "b": fin, "swap": False, "done": False}

    elif fase == "escanear":

        if j <= fin - 1:
           
            a = j
            b = fin 
            swap = False
            
            if items[j] <= valor_pivote:
               
                i += 1 
                items[i], items[j] = items[j], items[i]
                swap = True
                a = i
                b = j
            
            j += 1 
            return {"a": a, "b": b, "swap": swap, "done": False}
        
        else:

            fase = "swap_final"
            return {"a": i + 1, "b": fin, "swap": False, "done": False}

    elif fase == "swap_final":
        
        nuevo_indice_pivote = i + 1

        items[nuevo_indice_pivote], items[fin] = items[fin], items[nuevo_indice_pivote]
        

        pila.append((inicio, nuevo_indice_pivote - 1))
       
        pila.append((nuevo_indice_pivote + 1, fin))
        
        fase = "buscar_tarea"
        
        return {"a": nuevo_indice_pivote, "b": fin, "swap": True, "done": False}

    return {"done": True}
