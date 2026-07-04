from tqnn import TQNNClient

client = TQNNClient(
    api_key="YOUR_API_KEY"
)

sample = [
    22.5,
    0.81,
    145,
    7.4,
    0.12,
    1.9
]

result = client.run_any(
    data=sample,
    mode="TABULAR"
)

print(result)
