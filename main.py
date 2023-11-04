import pandas


a = (
    csv.total.str.replace("Rs.", "")
    .str.replace(",", "")
    .str.replace("total", "")
    .apply(lambda x: float(x) if x != "" else float("nan"))
    .astype(float)
    .sum()
)
# 38099.85 + 78082.59 + 3765.96 + 4572.0 + 2269.0
