"""
TQNN Python SDK Example

Error Handling

This example demonstrates recommended error handling when interacting
with the TQNN Fault-Tolerant Inference Platform.
"""

import os

from tqnn import TQNNClient


API_KEY = os.getenv("TQNN_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "TQNN_API_KEY environment variable is not set."
    )


client = TQNNClient(api_key=API_KEY)


try:

    response = client.run_any(
        data=[
            [1.2, 0.4, 3.3, 0.1],
            [2.1, 1.1, 0.9, 0.5],
        ],
        mode="TABULAR",
        task="classification",
        label="error_demo",
    )

    print("\nInference completed successfully.\n")

    print("Prediction:")
    print(response["result"])

    print("\nTQNN Report:")
    print(response["tqnn_report"])

    print("\nDiagnostics:")
    print(response["diagnostics"])

except ConnectionError:
    print(
        "Unable to connect to the TQNN API. "
        "Please check your internet connection."
    )

except TimeoutError:
    print(
        "The request timed out. "
        "Please try again later."
    )

except PermissionError:
    print(
        "Authentication failed. "
        "Verify that your API key is valid."
    )

except ValueError as exc:
    print(f"Invalid request: {exc}")

except RuntimeError as exc:
    print(f"Runtime error: {exc}")

except Exception as exc:
    print(f"Unexpected error: {exc}")