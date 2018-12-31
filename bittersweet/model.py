from .properties import generate_properties
from .input import read_file
import pickle


class BitterSweetModel():
    def __init__(self, model_paths):
        """ Initializes all the models at once and consolidates prediction methods. """

        for key, path in model_paths.items():
            setattr(self, key, pickle.load(open(path, 'rb')))

    def predict_bitter_taste(self, data, predict_receptors=False):
        """ Predict whether a molecule is bitter/non-bitter, and if it is, predict
        the linked bitter receptors.
 
        Args:
            data - Pandas DataFrame with each row as molecule and ChemoPy properties as columns.

        Returns:
            Pandas DataFrame with categorical prediction and probability values.
        """

        try:        
            d = data[self.bitter_model_features]
        except:
            raise("Unsufficient number of properties passed.")

        bitter_prob = self.bitter_model.predict_proba(d)[:, 1]
        bitter_taste = self.bitter_model.predict(d)

        if predict_receptors:
            raise NotImplementedError
        else:
            return pd.DataFrame()

    def predict_sweet_taste(self, data, predict_relative_sweetness=False):
        """ Predict whether a molecule is sweet/non-sweet, and if it is, 
        predict relative sweetness. 
        
        Args:
            data - Pandas DataFrame with each row as molecule and ChemoPy properties as columns.

        Returns:
            Pandas DataFrame with categorical prediction and probability values.
        """

        try:        
            d = data[self.sweet_model_features]
        except:
            raise("Unsufficient number of properties passed.")

        bitter_prob = self.bitter_model.predict_proba(d)[:, 1]
        bitter_taste = self.bitter_model.predict(d)

        if predict_relative_sweetness:
            raise NotImplementedError
        else:
            return pd.DataFrame()