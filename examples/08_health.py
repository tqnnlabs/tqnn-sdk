from tqnn import TQNNClient

client = TQNNClient(
    api_key="YOUR_API_KEY"
)

health = client.health()

print(health)
