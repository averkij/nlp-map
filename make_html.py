#%%

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

lang_df = pd.read_csv("./langs.csv")

fig = go.Figure()
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
            visible=True,
        )
    )

fig.update_layout(
    autosize=True,
)
fig.update_layout(showlegend=True)

fig.write_html("index.html", include_plotlyjs="cdn")

# %%
