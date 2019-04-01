from aip import AipNlp
import re
class BaiduNpl:
    def __init__(self):
        APP_ID = 'd491715c5684423e87657ac69449a8eb'
        API_KEY = '311e980421a5457daace65a8b1fb2d27'
        SECRET_KEY = 'a3e141a43f744682a45c40f1cf45e797'
        self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

    def getFenCi(self,text):
        text = re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", " ", text)
        res=self.client.lexer(text)
        ret=[]
        for one in res["items"]:
            ret.append(one["item"])
        return ret

    def getBaiduVec(self,word):
        res=self.client.wordEmbedding(word)
        return res

    def getVecFromJuzi(self,text):
        words=self.getFenCi(text)
        vecs=[]
        for word in words:
            res=self.getBaiduVec(word)
            if "vec" in res.keys():
                vec=res["vec"]
                vecs.append(vec)
        return vecs