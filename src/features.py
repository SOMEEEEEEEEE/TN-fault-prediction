import pandas as pd
import numpy as np


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build features for telecom fault ticket SLA prediction.

    Expected columns (string timestamps allowed):
    - create_time
    - fault_time
    - discover_time
    - accept_time
    - sla_limit
    - alarm_level
    - fault_level
    - region
    - maintenance_team
    - repeat_ticket_count
    """

    df = df.copy()

    # Convert timestamp columns (safe parsing)
    time_columns = [
        "create_time",
        "fault_time",
        "discover_time",
        "accept_time"
    ]

    for col in time_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Time-based features
    if "accept_time" in df.columns and "create_time" in df.columns:
        df["time_to_accept"] = (
            df["accept_time"] - df["create_time"]
        ).dt.total_seconds()

    if "discover_time" in df.columns and "fault_time" in df.columns:
        df["fault_to_discover"] = (
            df["discover_time"] - df["fault_time"]
        ).dt.total_seconds()

    if "create_time" in df.columns and "fault_time" in df.columns:
        df["fault_to_ticket"] = (
            df["create_time"] - df["fault_time"]
        ).dt.total_seconds()

    # Fill missing time features
    time_features = [
        "time_to_accept",
        "fault_to_discover",
        "fault_to_ticket"
    ]

    for col in time_features:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())

    # Numeric safety
    numeric_cols = [
        "repeat_ticket_count",
        "supervision_count",
        "reject_count",
        "affected_users"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].fillna(0)

    # Encode categorical features
    categorical_cols = [
        "alarm_level",
        "fault_level",
        "region",
        "maintenance_team",
        "vendor"
    ]

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype("category").cat.codes

    return df