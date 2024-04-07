from openai import OpenAI
# IMPORT 密碼進來
from KEYS import OPENAI_API_KEY

# 使用你的api-key，並且透過OpenAI API連線到OpenAI雲端
client = OpenAI(api_key=OPENAI_API_KEY)

# 只存文字訊息
# ["訊息一", "訊息二", "訊息三"]
history = list()

def update_history(message):
    # 更新對話紀錄，不論是User or System(Chatbot)，都會以純文字的方式儲存在對話紀錄中。
    history.append(message)

def create_chatgpt_message(history):
    # 生成符合ChatGPT官方API的格式
    roles = ('user', 'system')
    messages = []
    # 先把對話紀錄反過來，用來確保最後一句話一定是User說的。
    for index, content in enumerate(reversed(history)):
        messages.append(
            {
                "role": roles[ index%2 ], 
                "content": content
            }
        )
    # 最後再倒序成原來的順序
    messages.reverse()
    print(messages)
    return messages

def openai_chatgpt(last_user_message):
    
    # 更新 User 訊息到歷史紀錄
    update_history(last_user_message)
    
    # 產生回覆
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=create_chatgpt_message(history)
    )
    response = completion.choices[0].message

    # 更新 Chatbot回覆 到歷史紀錄
    update_history(response.content)
    return response.content