"""
TQNN Python SDK Example

Text Inference

This example demonstrates how unstructured text can be submitted to the
TQNN Fault-Tolerant Inference Platform for inference.
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


documents = [
    "Production line temperature remained stable throughout the shift.",
    "Sensor 12 experienced intermittent communication failures.",
    "Preventative maintenance was completed ahead of schedule.",
    "Hydraulic pressure dropped below the configured safety threshold.",
]


response = client.run_any(
    data=documents,
    mode="TEXT",
    task="document_classification",
    label="text_demo",
    metadata={
        "language": "en",
        "class_labels": [
            "normal_operation",
            "maintenance",
            "fault_event",
        ],
    },
)


print("\n=== Prediction ===")
pprint(response["result"])

print("\n=== TQNN Report ===")
pprint(response["tqnn_report"])

print("\n=== Diagnostics ===")
pprint(response["diagnostics"])