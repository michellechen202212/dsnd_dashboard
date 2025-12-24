import pickle
from pathlib import Path

# Set the absolute project root
project_root = Path(__file__).resolve().parent.parent

# Point to model.pkl in assets
model_path = project_root / "assets" / "model.pkl"

def load_model():
    with model_path.open('rb') as file:
        model = pickle.load(file)
    return model
