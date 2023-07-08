import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()


def load_dataset():
    """Load the sample dataset."""
    return load_iris()


def split_train_test(dataset):
    """
    Split the data set to train and test.
    In this example, we'll ignore the test set.
    """
    X_train, _, y_train, _ = train_test_split(
        dataset["data"], dataset["target"], test_size=0.9, random_state=0
    )
    return X_train, y_train


def train_model():
    """Train a new model based on the dataset dump to joblib file."""
    iris_dataset = load_dataset()
    X_train, y_train = split_train_test(iris_dataset)
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    joblib.dump(knn, "model.joblib")


if __name__ == "__main__":
    train_model()
