"""
TQNN SDK Quick Start

Before running:

export TQNN_API_KEY="YOUR_API_KEY"

or set the environment variable using your operating system.
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

response = client.run_any(
    data=[
        [1.2, 0.4, 3.3, 0.1],
        [2.1, 1.1, 0.9, 0.5],
        [0.7, 0.3, 1.2, 2.1],
    ],
    mode="TABULAR",
    task="fault_diagnosis",
    label="quickstart_demo",
    metadata={
        "class_labels": [
            "healthy",
            "fault",
        ]
    },
)

print("\n=== Prediction ===")
print(response["result"])

print("\n=== TQNN Report ===")
print(response["tqnn_report"])

print("\n=== Diagnostics ===")
print(response["diagnostics"])