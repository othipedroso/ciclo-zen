import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime, timedelta

# ==========================================
# CONFIGURATION & CONSTANTS
# ==========================================
st.set_page_config(page_title="CicloZen", page_icon="🌸", layout="centered")
HISTORY_FILE = "ciclo_history.json"
MAX_HISTORY = 24
DISPLAY_DEFAULT = 6

# ==========================================
# DATA ACCESS LAYER
# ==========================================
def load_history():
    """Carrega o histórico de ciclos do arquivo local JSON."""
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def save_cycle(start_date, cycle_length):
    """Salva um novo ciclo e retorna o status da operação."""
    history = load_history()
    
    # Bloqueia registros com a mesma data do último salvo
    if history and history[0].get("start_date") == start_date:
        return "duplicate"

    new_record = {
        "start_date": start_date,
        "cycle_length": cycle_length,
        "recorded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    history.insert(0, new_record)
    
    if len(history) > MAX_HISTORY:
        history = history[:MAX_HISTORY]
        
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=4)
        return "success"
    except Exception as e:
        return str(e)

# ==========================================
# BUSINESS LOGIC
# ==========================================
def calculate_cycle_metrics(last_period_date, cycle_length):
    """Calcula as fases com base no método Ogino-Knaus reverso."""
    start_date = datetime.strptime(last_period_date, "%Y-%m-%d")
    
    next_period = start_date + timedelta(days=cycle_length)
    ovulation = next_period - timedelta(days=14)
    fertile_start = ovulation - timedelta(days=3)
    fertile_end = ovulation + timedelta(days=1)
    tpm_start = next_period - timedelta(days=7)
    
    return {
        "next_period": next_period,
        "ovulation": ovulation,
        "fertile_start": fertile_start,
        "fertile_end": fertile_end,
        "tpm_start": tpm_start
    }

# ==========================================
# UI & PRESENTATION
# ==========================================
st.title("🌸 CicloZen")
st.markdown("Acompanhamento offline, focado em privacidade.")

history = load_history()
last_saved_date = datetime.now()
default_cycle = 28

if history:
    try:
        last_saved_date = datetime.strptime(history[0]["start_date"], "%Y-%m-%d")
        default_cycle = int(history[0]["cycle_length"])
    except ValueError:
        pass

with st.form("cycle_form"):
    col1, col2 = st.columns(2)
    with col1:
        last_period = st.date_input("Data da última menstruação", value=last_saved_date)
    with col2:
        cycle_days = st.number_input("Duração do ciclo (dias)", min_value=20, max_value=45, value=default_cycle)
    
    submitted = st.form_submit_button("Calcular e Salvar", use_container_width=True)

if submitted:
    date_str = last_period.strftime("%Y-%m-%d")
    status = save_cycle(date_str, cycle_days)
    
    if status == "success":
        st.success('Ciclo registrado com sucesso!')
        st.rerun()
    elif status == "duplicate":
        st.warning('Esta data já foi registrada no último ciclo. Nenhuma duplicata foi criada.')
    else:
        st.error(f'Erro interno ao tentar salvar o arquivo: {status}')

if history:
    st.divider()
    latest = history[0]
    metrics = calculate_cycle_metrics(latest["start_date"], latest["cycle_length"])
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info(f"**Próximo Ciclo**\n\n{metrics['next_period'].strftime('%d/%m/%Y')}")
    with c2:
        st.success(f"**Janela Fértil**\n\n{metrics['fertile_start'].strftime('%d/%m')} a {metrics['fertile_end'].strftime('%d/%m')}")
    with c3:
        st.error(f"**Alerta TPM**\n\nA partir de {metrics['tpm_start'].strftime('%d/%m/%Y')}")

    st.divider()
    st.subheader("📜 Histórico de Ciclos")
    
    df = pd.DataFrame(history)
    df['start_date'] = pd.to_datetime(df['start_date']).dt.strftime('%d/%m/%Y')
    df['recorded_at'] = pd.to_datetime(df['recorded_at']).dt.strftime('%d/%m/%Y %H:%M')
    df = df.rename(columns={'start_date': 'Início', 'cycle_length': 'Duração (Dias)', 'recorded_at': 'Registrado em'})
    
    recent_df = df.head(DISPLAY_DEFAULT)
    st.dataframe(recent_df, use_container_width=True, hide_index=True)
    
    if len(history) > DISPLAY_DEFAULT:
        with st.expander(f"Ver todos os registros salvos ({len(history)}/{MAX_HISTORY})"):
            st.dataframe(df, use_container_width=True, hide_index=True)