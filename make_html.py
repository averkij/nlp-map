#%%

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

lang_df = pd.read_csv("./langs_updated.csv")

fig = go.Figure()
colors = px.colors.qualitative.Light24

# add mt5
fig.add_trace(
    go.Scattergeo(
        name="mT5",
        lon=lang_df[lang_df["mt5"] == True]["longitude"],
        lat=lang_df[lang_df["mt5"] == True]["latitude"],
        text=lang_df[lang_df["mt5"] == True]["Name"],
        mode="markers",
        marker_color="blue",
        visible=True,
    )
)

# add mgpt
fig.add_trace(
    go.Scattergeo(
        name="mGPT",
        lon=lang_df[lang_df["mgpt"] == True]["longitude"],
        lat=lang_df[lang_df["mgpt"] == True]["latitude"],
        text=lang_df[lang_df["mgpt"] == True]["Name"],
        mode="markers",
        marker_color="red",
        visible=True,
    )
)

# add bloom
fig.add_trace(
    go.Scattergeo(
        name="BLOOM",
        lon=lang_df[lang_df["bloom"] == True]["longitude"],
        lat=lang_df[lang_df["bloom"] == True]["latitude"],
        text=lang_df[lang_df["bloom"] == True]["Name"],
        mode="markers",
        marker_color="green",
        visible=True,
    )
)

fig.update_layout(
    autosize=True,
)
fig.update_layout(showlegend=True)

fig.write_html("index.html", include_plotlyjs="cdn")

# %%
