import random

tf = 5000*60

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
    global tf

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

def get_totals(total_simulation):
    PARRS = 0
    PARRLL = 0
    PTV = 0
    PTC = 0

    for simulation in total_simulation:
        PARRS += simulation['parrs']
        PARRLL += simulation['parrll']
        PTV += simulation['ptv']
        PTC  += simulation['ptc']

    return PARRS, PARRLL, PTV, PTC 

def run_simulation(ci, cm, fdpArriboSemana, fdpSalidaSemana):
    total_simulation = []
    for x in range(100):
        PARRS, PARRLL, PTV, PTC = simularCaso(ci, cm, fdpArriboSemana, fdpSalidaSemana)
        total_simulation.append({'parrs': PARRS, 'parrll': PARRLL,'ptv':PTV,'ptc': PTC})
    PARRS, PARRLL, PTV, PTC = get_totals(total_simulation)
    
    print("CM: "+str(cm))
    print("CI: "+str(ci))
    print("TF: "+str(tf)+ " horas")
    print("PARRS: "+str(PARRS/100))
    print("PARRLL: "+str(PARRLL/100))
    print("PTV: "+str(PTV/100))
    print("PTC: "+str(PTC/100))

print("//////SEMANA///////")
run_simulation(0, 10, fdpArriboSemana, fdpSalidaSemana)
run_simulation(5, 10, fdpArriboSemana, fdpSalidaSemana)
run_simulation(10, 20, fdpArriboSemana, fdpSalidaSemana)
run_simulation(40, 50, fdpArriboSemana, fdpSalidaSemana)

print("//////FINDE///////")
run_simulation(0, 10, fdpArriboFinde, fdpSalidaFinde)
run_simulation(5, 10, fdpArriboFinde, fdpSalidaFinde)
run_simulation(10, 20, fdpArriboFinde, fdpSalidaFinde)
run_simulation(40, 50, fdpArriboFinde, fdpSalidaFinde)
