import math
from diagram import Diagram, PIVOT_H


def blueprint_svg(bp):
    d = Diagram()
    start = d.base(bp["base"])
    base_off = {"wall": (10, 90), "cup": (110, -40)}.get(bp["base"], (-120, 20))
    d.callout(start, "A", dx=base_off[0], dy=base_off[1])
    end = d.chain(start, bp["segs"])
    # main-chain tip: last payload position
    dx = end[0] - start[0]
    ref_y = 0
    if bp["base"] == "wall":
        d.dim_h(0, end[0], min(p[1] for p in d.pts) + 10, f"≈ {abs(end[0]):.0f} mm from wall")
    else:
        y = min(p[1] for p in d.pts) - 5
        if abs(dx) > 120:
            d.dim_h(start[0], end[0], y, f"≈ {abs(dx):.0f} mm reach")
        top = max(end[1], 0)
        xr = max(p[0] for p in d.pts) + 20
        d.dim_v(xr, 0, end[1], f"≈ {end[1]:.0f} mm")
    return d.render(bp["title"]), dx, end[1]
