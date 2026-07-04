from tqnn import TQNNClient

client = TQNNClient(
    api_key="YOUR_API_KEY"
)

market_data = {
    "price": 189.42,
    "volume": 1823456,
    "rsi": 64.3,
    "macd": 1.28,
    "signal": 1.11
}

result = client.run_any(
    data=market_data,
    mode="FINANCE"
)

print(result)
