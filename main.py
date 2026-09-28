from core.client import Client
from prompts.system import SYSTEM_PROMPT


def main():
    client = Client()
    history = []

    print("Eren is online. Type 'exit' to quit.\n")

    while True:
        user_input = input("you> ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        if not user_input:
            continue

        history.append({"role": "user", "content": user_input})

        reply = client.send(SYSTEM_PROMPT, history)
        print(f"eren> {reply}\n")

        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
