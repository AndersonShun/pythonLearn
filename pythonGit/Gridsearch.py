from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer

clf = estimator
clf.fit(x,y)
z = clf.predict(x)

def pe_score(y, y_pred):
    pe = prob_error(y_pred, y)
    return pe

pe_error = make_scorer(pe_score)
grid = GridSearchCV(SVC(), param_grid={'kernel':('linear', 'rbf'), 'C':[1, 10, 100,1000,10000]}, scoring= pe_error)