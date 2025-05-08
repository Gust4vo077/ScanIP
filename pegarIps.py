import psutil

def pegarLocalIps():
  interfaces = psutil.net_if_addrs()
  todosIpSuaInterface=list()
  for nomeInterface, enderecosInfos in interfaces.items():
    for counteudoEnderecos in enderecosInfos:
      todosIpSuaInterface.append(counteudoEnderecos.address)    
  return todosIpSuaInterface

