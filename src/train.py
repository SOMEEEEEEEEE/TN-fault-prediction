import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from lightgbm import LGBMClassifier

from features import build_features


# Load dataset (not included in repo)
df = pd.read_csv("data/telecom_faults.csv")

# Build features
df = build_features(df)

# Target column: timeout flag
# expected values: 0 / 1
target = "timeout_flag"

# Feature columns
features = [
    "time_to_accept",
    "fault_to_discover",
    "fault_to_ticket",
    "repeat_ticket_count",
    "supervision_count",
    "reject_count",
    "affected_users",
    "alarm_level",
    "fault_level",
    "region",
    "maintenance_team"
]

# Keep existing columns only
features = [f for f in features if f in df.columns]

X = df[features]
y = df[target]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# LightGBM baseline
model = LGBMClassifier(
    n_estimators=200,
    max_depth=6
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

acc = accuracy_score(y_test, pred)

print("Validation Accuracy:", acc)