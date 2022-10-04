import random
t=0

def get_value_fdp_llegada():
    global t
    b = 2.8763413175152936
    loc = -10.052864063826082
    scale= 10.06953072382608
    r = random.random()
    return (scale/ ( (1-r)**(1/b) ) + loc)

def get_value_fdp_salida():
    global t
    b = 2.731327334435317
    loc = -9.14575295002019
    scale = 9.162419610020189
    r = random.random()
    return (scale/ ( (1-r)**(1/b) ) + loc)

# Tiempo Actual
# variable estado
nsb = 40
# Cantidad inicial de bicicletas de la estacion
cib = 40
# Cantidad Maxima de biciletas
cm = 50
# Tiempo vacio
tv = 0
# Inicio tiempo vacio
itv = 0
# Cantidad total de llegadas
ntll = 0
# Cantidad total de Salidas
nts = 0
# Proxima llegada
tpll = 0
# Proxima salida
tps = get_value_fdp_salida()
# Tiempo de finalización de simulación
tf = 2000
# Arrepentidos de salida
arrs = 0
# Arrepentimiento de llegada
arrll = 0
# Tiempo completo
tc = 0
# Inicio Tiempo completo
itc = 0

def simulation():
    global t
    global nsb
    global cib
    global cm
    global tv
    global itv
    global ntll
    global nts
    global tpll
    global tps
    global tf
    global arrs
    global arrll
    global tc
    global itc
    if (tpll <= tps):
        t=tpll
        IALL = get_value_fdp_llegada()
        tpll=IALL+t
        if (nsb==cm):
            arrll = arrll + 1
        else:
            if(nsb==0):
                tv=tv+(t-itv)
            nsb = nsb + 1
            ntll=ntll+1
            if(nsb==cm):
                itc=t
    elif(tpll>tps):
        t=tps
        IAS = get_value_fdp_salida()
        tps = IAS + t
        if (nsb==cm):
            tc=tc+(t-itc)
        nsb=nsb-1
        if (nsb<0):
            arrs=arrs+1
            nsb=nsb+1
        else:
            nts=nts+1
            if(nsb==0):
                itv=t

while (t<tf):
    simulation()
    # print(t)
    # print("fin iteracion t="+str(t)+" cantidad de bicicletas="+str(nsb))

PARRS=arrs*100/(nts + arrs) if nts!=0 else 0
PARRLL=arrll*100/(ntll + arrll) if nts!=0 else 0
PTV=tv*100/t
PTC=tc*100/t

# print("t: "+str(t))
# print("ARRS:"+str(arrs))
# print("ARRLL:"+str(arrll))
print("PARRS:"+str(PARRS))
print("PARRLL:"+str(PARRLL))
print("PTV:"+str(PTV))
print("PTC:"+str(PTC))