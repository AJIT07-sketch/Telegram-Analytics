import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
app_dash = dash.Dash(__name__, server=app, routes_pathname_prefix='/dashboard/')
df = pd.DataFrame({"timestamp": pd.date_range(start="2025-01-01", periods=30, freq="D"), "message_count": [i * 2 for i in range(30)]})
fig = px.line(df, x="timestamp", y="message_count", title="Daily Messages")
app_dash.layout = html.Div([html.H1("Telegram Analytics Dashboard"), dcc.Graph(figure=fig)])