from tqnn import TQNNClient

client = TQNNClient(
    api_key="YOUR_API_KEY"
)

result = client.run_any(
    data=[1.2, 2.5, 3.1, 4.8],
    mode="TABULAR"
)

print(result)
