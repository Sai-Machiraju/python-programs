def is_leap(year):
    leap = False
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
            return leap
        else:
            return leap    
    elif year % 4 == 0:
        leap=True
        return leap
    else:            
        return leap

