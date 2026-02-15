import openai

openai.api_key = "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"

while True:
    prompt = input("You: ")
    if prompt.lower() in ["exit", "quit"]:
        break
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    print("ChatGPT:", response['choices'][0]['message']['content'])
