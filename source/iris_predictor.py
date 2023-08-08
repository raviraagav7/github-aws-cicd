import pickle
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = load_iris()
# Train a Logistic Regression model
model = LogisticRegression()

# Save the trained model
with open('iris_model.pkl', 'wb') as f:
    pickle.dump(model, f)

def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    """
    Make a prediction using the trained Logistic Regression model.
    """
    with open('data/iris_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)

    return data.target_names[prediction][0]

if __name__ == '__main__':
    print(predict_iris(5.1, 3.5, 1.4, 0.2))