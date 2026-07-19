# TQNN Python SDK

## Official Python client for the TQNN API

The TQNN Python SDK provides a simple interface for interacting with the TQNN Fault-Tolerant Inference Platform.

Build applications that perform confidence-aware inference across structured data using a consistent Python interface.

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
| data | Structured input data |
| mode | EEG, FINANCE, TABULAR, IMAGE or ANY |
| task | Optional inference context |
| label | Optional request label |
| metadata | Additional request metadata |

---

# Example Response

```python
{
    "platform": "TQNN",
    "engine": "fault_tolerant_inference",

    "result": {
        "prediction_index": 1,
        "prediction_label": "fault",
        "confidence": 0.94,
        "decision": "accept"
    },

    "tqnn_report": {
        "primary_capability": "Fault Diagnosis",

        "confidence": {
            "score": 0.94,
            "label": "high"
        },

        "data_integrity": {
            "score": 0.98,
            "label": "nominal"
        }
    },

    "diagnostics": {}
}
```

---

# Convenience Methods

The SDK includes helper methods for accessing commonly used sections of a response.

### Prediction

```python
result = client.result(response)
```

### TQNN Report

```python
report = client.report(response)
```

### Diagnostics

```python
diagnostics = client.diagnostics(response)
```

---

# Supported Modes

| Mode | Description |
|------|-------------|
| EEG | Biosignal inference |
| FINANCE | Financial time-series inference |
| TABULAR | Structured datasets |
| IMAGE | Structured image feature inference |
| ANY | Generic structured inference |

---

# Common Applications

The same SDK can be used for a wide range of structured inference problems, including:

- Fault Diagnosis
- Fault Detection
- Sensor Monitoring
- Industrial Process Monitoring
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

# Philosophy

The SDK is intentionally lightweight.

Its purpose is to provide a clean Python interface to the TQNN API while exposing the full standardized response returned by the platform.

Rather than hiding inference details, the SDK gives developers direct access to prediction results, confidence information, data integrity metrics, and diagnostics.

---

# License

The TQNN Python SDK is released under the MIT License.

The SDK is open source and intended to simplify integration with the hosted TQNN API.

The underlying TQNN inference runtime and proprietary implementation remain the intellectual property of TQNN Labs.

---

**TQNN Labs**

Official Python SDK for the TQNN Fault-Tolerant Inference Platform.