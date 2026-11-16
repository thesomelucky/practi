# Email spam: KNN and SVM
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Read and separate
df = pd.read_csv("emails.csv")
X = df.drop(["Email No.", "Prediction"], axis=1)
y = df["Prediction"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Select features BEFORE scaling
selector = SelectKBest(chi2, k=300)
X_train = selector.fit_transform(X_train, y_train)
X_test = selector.transform(X_test)

# Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train and compare
models = {"KNN": KNeighborsClassifier(n_neighbors=5),
           "SVM": SVC(kernel="rbf", C=10)}
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("\nModel:", name)
    print("Accuracy:", accuracy_score(y_test, pred))
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred, zero_division=0))
