import freeGPT
import re

async def main():
    with open("output.txt", "w", encoding="utf-8") as output_file:
        while True:
            prompt = input("👦: ")
            try:
                resp = await getattr(freeGPT, "gpt4").Completion().create(prompt) #gp3, gpt4, alpaca_7b, falcon_40b
                formatted_resp = re.sub(r'\\u([0-9a-fA-F]{4})', lambda x: chr(int(x.group(1), 16)), resp)
                output_file.write(f"🤖: {formatted_resp}\n")
                print(f"🤖: {formatted_resp}")
            except Exception as e:
                output_file.write(f"🤖: Error - {str(e)}\n")
                print(f"🤖: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
