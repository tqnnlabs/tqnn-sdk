"""
TQNN Python SDK Example

Health Check

This example demonstrates checking the availability of the
TQNN Fault-Tolerant Inference Platform before submitting
inference requests.
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


try:
    health = client.health()

    print("\n=== API Health ===")
    pprint(health)

    if health.get("status") == "healthy":
        print("\n✓ TQNN API is available.")
    else:
        print("\n⚠ API responded but reported a non-healthy status.")

except Exception as exc:
    print(f"\nHealth check failed: {exc}")