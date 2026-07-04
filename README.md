# TQNN SDK

The official Python SDK for the **TQNN AnyEngine API**.

TQNN provides a unified interface for cloud-hosted inference across multiple data domains. Whether you're working with biosignals, financial markets, chemistry, text, images, or structured datasets, the SDK allows you to interact with the TQNN inference engine through one simple Python interface.

---

# Installation

```bash
pip install tqnn
```

Upgrade to the latest version:

```bash
pip install --upgrade tqnn
```

---

# Why TQNN?

Most machine learning frameworks are designed around solving a single problem.

TQNN takes a different approach.

Using a single client and a single API, developers can analyze multiple data domains through one consistent interface.

Write your code once.

Change only the input data.

---

# Supported Modes

| Mode | Description |
|------|-------------|
| **ANY** | Automatic inference |
| **EEG** | EEG & biosignal analysis |
| **FINANCE** | Financial market analysis |
| **CHEM** | Molecular & chemistry analysis |
| **TEXT** | Natural language inference |
| **TABULAR** | Structured data analysis |
| **IMAGE** | Image feature analysis |

---

# Quick Start

```python
from tqnn import TQNNClient

client = TQNNClient(
    api_key="YOUR_API_KEY"
)

result = client.run_any(
    data=[1, 2, 3, 4],
    mode="ANY"
)

print(result)
```

---

# Examples

## EEG

```python
result = client.run_any(
    data=eeg_samples,
    mode="EEG",
    sfreq=250
)
```

---

## Finance

```python
result = client.run_any(
    data={
        "rsi": 63.2,
        "macd": 1.12,
        "slope": 0.05
    },
    mode="FINANCE"
)
```

---

## Chemistry

```python
result = client.run_any(
    data="CCO",
    mode="CHEM"
)
```

---

## Text

```python
result = client.run_any(
    data="Artificial intelligence is transforming science.",
    mode="TEXT"
)
```

---

## Tabular

```python
result = client.run_any(
    data=[18.2, 24.1, 0.82, 15.6],
    mode="TABULAR"
)
```

---

## Image

```python
result = client.run_any(
    data=image_array,
    mode="IMAGE"
)
```

---

# Optional Parameters

```python
result = client.run_any(
    data=my_data,
    mode="ANY",
    label="sample_001",
    metadata={
        "source": "demo"
    }
)
```

---

# API Reference

```python
client.run_any(
    data,
    mode="ANY",
    label=None,
    metadata=None,
    sfreq=None
)
```

| Parameter | Description |
|-----------|-------------|
| **data** | Input data for inference |
| **mode** | ANY, EEG, FINANCE, CHEM, TEXT, TABULAR or IMAGE |
| **label** | Optional sample label |
| **metadata** | Optional metadata dictionary |
| **sfreq** | Sampling frequency for EEG data |

---

# Example Response

```json
{
    "prediction": "class_a",
    "confidence": 0.94,
    "mode": "ANY"
}
```

---

# Authentication

Every request requires a valid TQNN API key.

```python
from tqnn import TQNNClient

client = TQNNClient(
    api_key="YOUR_API_KEY"
)
```

API keys are issued after subscribing through **TQNN Labs**.

---

# Documentation & Resources

**Website**

https://tqnnlabs.com

The GitHub repository includes:

- Complete SDK source code
- Working examples
- Release history
- Documentation
- Issue tracker

---

# Requirements

- Python 3.9+
- requests >= 2.31.0

---

# License

MIT License

Copyright (c) TQNN Labs.

The **TQNN SDK** is open source under the MIT License.

The **TQNN AnyEngine runtime**, backend infrastructure, proprietary inference engine, and computational methods remain the intellectual property of **TQNN Labs**.
