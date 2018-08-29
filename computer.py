import platform

def os():
    # retornar apenas o sistema
    return platform.uname().system 
def osVersion():
    # retornar apenas versão do SO
    return platform.uname().version
def name():
    # retornar nome do computador na rede
    return platform.uname().node
def arch():
    # retornar arquitetura da maquina
    return platform.uname().machine
def cpu():
    # retornar o processador
    return platform.uname().processor
def distro():
    # retornar distribuição linux
    if os() == 'Linux':
        return platform.linux_distribution()
    else:
        return os()