TQNN SDK

Python SDK for the TQNN AnyEngine API.

Access TQNN's cloud-hosted inference engine using a simple Python interface.

---

Installation

pip install tqnn

---

Quick Start

from tqnn import TQNNClient

client = TQNNClient(
    api_key="TQNN_xxxxxxxxxxxxxxxxx",
    base_url="https://YOUR_API_URL"
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

Every request requires a valid API key.

client = TQNNClient(
    api_key="TQNN_xxxxxxxxxxxxxxxxx",
    base_url="https://YOUR_API_URL"
)

API keys are issued after subscribing through TQNN Labs.

---

Basic Usage

from tqnn import TQNNClient

client = TQNNClient(
    api_key="TQNN_xxxxxxxxxxxxxxxxx",
    base_url="https://YOUR_API_URL"
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

Example Response

{
  "prediction": "class_a",
  "confidence": 0.94,
  "mode": "ANY"
}

---

Requirements

- Python 3.9+
- requests

---

License

MIT License

Copyright (c) TQNN Labs

---

TQNN SDK provides access to the TQNN AnyEngine API.

The underlying inference engine, backend infrastructure, and proprietary computational methods remain the intellectual property of TQNN Labs.
