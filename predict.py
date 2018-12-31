from bittersweet.model import Model

# Set model paths
MODEL_PATHS = {
    'bitter_model': 'models/bitter/random_forest_boruta.p',
    'bitter_model_features': 'models/bitter/boruta_features.p',
    'sweet_model': 'models/random_forest_boruta.p',
    'sweet_model_features': 'models/sweet/boruta_features.p',
    # 'relative_sweetness_model': 'models/relative-sweetness/ridge_regression.p',
    # 'relative_sweetness_model_features': 'models/relative-sweetness/features.p',
    # 'bitter_receptors_model': 'models/bitter-receptors/random_forest.p',
    # 'bitter_receptors_model_features': 'models/bitter-receptors/features.p',
    # 'bitter_receptors_features': 'models/bitter-receptors/receptor-features.tsv'
}

model = Model(model_paths=MODEL_PATHS)
