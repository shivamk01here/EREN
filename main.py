from core.providers import get_provider

def main():
    try:
        provider = get_provider()
        print(f"[SYSTEM] Eren initialized. Backend: {provider.__class__.__name__}")
        print("[SYSTEM] Awaiting input. (Type 'exit' to terminate)")
    except Exception as e:
        print(f"[CRITICAL] {e}")
        return
    
    while True:
        user_input = input("\n> ")
        
        if user_input.strip().lower() in ['exit', 'quit']:
            print("[SYSTEM] Shutting down.")
            break
            
        if not user_input.strip():
            continue

        try:
            # Look how clean the execution is. The interface hides the HTTP complexity.
            response = provider.generate(user_input)
            print(f"\n[Eren]\n{response}")
        except Exception as e:
            print(f"\n[ERROR] {e}")

if __name__ == "__main__":
    main()