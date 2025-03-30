import openai
import os
import json
import box
import dotenv

dotenv.load_dotenv()

client = openai.OpenAI(
    api_key = os.environ['OPENAI_API_KEY'],
    base_url = 'https://api.deepseek.com/beta'
)

with open('system.txt') as f:
    system = f.read()

with open('history.txt') as f:
    history = f.read()

def generate(context: str = None):
    global history
    if context:
        history += f'\n\n{context}'
    resp = client.chat.completions.create(
        messages = [
            {
                'role': 'system',
                'content': system
            },
            {
                'role': 'user',
                'content': history
            }
        ],
        model = 'deepseek-chat',
        max_tokens = 8192,
        temperature = 1.5,
        response_format = {'type': 'json_object'}
    )

    return box.Box(json.loads(resp.choiSces[0].message.content))

print(history)
resp = generate()

try:
    while True:
        print(f'\n{resp.story}')
        history += f'\n\n{resp.story}'
        print('\n选择：')
        for n, c in enumerate(resp.choices):
            print(f'\t[{n+1}] {c}')
        i = int(input('你的选择：'))
        resp = generate(resp.choices[i-1])
except KeyboardInterrupt:
    print('\n正在退出……')
finally:
    with open('history.txt', 'w') as f:
        f.write(history)
