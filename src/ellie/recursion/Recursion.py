import os

def countNumbersWithUniqueDigits(n: int) -> int:
    """countNumbersWithUniqueDigits
    Description
    Given an integer n, return the count of all numbers with unique digits.

    Parameters
    ----------
    n : int
        number of digits you may use

    Returns
    -------
    int
        Count of numbers without repeated digits. 
    Note
    ----
    For n=4 we have _ _ _ _. first index 9 without 0, then 9 zero again available and 8 on the last place.  9*(10-1)*(10-2)*(10-3)

    """
    def helperRecursion(n):

        if n==0:
            return 1
        elif n==1:
            return 10
        elif n==2:
            return 81
        
        return (10-n+1)*helperRecursion(n-1)
    ans =0
    for i in range(n+1):
        ans+=helperRecursion(i)
    return ans    
    

        
