"""
TQNN Python SDK Example

Financial Time-Series Inference

This example submits a structured financial feature window to the
TQNN Fault-Tolerant Inference Platform.

The values below are illustrative only and are not live market data
or financial advice.
"""

import os
from pprint import pprint

from tqnn import TQNNClient


API_KEY = os.getenv("TQNN_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "TQNN_API_KEY environment variable is not set. "
        "Set it before running this example."
    )


client = TQNNClient(api_key=API_KEY)


# Each row represents one time-ordered market snapshot.
#
# Feature order:
# [
#     open,
#     high,
#     low,
#     close,
#     volume,
#     rsi_14,
#     macd,
#     macd_signal,
#     trend_slope,
# ]
finance_data = [
    [150.20, 151.10, 149.80, 150.75, 3_120_000, 54.2, 0.84, 0.71, 0.031],
    [150.75, 152.00, 150.30, 151.65, 3_480_000, 57.6, 0.96, 0.76, 0.044],
    [151.65, 152.40, 150.90, 151.20, 3_050_000, 55.1, 0.91, 0.79, 0.026],
    [151.20, 153.10, 151.00, 152.85, 3_920_000, 61.8, 1.14, 0.86, 0.058],
]


response = client.run_any(
    data=finance_data,
    mode="FINANCE",
    task="trend_classification",
    label="finance_window_demo",
    metadata={
        "symbol": "DEMO",
        "interval": "15m",
        "currency": "USD",
        "feature_names": [
            "open",
            "high",
            "low",
            "close",
            "volume",
            "rsi_14",
            "macd",
            "macd_signal",
            "trend_slope",
        ],
        "class_labels": [
            "downward",
            "neutral",
            "upward",
        ],
    },
)


print("\n=== Prediction ===")
pprint(response["result"])

print("\n=== TQNN Report ===")
pprint(response["tqnn_report"])

print("\n=== Diagnostics ===")
pprint(response["diagnostics"])