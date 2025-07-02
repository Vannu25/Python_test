class ZeroDenominatorError(Exception):
    try:
        a = 10
        b = 0
        if(b==0):
            raise ZeroDivisionError()
        c = a/b
    except ZeroDivisionError:
        print('Zero Division Error occured')

z = ZeroDenominatorError()