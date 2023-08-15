#KINEMATICS (I-D)
import math
print("s=displacement \nt=time \nu=initial velocity \nv=final \nvelocity \na=accerlation \nj=jerk")
print("\nv+u+at \ns=ut+1/2at^2 \nv^2=u^2+2as")

d1={"u":None,"v":None,"t":None,"a":None,"j":None,"s":None}
l1=[]
l2=[]
l3=["u","v","t","a","j","s"]
n=None

def eqrt( A, B, C):
    global x1
    global x2
    D = B*B - 4*A*C
    sq = math.sqrt(abs(D))
    if (D > 0):
        x1=(-B + sq)/(2*A)
        x2=(-B - sq)/(2*A)
    elif (D == 0):
        x1=(-B / (2 * A))
        x2=(-B / (2 * A))
    else:
        print("Undefined")
        
def asgn1():
    print("ENTER ONLY THOSE VALUES WHICH ARE KNOWN, else give input as 'n' ")
    u=eval(input("Enter u= "))
    d1["u"]=u
    v=eval(input("Enter v= "))
    d1["v"]=v
    a=eval(input("Enter a= "))
    d1["a"]=a
    t=eval(input("Enter t= "))
    d1["t"]=t
    s=eval(input("Enter s= "))
    d1["s"]=s
    j=eval(input("Enter j= "))
    d1["j"]=j
    #print(d1)

def cu():
    asgn1()
    global v
    global u
    global t
    global a
    global s
    
    v=d1["v"]
    a=d1["a"]
    t=d1["t"]
    s=d1["s"]
    print(v,a,t,s)
    
    if v and a and t is not None:
        #u= v-(a*t)
        print("u=")
    elif s and a and t is not None:
        u=(s/t)-(0.5*a*t)
        print("u=",u)
    elif v and a and s is not None:
        z1=(math.pow(v,2))-2*a*s
        u=math.pow(z1,0.5)
        print("u=",u)
    else:
        pass

def cv():
    asgn1()
    global v
    global u
    global t
    global a
    global s
    
    u=d1["u"]
    a=d1["a"]
    t=d1["t"]
    s=d1["s"]
    
    if u and a and t is not None:
        v=u+(a*t)
        print("v=",v)
        
    elif u and a and s is not None:
        z1=(math.pow(v,2))+2*a*s
        v=math.pow(z1,0.5)
        print("v=",v)
    else:
        pass 
    
def ca():
    asgn1()
    global v
    global u
    global t
    global a
    global s
    v=d1["v"]
    u=d1["u"]
    t=d1["t"]
    s=d1["s"]
    
    if v and u and t is not None:
        a=(v-u)/t
    
    elif s and u and t is not None:
        a1=2*(s-u*t)
        a2=math.pow(t,2)
        a=a1/a2
    elif v and u and s is not None:
        z1=(v+u)*(v-u)
        a=z1/(2*s)
    else:
        pass 
    print("a=",a)

def ct():
    asgn1()
    global v
    global u
    global t
    global a
    global s
    v=d1["v"]
    a=d1["a"]
    u=d1["u"]
    s=d1["s"]

    if v and a and u is not None:
        t=(v-u)/a
        
    elif s and a and u is not None:
        eqrt(a,2*u,(-2)*s)
        if(x1>0):
            print("t=",x1)
        elif(x2>0):
            print("t=",x2)
        
    elif v and a and s is not None:
        pass
    else:
        pass 
    
def cs():
    asgn1()
    global v
    global u
    global t
    global a
    global s
    v=d1["v"]
    a=d1["a"]
    t=d1["t"]
    u=d1["u"]

    if u and a and t is not None:
        s=(u*t)+(0.5*a*t*t)
    elif v and u and a is not None:
        z1=(v+u)*(v-u)
        s=z1/(2*a)
    else:
        pass 
    print("s=",s)
    
def cj():
    asgn1()
    a=d1["a"]
    t=d1["t"]
    if a and t is not None:
        j=a/t
        print("j=",j)
    else:
        pass

arg=str(input("TBC?= "))

if(arg=="u"):
    cu()
elif(arg=="v"):
    cv()
elif(arg=="a"):
    ca()
elif(arg=="t"):
    ct()
elif(arg=="s"):
    cs()
elif(arg=="j"):
    cj()
else:
    print("Wrong Input")
