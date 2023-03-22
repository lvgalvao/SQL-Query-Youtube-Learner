from config import API_KEY_CHATGPT
import openai

def GetAnswer(query: str):
    
    openai.api_key = API_KEY_CHATGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "I want you to act as a SQL developer teacher \
                 You will apply your knowledge in data principles \
                 and software techniques to understain just the main topic about a SQL query. \
                 Write just the most important topic in just 5 words"},
                {"role": "user", "content": f"{query}"},
            ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    return result