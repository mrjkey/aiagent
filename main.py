import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

def main():
    if api_key is None:
        raise RuntimeError("no api key!")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    print(args.user_prompt)
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    # user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    user_prompt = args.user_prompt
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        temperature=0,
    )
    if response.usage is None:
        raise RuntimeError("response usage was None")
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {completion_tokens}")
    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")
    else:
        print(message.content)


if __name__ == "__main__":
    main()
