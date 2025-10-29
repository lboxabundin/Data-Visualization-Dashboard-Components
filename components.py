"""Dashboard component factories: return lightweight objects for UI layers to render."""
from typing import Optional, Dict, Any, List
import pandas as pd
import plotly.express as px

def kpi_card(title: str, value: Any, delta: Optional[float] = None, subtitle: Optional[str] = None) -> Dict[str, Any]:
    return {"type": "kpi", "title": title, "value": value, "delta": delta, "subtitle": subtitle}

def chart_card(title: str, df: pd.DataFrame, x: str, y: str, kind: str = 'line', **px_kwargs):
    if kind == 'line':
        fig = px.line(df, x=x, y=y, title=title, **px_kwargs)
    elif kind == 'bar':
        fig = px.bar(df, x=x, y=y, title=title, **px_kwargs)
    elif kind == 'scatter':
        fig = px.scatter(df, x=x, y=y, title=title, **px_kwargs)
    elif kind == 'area':
        fig = px.area(df, x=x, y=y, title=title, **px_kwargs)
    else:
        raise ValueError(f"Unknown kind: {kind}")
    return {"type": "chart", "title": title, "figure": fig}

def data_table(df: pd.DataFrame, max_rows: int = 100):
    return {"type": "table", "data": df.head(max_rows)}

def summary_kpis(df: pd.DataFrame, numeric_cols: Optional[List[str]] = None):
    if numeric_cols is None:
        numeric_cols = df.select_dtypes('number').columns.tolist()
    kpis = []
    for c in numeric_cols:
        total = float(df[c].sum())
        mean = float(df[c].mean())
        kpis.append(kpi_card(f"{c}", total, delta=None, subtitle=f"mean={mean:.2f}"))
    return kpis
