import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

with open("data/narratives.json", "r") as f:
    narratives = json.load(f)

def ask_openai(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return response.output_text

for narrative in narratives:
    seed = narrative["seed"]

    narrative["regenerated_from_seed"] = ask_openai(
        f"""
Expand this abstract narrative seed into a vivid reflective passage.

Do not copy the original text.
Preserve the emotional and conceptual structure of the seed.
Write in approximately 200 words.

Seed:
{seed}
"""
    )

with open("data/narratives.json", "w") as f:
    json.dump(narratives, f, indent=2, ensure_ascii=False)

print("Regeneration complete.")