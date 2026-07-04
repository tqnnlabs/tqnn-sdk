from tqnn import TQNNClient

client = TQNNClient(
    api_key="YOUR_API_KEY"
)

eeg = [
    0.12,
    -0.08,
    0.32,
    0.45,
    -0.16,
    0.28
]

result = client.run_any(
    data=eeg,
    mode="EEG",
    sfreq=250
)

print(result)
