from tqnn import (
    TQNNClient,
    InvalidAPIKeyError,
    RateLimitExceededError,
    TQNNServerError,
)

try:

    client = TQNNClient(
        api_key="YOUR_API_KEY"
    )

    result = client.run_any(
        data=[1, 2, 3],
        mode="TABULAR"
    )

    print(result)

except InvalidAPIKeyError:
    print("Invalid API key.")

except RateLimitExceededError:
    print("Monthly quota exceeded.")

except TQNNServerError:
    print("TQNN server unavailable.")
