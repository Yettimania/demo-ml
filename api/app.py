import joblib
from flask import Flask, request
from train import train_model
from predict import model_predict


app = Flask(__name__)

# Return meaninful lables instead of index
labels = ["setosa", "versicolor", "virginica"]


# Ability to retrain the model and store it locally in the container that is running.
@app.route("/train", methods=["POST"])
def train():
    train_model()
    return "Model successfully trained.", 200


# Predict method based on input payload from.
# Returns model prediction
@app.route("/predict", methods=["GET"])
def predict():
    # Load trained KNN model for iris dataset.
    model = joblib.load("model.joblib")
    input = [float(d) for d in request.form.get("data").split(",")]
    index = model_predict(model, [input])[0]
    label = labels[index]
    return label, 200


if __name__ == "__main__":
    app.run(debug=True)
