import psutil

def size():
    # retornar tamanho da memória
    return round(psutil.virtual_memory().total/(1024*1024*1024),1)

def percentage():
    # procentagem de consumo da memória
    return psutil.virtual_memory().percent

def free():
    # retornar quantidade de memória livre
    return round(psutil.virtual_memory().free/(1024*1024*1024),1)

def used():
    #retornar quantidade de memória usada
    return round(psutil.virtual_memory().used/(1024*1024*1024),1)