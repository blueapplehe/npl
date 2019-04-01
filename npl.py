from aip import AipNlp
import re
import sys
sys.path.append("/data/keras/npl/") 
import baidunpl 
#print(res)
def getBaiduVec(word):
    APP_ID = 'd491715c5684423e87657ac69449a8eb'
    API_KEY = '311e980421a5457daace65a8b1fb2d27'
    SECRET_KEY = 'a3e141a43f744682a45c40f1cf45e797'
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    res=client.wordEmbedding(word)
    return res
word = "漂亮"
res=getBaiduVec(word);
print(len(res["vec"]))

import jieba

def getFenCi(text):
    text = re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", " ", text)
    APP_ID = 'd491715c5684423e87657ac69449a8eb'
    API_KEY = '311e980421a5457daace65a8b1fb2d27'
    SECRET_KEY = 'a3e141a43f744682a45c40f1cf45e797'
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    res=client.lexer(text)
    ret=[]
    for one in res["items"]:
        ret.append(one["item"])
    return ret

res=getFenCi("今天天气如何?")
for word in res:
    print(word)