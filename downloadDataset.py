import pandas as pd 
import urllib

data = pd.read_json("./numPlateDataset.json")

cnt = 0

for i in data["data"]:
    cnt += 1
    urllib.request.urlretrieve(i['content'],"./datasets/car"+str(cnt)+".jpeg")
