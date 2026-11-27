from anthropic import Anthropic
from db_report import get_hours_per_topic

client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment

def write_summary(rows):
    data = ", ".join(f"{topic}: {hours}h" for topic, hours in rows)
    message = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=300,
        messages=[{
            "role": "user",
            "content": f"Write a 3-sentence summary of this study log: {data}"
        }],
    )
    return "".join(block.text for block in message.content if block.type == "text")

if __name__ == "__main__":
    print(write_summary(get_hours_per_topic()))