import numpy as np
import scipy.linalg as spLin
import RisolviSis

def jacobi(A,b,x0,toll,it_max):
    
    errore=1000
    M=np.diag(1/np.diag(A)) #inversa di M
    E=np.tril(A,-1)
    F=np.triu(A,1)
    N=-(E+F)
    T=M@N
    
    raggiospettrale=np.max(np.abs(np.linalg.eigvals(T)))    #più è grande e più è mal condizionata
    print("raggio spettrale jacobi", raggiospettrale)   #il metodo converge per raggiospettrale < 1
    #if raggiospettrale < 1: print("metodo convergente")
    it=0
    
    er_vet=[]
    while it <= it_max and errore >= toll:
        x=(T@x0)+(M@b)
        errore=np.linalg.norm(x-x0)/np.linalg.norm(x)
        er_vet.append(errore)
        x0=x.copy()
        it=it+1
    return x,it,er_vet


#Converge sempre per matrici simmetriche definite positive
def gauss_seidel(A,b,x0,toll,it_max):
    errore=1000
     
    D=np.diag(np.diag(A))
    E=np.tril(A,-1)
    F=np.triu(A,1)
    M=np.linalg.inv(E+D)   #M^-1
    ''' M=E+D
        invM=np.linalg.inv(M)'''
    N=-F
    T=M@N

    raggiospettrale=np.max(np.abs(np.linalg.eigvals(T)))    
    print("raggio spettrale Gauss-Seidel ",raggiospettrale) 
    ''' il metodo converge per raggiospettrale < 1
    più si avvicina a 0 e più la convergenza alla soluzione reale
    è veloce, per quanto riguarda l'indice di condizionamento
    si considera una matrice mal condizionata se è nell'ordine di 
    10^3 o maggiore, ben condizionata se è < 1 '''
    it=0
    er_vet=[]
    while it<=it_max and errore>=toll:
        x=(-M@F@x0)+(M@b)
        errore=np.linalg.norm(x-x0)/np.linalg.norm(x)
        er_vet.append(errore)
        x0=x.copy()
        it=it+1
    return x,it,er_vet

'''
servono per le matrici mal condizionate
omega è il parametro di rilassamento > 0
a volte consente di far convergere il metodo
che normalmente non converge'''
def gauss_seidel_sor(A,b,x0,toll,it_max,omega):
    errore=1000
     
    D=np.diag(np.diag(A))
    invD=np.linalg.inv(D)
    E=np.tril(A,-1)
    F=np.triu(A,1)
    #Calcolo della matrice di iterazione di Gassu_Seidel SOR
    Momega=D+omega*E
    Nomega=(1-omega)*D-omega*F
    T=np.dot(np.linalg.inv(Momega),Nomega)#npl.inv(Momega)@Nomega
    
    raggiospettrale=np.max(np.abs(np.linalg.eigvals(T)))
    print("raggio spettrale Gauss-Seidel SOR ", raggiospettrale)
    
    M=D+E
    N=-F 
    it=0
    xold=x0.copy()
    xnew=x0.copy()
    er_vet=[]
    while it<=it_max and errore>=toll:
         
        xtilde=RisolviSis.Lsolve(M,b-F@xold)
        xnew=(1-omega)*xold+omega*xtilde
        errore=np.linalg.norm(xnew-xold)/np.linalg.norm(xnew)   #solo se xnew != 0
        er_vet.append(errore)
        xold=xnew.copy()
        it+=1
    return xnew,it,er_vet

def steepestdescent(A,b,x0,itmax,tol):
    
#Metodo del gradiente per la soluzione di un sistema lineare con matrice dei coefficienti simmetrica e definita positiva
    n,m=A.shape
    if n!=m:
        print("Matrice non quadrata")
        return [],[]
    
    
   #inizializzare le variabili necessarie
    x = x0
    r =  
    p =  
    it = 0
    nb= 
    errore= 
    vec_sol=[]
    vec_sol.append(x)
    vet_r=[]
    vet_r.append(errore)
     
# utilizzare il metodo del gradiente per trovare la soluzione
    while  
        it=it+1
        Ap 
        rTr= 
        alpha =  
                
        x =  
        vec_sol.append(x)
        r= 
        errore= 
        vet_r.append( )
        p = -  
        
    
    return x,vet_r,vec_sol,it


def conjugate_gradient(A,b,x0,itmax,tol):
    
#Metodo del gradiente coniugato per la soluzione di un sistema lineare con matrice dei coefficienti simmetrica e definita positiva
    n,m=A.shape
    if n!=m:
        print("Matrice non quadrata")
        return [],[]
    
    
   # inizializzare le variabili necessarie
    x =  
    r =  
    p = - 
    it = 0
    nb= 
    errore= 
    vec_sol=[]
    vec_sol.append( )
    vet_r=[]
    vet_r.append( )
# utilizzare il metodo del gradiente coniugato per trovare la soluzione
    while e 
        it=it+1
        Ap= 
        rtr= 
        alpha =  
        x =  
        vec_sol.append(x)
        r= 
        gamma= 
        errore= 
        vet_r.append()
        p =  
   
    
    return x,vet_r,vec_sol,it

def eqnorm(A,b):
#Soluzione di un sistema sovradeterminato facendo uso delle equazioni normali
    G= 
    f= 
    L= 
    x =
     
    
    
    return x
#Soluzione di un sistema sovradeterminato facendo uso della fattorizzazione QR    
def qrLS(A,b):
    n=A.shape[1]  # numero di colonne di A
    #Calcola la fattorizzazione QR di A e utilizzala per calcolare
    #la soluzione nel senso dei minimi quadrati di Ax=b
    
    return x,residuo
#Soluzione di un sistema sovradeterminato facendo uso della fattorizzazione SVD
def SVDLS(A,b): 
    #Calcola la fattorizzazione SVD di A e utilizzala per calcolare
    #la soluzione nel senso dei minimi quadrati di Ax=b
    
        
    thresh=np.spacing(1)*m*s[0] ##Calcolo del rango della matrice, numero dei valori singolari maggiori di una soglia
    k=np.count_nonzero(s>thresh)
     
    d= 
    d1= 
    s1= 
    #Risolve il sistema diagonale di dimensione kxk avene come matrice    dei coefficienti la matrice Sigma
    c= 
    x=V[:,:k]@c 
    residuo= 
    return x,residuo

#Funzioni per la costruzione del polinomio interpolatore nella base di
#Lagrange

def plagr(xnodi,k):
    """
    Restituisce i coefficienti del k-esimo pol di
    Lagrange associato ai punti del vettore xnodi
    """
    xzeri=np.zeros_like(xnodi)
    n=xnodi.size
    if k==0:
       xzeri=xnodi[1:n]
    else:
       xzeri=np.append(xnodi[0:k],xnodi[k+1:n])
    
    num= 
    den= 
    
    p= 
    
    return p

def InterpL(x, f, xx):
     """"
        %funzione che determina in un insieme di punti il valore del polinomio
        %interpolante ottenuto dalla formula di Lagrange.
        % DATI INPUT
        %  x  vettore con i nodi dell'interpolazione
        %  f  vettore con i valori dei nodi 
        %  xx vettore con i punti in cui si vuole calcolare il polinomio
        % DATI OUTPUT
        %  y vettore contenente i valori assunti dal polinomio interpolante
        %
     """
     n=x.size
     m=xx.size
     L=np.zeros((m,n))
     for k in range(n):
        p= 
        L[:,k]= 
    
    
     return np.dot(L,f)