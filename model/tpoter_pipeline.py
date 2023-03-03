

from .preprocess_pipeline import PipelineBuilder
from tpot import TPOTRegressor
from sklearn.pipeline import make_pipeline
import pandas as pd
from joblib import dump
from model.utils import get_path



preprocess_pipeline = PipelineBuilder()

built_preppreprocess_pipeline = preprocess_pipeline.build_data_preprocess_pipeline()



class TpotModeler(object):
    def __init__(self, training_features: pd.DataFrame,
                 training_target_variable: pd.DataFrame,
                 testing_features: pd.DataFrame,
                 testing_target_variable: pd.DataFrame,
                 pipeline: PipelineBuilder = PipelineBuilder
                 ):
        self.training_features = training_features
        self.training_target_variable = training_target_variable
        self.testing_features = testing_features
        self.testing_target_variable = testing_target_variable
        self.pipeline = pipeline
              
    def fit_models(self, max_time_mins=1, verbosity=2, config_dict="TPOT sparse",
                   random_state=0,
                    **kwargs):
        optimizer = TPOTRegressor(max_time_mins=max_time_mins, verbosity=verbosity,
                                  random_state = random_state, config_dict=config_dict,
                                  **kwargs)
        self.optimizer_pipeline = make_pipeline(built_preppreprocess_pipeline,
                                           optimizer
                                           )
        
        self.optimizer_pipeline.fit(self.training_features, self.training_target_variable)
        return self.optimizer_pipeline
        
        
    def evaluate_testset(self):
        test_score = self.optimizer_pipeline.score(self.testing_features, self.testing_target_variable)
        return test_score
    
    
    def predict_booked_days(self, device_class, city, country, 
                            instant_booking, user_verified,
                            num_sessions):
        in_data = {'num_sessions': num_sessions, 'city': city, 'country': country,
                    'device_class': device_class, 'instant_booking': instant_booking,
                    'user_verified': user_verified
                    }
        
        prediction_input_data = pd.DataFrame(data=in_data, index=[0])
        y_pred = self.optimizer_pipeline.predict(prediction_input_data)
        return y_pred
    
    def save_best_model(self, model_store_folder: str = 'model_store', model_name: str = 'best_model.model'):
        # Pickel is unable to save TPOT model object which is the object type
        # of the estimator in the pipeline. As a work around, we loop to 
        # get the estimator object from the pipeline and access the fitted pipeline
        # from it. The fiited pipeline can be save by Pickel.
        # Then, we recreate the pipeline with the preprocessing and the fitted model
        # and save the result
        fitted_model = self.optimizer_pipeline[1].fitted_pipeline_
        preprocess_obj = self.optimizer_pipeline[0]
        packed_pipeline = make_pipeline(preprocess_obj, fitted_model)
        model_storepath = get_path(folder_name=model_store_folder, file_name=model_name)
        
        dump(value=packed_pipeline, filename=model_storepath)
        print('Successfully saved Best model')
        
        
        
        

     