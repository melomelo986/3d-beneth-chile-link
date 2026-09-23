import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "earthquakes.xy",
    sep=" ",
    header=None,
    names=["longitude", "latitude", "depth", "magnitude"]
)

fig = plt.figure(figsize=(10, 7))

ax = fig.add_subplot(111, projection="3d")

ax.scatter(
    df["longitude"],
    df["latitude"],
    df["depth"],
    s=3
)

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_zlabel("Depth (km)")

ax.set_xlim(-76, -65)
ax.set_ylim(-56, -18)
ax.set_zlim(300, 0)

ax.set_title("3-D Distribution of Earthquakes beneath Chile (trial)")

plt.show()
