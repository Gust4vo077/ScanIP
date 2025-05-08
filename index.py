import csv
import pegarIps
import api
import filtar
from view import tela

caminho= tela.telaPegarDiretorio()

with open(caminho, "r") as arquivo:
    conteudo = csv.reader(arquivo)
    next(conteudo)  
    conteudo = list(conteudo)

    conteudoSemRepitir = set() 
    todosIpLocais = pegarIps.pegarLocalIps()

    def jaExiste(ipParaSerAdicionado):
        if ipParaSerAdicionado not in conteudoSemRepitir and ipParaSerAdicionado not in todosIpLocais:
            conteudoSemRepitir.add(ipParaSerAdicionado)

    for linha in conteudo:
        jaExiste(linha[3])

    print("   IP(s) que foram achados denúncias sobre ele(s)\n")

    for ip in conteudoSemRepitir:
     resultado = api.verificarIp(ip)
     resultado = resultado.json()
     filtar.PrintarResultados(resultado)

    