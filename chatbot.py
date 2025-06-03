# chatbot.py

import random

print("🤖 CryptoBestie: Yo! I'm your crypto compass 🌍💰 Ask me anything about trends, sustainability, or growth!")

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

disclaimer = "⚠️ Heads up! Crypto is risky—always do your own research before diving in. 🚨"

def chatbot_response(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBestie: Go green with {recommend}! 🌿 It's planet-friendly *and* promising! 🌎✨")
        print(disclaimer)

    elif "trending" in user_query or "rising" in user_query:
        trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending:
            emoji = random.choice(["🚀", "📈", "🔥"])
            print(f"CryptoBestie: Ooh, check these out—they’re on fire {emoji}: {', '.join(trending)}")
        else:
            print("CryptoBestie: Hmm, not much heating up right now. Check back soon! 🕵️")
        print(disclaimer)

    elif "long-term" in user_query or "growth" in user_query:
        found = False
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                print(f"CryptoBestie: {name} is your long-game champ! 🏆 HODL strong. 💪")
                found = True
                break
        if not found:
            print("CryptoBestie: Hmm, no perfect match for that strategy right now. 🤷‍♀️")
        print(disclaimer)

    else:
        print("CryptoBestie: Huh? 🤔 Try asking me stuff like 'What’s trending?' or 'Which coin is eco-friendly?'")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("CryptoBestie: Peace out! 💸 May your wallets grow and your risks be low! 🫡")
        break
    chatbot_response(user_input)


   

 






