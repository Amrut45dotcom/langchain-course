import os

from dotenv import load_dotenv


def main():
    load_dotenv()  # 🔥 THIS ACTUALLY LOADS THE .env FILE
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
