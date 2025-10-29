import streamlit as st
from dashboard_components.components import chart_card, kpi_card, data_table, summary_kpis
from dashboard_components.data import sample_timeseries, sample_categorical

st.set_page_config(layout='wide', page_title='Dashboard Components Demo')

st.title('Dashboard Components — Streamlit Demo')

df = sample_timeseries(120)
kpis = summary_kpis(df, numeric_cols=['value'])

cols = st.columns(len(kpis))
for c, k in zip(cols, kpis):
    c.metric(k['title'], f"{k['value']:.2f}", k.get('subtitle'))

st.markdown('---')

left, right = st.columns([3,1])
chart = chart_card('Value over time', df, x='date', y='value', kind='line')
with left:
    st.plotly_chart(chart['figure'], use_container_width=True)
with right:
    st.write('Sample categorical data')
    st.dataframe(data_table(sample_categorical(20)['data'] if False else sample_categorical(20).head(10)))
