"""

* DataFrameMapper: pandas data frame -> sklearn transformations
* cross_val_score: 'sklearn.cross_validation.cross_val_score' for pandas DataFrames

"""
from sklearn_pandas import DataFrameMapper, cross_val_score
import pandas as pd
import numpy as np
import sklearn.preprocessing, sklearn.decomposition, \
    sklearn.linear_model, sklearn.pipeline, sklearn.metrics
from sklearn.feature_extraction.text import CountVectorizer


# WIP
# https://github.com/scikit-learn-contrib/sklearn-pandas
def test_mapping_columns_to_transformations():
    data = pd.DataFrame({'pet':      ['cat', 'dog', 'dog', 'fish',
                                      'cat', 'dog', 'cat', 'fish'],
                         'children': [4., 6, 3, 3,
                                      2, 3, 5, 4],
                         'salary':   [90., 24, 44, 27,
                                      32, 59, 36, 27]})

    # Some transformers expect a 1-dimensional input (the label-oriented ones)
    # OneHotEncoder or Imputer expect 2-dimensional input ([n_samples, n_features]. )
    mapper = DataFrameMapper([
        (
            'pet',  # a column name. (1-d input)
            sklearn.preprocessing.LabelBinarizer()  # transformer
            # a dictionary -  optional transformation options
         ),
        (
            ['children'],  # can be a list. (2-d input)
            sklearn.preprocessing.StandardScaler()
        )
    ])
