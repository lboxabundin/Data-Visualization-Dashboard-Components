from dashboard_components.data import sample_timeseries
from dashboard_components.components import chart_card, summary_kpis
import pandas as pd

def test_sample_timeseries():
    df = sample_timeseries(10)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10

def test_chart_card():
    df = sample_timeseries(20)
    card = chart_card('t', df, x='date', y='value', kind='line')
    assert card['type'] == 'chart'
    assert hasattr(card['figure'], 'data')

def test_summary_kpis():
    df = sample_timeseries(5)
    kpis = summary_kpis(df, numeric_cols=['value'])
    assert isinstance(kpis, list)
    assert len(kpis) >= 1
