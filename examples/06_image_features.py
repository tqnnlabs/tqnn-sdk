from tqnn import TQNNClient

client = TQNNClient(
    api_key="YOUR_API_KEY"
)

image_features = [
    0.83,
    0.15,
    0.71,
    0.48,
    0.29
]

result = client.run_any(
    data=image_features,
    mode="IMAGE"
)

print(result)
