# dependencies
import tabpy_client
from tabpy.tabpy_tools.client import Client
client = tabpy_client.Client('http://localhost:9004/')

def wine_predictor(_arg1, _arg2, _arg3, _arg4, _arg5, _arg6):
    import pandas as pd

    row = {'country': _arg1,
           'province': _arg2,
           'winery': _arg3,
           'price': _arg4,
           'vintage': _arg5,
           'variety': _arg6}

    test_features = pd.DataFrame(data=row, index=[0])
    predict_quality_prob = random_forest.predict_proba(test_features)
    return [probability[1] for probability in predict_quality_prob]

client.deploy('wine_predictor', wine_predictor, 'Predicts probability of good quality.', override=True)