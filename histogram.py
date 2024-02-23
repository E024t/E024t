import numpy as np
import json

x = np.linspace(0,255,256)
y = np.round(255/(1+(60/(x+1))**4))
strX=np.ndarray.tolist(x)
strY=np.ndarray.tolist(y)
Dic_hist = {
    "histX":strX,
    "histY":strY
}
# print(Dic_hist["histY"])
with open('Hist.json', 'w') as file:
    # file.write(jsonify(data))
    file.write(json.dumps(Dic_hist, separators=(',', ':')))