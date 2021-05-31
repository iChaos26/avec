def is_leap(year):

    if not (year%4) == 0:
        if not (year%100) == 0:
            if not (year%400) == 0:
                return False
            else:
                return True        
        