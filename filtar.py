def PrintarResultados(conteudo):

    if("data" in conteudo ):
      data = conteudo["data"] 
    
      if data["totalReports"] > 0:
          print(f"O IP {data['ipAddress']} apresenta denúncias de outros usuários, com um total de {data['totalReports']} reportes.")
          print(f"Sua última denúncia foi feita em {data['lastReportedAt'][:10]}.")
  
          score = data["abuseConfidenceScore"]
          if score < 40:
              print(" Nível de confiabilidade: **baixo**")
          elif 40 <= score < 60:
              print(" Nível de confiabilidade: **médio**")
          else:
              print(" Nível de confiabilidade: **alto**")
  
          print("--Informações adicionais sobre o IP--")
          print(f" País: {data['countryCode']}")
          print(f" Domínio: {data['domain']}")
          print(f" Provedor (ISP): {data['isp']}")
          print(f" Tipo de uso: {data['usageType']}")
  
          for hostname in data.get("hostnames", []):
              print(f" O nome(s) do hostname associado ao ip seria: {hostname}")
  
          if data["isWhitelisted"]:
              print(" Este IP está na lista de confiança (whitelist). \n")
          else:
              print(" Este IP **não** está na lista de confiança (whitelist). \n")

