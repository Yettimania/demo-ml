import joblib


def model_predict(model, data):
    """Predict iris flower based on input array."""
    return model.predict(data)


if __name__ == "__main__":
    data = [[5.1, 3.5, 1.4, 0.2]]
    model = joblib.load("model.joblib")
    print(model_predict(model, data))
