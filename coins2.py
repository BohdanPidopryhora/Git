C = int(raw_input("X="))
V = int(raw_input("B="))
B = int(raw_input("C="))
N = int(raw_input("D="))



def change(X, b=25, c =5, d=1):
    F=X
    if X % b == 0:
        A=X/b
        print "po " + str(b), A
    else:
        A=X/b
        X=X-A*b
        if X%c==0:
            B=X/c
            if A > 0:
                print "po " + str(b), A
            print "po " + str(c), B
        else:
            B=X/c
            X=X-B*c
            C=X/d
            if A>0:
                print "po " + str(b), A
            if B>0:
                print "po " + str(c), B
            print "po " + str(d), C
            print "ostacha " + str(F-A*b-B*c-C*d)

change(C,V,B,N)
