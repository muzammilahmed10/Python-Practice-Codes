def disp(a,b):
    try:
        print(a/b)
    except:
        print('Some error Handeled')
    else:
        print('Task executed without any exception')
    finally:
        print('Task Ended')

disp(10,0)
disp(10,5)
disp(20,2)