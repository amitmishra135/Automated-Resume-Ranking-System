from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import numpy as np

def train_model(X, y):
    # Convert to numpy arrays if they're not already
    X = np.array(X)
    y = np.array(y)

    # Print shapes and unique values for debugging
    print(f"X shape: {X.shape}")
    print(f"y shape: {y.shape}")
    print(f"Unique values in y: {np.unique(y)}")

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.4f}")

    # Print detailed classification report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Save the model
    joblib.dump(model, 'resume_ranking_model.joblib')

    return model

def prepare_training_data():
    # This is a simplified example. In reality, you'd need a large dataset of resumes and their rankings.
    X = [[0.5], [0.6], [0.7], [0.8], [0.9]]  # Example similarity scores
    y = [0, 0, 1, 1, 1]  # Example rankings (0 for not suitable, 1 for suitable)
    return X, y

if __name__ == "__main__":
    X, y = prepare_training_data()
    train_model(X, y)