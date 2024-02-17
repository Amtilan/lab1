import json
import pandas as pd

file_path = 'json1\\data.json'

with open(file_path) as json_file:
    data = json.load(json_file)

dns = []
descriptions = []
speeds = []
mtus = []

print("Interface status")
print("=" * 80)
print("DN", " " * 38, "Description", " " * 3, "Speed", " " * 8, "MTU")
print("-" * 41, "-" * 13, " ", "-" * 6, " " * 6, "-" * 6)

for imdata in data["imdata"]:
    for i in imdata:    
        for j in imdata[i]:
            print(imdata[i][j]["dn"],"\t", "\t", imdata[i][j]["speed"], "\t", imdata[i][j]["mtu"])
            dns.append(imdata[i][j]["dn"])
            descriptions.append(imdata[i][j].get("descr", ""))
            speeds.append(imdata[i][j]["speed"])
            mtus.append(imdata[i][j]["mtu"])

df = pd.DataFrame({
    "DN": dns,
    "Description": descriptions,
    "Speed": speeds,
    "MTU": mtus,
})

excel_file_path = 'JSON.xlsx'

df.to_excel(excel_file_path, index=False)

print("JSON был загружен в Excel File.")
