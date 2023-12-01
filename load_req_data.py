import pandas as pd
import yaml
import os
import io

params=yaml.safe_load(open("params.yaml"))["filter_criteria"]
df = pd.read_csv("raw_data/number.csv")
df = df[df["num"] > params["num"]]
os.makedirs(os.path.join("output","req_data"),exist_ok=True)
df.to_csv("output/req_data/output.csv")
print("Data loaded successfully.")