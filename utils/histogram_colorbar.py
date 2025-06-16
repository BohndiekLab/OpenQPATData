import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.patheffects as path_effects


def add_histogram_colorbar(ax, data, width=None, height=None, cmap=None, label=None,
                           vmin=None, vmax=None, min_label=None, max_label=None, fontsize=8, color=None, stroke=None):

    ydim, xdim = np.shape(data)

    if width is None:
        width = xdim / 3
    if height is None:
        height = ydim / 10
    if cmap is None:
        try:
            cmap = ax.images[0].get_cmap()
        except:
            cmap = "viridis"
    if label is None:
        label = ""
    if vmin is None:
        vmin = np.percentile(data, 2)
    if vmax is None:
        vmax = np.percentile(data, 98)
    if min_label is None:
        min_label = "2$^{nd}$"
    if max_label is None:
        max_label = "98$^{th}$"
    if color is None:
        color = "white"
    if stroke is None:
        stroke = True

    bar_height = int(1 / 15 * ydim)
    bar_offset = int(1 / 50 * ydim)

    baseline = ydim - bar_height - bar_offset
    leftshift = 15
    outline_color = "black"

    hist, _ = np.histogram(np.reshape(data, (-1, )), bins=50, range=(vmin, vmax))
    bins = np.linspace(0, 100, 51)
    ax.plot([xdim - width - leftshift, xdim - leftshift],
            [baseline, baseline], c=outline_color, linewidth=1)
    ax.stairs(baseline - (hist / np.max(hist) * height),
              (xdim - leftshift - width + bins / 100 * width),
              baseline=baseline, fill=True, color="lightgray")
    ax.stairs(baseline - (hist / np.max(hist) * height),
              (xdim - leftshift - width + bins / 100 * width),
              baseline=baseline, fill=False, color=outline_color, linewidth=1)
    x_points = np.asarray(xdim - leftshift - width + bins / 100 * width)

    for i in np.arange(0, bar_height, 2):
        ax.scatter(x_points, np.ones_like(x_points) * baseline + 2 + i,
                   c=((x_points - np.min(x_points)) / (np.max(x_points) - np.min(x_points))),
                   s=2, marker="s", cmap=cmap)

    ax.add_artist(Rectangle((xdim - leftshift - width - 2, baseline), width + 4,
                            bar_height + 2, fill=False, edgecolor="black"))

    labels_ypos = baseline + 0.75 * bar_height

    texts = []
    texts.append(ax.text(xdim - leftshift - width, labels_ypos, min_label, color=color, fontsize=fontsize, ha="left"))
    texts.append(ax.text(xdim - leftshift - width / 2, labels_ypos, label, color=color, fontsize=fontsize, ha="center"))
    texts.append(ax.text(xdim - leftshift, labels_ypos, max_label, color=color, fontsize=fontsize, ha="right"))

    if stroke:
        for text in texts:
            text.set_path_effects([
                path_effects.Stroke(linewidth=2, foreground='black'),
                path_effects.Normal()
            ])