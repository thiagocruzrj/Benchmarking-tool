import psutil

def freq():
    # retornar velocidade o processador atual e arredondar para 1 digito dps da virgula
    return round(psutil.cpu_freq().current/ 1000,1)
def cores():
    # retornar quantidade de núcleos que o pc tem
    return psutil.cpu_count()
def phyCores():
    # retornar quantidade de núcleos físicos
    return psutil.cpu_count(logical=False)
def percentage():
    # porcentagem de cpu usada de 1 em 1 segundo
    return psutil.cpu_times_percent(interval=1)