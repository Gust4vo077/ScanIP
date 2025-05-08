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

As dependências estão listadas no arquivo `requirements.txt`. Para instalá-las, utilize:

```bash
git clone https://github.com/Gust4vo077/ScanIP.git
cd ScanIP
pip install -r requirements.txt

## 🛠 **Tecnologias e Dependências**

Como o arquivos deve ser 




