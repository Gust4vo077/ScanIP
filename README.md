# 🌐 **ScanIP – Wireshark IP Threat Analyzer**

**ScanIP** é um projeto em Python que analisa arquivos CSV exportados do **Wireshark**, identifica os endereços IP de origem e destino, e verifica se esses IPs estão associados a atividades maliciosas. A verificação é realizada utilizando a API [AbuseIPDB](https://api.abuseipdb.com/api/v2/check) ou uma lista local de IPs suspeitos.

---

## 🚀 **Funcionalidades**

- **Leitura de arquivos CSV** exportados do Wireshark.
- **Extração de IPs** de origem e destino do tráfego de rede.
- **Verificação de IPs** contra a API AbuseIPDB ou lista local de ameaças.
- **Relatório gerado** com classificação de IPs como **seguros** ou **suspeitos**.
- **Interface simples** em linha de comando.

---

## 🛠 **Tecnologias e Dependências**

Este projeto utiliza as seguintes bibliotecas:

- **Python 3.x**
- **certifi** 
- **charset-normalizer**
- **dotenv**
- **idna**
- **psutil**
- **PyQt5**
- **PyQt5-Qt5**
- **PyQt5_sip**
- **python-dotenv**
- **requests**
- **tk**
- **urllib3**
-
## 🛠 Formato dos Arquivos CSV**

- O ScanIP foi desenvolvido para ler arquivos CSV exportados diretamente do Wireshark. Um exemplo de formato de arquivo CSV esperado:

| No. | Time      | Source                                | Destination                          | Protocol | Length | Info                                          | ab Time           |
|-----|-----------|---------------------------------------|--------------------------------------|----------|--------|-----------------------------------------------|-------------------|
| 1   | 0.000000  | 2804:d20:8156:9600:5108:6f97:5de4:1f86 | 2603:1063:27:1::254                  | TCP      | 74     | 53730 > 443 [FIN, ACK] Seq=1 Ack=1 Win=1023 Len=0 | 15:14:28.372420   |
| 2   | 0.000467  | 192.168.2.186                         | 204.79.197.203                       | TCP      | 54     | 64632 > 443 [FIN, ACK] Seq=1 Ack=1 Win=1021 Len=0 | 15:14:28.372887   |

- O projeto irá extrair automaticamente os endereços IP de origem e destino e realizar a verificação de segurança, com base nas APIs ou lista local configurada.


## As dependências estão listadas no arquivo `requirements.txt`. Para instalá-las, utilize:**

```bash
git clone https://github.com/Gust4vo077/ScanIP.git
cd ScanIP
pip install -r requirements.txt

