items = []
n = 0
salto = 0  
i = 0      
j = None   

def init(vals):
    global items, n, salto, i, j
    items = list(vals)
    n = len(items)
    
    salto = n // 2
    
    i = salto
    j = None

def step():
    global items, n, salto, i, j


    if salto <= 0:
        return {"done": True}

    if i >= n:
        salto //= 2

        if salto <= 0:
            return {"done": True}
            
        i = salto    
        j = None
        
        return {"a": 0, "b": 0, "swap": False, "done": False}



   
    if j is None:
        j = i  
        a = max(0, j - salto)
        b = j
        
        return {"a": a, "b": b, "swap": False, "done": False}


    if j >= salto and items[j - salto] > items[j]:
       
        a = j - salto
        b = j
        items[a], items[b] = items[b], items[a]
        
        j -= salto
        
        return {"a": a, "b": b, "swap": True, "done": False}


    else:
        
        
        a = max(0, j - salto)
        b = j
        
        i += 1      
        j = None    
        
        return {"a": a, "b": b, "swap": False, "done": False}
