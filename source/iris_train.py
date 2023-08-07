import pickle
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def train_iris():
    # Load Iris dataset
    data = load_iris()
    X, y = data.data, data.target
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    # Train a Logistic Regression model
    model = LogisticRegression()
    model.fit(X_scaled, y)

    # Save the trained model
    with open('data/iris_model.pkl', 'wb') as f:
        pickle.dump(model, f)


if __name__ == '__main__':
    train_iris()