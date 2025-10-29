# Data Visualization — Dashboard Components

A curated collection of reusable **Data Visualization / Dashboard Components** designed for quick integration into Streamlit and Plotly Dash apps.  
Sponsor-friendly: compact, well-documented, and ideal for tutorials, demos, and production prototypes — perfect for GitHub Sponsors.

## Highlights

- UI-agnostic component factories (KPI cards, Chart cards, Data table helpers).
- Ready examples for **Streamlit** and **Dash** to get running in minutes.
- Small test suite + CI template for GitHub Actions.
- `FUNDING.yml` and Sponsor guidance included to help you accept support.

## Features

- `kpi_card`, `chart_card`, `data_table` component helpers returning lightweight objects (dicts / Plotly figures).
- Example dashboards showing layout patterns, responsive charts, and KPI rows.
- Sample data generator for reproducible demos.
- Tests and CI to help maintain quality.

## Quickstart

1. Create virtualenv and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run the Streamlit demo:
```bash
streamlit run examples/streamlit_app.py
# Opens at http://localhost:8501
```

3. Run the Dash demo:
```bash
python examples/dash_app.py
# Opens at http://127.0.0.1:8050
```

## Sponsorship

If this project saves you time, please consider sponsoring to fund:
- More components (maps, heatmaps, interactive tables)
- Framework integrations (React components, Vue wrappers)
- Accessibility and performance improvements

Add a Sponsor button and `FUNDING.yml` to your GitHub repo to collect support.

## Structure

- `src/dashboard_components` — component code and data helpers
- `examples` — runnable demos
- `docs` — usage and extension notes
- `tests` — pytest tests
- `.github` — CI and templates

## License

MIT
