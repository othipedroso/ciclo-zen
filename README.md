# 🌸 CicloZen

> **Sistema de monitoramento de ciclo menstrual com arquitetura Privacy-First e processamento local.**

## 🎯 Arquitetura e Propósito
Como estudante de Ciência da Computação, identifiquei uma falha de privacidade comum nas aplicações de *health-tech* atuais, que frequentemente trafegam dados biológicos sensíveis para servidores de terceiros. 

Desenvolvi o CicloZen para resolver esse problema utilizando Python e Streamlit. A aplicação adota uma abordagem estrita de *Privacy-First* e *Offline-First*. Toda a carga de processamento das regras de negócio (como a estimativa de ovulação via método de Ogino-Knaus) e o armazenamento de histórico em formato JSON ocorrem exclusivamente no ambiente local da usuária, garantindo zero vazamento de informações.