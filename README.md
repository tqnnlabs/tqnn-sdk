# TQNN Python SDK

Official Python SDK for the **TQNN Fault-Tolerant Inference Platform**.

The TQNN Python SDK provides a clean, lightweight interface for interacting with the managed TQNN cloud runtime.

Build Python applications that perform confidence-aware inference on noisy, incomplete, or uncertain data through a simple and consistent API.

---

# Features

- Official Python client for the TQNN Platform
- Confidence-aware inference
- Input-integrity reporting
- Controlled decision states
- Runtime diagnostics
- Domain-agnostic inference
- Managed cloud execution
- Simple Python interface

---

# Installation

```bash
pip install tqnn
```

---

# Requirements

- Python 3.9+
- Active TQNN API key

---

# Quick Start

```python
from tqnn import TQNNClient

client = TQNNClient(
    api_key="TQNN_xxxxxxxxxxxxxxxxx"
)

response = client.run_any(
    data=[1.2, 1.4, 1.6, 2.1],
    mode="TABULAR",
    task="fault_diagnosis"
)

print(response)
```

---

# Creating a Client

```python
from tqnn import TQNNClient

client = TQNNClient(
    api_key="YOUR_API_KEY"
)
```

The SDK automatically communicates with the managed TQNN cloud runtime.

No custom endpoint configuration is required for standard deployments.

---

# Running Inference

```python
response = client.run_any(
    data=data,
    mode="TABULAR",
    task="fault_diagnosis",
    label="pump_sensor_window",
    metadata={
        "class_labels": [
            "healthy",
            "fault"
        ]
    }
)
```

---

# Parameters

| Parameter | Description |
|------------|-------------|
| data | Structured numerical input |
| mode | EEG, FINANCE, TABULAR, IMAGE or ANY |
| task | Optional inference context |
| label | Optional request label |
| sfreq | Optional sampling frequency |
| metadata | Additional application metadata |

---

# Example Response

```json
{
    "platform": "TQNN",
    "engine": "TQNN Fault-Tolerant Inference Engine",
    "engine_version": "2.0.0",

    "mode": "TABULAR",

    "result": {
        "prediction_index": 1,
        "prediction_label": "fault",
        "confidence": 0.94,
        "decision": "ACCEPT"
    },

    "tqnn_report": {

        "primary_capability": "fault-tolerant inference",

        "confidence": {
            "score": 0.94,
            "label": "high",
            "margin": 0.28,
            "entropy": 0.17
        },

        "data_integrity": {
            "score": 0.98,
            "label": "valid",
            "feature_count": 4,
            "finite_fraction": 1.0,
            "missing_fraction": 0.0,
            "constant_input": false
        },

        "decision": {
            "status": "ACCEPT",
            "threshold_met": true
        },

        "warnings": []
    },

    "diagnostics": {
        "probabilities": [0.06, 0.94],
        "confidence_margin": 0.28,
        "normalized_entropy": 0.17,
        "acceptance_threshold": 0.61,
        "threshold_met": true,
        "qualia": {},
        "intent": [],
        "meta": {}
    }
}
```

---

# Convenience Methods

The SDK provides helper methods for quickly accessing common sections of a response.

## Prediction

```python
result = client.result(response)
```

## TQNN Report

```python
report = client.report(response)
```

## Diagnostics

```python
diagnostics = client.diagnostics(response)
```

---

# Controlled Decisions

Every inference returns a standardized decision state.

Possible values include:

- ACCEPT
- REVIEW
- REJECT

Applications should use these decision states to determine whether an inference should be accepted automatically or reviewed before action.

---

# Supported Modes

| Mode | Description |
|------|-------------|
| ANY | Domain-agnostic inference |
| TABULAR | Structured datasets |
| EEG | Biosignal inference |
| FINANCE | Financial time-series |
| IMAGE | Structured image features |

---

# Example Applications

The SDK can be integrated into applications including:

- Fault Detection
- Fault Diagnosis
- Sensor Monitoring
- Industrial Process Monitoring
- Predictive Maintenance
- Biosignal Analysis
- Financial Time-Series
- Scientific Computing
- General Structured Data

---

# Error Handling

```python
try:

    response = client.run_any(
        data=data,
        mode="TABULAR"
    )

except Exception as e:
    print(e)
```

---

# Best Practices

Store API keys using environment variables.

```bash
export TQNN_API_KEY="TQNN_xxxxxxxxxxxxxxxxx"
```

```python
import os

from tqnn import TQNNClient

client = TQNNClient(
    api_key=os.environ["TQNN_API_KEY"]
)
```

Never commit API keys to public repositories.

---

# Version Compatibility

This SDK is designed for the **TQNN Fault-Tolerant Inference API v2**.

Future SDK releases will remain aligned with the public API contract.

---

# Philosophy

The SDK is intentionally lightweight.

Rather than hiding inference details, it exposes the complete standardized response returned by the platform.

Applications receive:

- Prediction results
- Confidence scores
- Decision status
- Input-integrity reporting
- Runtime diagnostics
- Structured metadata

The SDK acts as a thin Python layer over the managed TQNN cloud runtime.

---

# License

The TQNN Python SDK is released under the MIT License.

The following components are open source:

- Python SDK
- Client utilities
- Integration helpers
- Example code

The managed inference runtime, execution substrate, orchestration services, and production infrastructure remain proprietary intellectual property of TQNN Labs.

---

# About TQNN Labs

TQNN Labs develops cloud-hosted fault-tolerant inference infrastructure for applications operating on noisy, incomplete, or unreliable data.

The platform combines:

- Hybrid quantum-classical execution
- Confidence-aware inference
- Input-integrity reporting
- Controlled decision logic
- Managed cloud deployment

Website:

https://tqnnlabs.com

Built in Canada 🇨🇦

---

# Vision

TQNN Labs is building infrastructure that helps applications understand not only **what** was predicted, but **how much confidence** should be placed in the prediction.

Reliable inference should continue working even when real-world data does not.

**Build once. Infer through uncertainty.**