import random
from datetime import date, timedelta

from components.ui.heatmap import heatmap


def heatmap_github():
    data = []

    d = date(2025, 1, 1)
    while d <= date(2025, 12, 31):
        if random.random() > 0.3:  # noqa: S311  # nosec B311 - demo data, not security-sensitive
            data.append({"date": str(d), "value": random.randint(1, 20)})  # noqa: S311  # nosec B311 - demo data, not security-sensitive
        d += timedelta(days=1)

    return heatmap(
        data=data,
        start_date="2025-01-01",
        end_date="2025-11-30",
        color_mode="discrete",
        value_label="contributions",
        cell_size=14,
        root_class="scrollbar-none",
    )
