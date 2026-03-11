import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

st.set_page_config(page_title="Israel Health 2020-2025", page_icon="🏥", layout="wide")
st.title("🏥 Impacto en la Salud de Israel (2020–2025)")
st.caption("DOI: 10.7910/DVN/PL3G1E | Harvard Dataverse | CC0 1.0")

page = st.sidebar.selectbox("Sección", [
    "Inicio","Esperanza de Vida","Mortalidad","COVID-19","Vacunación",
    "Salud Mental","Guerra & Salud","Sistema Sanitario","Enf. Crónicas",
    "Comparativa OCDE","Factores de Riesgo","Gasto Sanitario","Indicadores Clave","Tendencias","Población"
])
years = [2020,2021,2022,2023,2024,2025]

if page == "Inicio":
    c1,c2,c3 = st.columns(3)
    c1.metric("Esperanza de vida 2024","83.1 años")
    c2.metric("Vacunas COVID-19","6.8M")
    c3.metric("TEPT post-7 Oct","37%")
    c4,c5,c6 = st.columns(3)
    c4.metric("Gasto sanitario/PIB","8.2%")
    c5.metric("Médicos/1.000 hab.","3.1")
    c6.metric("Camas/1.000 hab.","2.2")
    st.info("Dataset sobre el impacto en la salud de Israel 2020-2025: pandemia COVID-19, vacunación masiva e impacto del conflicto del 7-Oct-2023. Fuentes: Centro Taub, NIH, OMS, OCDE.")
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=years,y=[82.1,81.8,82.5,82.8,83.1,83.3],name="Esperanza de vida",line=dict(color="#58a6ff",width=3)),secondary_y=False)
    fig.add_trace(go.Scatter(x=years,y=[7.8,7.9,8.0,8.1,8.2,8.3],name="Gasto %PIB",line=dict(color="#3fb950",width=3)),secondary_y=True)
    fig.update_layout(template="plotly_dark",height=400,title="Panorama General 2020-2025")
    st.plotly_chart(fig,use_container_width=True)
elif page == "Esperanza de Vida":
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years,y=[82.1,81.8,82.5,82.8,83.1,83.3],name="Total",line=dict(color="#58a6ff",width=3)))
    fig.add_trace(go.Scatter(x=years,y=[80.5,80.2,80.9,81.2,81.6,81.8],name="Hombres",line=dict(color="#3fb950",width=3)))
    fig.add_trace(go.Scatter(x=years,y=[83.6,83.3,84.0,84.3,84.5,84.7],name="Mujeres",line=dict(color="#ff7b72",width=3)))
    fig.update_layout(template="plotly_dark",height=450,title="Esperanza de vida por género",yaxis_title="Años")
    st.plotly_chart(fig,use_container_width=True)
elif page == "Mortalidad":
    fig = go.Figure()
    fig.add_trace(go.Bar(x=years,y=[5.6,6.1,5.8,5.7,5.5,5.4],name="Mortalidad general/1.000",marker_color="#58a6ff"))
    fig.add_trace(go.Bar(x=years,y=[1.2,2.1,1.4,0.9,0.4,0.2],name="Mortalidad COVID/100.000",marker_color="#ff7b72"))
    fig.update_layout(template="plotly_dark",barmode="group",height=420,title="Tasas de mortalidad 2020-2025")
    st.plotly_chart(fig,use_container_width=True)
elif page == "COVID-19":
    c1,c2,c3 = st.columns(3)
    c1.metric("Casos confirmados","~4.8M")
    c2.metric("Fallecidos","~12.300")
    c3.metric("3ª dosis cobertura","~56%")
    fig = go.Figure(go.Scatter(x=[2020,2021,2022,2023],y=[150000,1200000,2800000,4800000],fill='tozeroy',line=dict(color="#ff7b72")))
    fig.update_layout(template="plotly_dark",height=400,title="Casos COVID-19 acumulados")
    st.plotly_chart(fig,use_container_width=True)
elif page == "Vacunación":
    c1,c2 = st.columns(2)
    c1.metric("Vacunas administradas","6.8M")
    c2.metric("Cobertura 2ª dosis","~64%")
    fig = go.Figure(go.Bar(x=["1ª dosis","2ª dosis","3ª dosis","4ª dosis"],y=[6800000,6100000,4200000,2100000],marker_color=["#58a6ff","#3fb950","#ffa657","#ff7b72"]))
    fig.update_layout(template="plotly_dark",height=400,title="Dosis administradas por tipo")
    st.plotly_chart(fig,use_container_width=True)
elif page == "Salud Mental":
    c1,c2,c3 = st.columns(3)
    c1.metric("TEPT post-guerra","37%")
    c2.metric("Ansiedad generalizada","25%")
    c3.metric("Depresión mayor","18%")
    fig = go.Figure(go.Bar(x=["TEPT","Ansiedad","Depresión","Burnout sanitario","Trastornos sueño"],y=[37,25,18,42,55],marker_color="#58a6ff"))
    fig.update_layout(template="plotly_dark",height=400,title="Prevalencia de condiciones de salud mental (%)",yaxis_title="%")
    st.plotly_chart(fig,use_container_width=True)
elif page == "Guerra & Salud":
    c1,c2,c3 = st.columns(3)
    c1.metric("Heridos en conflicto","~8.730")
    c2.metric("Personal médico movilizado","~15.000")
    c3.metric("Hospitales en zona conflicto","12")
    st.warning("El conflicto del 7-Oct-2023 generó un aumento masivo de trauma físico y psicológico en la población.")
    fig = go.Figure(go.Bar(x=["Trauma físico","TEPT (miles)","Cap. hospitalaria %","Desplazados (miles)","Atención 1ª %"],y=[8730,37,25,200,30],marker_color=["#ff7b72","#ffa657","#58a6ff","#d2a8ff","#3fb950"]))
    fig.update_layout(template="plotly_dark",height=400,title="Indicadores de impacto del conflicto")
    st.plotly_chart(fig,use_container_width=True)
elif page == "Sistema Sanitario":
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Médicos/1.000","3.1")
    c2.metric("Camas/1.000","2.2")
    c3.metric("Gasto/PIB","8.2%")
    c4.metric("Hospitales públicos","41")
    ind = ["Médicos/1.000","Enfermeras/1.000","Camas/1.000","Médicos esp./1.000"]
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Israel",x=ind,y=[3.1,5.1,2.2,1.8],marker_color="#58a6ff"))
    fig.add_trace(go.Bar(name="OCDE media",x=ind,y=[3.5,8.8,4.3,1.9],marker_color="#3fb950"))
    fig.update_layout(template="plotly_dark",barmode="group",height=420,title="Recursos sanitarios: Israel vs OCDE")
    st.plotly_chart(fig,use_container_width=True)
elif page == "Enf. Crónicas":
    fig = go.Figure(go.Bar(x=["Cardiovascular","Diabetes tipo 2","Obesidad","Cáncer","Hipertensión","EPOC"],y=[28,8.5,26,12,33,6],marker_color=["#ff7b72","#ffa657","#ffd700","#58a6ff","#3fb950","#d2a8ff"]))
    fig.update_layout(template="plotly_dark",height=420,title="Prevalencia de enfermedades crónicas (%)",yaxis_title="%")
    st.plotly_chart(fig,use_container_width=True)
elif page == "Comparativa OCDE":
    ind = ["Esperanza de vida","Mortalidad infantil","Gasto/PIB","Médicos/1.000","Satisfacción salud"]
    ranks = [4,8,22,18,5]
    fig = go.Figure(go.Bar(x=ind,y=ranks,marker_color="#58a6ff",text=ranks,textposition="outside"))
    fig.update_layout(template="plotly_dark",height=420,title="Posición de Israel en la OCDE (38 países, menor = mejor)",yaxis=dict(autorange="reversed",title="Ranking"))
    st.plotly_chart(fig,use_container_width=True)
elif page == "Factores de Riesgo":
    fig = go.Figure(go.Bar(x=["Sedentarismo","Tabaquismo","Obesidad","Alcohol","Dieta poco saludable","Estrés crónico"],y=[35,20,26,8,40,45],marker_color="#ffa657"))
    fig.update_layout(template="plotly_dark",height=420,title="Prevalencia de factores de riesgo (%)",yaxis_title="%")
    st.plotly_chart(fig,use_container_width=True)
elif page == "Gasto Sanitario":
    fig = make_subplots(specs=[[{"secondary_y":True}]])
    fig.add_trace(go.Scatter(x=years,y=[7.8,7.9,8.0,8.1,8.2,8.3],name="% PIB",line=dict(color="#3fb950",width=3)),secondary_y=False)
    fig.add_trace(go.Scatter(x=years,y=[2800,2950,3100,3250,3400,3550],name="USD per cápita",line=dict(color="#ffa657",width=3)),secondary_y=True)
    fig.update_layout(template="plotly_dark",height=420,title="Evolución del gasto sanitario")
    st.plotly_chart(fig,use_container_width=True)
elif page == "Indicadores Clave":
    df = pd.DataFrame({
        "Indicador":["Esperanza de vida (años)","Mortalidad infantil (por 1.000 NV)","Gasto sanitario (% PIB)","Médicos (por 1.000 hab.)","Camas hospitalarias (por 1.000)","Prevalencia obesidad (%)","Prevalencia tabaquismo (%)","Cobertura vacunación (%)","Satisfacción sistema salud (%)","Mortalidad cardiovascular (por 100.000)"],
        "2020":[82.1,3.0,7.8,3.0,2.2,24.5,22.0,94.0,72.0,98.0],
        "2022":[82.5,2.8,8.0,3.1,2.2,25.5,21.0,94.5,74.0,94.0],
        "2024":[83.1,2.6,8.2,3.1,2.2,26.0,20.0,95.0,75.0,90.0]
    })
    st.dataframe(df,use_container_width=True)
elif page == "Tendencias":
    fig = make_subplots(specs=[[{"secondary_y":True}]])
    fig.add_trace(go.Scatter(x=years,y=[82.1,81.8,82.5,82.8,83.1,83.3],name="Esperanza de vida",line=dict(color="#58a6ff")),secondary_y=False)
    fig.add_trace(go.Scatter(x=years,y=[3.0,3.0,2.9,2.8,2.6,2.5],name="Mortalidad infantil",line=dict(color="#ff7b72")),secondary_y=True)
    fig.update_layout(template="plotly_dark",height=420,title="Tendencias clave de salud 2020-2025")
    st.plotly_chart(fig,use_container_width=True)
elif page == "Población":
    fig = go.Figure(go.Scatter(x=years,y=[9.2,9.4,9.6,9.8,10.0,10.2],name="Población (millones)",line=dict(color="#58a6ff",width=3)))
    fig.update_layout(template="plotly_dark",height=400,title="Evolución de la población de Israel",yaxis_title="Millones")
    st.plotly_chart(fig,use_container_width=True)
    fig2 = go.Figure(go.Pie(labels=["0-14","15-29","30-44","45-59","60-74","75+"],values=[27.5,20.1,18.8,15.2,11.9,6.5],hole=0.4))
    fig2.update_layout(template="plotly_dark",height=400,title="Estructura de edad (2024)")
    st.plotly_chart(fig2,use_container_width=True)

st.divider()
st.markdown("**Citación:** de la Serna, J.M. (2026). *Base de Datos del Impacto en la Salud de Israel (2020-2025)*. Harvard Dataverse. https://doi.org/10.7910/DVN/PL3G1E")
