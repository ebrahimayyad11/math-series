def fibonacci(n):
    '''description for the function

    parameters: 
    n(int)

    returns:
    int: returning value

    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)



def lucas(n):
    '''description for the function

    parameters: 
    n(int)

    returns:
    int: returning value
     
    '''
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)



def sum_series(n,x = 0,y = 1):
    '''description for the function

    parameters: 
    n(int)
    x(int)
    y(int)

    returns:
    int: returning value
     
    '''
    if x == 0 and y == 1:
        return fibonacci(n)
    elif x == 2 and y == 1:
        return lucas(n)
    else:
        arr = [x,y]
        for i in range(n):
            arr.append(arr[i]+arr[i+1])
        return arr[n]
