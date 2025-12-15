from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import joblib
from sklearn.ensemble import RandomForestClassifier

data =  load_iris()
X = data['data']
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=44)

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)


# Save the model
joblib.dump(model, "iris_model.pkl")