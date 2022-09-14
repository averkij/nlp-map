#%%

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

pio.templates.default = "seaborn"

lang_df = pd.read_csv("./langs.csv")

BG_COLOR = "#659dbd"


def create_figure():
    fig = go.Figure()
    fig.update_geos(
        projection_type="natural earth",
        showcoastlines=True,
        coastlinecolor="#aaaaaa",
        lataxis_showgrid=True,
        lonaxis_showgrid=True,
        bgcolor=BG_COLOR,
        showocean=True,
        oceancolor="white",
    )
    return fig


def update_figure(fig, title):
    fig.update_layout(
        autosize=True,
        showlegend=True,
        font_color="#555555",
        legend_bgcolor="white",
        paper_bgcolor=BG_COLOR,
        title=dict(
            text=title,
            x=0.5,
            y=0.96,
            font=dict(family="Josefin Sans", size=32, color="white"),
        ),
        legend=dict(
            x=0.92,
            y=1,
            font=dict(family="Arial", size=12, color="black"),
            bgcolor="white",
            bordercolor="#555555",
            borderwidth=1,
        ),
    )


fig = create_figure()

groups = {
    "mT5": {"col": "mt5", "color": "blue", "marker": "arrow-down", "marker-size": 7},
    "mGPT": {"col": "mgpt", "color": "red", "marker": "arrow-up", "marker-size": 7},
    "BLOOM": {
        "col": "bloom",
        "color": "green",
        "marker": "arrow-left",
        "marker-size": 5,
    },
    "XGLM": {
        "col": "xglm",
        "color": "orange",
        "marker": "arrow-right",
        "marker-size": 7,
    },
}

colors = px.colors.qualitative.Plotly

for i, (name, val) in enumerate(groups.items()):
    fig.add_trace(
        go.Scattergeo(
            name=name,
            lon=lang_df[lang_df[val["col"]] == True]["longitude"],
            lat=lang_df[lang_df[val["col"]] == True]["latitude"],
            text=lang_df[lang_df[val["col"]] == True]["Name"],
            mode="markers",
            marker=dict(
                size=7,
                color=colors[i % 10],
                symbol=val["marker"],
            ),
            visible=True,
        )
    )

update_figure(fig, title="Language models on the map")

fig.write_html("index.html", include_plotlyjs="cdn")
fig.show()

# %%
