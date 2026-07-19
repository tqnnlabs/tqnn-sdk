"""
TQNN Python SDK Example

Image Feature Inference

This example demonstrates submitting pre-extracted image features to the
TQNN Fault-Tolerant Inference Platform.

TQNN receives numeric feature data rather than an image file directly.
The values below are illustrative only.
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


# Each row represents one image region or patch.
#
# Example feature order:
# [
#     mean_intensity,
#     intensity_std,
#     edge_density,
#     contrast,
#     entropy,
#     red_mean,
#     green_mean,
#     blue_mean,
# ]
image_features = [
    [0.62, 0.18, 0.31, 0.44, 0.71, 0.58, 0.63, 0.66],
    [0.59, 0.21, 0.38, 0.49, 0.76, 0.55, 0.60, 0.64],
    [0.28, 0.34, 0.67, 0.73, 0.82, 0.31, 0.27, 0.25],
    [0.64, 0.17, 0.29, 0.41, 0.69, 0.61, 0.65, 0.68],
]


response = client.run_any(
    data=image_features,
    mode="IMAGE",
    task="visual_anomaly_classification",
    label="image_feature_demo",
    metadata={
        "input_type": "pre_extracted_features",
        "image_width": 640,
        "image_height": 480,
        "patch_count": len(image_features),
        "feature_names": [
            "mean_intensity",
            "intensity_std",
            "edge_density",
            "contrast",
            "entropy",
            "red_mean",
            "green_mean",
            "blue_mean",
        ],
        "class_labels": [
            "normal",
            "possible_anomaly",
            "anomaly",
        ],
    },
)


print("\n=== Prediction ===")
pprint(response["result"])

print("\n=== TQNN Report ===")
pprint(response["tqnn_report"])

print("\n=== Diagnostics ===")
pprint(response["diagnostics"])