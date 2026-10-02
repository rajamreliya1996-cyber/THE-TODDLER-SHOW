import json
import random
from pathlib import Path

TOPICS_FILE = Path("content/topics/topics.json")
USED_FILE = Path("content/topics/used_topics.json")
OUTPUT_FILE = Path("content/topics/selected_topic.json")


def load_json(file_path, default):
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    return default


# Load all available topics
topics = load_json(TOPICS_FILE, [])

# Load previously used topic IDs
used_topics = load_json(USED_FILE, [])

used_ids = set(used_topics)

# Find topics that have not been used
available_topics = [
    topic for topic in topics
    if topic["id"] not in used_ids
]

# If every topic has been used, start a new cycle
if not available_topics:
    used_ids = set()
    available_topics = topics

# Select a random unused topic
selected_topic = random.choice(available_topics)

# Save selected topic
with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(selected_topic, file, indent=2, ensure_ascii=False)

# Add topic to used list
used_topics.append(selected_topic["id"])

with open(USED_FILE, "w", encoding="utf-8") as file:
    json.dump(used_topics, file, indent=2)

print("Selected topic:")
print(selected_topic["topic"])
print("Category:")
print(selected_topic["category"])
