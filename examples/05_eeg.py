"""
TQNN Python SDK Example

EEG Inference

This example demonstrates submitting an EEG feature matrix to the
TQNN Fault-Tolerant Inference Platform.

The feature values below are illustrative only.
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


# Example EEG feature matrix
#
# Each row represents one observation.
#
# Example feature order:
# [
#     C3_mu,
#     C3_beta,
#     Cz_mu,
#     Cz_beta,
#     C4_mu,
#     C4_beta,
# ]
eeg_data = [
    [0.82, 0.31, 0.76, 0.28, 0.80, 0.30],
    [0.79, 0.34, 0.74, 0.27, 0.78, 0.32],
    [0.75, 0.29, 0.71, 0.25, 0.74, 0.28],
    [0.88, 0.36, 0.83, 0.33, 0.86, 0.35],
]


response = client.run_any(
    data=eeg_data,
    mode="EEG",
    task="motor_imagery_classification",
    label="eeg_demo",
    metadata={
        "sampling_rate": 250,
        "channels": [
            "C3",
            "Cz",
            "C4",
        ],
        "class_labels": [
            "left_hand",
            "right_hand",
            "feet",
            "tongue",
        ],
    },
)


print("\n=== Prediction ===")
pprint(response["result"])

print("\n=== TQNN Report ===")
pprint(response["tqnn_report"])

print("\n=== Diagnostics ===")
pprint(response["diagnostics"])