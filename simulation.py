import random

def fdpArriboSemana():
    b = 2.8763413175152936
    loc = -10.052864063826082
    scale= 10.06953072382608
    r = random.random()
    return (scale/ ( (1-r)**(1/b) ) + loc)

def fdpSalidaSemana():
    b = 2.731327334435317
    loc = -10.052864063826082
    scale= 10.06953072382608
    r = random.random()
    return (scale/ ( (1-r)**(1/b) ) + loc)

def fdpArriboFinde():
    b = 13.597399902568572
    loc = -96.53864955632271
    scale= 96.55531621632271
    r = random.random()
    return (scale/ ( (1-r)**(1/b) ) + loc)

def fdpSalidaFinde():
    b = 7.834420926029725
    loc = -49.712675426437265
    scale= 49.72934208643726
    r = random.random()
    return (scale/ ( (1-r)**(1/b) ) + loc)

def simularCaso(cib, cm, fdpArribo, fdpSalida):
    
    t = 0 # Tiempo Actual
    nsb = cib # variable estado
    tv = 0 # Tiempo vacio
    itv = 0 # Inicio tiempo vacio
    ntll = 0 # Cantidad total de llegadas
    nts = 0 # Cantidad total de Salidas
    tpll = 0 # Proxima llegada
    tps = fdpSalida() # Proxima salida
    tf = 2000 # Tiempo de finalización de simulación
    arrs = 0 # Arrepentidos de salida
    arrll = 0 # Arrepentimiento de llegada
    tc = 0 # Tiempo completo
    itc = 0 # Inicio Tiempo completo

    while (t<tf):

        if (tpll <= tps):
            t=tpll
            IALL = fdpArribo()
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
            IAS = fdpSalida()
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

    PARRS=arrs*100/(nts + arrs) if nts!=0 else 0
    PARRLL=arrll*100/(ntll + arrll) if nts!=0 else 0
    PTV=tv*100/t
    PTC=tc*100/t

    return PARRS, PARRLL, PTV, PTC

PARRS_1, PARRLL_1, PTV_1, PTC_1 = simularCaso(0, 10, fdpArriboSemana, fdpSalidaSemana)
PARRS_2, PARRLL_2, PTV_2, PTC_2 = simularCaso(5, 15, fdpArriboSemana, fdpSalidaSemana)
PARRS_3, PARRLL_3, PTV_3, PTC_3 = simularCaso(10, 20, fdpArriboSemana, fdpSalidaSemana)
PARRS_4, PARRLL_4, PTV_4, PTC_4 = simularCaso(15, 25, fdpArriboSemana, fdpSalidaSemana)

print("\n")
print("PARRS:"+str(PARRS_1))
print("PARRLL:"+str(PARRLL_1))
print("PTV:"+str(PTV_1))
print("PTC:"+str(PTC_1))
print("\n")
print("PARRS:"+str(PARRS_2))
print("PARRLL:"+str(PARRLL_2))
print("PTV:"+str(PTV_2))
print("PTC:"+str(PTC_2))
print("\n")
print("PARRS:"+str(PARRS_3))
print("PARRLL:"+str(PARRLL_3))
print("PTV:"+str(PTV_3))
print("PTC:"+str(PTC_3))
print("\n")
print("PARRS:"+str(PARRS_4))
print("PARRLL:"+str(PARRLL_4))
print("PTV:"+str(PTV_4))
print("PTC:"+str(PTC_4))
print("\n")