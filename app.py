"""
🎯 PREDICTFY DASHBOARD - BENTO GRID ULTRA MODERNA V3 RESPONSIVA
====================================================

Dashboard estilizada com design moderno, gradiente Ciano-Azul-Roxo
e layout Bento Grid totalmente responsivo para Mobile/Tablet/Desktop

Autor: Predictfy Team
Data: Novembro 2025
Versão: 3.0 - Premium Edition (Mobile Ready) - Fixed Overflow
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import os
from pathlib import Path

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================

st.set_page_config(
    page_title="Predictfy | ClickBus Analytics",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# TEMA FIXO - DARKER
# ============================================================================

tema_atual = {
    'bg': 'linear-gradient(135deg, #050510 0%, #0a0a15 25%, #0f0f1f 50%, #0a0a15 75%, #050510 100%)',
    'accent1': '#0891b2',
    'accent2': '#2563eb',
    'accent3': '#7c3aed',
    'glow': 'rgba(37, 99, 235, 0.5)'
}

# ============================================================================
# ESTILOS CSS ULTRA MODERNOS
# ============================================================================

st.markdown(f"""
    <style>
    /* IMPORTAR FONTE MODERNA */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    
    * {{
        font-family: 'Inter', sans-serif !important;
    }}
    
    /* === PARTÍCULAS ANIMADAS === */
    @keyframes float {{
        0%, 100% {{ transform: translateY(0px) translateX(0px); opacity: 0.3; }}
        25% {{ transform: translateY(-20px) translateX(10px); opacity: 0.5; }}
        50% {{ transform: translateY(-40px) translateX(-10px); opacity: 0.7; }}
        75% {{ transform: translateY(-20px) translateX(5px); opacity: 0.5; }}
    }}
    
    .particle {{
        position: fixed;
        width: 3px;
        height: 3px;
        background: {tema_atual['accent1']};
        border-radius: 50%;
        pointer-events: none;
        z-index: 1;
        animation: float 15s infinite ease-in-out;
        box-shadow: 0 0 10px {tema_atual['accent1']};
    }}
    
    .particle:nth-child(2) {{ left: 20%; top: 20%; animation-delay: 2s; animation-duration: 18s; }}
    .particle:nth-child(3) {{ left: 40%; top: 60%; animation-delay: 4s; animation-duration: 20s; }}
    .particle:nth-child(4) {{ left: 60%; top: 30%; animation-delay: 1s; animation-duration: 16s; }}
    .particle:nth-child(5) {{ left: 80%; top: 70%; animation-delay: 3s; animation-duration: 22s; }}
    .particle:nth-child(6) {{ left: 15%; top: 80%; animation-delay: 5s; animation-duration: 19s; }}
    .particle:nth-child(7) {{ left: 70%; top: 15%; animation-delay: 2.5s; animation-duration: 17s; }}
    .particle:nth-child(8) {{ left: 35%; top: 45%; animation-delay: 4.5s; animation-duration: 21s; }}
    
    /* FUNDO ANIMADO */
    @keyframes animated-gradient {{
      0% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
      100% {{ background-position: 0% 50%; }}
    }}
    
    [data-testid="stAppViewContainer"] {{
        background: {tema_atual['bg']};
        background-size: 300% 300%;
        animation: animated-gradient 25s ease infinite;
        min-height: 100vh;
        overflow-y: visible !important;
    }}
    
    [data-testid="stHeader"] {{
        background: transparent;
    }}
    
    html, body {{
        overflow-y: auto !important;
        height: auto !important;
    }}
    
    /* REMOVER PADDING PADRÃO */
    .block-container {{
        padding-top: 3rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: 100%;
    }}
    
    h1 {{
        color: #fafafa;
        font-weight: 900;
        font-size: 3rem !important;
        letter-spacing: -1px;
        margin-bottom: 0.5rem;
        text-align: center;
    }}
    
    h2 {{
        color: #e0e0e0;
        font-weight: 700;
        font-size: 1.5rem !important;
        margin-top: 2rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap;
    }}
    
    h3 {{
        color: #fafafa;
        font-weight: 600;
        font-size: 1.1rem !important;
        margin-bottom: 1rem;
    }}
    
    /* === EFEITO 3D NOS CARDS === */
    .bento-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
        margin-bottom: 20px;
        position: relative;
        z-index: 1;
        overflow: hidden;
    }}
    
    .bento-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 15px 40px 0 {tema_atual['glow']};
        border: 1px solid {tema_atual['accent2']};
        z-index: 10;
    }}
    
    /* METRIC CARDS */
    .metric-card {{
        background: linear-gradient(135deg, rgba(8, 145, 178, 0.1) 0%, rgba(37, 99, 235, 0.1) 50%, rgba(124, 58, 237, 0.1) 100%);
        border: 2px solid transparent;
        border-image: linear-gradient(135deg, {tema_atual['accent1']}, {tema_atual['accent2']}, {tema_atual['accent3']}) 1;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
        margin-bottom: 15px;
        position: relative;
        z-index: 1;
    }}

    .metric-card:hover {{
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 0 30px {tema_atual['glow']};
        z-index: 10;
    }}

    .stPlotlyChart {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 16px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
        margin-bottom: 20px;
        position: relative;
        z-index: 1;
        overflow: hidden;
    }}

    .stPlotlyChart:hover {{
        transform: translateY(-5px);
        box-shadow: 0 15px 40px 0 {tema_atual['glow']};
        border: 1px solid {tema_atual['accent2']};
        z-index: 10;
    }}
    
    /* === ANIMAÇÃO DE ENTRADA === */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    .fade-in {{
        animation: fadeInUp 0.8s ease-out forwards;
    }}
    
    .metric-value {{
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, {tema_atual['accent1']} 0%, {tema_atual['accent2']} 50%, {tema_atual['accent3']} 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        color: transparent;
        margin: 0;
        line-height: 1.2;
        display: inline-block;
    }}
    
    .metric-label {{
        font-size: 0.85rem;
        color: #a0a0a0;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: 8px;
        font-weight: 600;
    }}
    
    .metric-delta {{
        font-size: 0.8rem;
        color: {tema_atual['accent1']};
        margin-top: 4px;
        font-weight: 600;
    }}
    
    /* === TOOLTIPS INFORMATIVOS === */
    .tooltip-icon {{
        display: inline-block;
        width: 20px;
        height: 20px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        text-align: center;
        line-height: 20px;
        font-size: 12px;
        cursor: help;
        margin-left: 8px;
        transition: all 0.3s ease;
    }}
    
    .tooltip-icon:hover {{
        background: {tema_atual['accent2']};
        transform: scale(1.2);
    }}
    
    .tooltip-icon::after {{
        content: 'ℹ️';
        font-size: 10px;
    }}
    
    /* BADGES COLORIDOS */
    .badge {{
        display: inline-block;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin: 4px;
    }}
    
    .badge-cyan {{
        background: linear-gradient(135deg, {tema_atual['accent1']} 0%, #0891b2 100%);
        color: white;
        box-shadow: 0 4px 15px {tema_atual['glow']};
    }}
    
    .badge-blue {{
        background: linear-gradient(135deg, {tema_atual['accent2']} 0%, #2563eb 100%);
        color: white;
        box-shadow: 0 4px 15px {tema_atual['glow']};
    }}
    
    .badge-purple {{
        background: linear-gradient(135deg, {tema_atual['accent3']} 0%, #7c3aed 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4);
    }}
    
    .badge-orange {{
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.4);
    }}
    
    .badge-red {{
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(239, 68, 68, 0.4);
    }}
    
    /* ALERT BOX */
    .alert-box {{
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.15) 0%, rgba(251, 146, 60, 0.15) 100%);
        border-left: 4px solid #f59e0b;
        border-radius: 12px;
        padding: 16px 20px;
        margin: 20px 0;
        color: #fbbf24;
    }}
    
    .alert-box strong {{
        color: #f59e0b;
    }}
    
    /* INSIGHT CARDS */
    .insight-card {{
        background: rgba(255, 255, 255, 0.03);
        border-radius: 16px;
        padding: 20px;
        border-left: 4px solid;
        transition: all 0.3s ease;
        margin-bottom: 12px;
    }}
    
    .insight-card:hover {{
        background: rgba(255, 255, 255, 0.05);
        transform: translateX(5px);
    }}
    
    .insight-card h3 {{
        margin-top: 0;
        margin-bottom: 12px;
    }}
    
    /* === MINI DASHBOARD COMPARATIVO (SEMPRE ABERTO) === */
    .comparison-mini {{
        background: rgba(255, 255, 255, 0.03);
        border-radius: 16px;
        padding: 20px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    .comparison-header {{
        font-weight: 700;
        color: {tema_atual['accent2']};
        font-size: 1.1rem;
        margin-bottom: 20px;
    }}
    
    .comparison-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }}
    
    /* REMOVER ELEMENTOS DESNECESSÁRIOS */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* ANIMAÇÃO PULSE */
    @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.85; }}
    }}
    
    .pulse {{
        animation: pulse 2.5s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }}
    
    /* SCROLLBAR ESTILIZADA */
    ::-webkit-scrollbar {{
        width: 8px;
        height: 8px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: rgba(255, 255, 255, 0.05);
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: linear-gradient(135deg, {tema_atual['accent1']}, {tema_atual['accent2']}, {tema_atual['accent3']});
        border-radius: 10px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: linear-gradient(135deg, #0891b2, #2563eb, #7c3aed);
    }}
    
    /* ===================================================================== */
    /* 📱 RESPONSIVIDADE MOBILE/TABLET */
    /* ===================================================================== */
    
    /* TABLETS E TELAS MÉDIAS (< 1024px) */
    @media screen and (max-width: 1024px) {{
        .block-container {{
            padding-left: 1.5rem;
            padding-right: 1.5rem;
            padding-top: 2rem;
        }}
        
        h1 {{
            font-size: 2.2rem !important;
        }}
        
        h2 {{
            font-size: 1.3rem !important;
        }}
        
        h3 {{
            font-size: 1rem !important;
        }}
        
        .metric-card {{
            padding: 18px;
        }}
        
        .metric-value {{
            font-size: 2rem;
        }}
        
        .metric-label {{
            font-size: 0.75rem;
            letter-spacing: 1.5px;
        }}
        
        .bento-card {{
            padding: 18px;
        }}
        
        .stPlotlyChart {{
            padding: 14px;
        }}
        
        .comparison-header {{
            font-size: 1rem;
        }}
    }}
    
    /* MOBILE E TELAS PEQUENAS (< 768px) */
    @media screen and (max-width: 768px) {{
        .block-container {{
            padding: 1.5rem 1rem;
        }}
        
        h1 {{
            font-size: 1.8rem !important;
            letter-spacing: -0.5px;
            line-height: 1.2;
        }}
        
        h2 {{
            font-size: 1.1rem !important;
            margin-top: 1.5rem;
        }}
        
        h3 {{
            font-size: 0.95rem !important;
        }}
        
        /* Cards menores e empilhados */
        .metric-card {{
            padding: 16px 12px;
            margin-bottom: 12px;
        }}
        
        .metric-value {{
            font-size: 1.8rem;
        }}
        
        .metric-label {{
            font-size: 0.7rem;
            letter-spacing: 1px;
        }}
        
        .metric-delta {{
            font-size: 0.7rem;
        }}
        
        .bento-card {{
            padding: 16px;
            margin-bottom: 15px;
        }}
        
        .stPlotlyChart {{
            padding: 12px;
            margin-bottom: 15px;
        }}
        
        /* Grid responsivo - empilha em 1 coluna */
        .comparison-grid {{
            grid-template-columns: 1fr !important;
            gap: 15px;
        }}
        
        .comparison-mini {{
            padding: 15px;
        }}
        
        .comparison-header {{
            font-size: 0.95rem;
            margin-bottom: 15px;
        }}
        
        /* Badges menores */
        .badge {{
            font-size: 0.65rem;
            padding: 5px 10px;
            margin: 3px;
        }}
        
        /* Alert box responsivo */
        .alert-box {{
            padding: 12px 16px;
            font-size: 0.85rem;
            margin: 15px 0;
        }}
        
        /* Insight cards */
        .insight-card {{
            padding: 16px;
            margin-bottom: 10px;
        }}
        
        .insight-card h3 {{
            font-size: 0.9rem !important;
        }}
        
        .insight-card p {{
            font-size: 0.85rem;
            line-height: 1.5;
        }}
        
        /* Desabilitar efeitos 3D no mobile (performance) */
        .bento-card:hover,
        .metric-card:hover,
        .stPlotlyChart:hover {{
            transform: none;
        }}
        
        /* Partículas desabilitadas no mobile (performance) */
        .particle {{
            display: none;
        }}
        
        /* Texto do subtítulo menor */
        p {{
            font-size: 0.85rem;
        }}
    }}
    
    /* MOBILE MUITO PEQUENO (< 480px) */
    @media screen and (max-width: 480px) {{
        .block-container {{
            padding: 1rem 0.75rem;
        }}
        
        h1 {{
            font-size: 1.5rem !important;
            margin-bottom: 0.3rem;
        }}
        
        h2 {{
            font-size: 1rem !important;
            margin-top: 1rem;
        }}
        
        h3 {{
            font-size: 0.85rem !important;
        }}
        
        .metric-card {{
            padding: 12px 10px;
        }}
        
        .metric-value {{
            font-size: 1.5rem;
        }}
        
        .metric-label {{
            font-size: 0.65rem;
            letter-spacing: 0.5px;
        }}
        
        .bento-card {{
            padding: 12px;
        }}
        
        .stPlotlyChart {{
            padding: 10px;
        }}
        
        .comparison-mini {{
            padding: 12px;
        }}
        
        .comparison-header {{
            font-size: 0.85rem;
        }}
        
        .badge {{
            font-size: 0.6rem;
            padding: 4px 8px;
        }}
        
        .alert-box {{
            font-size: 0.8rem;
            padding: 10px 12px;
        }}
        
        .insight-card {{
            padding: 12px;
        }}
        
        .tooltip-icon {{
            width: 16px;
            height: 16px;
            font-size: 10px;
        }}
    }}
    
    /* LANDSCAPE MOBILE (altura < 500px) */
    @media screen and (max-height: 500px) {{
        h1 {{
            font-size: 1.3rem !important;
        }}
        
        .metric-card {{
            padding: 10px;
        }}
        
        .metric-value {{
            font-size: 1.3rem;
        }}
    }}
    
    /* FORÇAR CONTENÇÃO DOS GRÁFICOS */
    [data-testid="stVerticalBlock"] > div {{
        overflow: hidden !important;
    }}
    
    [data-testid="column"] {{
        overflow: hidden !important;
        padding: 0 8px !important;
        position: relative;
        z-index: 1;
    }}
    
    [data-testid="column"]:hover {{
        z-index: 10;
    }}
    
    </style>
    
    <!-- PARTÍCULAS ANIMADAS -->
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    
    <!-- JAVASCRIPT PARA ANIMAÇÃO DE ENTRADA -->
    <script>
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.classList.add('fade-in');
                }}
            }});
        }}, {{ threshold: 0.1 }});
        
        setTimeout(() => {{
            document.querySelectorAll('.metric-card, .bento-card, .stPlotlyChart').forEach(el => {{
                observer.observe(el);
            }});
        }}, 100);
    </script>
""", unsafe_allow_html=True)

# ============================================================================
# FUNÇÕES DE CARREGAMENTO DE DADOS
# ============================================================================

try:
    notebook_path = os.path.dirname(__file__)
except NameError:
    notebook_path = os.getcwd()

project_root = notebook_path
while not os.path.exists(os.path.join(project_root, '.gitignore')):
    project_root = os.path.dirname(project_root)
    if project_root == os.path.dirname(project_root):
        project_root = notebook_path
        break

PASTA_GRAFICOS = os.path.join(project_root, 'Desafios', 'data', 'bi') + '/'
CSV = os.path.join(project_root, 'Desafios', 'data', 'csv') + '/'

@st.cache_data
def carregar_dados_clusters():
    """Carrega dados de clusters do CSV."""
    try:
        df = pd.read_csv(f'{CSV}cluster.csv', sep=',', encoding='utf-8')
        df['tipo'] = df['cluster'].apply(lambda x: 'Empresa' if 'Empresa' in x else 'Pessoa')
        df = df.rename(columns={
            'Qtd': 'quantidade',
            'recency_mean': 'recencia_media',
            'frequency_mean': 'frequencia_media',
            'monetary_mean': 'gasto_medio_total'
        })
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados de clusters: {e}")
        return None

@st.cache_data
def carregar_dados_clientes():
    """Carrega dados de clientes."""
    try:
        df = pd.read_csv(f'{CSV}cliente.csv', sep=',', encoding='utf-8')
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados de clientes: {e}")
        return None

@st.cache_data
def carregar_recomendacoes():
    """Carrega recomendações."""
    try:
        df = pd.read_csv(f'{CSV}recomendacoes_finais_desafio3.csv', sep=',', encoding='utf-8')
        return df
    except Exception as e:
        st.error(f"Erro ao carregar recomendações: {e}")
        return None

df_clusters = carregar_dados_clusters()
df_clientes = carregar_dados_clientes()
df_recomendacoes = carregar_recomendacoes()

# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def formatar_numero(n):
    """Formata número de forma compacta."""
    if abs(n) < 1000:
        return f'{n:.0f}'
    elif abs(n) < 1_000_000:
        return f'{n/1000:.1f}k'.replace('.0k', 'k')
    elif abs(n) < 1_000_000_000:
        return f'{n/1_000_000:.1f}M'.replace('.0M', 'M')
    else:
        return f'{n/1_000_000_000:.1f}G'.replace('.0G', 'G')

def criar_metric_card(valor, label, delta=None):
    """Cria um card de métrica estilizado."""
    delta_html = f'<div class="metric-delta">↗ {delta}</div>' if delta else ''
    return f"""
    <div class="metric-card">
        <div class="metric-value">{valor}</div>
        <div class="metric-label">{label}</div>
        {delta_html}
    </div>
    """

def criar_badge(texto, cor="cyan"):
    """Cria um badge colorido."""
    return f'<span class="badge badge-{cor}">{texto}</span>'

def criar_tooltip(texto_tooltip):
    """Cria um ícone de tooltip com informação."""
    return f'<span class="tooltip-icon" title="{texto_tooltip}"></span>'

# ============================================================================
# VERIFICAR SE DADOS FORAM CARREGADOS
# ============================================================================

if df_clusters is None:
    st.error("❌ Erro ao carregar dados! Verifique o caminho dos arquivos CSV.")
    st.stop()

# ============================================================================
# HEADER PRINCIPAL COM GRADIENTE
# ============================================================================

st.markdown(f"""
<div style="text-align: center; margin-bottom: 40px;">
    <h1 class="pulse" style="
        color: {tema_atual['accent2']};
        display: inline-block;
        margin-bottom: 10px;
        text-shadow: 0 0 30px {tema_atual['glow']}, 0 0 60px {tema_atual['glow']};
    ">PREDICTFY X CLICKBUS</h1>
    <p style="color: #a0a0a0; font-size: 1rem; letter-spacing: 3px; margin-top: 0;">
        CLUSTERIZAÇÃO INTELIGENTE | CHALLENGE CLICKBUS 2025 | NEXT 2025
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# MÉTRICAS PRINCIPAIS
# ============================================================================

total_clientes = df_clusters['quantidade'].sum()
total_clusters = len(df_clusters)
ticket_medio_geral = (df_clusters['quantidade'] * df_clusters['gasto_medio_total']).sum() / total_clientes
clientes_pf = df_clusters[df_clusters['tipo'] == 'Pessoa']['quantidade'].sum()
pct_pf = (clientes_pf / total_clientes * 100)

col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
    st.markdown(criar_metric_card(
        formatar_numero(total_clientes),
        "TOTAL CLIENTES",
        "Base completa"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(criar_metric_card(
        f"{total_clusters}",
        "CLUSTERS",
        "Segmentos"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(criar_metric_card(
        f"R$ {formatar_numero(ticket_medio_geral)}",
        "TICKET MÉDIO",
        "Lifetime Value"
    ), unsafe_allow_html=True)

with col4:
    st.markdown(criar_metric_card(
        f"{pct_pf:.1f}%",
        "PESSOA FÍSICA",
        f"{formatar_numero(clientes_pf)} clientes"
    ), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================================
# MINI DASHBOARD COMPARATIVO (SEMPRE ABERTO)
# ============================================================================

st.markdown(f"""
<div class="comparison-mini">
    <div class="comparison-header">
        📊 COMPARAÇÃO RÁPIDA: PF vs PJ
    </div>
    <div class="comparison-grid">
        <div style="text-align: center; padding: 20px; background: rgba(37, 99, 235, 0.1); border-radius: 12px;">
            <div style="font-size: 0.8rem; color: #888; margin-bottom: 10px;">👥 PESSOA FÍSICA</div>
            <div style="font-size: 2rem; color: {tema_atual['accent2']}; font-weight: 900;">{formatar_numero(clientes_pf)}</div>
            <div style="font-size: 0.75rem; color: #888; margin-top: 5px;">clientes</div>
        </div>
        <div style="text-align: center; padding: 20px; background: rgba(16, 185, 129, 0.1); border-radius: 12px;">
            <div style="font-size: 0.8rem; color: #888; margin-bottom: 10px;">🏢 PESSOA JURÍDICA</div>
            <div style="font-size: 2rem; color: #10b981; font-weight: 900;">{df_clusters[df_clusters['tipo'] == 'Empresa']['quantidade'].sum()}</div>
            <div style="font-size: 0.75rem; color: #888; margin-top: 5px;">empresas</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================================
# SEÇÃO PESSOA FÍSICA
# ============================================================================

st.markdown(f"""
## 👥 Análise: Pessoa Física {criar_tooltip("Análise detalhada dos clientes pessoa física segmentados por comportamento de compra")}
""", unsafe_allow_html=True)

df_pessoa = df_clusters[df_clusters['tipo'] == 'Pessoa'].sort_values('quantidade', ascending=False)

col1, col2 = st.columns([1, 1], gap="small")

with col1:
    cores_pf = [tema_atual['accent1'], tema_atual['accent2'], tema_atual['accent3'], '#a855f7']
    
    fig = px.pie(
        df_pessoa,
        values='quantidade',
        names=df_pessoa['cluster'].str.replace('Pessoa - ', ''),
        color_discrete_sequence=cores_pf,
        hole=0.5
    )
    
    fig.update_traces(
        textposition='outside',
        textinfo='percent+label',
        textfont=dict(color='white', size=11, family='Inter'),
        marker=dict(line=dict(color='#0a0e27', width=3))
    )
    
    fig.update_layout(
        title=dict(
            text='📊 Distribuição de Clientes PF',
            font=dict(color='#fafafa', size=16, family='Inter'),
            x=0.05, y=0.95, xanchor='left', yanchor='top'
        ),
        height=380,
        margin=dict(l=5, r=5, t=60, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=11, family='Inter'),
        showlegend=True,
        legend=dict(
            orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.01,
            bgcolor='rgba(255,255,255,0.05)',
            bordercolor='rgba(255,255,255,0.1)', borderwidth=1,
            font=dict(size=10)
        ),
        autosize=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = go.Figure()
    
    for idx, (index, row) in enumerate(df_pessoa.iterrows()):
        fig.add_trace(go.Bar(
            y=[row['cluster'].replace('Pessoa - ', '')],
            x=[row['gasto_medio_total']],
            orientation='h',
            marker=dict(color=cores_pf[idx], line=dict(color='white', width=2)),
            text=f"R$ {formatar_numero(row['gasto_medio_total'])}",
            textposition='auto',
            textfont=dict(color='white', size=12, family='Inter'),
            showlegend=False,
            hovertemplate=f"<b>{row['cluster']}</b><br>R$ {row['gasto_medio_total']:.2f}<extra></extra>"
        ))
    
    fig.update_layout(
        title=dict(
            text='💰 Gasto Médio por Cluster PF',
            font=dict(color='#fafafa', size=16, family='Inter'),
            x=0.05, y=0.95, xanchor='left', yanchor='top'
        ),
        height=380,
        margin=dict(l=5, r=5, t=60, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', color='white', title=None),
        yaxis=dict(showgrid=False, color='white'),
        font=dict(color='white', family='Inter'),
        autosize=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns([3, 2], gap="small")

with col1:
    fig = px.scatter(
        df_pessoa,
        x='recencia_media',
        y='frequencia_media',
        size='quantidade',
        color='gasto_medio_total',
        hover_name='cluster',
        color_continuous_scale=[[0, tema_atual['accent1']], [0.5, tema_atual['accent2']], [1, tema_atual['accent3']]],
        size_max=60
    )
    
    fig.update_layout(
        title=dict(
            text='⚡ Recência vs Frequência PF',
            font=dict(color='#fafafa', size=16, family='Inter'),
            x=0.05, y=0.95, xanchor='left', yanchor='top'
        ),
        height=350,
        margin=dict(l=5, r=5, t=60, b=5),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', color='white', title='Recência (dias)'),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', color='white', title='Frequência'),
        font=dict(color='white', family='Inter'),
        coloraxis_colorbar=dict(
            title="Gasto<br>Médio", titleside="right",
            titlefont=dict(color='white', size=10), tickfont=dict(color='white', size=9),
            bgcolor='rgba(255,255,255,0.05)',
            bordercolor='rgba(255,255,255,0.1)', borderwidth=1,
            len=0.7
        ),
        autosize=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)

    df_pessoa['valor_total'] = df_pessoa['quantidade'] * df_pessoa['gasto_medio_total']
    
    fig_treemap_pf = px.treemap(
        df_pessoa,
        path=[px.Constant("Clientes PF"), df_pessoa['cluster'].str.replace('Pessoa - ', '')],
        values='valor_total',
        color='gasto_medio_total',
        color_continuous_scale=[[0, tema_atual['accent1']], [0.5, tema_atual['accent2']], [1, tema_atual['accent3']]],
        hover_data={'quantidade': ':.0f', 'gasto_medio_total': ':.2f', 'valor_total': ':.2f'},
        custom_data=['quantidade', 'gasto_medio_total', 'valor_total']
    )
    
    fig_treemap_pf.update_traces(
        texttemplate="<b>%{label}</b><br>R$ %{value:,.2s}",
        textfont=dict(color='white', size=13, family='Inter'),
        hovertemplate="<b>%{label}</b><br><br>Valor Total: R$ %{customdata[2]:,.2f}<br>Clientes: %{customdata[0]:,.0f}<br>Gasto Médio: R$ %{customdata[1]:,.2f}<extra></extra>"
    )
    
    fig_treemap_pf.update_layout(
        title=dict(
            text='💸 Impacto Financeiro Total por Cluster PF',
            font=dict(color='#fafafa', size=16, family='Inter'),
            x=0.05, y=0.95, xanchor='left', yanchor='top'
        ),
        height=400,
        margin=dict(l=5, r=5, t=60, b=5),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', family='Inter'),
        coloraxis_colorbar=dict(
            title="Gasto<br>Médio", titleside="right",
            titlefont=dict(color='white', size=10), tickfont=dict(color='white', size=9),
            bgcolor='rgba(255,255,255,0.05)',
            bordercolor='rgba(255,255,255,0.1)', borderwidth=1,
            len=0.7
        ),
        autosize=True
    )
    
    st.plotly_chart(fig_treemap_pf, use_container_width=True)

with col2:
    badges_cores = ['cyan', 'blue', 'purple', 'orange']
    
    html_content = '<div class="bento-card"><h3>🎯 Top Oportunidades PF</h3>'
    
    for idx, (index, row) in enumerate(df_pessoa.head(4).iterrows()):
        html_content += f'<div class="insight-card" style="border-left-color: {cores_pf[idx]}; margin-bottom: 12px;">'
        html_content += f'{criar_badge(row["cluster"].replace("Pessoa - ", ""), badges_cores[idx])}'
        html_content += '<div style="margin-top: 10px;">'
        html_content += f'<span style="color: {cores_pf[idx]}; font-weight: bold; font-size: 1.3rem;">{formatar_numero(row["quantidade"])}</span>'
        html_content += '<span style="color: #888; margin-left: 8px; font-size: 0.9rem;">clientes</span>'
        html_content += '</div>'
        html_content += f'<div style="margin-top: 6px; color: {tema_atual["accent1"]}; font-size: 0.85rem;">💰 R$ {formatar_numero(row["gasto_medio_total"])} médio</div>'
        html_content += '</div>'
    
    html_content += '</div>'
    st.markdown(html_content, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ============================================================================
# ALERT
# ============================================================================

df_empresa = df_clusters[df_clusters['tipo'] == 'Empresa'].sort_values('quantidade', ascending=False)

st.markdown(f"""
<div class="alert-box">
    <strong>⚠️ ATENÇÃO:</strong> Dados de empresas são extremamente discrepantes de PF. 
    Total: <strong>{df_empresa['quantidade'].sum()} empresas</strong> vs 
    <strong>{formatar_numero(df_pessoa['quantidade'].sum())} pessoas</strong>. 
    Visualizações separadas para melhor análise e compreensão.
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SEÇÃO EMPRESA
# ============================================================================

st.markdown(f"""
## 🏢 Análise: Pessoa Jurídica {criar_tooltip("Análise de empresas com alto volume de compras e transações recorrentes")}
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 2, 2], gap="small")

with col1:
    cores_pj = ['#10b981', '#14b8a6', tema_atual['accent1'], '#0ea5e9']
    
    fig = px.pie(
        df_empresa,
        values='quantidade',
        names=df_empresa['cluster'].str.replace('Empresa - ', ''),
        color_discrete_sequence=cores_pj,
        hole=0.5
    )
    
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        textfont=dict(color='white', size=11, family='Inter'),
        marker=dict(line=dict(color='#0a0e27', width=3))
    )
    
    fig.update_layout(
        title=dict(
            text='📊 Distribuição PJ',
            font=dict(color='#fafafa', size=16, family='Inter'),
            x=0.05, y=0.95, xanchor='left', yanchor='top'
        ),
        height=320,
        margin=dict(l=5, r=5, t=60, b=5),
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        font=dict(color='white', family='Inter'),
        autosize=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = go.Figure()
    
    for idx, (index, row) in enumerate(df_empresa.iterrows()):
        fig.add_trace(go.Bar(
            y=[row['cluster'].replace('Empresa - ', '')],
            x=[row['gasto_medio_total']],
            orientation='h',
            marker=dict(color=cores_pj[idx], line=dict(color='white', width=2)),
            text=f"R$ {formatar_numero(row['gasto_medio_total'])}",
            textposition='auto',
            textfont=dict(color='white', size=11, family='Inter'),
            showlegend=False
        ))
    
    fig.update_layout(
        title=dict(
            text='💎 Valor Médio PJ',
            font=dict(color='#fafafa', size=16, family='Inter'),
            x=0.05, y=0.95, xanchor='left', yanchor='top'
        ),
        height=320,
        margin=dict(l=5, r=5, t=60, b=5),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, color='white'),
        yaxis=dict(showgrid=False, color='white'),
        font=dict(color='white', family='Inter'),
        autosize=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col3:
    vip = df_empresa[df_empresa['cluster'].str.contains('VIP')].iloc[0] if len(df_empresa[df_empresa['cluster'].str.contains('VIP')]) > 0 else df_empresa.iloc[0]
    
    html_content = f'<div class="bento-card">'
    html_content += '<h3>🔥 Destaques PJ</h3>'
    html_content += f'<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(6, 182, 212, 0.15)); border-radius: 14px; margin-bottom: 16px; border: 1px solid rgba(16, 185, 129, 0.3);">'
    html_content += f'<div style="font-size: 2.2rem; font-weight: 900; color: #10b981;">{int(vip["frequencia_media"])}</div>'
    html_content += '<div style="color: #a0a0a0; font-size: 0.75rem; margin-top: 4px; letter-spacing: 1px;">COMPRAS MÉDIAS<br>EMPRESA VIP</div>'
    html_content += '</div>'
    html_content += f'<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, rgba(20, 184, 166, 0.15), rgba(6, 182, 212, 0.15)); border-radius: 14px; border: 1px solid rgba(20, 184, 166, 0.3);">'
    html_content += f'<div style="font-size: 2.2rem; font-weight: 900; color: #14b8a6;">R$ {formatar_numero(vip["gasto_medio_total"])}</div>'
    html_content += '<div style="color: #a0a0a0; font-size: 0.75rem; margin-top: 4px; letter-spacing: 1px;">VALOR MÉDIO<br>EMPRESA VIP</div>'
    html_content += '</div>'
    html_content += '</div>'
    
    st.markdown(html_content, unsafe_allow_html=True)

st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)

col_map_pj, _ = st.columns([2, 1], gap="small")

with col_map_pj:
    df_empresa['valor_total'] = df_empresa['quantidade'] * df_empresa['gasto_medio_total']
    
    fig_treemap_pj = px.treemap(
        df_empresa,
        path=[px.Constant("Empresas PJ"), df_empresa['cluster'].str.replace('Empresa - ', '')],
        values='valor_total',
        color='gasto_medio_total',
        color_continuous_scale=[[0, '#10b981'], [0.5, '#14b8a6'], [1, '#0ea5e9']],
        hover_data={'quantidade': ':.0f', 'gasto_medio_total': ':.2f', 'valor_total': ':.2f'},
        custom_data=['quantidade', 'gasto_medio_total', 'valor_total']
    )
    
    fig_treemap_pj.update_traces(
        texttemplate="<b>%{label}</b><br>R$ %{value:,.2s}",
        textfont=dict(color='white', size=13, family='Inter'),
        hovertemplate="<b>%{label}</b><br><br>Valor Total: R$ %{customdata[2]:,.2f}<br>Empresas: %{customdata[0]:,.0f}<br>Gasto Médio: R$ %{customdata[1]:,.2f}<extra></extra>"
    )
    
    fig_treemap_pj.update_layout(
        title=dict(
            text='💸 Impacto Financeiro Total por Cluster PJ',
            font=dict(color='#fafafa', size=16, family='Inter'),
            x=0.05, y=0.95, xanchor='left', yanchor='top'
        ),
        height=400,
        margin=dict(l=5, r=5, t=60, b=5),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', family='Inter'),
        coloraxis_colorbar=dict(
            title="Gasto<br>Médio", titleside="right",
            titlefont=dict(color='white', size=10), tickfont=dict(color='white', size=9),
            bgcolor='rgba(255,255,255,0.05)',
            bordercolor='rgba(255,255,255,0.1)', borderwidth=1,
            len=0.7
        ),
        autosize=True
    )
    
    st.plotly_chart(fig_treemap_pj, use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ============================================================================
# COMPARAÇÃO PF vs PJ
# ============================================================================

st.markdown(f"""
## ⚖️ Comparação: PF vs PJ {criar_tooltip("Análise comparativa entre perfis de pessoa física e jurídica")}
""", unsafe_allow_html=True)

total_pf = df_pessoa['quantidade'].sum()
total_pj = df_empresa['quantidade'].sum()
gasto_medio_pf = (df_pessoa['quantidade'] * df_pessoa['gasto_medio_total']).sum() / total_pf
gasto_medio_pj = (df_empresa['quantidade'] * df_empresa['gasto_medio_total']).sum() / total_pj
freq_media_pf = (df_pessoa['quantidade'] * df_pessoa['frequencia_media']).sum() / total_pf
freq_media_pj = (df_empresa['quantidade'] * df_empresa['frequencia_media']).sum() / total_pj

col1, col2 = st.columns(2, gap="small")

with col1:
    html_content = f'<div class="bento-card" style="border: 2px solid {tema_atual["accent2"]};">'
    html_content += '<h3>👥 PESSOA FÍSICA</h3>'
    html_content += '<div style="text-align: center; margin: 20px 0;">'
    html_content += f'<div style="font-size: 2.8rem; font-weight: 900; background: linear-gradient(90deg, {tema_atual["accent1"]}, {tema_atual["accent2"]}, {tema_atual["accent3"]}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; color: transparent; display: inline-block;">{formatar_numero(total_pf)}</div>'
    html_content += '<div style="color: #888; font-size: 0.85rem; margin-top: 8px; letter-spacing: 1px;">CLIENTES TOTAIS</div>'
    html_content += '</div>'
    html_content += '<hr style="border: 1px solid rgba(255,255,255,0.1); margin: 20px 0;">'
    html_content += '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 20px;">'
    html_content += f'<div style="text-align: center; padding: 16px; background: rgba(59, 130, 246, 0.1); border-radius: 12px;">'
    html_content += f'<div style="font-size: 1.5rem; color: {tema_atual["accent2"]}; font-weight: 700;">R$ {formatar_numero(gasto_medio_pf)}</div>'
    html_content += '<div style="color: #888; font-size: 0.75rem; margin-top: 4px;">GASTO MÉDIO</div>'
    html_content += '</div>'
    html_content += f'<div style="text-align: center; padding: 16px; background: rgba(124, 58, 237, 0.1); border-radius: 12px;">'
    html_content += f'<div style="font-size: 1.5rem; color: {tema_atual["accent3"]}; font-weight: 700;">{freq_media_pf:.1f}</div>'
    html_content += '<div style="color: #888; font-size: 0.75rem; margin-top: 4px;">FREQ. MÉDIA</div>'
    html_content += '</div>'
    html_content += '</div>'
    html_content += '</div>'
    
    st.markdown(html_content, unsafe_allow_html=True)

with col2:
    html_content = f'<div class="bento-card" style="border: 2px solid #10b981;">'
    html_content += '<h3>🏢 PESSOA JURÍDICA</h3>'
    html_content += '<div style="text-align: center; margin: 20px 0;">'
    html_content += f'<div style="font-size: 2.8rem; font-weight: 900; background: linear-gradient(90deg, #10b981, #14b8a6, {tema_atual["accent1"]}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; color: transparent; display: inline-block;">{total_pj}</div>'
    html_content += '<div style="color: #888; font-size: 0.85rem; margin-top: 8px; letter-spacing: 1px;">EMPRESAS TOTAIS</div>'
    html_content += '</div>'
    html_content += '<hr style="border: 1px solid rgba(255,255,255,0.1); margin: 20px 0;">'
    html_content += '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 20px;">'
    html_content += '<div style="text-align: center; padding: 16px; background: rgba(16, 185, 129, 0.1); border-radius: 12px;">'
    html_content += f'<div style="font-size: 1.5rem; color: #10b981; font-weight: 700;">R$ {formatar_numero(gasto_medio_pj)}</div>'
    html_content += '<div style="color: #888; font-size: 0.75rem; margin-top: 4px;">GASTO MÉDIO</div>'
    html_content += '</div>'
    html_content += '<div style="text-align: center; padding: 16px; background: rgba(20, 184, 166, 0.1); border-radius: 12px;">'
    html_content += f'<div style="font-size: 1.5rem; color: #14b8a6; font-weight: 700;">{freq_media_pj:.1f}</div>'
    html_content += '<div style="color: #888; font-size: 0.75rem; margin-top: 4px;">FREQ. MÉDIA</div>'
    html_content += '</div>'
    html_content += '</div>'
    html_content += '</div>'
    
    st.markdown(html_content, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ============================================================================
# INSIGHTS FINAIS
# ============================================================================

st.markdown(f"""
## 💡 Insights Principais {criar_tooltip("Principais descobertas e oportunidades identificadas na análise")}
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4, gap="small")

potencial_qtd = df_pessoa[df_pessoa['cluster'].str.contains('Potencial')]['quantidade'].sum()
dormindo_qtd = df_pessoa[df_pessoa['cluster'].str.contains('Dormindo')]['quantidade'].sum()
quase_dormindo = df_pessoa[df_pessoa['cluster'].str.contains('Quase dormindo')]
quase_dormindo_qtd = quase_dormindo['quantidade'].sum()
quase_dormindo_pct = (quase_dormindo_qtd / total_pf) * 100
quase_dormindo_recencia = quase_dormindo['recencia_media'].iloc[0]

with col1:
    html_content = f'<div class="insight-card" style="border-left-color: {tema_atual["accent2"]}; height: 100%;">'
    html_content += f'<h3 style="color: {tema_atual["accent2"]};">🎯 Oportunidade</h3>'
    html_content += f'<p style="color: #c0c0c0; line-height: 1.6; font-size: 0.9rem;"><strong>{formatar_numero(potencial_qtd)}</strong> clientes no grupo <strong>Potencial</strong> são compradores recentes e representam a maior chance de cross-sell.</p>'
    html_content += f'<div style="margin-top: 12px;">{criar_badge("HIGH PRIORITY", "blue")}</div>'
    html_content += '</div>'
    st.markdown(html_content, unsafe_allow_html=True)

with col2:
    html_content = f'<div class="insight-card" style="border-left-color: #f59e0b; height: 100%;">'
    html_content += '<h3 style="color: #f59e0b;">🔔 Risco de Churn</h3>'
    html_content += f'<p style="color: #c0c0c0; line-height: 1.6; font-size: 0.9rem;"><strong>{formatar_numero(quase_dormindo_qtd)}</strong> clientes ({quase_dormindo_pct:.0f}% da base PF) estão há <strong>{quase_dormindo_recencia:.0f} dias</strong> sem comprar.</p>'
    html_content += f'<div style="margin-top: 12px;">{criar_badge("RETENTION", "orange")}</div>'
    html_content += '</div>'
    st.markdown(html_content, unsafe_allow_html=True)

with col3:
    html_content = f'<div class="insight-card" style="border-left-color: #10b981; height: 100%;">'
    html_content += '<h3 style="color: #10b981;">💎 Alto Valor</h3>'
    html_content += f'<p style="color: #c0c0c0; line-height: 1.6; font-size: 0.9rem;">Empresas <strong>VIP</strong> gastam em média <strong>R$ {formatar_numero(gasto_medio_pj)}</strong>, representando <strong>{gasto_medio_pj/gasto_medio_pf:.0f}x</strong> o valor de PF.</p>'
    html_content += f'<div style="margin-top: 12px;">{criar_badge("PREMIUM", "cyan")}</div>'
    html_content += '</div>'
    st.markdown(html_content, unsafe_allow_html=True)

with col4:
    html_content = f'<div class="insight-card" style="border-left-color: #ef4444; height: 100%;">'
    html_content += '<h3 style="color: #ef4444;">⚠️ Reativação</h3>'
    html_content += f'<p style="color: #c0c0c0; line-height: 1.6; font-size: 0.9rem;"><strong>{formatar_numero(dormindo_qtd)}</strong> clientes dormindo há <strong>+950 dias</strong> precisam de campanhas win-back urgentes.</p>'
    html_content += f'<div style="margin-top: 12px;">{criar_badge("ACTION NEEDED", "red")}</div>'
    html_content += '</div>'
    st.markdown(html_content, unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align: center; padding: 40px 20px; background: rgba(255,255,255,0.02); border-radius: 20px; margin-top: 40px; border: 1px solid rgba(255,255,255,0.05);">
    <div style="font-size: 1.4rem; font-weight: 700; margin-bottom: 12px; background: linear-gradient(90deg, {tema_atual['accent1']}, {tema_atual['accent2']}, {tema_atual['accent3']}); 
         -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; color: transparent; display: inline-block;">
        PREDICTFY X CLICKBUS
    </div>
    <div style="color: #888; font-size: 0.85rem; letter-spacing: 2px;">
        CHALLENGE CLICKBUS 2025 | DATA SCIENCE & ANALYTICS | NEXT 2025
    </div>
    <div style="margin-top: 20px; display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;">
        <span class="badge badge-cyan">🎯 CLUSTERIZAÇÃO</span>
        <span class="badge badge-blue">💡 INSIGHTS</span>
        <span class="badge badge-purple">📊 ANALYTICS</span>
    </div>
</div>
""", unsafe_allow_html=True)