#%%

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

pio.templates.default = "seaborn"

lang_df = pd.read_csv("./langs.csv")

fig = go.Figure()
fig.update_geos(projection_type="natural earth")
fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
fig.update_geos(
    showcoastlines=True,
    coastlinecolor="#aaaaaa",
)

fig.update_layout(
    font_color="#555555",
    title_font_color="#444444",
    title_text="Language models on the map",
    title_x=0.5,
    title_font_size=20,
    legend_x=0.92,
)

colors = px.colors.qualitative.Light24

groups = {
    "mT5": {"col": "mt5", "color": "blue"},
    "mGPT": {"col": "mgpt", "color": "red"},
    "BLOOM": {"col": "bloom", "color": "green"},
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
            marker_symbol="diamond",
            visible=True,
        )
    )

fig.update_layout(
    autosize=True,
)
fig.update_layout(showlegend=True)


fig.write_html("index.html", include_plotlyjs="cdn")

fig.show()

# %%
