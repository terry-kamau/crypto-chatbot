# 🚀 CryptoBestie - Your Eco-Friendly Crypto Sidekick 💰🌱

CryptoBestie is a fun, interactive Python chatbot that helps users explore trending and sustainable cryptocurrencies. Whether you're a crypto newbie or just curious, CryptoBestie is here to guide you with smart logic and a touch of personality.

## 💡 Features
- Identifies trending cryptos
- Recommends the most sustainable coin
- Friendly and meme-ish personality
- Gives basic investment tips (with an important disclaimer!)

## 🛠️ How It Works
CryptoBestie uses a predefined dataset and keyword-based logic to simulate intelligent decision-making:
- If you ask about **sustainability**, it recommends the coin with the highest score and lowest energy use.
- If you ask about **growth**, it picks cryptos with rising trends and strong market caps.

## 🧠 Sample Dataset

```python
crypto_db = {
    "Bitcoin": {"price_trend": "rising", "market_cap": "high", "energy_use": "high", "sustainability_score": 3/10},
    "Ethereum": {"price_trend": "stable", "market_cap": "high", "energy_use": "medium", "sustainability_score": 6/10},
    "Cardano": {"price_trend": "rising", "market_cap": "medium", "energy_use": "low", "sustainability_score": 8/10}
}
