X = int(raw_input("X="))
if X % 25 == 0:
    A=X/25
    print "po 25", A
else:
    A=X/25
    X=X-A*25
    if X%5==0:
        B=X/5
        if A > 0:
            print "po 25", A
        print "po 5", B
    else:
        B=X/5
        X=X-B*5
        C=X/1
        if A>0:
            print "po 25", A
        if B>0:
            print "po 5", B
        print "po 1", C
