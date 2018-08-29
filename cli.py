from bench import computer
from bench import cpu
from bench import memory
import sys


params = sys.argv

if len(params) > 1:
    if params[1] == 'os' or params[1] == 'system':
        print('Sistema operacional: ', computer.os())
        print('Versão: ', computer.osVersion())
    elif params[1] == 'name':
        print('Node de rede: ', computer.name())
    elif params[1] == 'distro':
        print('Distribuição: ', computer.distro())
    elif params[1] == 'processor' or params[1] == '-p':
        # Usando 4 parametros, primeiro o nome 'cli.py', segundo '-p' ou 'processor', terceiro 'percentage' e quarto 'maior ou igual a 1'
        if len(params) == 4 and params[2] == 'percentage' and int(params[3]) >= 1: # convertendo o param[3] para int pois antes era uma string
            for x in range(int(params[3])): # repetição enquanto o numero digitado no terceiro parametro for alcançado
                print('Cosumindo: ', round(cpu.percentage().user + cpu.percentage().system,1), '%') # somar o quanto o usuário está gastando com o quanto o sistema está gastando
                print('Livre:', round(cpu.percentage().idle,1), '%')
                print('______________________')
        elif len(params) == 4 and params[2] == 'benchmarking' and int(params[3]) >= 1:
            print('Analisando o uso da CPU ...')
            media = 0
            for x in range(int(params[3])):
                media += cpu.percentage().user + cpu.percentage().system
            media = media/int(params[3])
            print('Média de consumo da cpu durante: ',params[3], 'segundos: ', round(media,1),'%')
        else:
            print('Processador: ', computer.cpu())
            print('Velocidade: ', cpu.freq(),'GHz')
            print('Cores: ', cpu.cores())
            print('Cores físicos: ', cpu.phyCores())
    elif params[1] == 'memory' or params[1] == '-m':
        if str(params).find('size') > 0: # se dentro dos parametros achar a palavra 'size' fará ...
            print('Tamanho da memória: ', memory.size(),'GB')
        if str(params).find('percentage') > 0:
            print('Consumo atual da memória: ', memory.percentage(),'%')
        if str(params).find('free') > 0:
            print('Memória Livre: ', memory.free(),'GB')
        if str(params).find('used') > 0:
            print('Memória sendo usada: ', memory.used(),'GB')
    elif params[1] == 'arch':
        print('Arquitetura da máquina: ', computer.arch())
    else:
        print('Parametro desconhecido')
else:
    print('Sistema operacional: ',computer.os())