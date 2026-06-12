import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

with open("data/narratives.json", "r") as f:
    narratives = json.load(f)

narrative = narratives[0]

original_text = narrative["original"]


def ask_openai(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return response.output_text


narrative["summary_300"] = ask_openai(
    f"Summarize this passage in approximately 300 words:\n\n{original_text}"
)

narrative["summary_100"] = ask_openai(
    f"Summarize this passage in approximately 100 words:\n\n{original_text}"
)

narrative["summary_25"] = ask_openai(
    f"Summarize this passage in approximately 25 words:\n\n{original_text}"
)

narrative["sentence"] = ask_openai(
    f"Reduce this passage to one clear sentence:\n\n{original_text}"
)

narrative["seed"] = ask_openai(
    f"Reduce this passage to one abstract narrative seed. The seed should capture the generative structure of the passage, not just summarize events:\n\n{original_text}"
)

with open("data/narratives.json", "w") as f:
    json.dump(narratives, f, indent=2, ensure_ascii=False)

print("Compression complete.")