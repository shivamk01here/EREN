import g4f
from prompts.system import RUTHLESS_SYSTEM

def generate_response(user_text: str) -> str:
    messages = [
        {"role": "system", "content": RUTHLESS_SYSTEM},
        {"role": "user", "content": user_text}
    ]

    try:
        # g4f automatically routes to a free working provider
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4o,
            messages=messages,
        )
        return response
    
    except Exception as e:
        raise Exception(f"Provider Error: {e}")