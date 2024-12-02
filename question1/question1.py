def longestpre(arrays):
    if not arrays:
        return ""
    
    firstarray = arrays[0]

    for array in arrays[1:]:
        while not array.startswith(firstarray):  
            firstarray = firstarray[:-1]
            if not firstarray:
                return ""
    
    return firstarray



