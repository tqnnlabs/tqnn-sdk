"""
TQNN SDK Example

Tabular Data Inference
"""

import os

from tqnn import TQNNClient


API_KEY = os.getenv("TQNN_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "TQNN_API_KEY environment variable is not set."
    )


client = TQNNClient(
    api_key=API_KEY,
)


# Example tabular dataset
#
# Each row represents one sample.
# Each column represents one feature.
dataset = [
    [1.20, 0.40, 3.30, 0.10],
    [2.10, 1.10, 0.90, 0.50],
    [0.70, 0.30, 1.20, 2.10],
    [1.50, 0.80, 2.40, 0.60],
]


response = client.run_any(
    data=dataset,
    mode="TABULAR",
    task="classification",
    label="tabular_demo",
    metadata={
        "class_labels": [
            "Class A",
            "Class B",
            "Class C",
        ]
    },
)


print("\n=== Prediction ===")
print(response["result"])

print("\n=== TQNN Report ===")
print(response["tqnn_report"])

print("\n=== Diagnostics ===")
print(response["diagnostics"])