from catboost import CatBoostClassifier

def predict_res (li):
    model = CatBoostClassifier()  
    model.load_model('nasa__f')
    res=model.predict(li)
    if res == 0 :
        resultat='There is no storm'
    else:
        resultat='There is a storm , ATTENTION !'
    return resultat


'''
test_li=[0,2.114200e+09,3.600000e+21,1.204120e+12,2472.887,159.145,1.697619,6]
x=predict_res(test_li)
print(x)
'''