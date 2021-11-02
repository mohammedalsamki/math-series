def fibonacci(n):


    '''
    function that ask for a val and then it take -1 from it until it equal to 1 and that is call recurion
    '''



    if n<= 1:
        if n ==0:
         return 0
        else:
         return 1
    return fibonacci(n-1) + fibonacci (n-2)
    


def lucas(n):
    '''
    fun that reqire val and then 
    
    '''
  
    if (n==0):
        return 2
    if (n==1):
        return 1
    return lucas(n - 1 ) + lucas( n - 2) 





def sum_series(n,first=0,sec=1):


      
        if n ==0:
         return first
        if n==1:
            return sec 
        else:
         return sum_series(n-1,first,sec) + sum_series(n-2,first,sec)
       