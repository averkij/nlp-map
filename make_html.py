#%%

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

pio.templates.default = "seaborn"

lang_df = pd.read_csv("./langs.csv")

fig = go.Figure()
fig.update_geos(
    projection_type="natural earth",
    showcoastlines=True,
    coastlinecolor="#aaaaaa",
    lataxis_showgrid=True,
    lonaxis_showgrid=True,
)

colors = px.colors.qualitative.Light24

groups = {
    "mT5": {"col": "mt5", "color": "blue", "marker": "arrow-down", "marker-size": 9},
    "mGPT": {"col": "mgpt", "color": "red", "marker": "arrow-up", "marker-size": 7},
    "BLOOM": {
        "col": "bloom",
        "color": "green",
        "marker": "arrow-left",
        "marker-size": 5,
    },
}

for name, val in groups.items():
    fig.add_trace(
        go.Scattergeo(
            name=name,
            lon=lang_df[lang_df[val["col"]] == True]["longitude"],
            lat=lang_df[lang_df[val["col"]] == True]["latitude"],
            text=lang_df[lang_df[val["col"]] == True]["Name"],
            mode="markers",
            marker_color=val["color"],
            # marker_symbol=val["marker"],
            marker_symbol="diamond",
            # marker_size=val["marker-size"],
            visible=True,
        )
    )

fig.update_layout(
    autosize=True,
    showlegend=True,
    font_color="#555555",
    title_font_color="#444444",
    title_text="Language models on the map",
    title_x=0.5,
    title_font_size=20,
    legend_x=0.92,
)

fig.write_html("index.html", include_plotlyjs="cdn")

fig.show()

# %%
