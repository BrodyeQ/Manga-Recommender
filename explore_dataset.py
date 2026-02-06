# Download dataset from HuggingFace
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("Madnesss/manga-query", split="train")

# Explore dataset structure
print(dataset.features)
print(f"Total entries: {len(dataset)}")

# Look at first entry in dataset key fields
print("\n--- First Entry Details ---")
print(f"Title: {dataset[0]['title']}")
print(f"Cover URL: {dataset[0]['cover']}")
print(f"Tags: {dataset[0]['tags']}")
print(f"Description: {dataset[0]['description'][:100]}...") 

# Look at other entries to see variety of tags
print("\n--- Looking at first 5 entries' tags ---")
for i in range(5):
    print(f"{i+1}. {dataset[i]['title']}: {dataset[i]['tags']}")

# Find entries with MULTIPLE SPECIFIED tags (all must be present)
print("\n--- Finding Entries With Multiple Tags ---")

required_tags = ["Action", "Adventure", "Mystery"] 

count = 0
for entry in dataset:
    # Check if ALL required tags are in this entry's tags
    if all(tag in entry['tags'] for tag in required_tags):
        count = count + 1

print(f"Found {count} manga with ALL tags: {required_tags}")

# Randomly pick from 
import random

# Filter to entries with all required tags
print("\n--- Creating Your Working Dataset ---")

required_tags = ['Action', 'Adventure', 'Mystery']

# First, filter to only entries with all tags
filtered_entries = []
for entry in dataset:
    if all(tag in entry['tags'] for tag in required_tags):
        filtered_entries.append(entry)

print(f"Found {len(filtered_entries)} manga with all required tags")

# Randomly select 50 from the filtered entries
random.seed(42)  # This makes your "random" selection repeatable
working_dataset = random.sample(filtered_entries, 50)

print(f"Randomly selected {len(working_dataset)} for your project")

# Look at a few to verify
print("\n--- Sample from your working dataset ---")
for i in range(3):
    print(f"{i+1}. {working_dataset[i]['title']}")



import json

# Save your working dataset to a JSON file
print("\n--- Saving Working Dataset ---")

output_file = "working_dataset.json"

# Convert to a format we can save
dataset_to_save = []
for entry in working_dataset:
    dataset_to_save.append({
        'title': entry['title'],
        'description': entry['description'],
        'tags': entry['tags'],
        'cover_url': entry['cover']
    })

# Save to JSON file
with open(output_file, 'w') as f:
    json.dump(dataset_to_save, f, indent=2)

print(f"Saved {len(dataset_to_save)} entries to {output_file}")
print(f"File location: {output_file}")
