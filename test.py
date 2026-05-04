import requests

# ✅ Correct endpoint (FIXED)
url = "<deployment-url>"

API_KEY = "<primary api key>"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
    "messages": [
        {"role": "user", "content": "Explain machine learning in simple terms"}
    ],
    "max_tokens": 150,
    "temperature": 0.7
}

try:
    response = requests.post(url, headers=headers, json=payload)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        print("\n✅ Model Response:\n")
        print(data["choices"][0]["message"]["content"])
    else:
        print("\n❌ Error:\n", response.text)

except Exception as e:
    print("Exception occurred:", str(e))