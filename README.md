# 🌸 CicloZen

![Tech Stack](https://img.shields.io/badge/Tech-HTML5%20%7C%20CSS3%20%7C%20JS-pink?style=flat-square)
![Privacy](https://img.shields.io/badge/Data-Local%20Storage%20(Offline)-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

> **Rastreador de ciclo menstrual focado em privacidade e simplicidade.** Uma aplicação web para estimar janelas de fertilidade, previsão menstrual e alertas de fase lútea (TPM) sem enviar dados para a nuvem.

---

## 🔗 [Acesse o App Online](https://othipedroso.github.io/ciclo-zen/)

---

## 🎯 O Propósito
A maioria dos aplicativos de saúde feminina exige cadastro, login e envia dados íntimos para servidores externos. O **CicloZen** foi criado com a filosofia **"Privacy-First"**: todos os cálculos são feitos no navegador da usuária e os dados persistem apenas no dispositivo dela.

É uma ferramenta útil para o dia a dia, ajudando no planejamento pessoal e no autoconhecimento do corpo.

---

## ✨ Funcionalidades

### 1. 🩸 Previsão de Ciclo
- Calcula a data exata do início da próxima menstruação com base na duração média do ciclo da usuária.
- Algoritmo ajustável (ex: ciclos de 28, 30 ou 35 dias).

### 2. 🌿 Janela Fértil & Ovulação
- Utiliza o método de **Tabela (Ogino-Knaus)** reverso.
- Estima a ovulação 14 dias antes do final do ciclo e projeta a janela de maior probabilidade de gravidez.

### 3. 😡 Alerta de TPM (Fase Lútea)
- Identifica a entrada na fase lútea (aproximadamente 1 semana antes da menstruação), período comum para oscilações de humor e sintomas físicos.

### 4. 🔒 Persistência Local (Offline)
- Usa a API `localStorage` do navegador.
- A usuária não precisa redigitar as datas toda vez que abre o app.
- **Zero rastreamento:** Nenhuma informação sai do dispositivo.

---

## 🛠️ Tecnologias Utilizadas

- **HTML5 Semântico:** Estrutura acessível.
- **CSS3 Moderno:** Design responsivo, paleta de cores suaves ("Calm UI") e Cards informativos.
- **Vanilla JavaScript:**
  - Manipulação avançada do objeto `Date()` (cálculo de milissegundos, dias e meses).
  - Lógica de persistência de dados no Front-end.

---

## 🚀 Como rodar localmente

1. Clone este repositório:
   ```bash
   git clone [https://github.com/othipedroso/ciclo-zen.git](https://github.com/othipedroso/ciclo-zen.git)
