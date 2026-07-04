from tqnn import TQNNClient

client = TQNNClient(
    api_key="YOUR_API_KEY"
)

text = """
Artificial intelligence is transforming
scientific research across multiple disciplines.
"""

result = client.run_any(
    data=text,
    mode="TEXT"
)

print(result)
