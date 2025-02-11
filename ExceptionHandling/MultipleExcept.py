def disp(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('ZeroDivisionError Occurred and Handled')
    except NameError:
        print('Name Error occured and handled')
    except TypeError:
        print('Type Error Occured and handled')
    except:
        print('Some unkown Error Occured and handled')
disp(10,'Kodnest')