items = []
n = 0
i = 1     
j = None 


def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1
    j = None

def step():
    global items, n, i, j

    if i >= n:
        return {"done": True}

    if j is None:
        j = i  
        
        a = max(0, j - 1) 
        b = j
        return {"a": a, "b": b, "swap": False, "done": False}

 
    if j > 0 and items[j - 1] > items[j]:
        a = j - 1
        b = j
        items[a], items[b] = items[b], items[a]
    
        j -= 1
        
        return {"a": a, "b": b, "swap": True, "done": False}

    else:

        a = max(0, j - 1)
        b = j

        i += 1     
        j = None    
        
        return {"a": a, "b": b, "swap": False, "done": False}
