

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer
from arguments import args
from sklearn.pipeline import make_pipeline


one = OneHotEncoder(handle_unknown='ignore')
scaler = StandardScaler()


class PipelineBuilder(object):
    def __init__(self, num_features: list = args.numeric_features,
                 categorical_features: list = args.categorical_features
                 ):
        self.num_features = num_features
        self.categorical_features = categorical_features
   
   
    def build_data_preprocess_pipeline(self):
        self.preprocess_pipeline =  make_column_transformer((scaler, self.num_features),
                                                        (one, self.categorical_features)
                                                      )
        
        return self.preprocess_pipeline
        


