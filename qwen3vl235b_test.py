from openai import OpenAI

client = OpenAI(
    base_url='https://api-inference.modelscope.cn/v1',
    api_key='ms-007121f0-c729-45af-a98e-8392924edf6c', # ModelScope Token
)

response = client.chat.completions.create(
    model='Qwen/Qwen3-VL-235B-A22B-Instruct', # ModelScope Model-Id, required
    messages=[{
        'role':
            'user',
        'content': [{
            'type': 'text',
            'text': '描述这幅图',
        }, {
            'type': 'image_url',
            'image_url': {
                'url':
                    'https://modelscope.oss-cn-beijing.aliyuncs.com/demo/images/audrey_hepburn.jpg',
            },
        }],
    }],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end='', flush=True)