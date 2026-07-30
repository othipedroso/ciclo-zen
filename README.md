# 🌸 CicloZen

![Tech Stack](https://img.shields.io/badge/Tech-HTML5%20%7C%20CSS3%20%7C%20Vanilla_JS-pink?style=flat-square)
![Privacy](https://img.shields.io/badge/Data-Local_Storage_(Offline)-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Production-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

> **Aplicação web focada em privacidade (Privacy-First) para monitoramento de ciclos menstruais.**
> Cálculos de janelas de fertilidade, previsão de ciclos e alertas de fase lútea executados 100% no client-side.

[🚀 Acesse a Aplicação em Produção](https://othipedroso.github.io/ciclo-zen/)

---

## 🎯 Proposta de Valor e Arquitetura do Projeto
O mercado de *health-tech* apresenta diversas soluções que exigem cadastro e armazenam dados biológicos sensíveis em servidores de terceiros. O **CicloZen** foi arquitetado para solucionar esse problema através de uma abordagem estrita de **Privacy-First**.

O projeto funciona sob o conceito de uma aplicação *serverless* e *offline-first*, onde todas as lógicas de negócio e cálculos cronológicos ocorrem localmente no navegador do usuário. Isso garante que nenhuma informação sensível seja trafegada em rede, entregando autonomia, segurança e valor prático ao usuário final.

---

## ⚙️ Regras de Negócio e Funcionalidades

### 1. Motor de Previsão de Ciclo
- Processa o *input* do usuário para projetar a data exata do início do próximo ciclo.
- Algoritmo dinâmico que se adapta a durações customizadas (ex: ciclos de 28, 30 ou 35 dias).

### 2. Estimativa de Janela Fértil
- Implementação lógica do método da **Tabela (Ogino-Knaus)** de forma reversa.
- Isola matematicamente a data de ovulação (14 dias antes do fim do ciclo) e projeta a janela de alta probabilidade de concepção.

### 3. Indicador de Fase Lútea (TPM)
- Sinaliza automaticamente a transição para a fase lútea (tipicamente 7 dias antes do reinício do ciclo), fornecendo previsibilidade sobre alterações físicas e de humor.

### 4. Persistência de Dados Zero-Trust (Local)
- Integração direta com a API `localStorage` do navegador para retenção de estado.
- Garante uma experiência de usuário (UX) fluida sem necessidade de reentrada de dados, mantendo total soberania das informações.

---

## 💻 Stack Tecnológico e Decisões Técnicas

- **HTML5:** Estruturação semântica do DOM focada em acessibilidade.
- **CSS3:** Design responsivo baseado no sistema "Calm UI", utilizando variáveis CSS para padronização global e *Grid Layout* para os componentes de resultados.
- **Vanilla JavaScript (ES6):**
  - Manipulação avançada do objeto `Date()` (tratamento de *edge cases* e *timezone offsets* utilizando *strings* ISO para evitar inconsistências de fuso horário).
  - Manipulação de DOM e gerenciamento de estado da interface em tempo real.
  - Lógica de persistência de dados *client-side*.

---

## 🚀 Execução Local

Por ser uma aplicação 100% *client-side*, não há necessidade de provisionamento de *backend* ou contêineres.

1. Clone o repositório:
   ```bash
   git clone [https://github.com/othipedroso/ciclo-zen.git](https://github.com/othipedroso/ciclo-zen.git)
