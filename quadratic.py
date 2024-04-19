# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    x1=(-b+((b**2)-(4*a*c))**(1/2))/(2*a)
    x2=(-b-((b**2)-(4*a*c))**(1/2))/(2*a)
    if x1==x2:
        return "("+str(x1)+")"
    elif x1!=x2 and 'j' in str(x1) and 'j' in str(x2):
        return '( )'
    elif x1!=x2:
        return "("+str(x1)+", "+str(x2)+")"
    


def value_y(a, b, c, x):
    y= a*(x**2)+b*x+c
    return y


def to_string(a, b, c):
    if a!=0 and b!=0 and c!=0:
        return 'f(x) = '+str(a)+' * X^2 + '+str(b)+' * X + '+str(c)
    elif a==0 and b!=0 and c!=0:
        return 'f(x) = '+str(b)+' * X + '+str(c)
    elif a!=0 and b==0 and c!=0:
        return 'f(x) = '+str(a)+' * X^2 + '+str(c)
    elif a==0 and b==0 and c!=0:
        return 'f(x) = '+str(c)



def derivation(a, b, c):
    deriv1=str(a*2)+' * X + '+str(b)
    if a!=0 and b!=0:
        return "f'(x) = "+str(deriv1)
    elif a==0 and b!=0:
        return "f'(x) = "+str(b)
    elif a!=0 and b==0:
        return "f'(x) = "+str(a*2)+' * X'
    elif a==0 and b==0:
        return "f'(x) = 0"

