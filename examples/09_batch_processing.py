"""
TQNN Python SDK Example

Batch Processing

This example demonstrates processing multiple datasets
using the TQNN Fault-Tolerant Inference Platform.
"""

import os
from pprint import pprint

from tqnn import TQNNClient


API_KEY = os.getenv("TQNN_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "TQNN_API_KEY environment variable is not set."
    )


client = TQNNClient(api_key=API_KEY)


datasets = [
    {
        "label": "sample_001",
        "data": [
            [1.2, 0.4, 3.3, 0.1],
            [2.1, 1.1, 0.9, 0.5],
        ],
    },
    {
        "label": "sample_002",
        "data": [
            [0.7, 1.5, 2.8, 0.3],
            [1.8, 0.6, 1.9, 0.9],
        ],
    },
    {
        "label": "sample_003",
        "data": [
            [2.4, 1.2, 0.4, 1.1],
            [2.2, 0.9, 0.8, 0.7],
        ],
    },
]


print(f"\nProcessing {len(datasets)} datasets...\n")


for i, dataset in enumerate(datasets, start=1):

    print("=" * 60)
    print(f"Dataset {i}: {dataset['label']}")
    print("=" * 60)

    try:

        response = client.run_any(
            data=dataset["data"],
            mode="TABULAR",
            task="classification",
            label=dataset["label"],
            metadata={
                "class_labels": [
                    "Class A",
                    "Class B",
                    "Class C",
                ]
            },
        )

        print("\nPrediction")
        pprint(response["result"])

        print("\nConfidence")
        pprint(response["tqnn_report"]["confidence"])

    except Exception as exc:

        print(f"Failed: {exc}")

    print()

print("Batch processing complete.")