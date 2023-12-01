import pandas as pd
import os
import yaml

#params = yaml.safe_load(open("params.yaml"))["analysis"]
df=pd.read_csv(os.path.join("output","req_data","output.csv"))
#df=df.head(params["top_rows"])
os.makedirs(os.path.join("output","analysis"),exist_ok=True)
analysis_path= os.path.join("output","analysis","output.txt")
with open(analysis_path, "w") as f:
    f.write(str(df.describe()))

print("Analysis added successfully.")    