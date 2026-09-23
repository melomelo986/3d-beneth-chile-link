import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "earthquakes.xy",
    sep=" ",
    header=None,
    names=["longitude", "latitude", "depth", "magnitude"]
)

fig = px.scatter_3d(
    df,
    x="longitude",
    y="latitude",
    z="depth",
    color="depth",
    hover_data=["magnitude"],
    title="3-D Distribution of Earthquakes beneath Chile"
)

fig.update_layout(
    scene=dict(
        zaxis=dict(
            autorange="reversed"
        )
    )
)

fig.write_html("chile_3d.html")
