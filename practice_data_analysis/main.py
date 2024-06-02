import pandas as pd
import numpy as np
import requests


file_path: str = ("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud"
                  "/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv")

def download(url: str, filename: str):
 res = requests.get(url=url)
 if res.status_code == 200:
  with open(filename, "wb") as file:
   file.write(res.content)

# this is to download(file_path, "laptops.csv")
def read_file() -> pd.DataFrame | None:
 try:
  df = pd.read_csv("laptops.csv", header=None)
 except FileNotFoundError:
  print("It can not be found the file. Enter a filename valid please...")
 else:
  return df

df_laptops: pd.DataFrame | None = read_file()
if df_laptops is not None:
 headers = ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", 
            "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]
 df_laptops.columns = headers
 df_laptops.replace('?', np.nan, inplace=True)
 df_laptops.to_csv("laptops_new.csv")
 # print statistical description -> print(df_laptops.describe())
 # print datatype of columns -> print(df_laptops.dtypes)
