TQNN SDK

Python SDK for the TQNN AnyEngine API.

Access TQNN's cloud-hosted inference engine through a simple Python interface.

---

Installation

pip install tqnn

---

Quick Start

from tqnn import TQNNClient

client = TQNNClient(
    api_key="TQNN_xxxxxxxxxxxxxxxxx",
    base_url="[https://tqnn-anyengine-api-914075492772.northamerica-northeast1.run.app]"
)

result = client.run_any(
    data=[1, 2, 3, 4],
    mode="ANY"
)

print(result)

---

Supported Modes

Mode| Description
ANY| Automatic inference
EEG| EEG and biosignal analysis
FINANCE| Financial data analysis
CHEM| Molecular and chemistry analysis
TEXT| Text inference
TABULAR| Structured data analysis
IMAGE| Image feature analysis

---

Authentication

Every request requires a valid TQNN API key.

client = TQNNClient(
    api_key="TQNN_xxxxxxxxxxxxxxxxx",
    base_url="https://tqnn-anyengine-api-914075492772.northamerica-northeast1.run.app"
)

API keys are issued after subscribing through TQNN Labs.

---

Basic Usage

from tqnn import TQNNClient

client = TQNNClient(
    api_key="TQNN_xxxxxxxxxxxxxxxxx",
    base_url="[https://tqnn-anyengine-api-914075492772.northamerica-northeast1.run.app]"
)

result = client.run_any(
    data=[1, 2, 3, 4],
    mode="ANY"
)

print(result)

---

EEG Example

result = client.run_any(
    data=eeg_samples,
    mode="EEG",
    sfreq=250
)

---

Finance Example

result = client.run_any(
    data={
        "rsi": 63.2,
        "macd": 1.12,
        "slope": 0.05
    },
    mode="FINANCE"
)

---

Chemistry Example

result = client.run_any(
    data="CCO",
    mode="CHEM"
)

---

Optional Parameters

result = client.run_any(
    data=my_data,
    mode="ANY",
    label="sample",
    metadata={
        "source": "demo"
    }
)

---

API Reference

client.run_any(
    data,
    mode="ANY",
    label=None,
    metadata=None,
    sfreq=None
)

Parameters

Parameter| Description
data| Input data for inference
mode| ANY, EEG, FINANCE, CHEM, TEXT, TABULAR, IMAGE
label| Optional sample label
metadata| Optional metadata dictionary
sfreq| Sampling frequency for EEG data

---

Example Response

{
  "prediction": "class_a",
  "confidence": 0.94,
  "mode": "ANY"
}

---

Status

TQNN SDK Version: 0.1.0

Public API: Active

Supported Modes:

- ANY
- EEG
- FINANCE
- CHEM
- TEXT
- TABULAR
- IMAGE

---

Requirements

- Python 3.9+
- requests >= 2.31.0

---

License

MIT License

Copyright (c) TQNN Labs

---

TQNN SDK provides access to the TQNN AnyEngine API.

The underlying inference engine, backend infrastructure, and proprietary computational methods remain the intellectual property of TQNN Labs.
