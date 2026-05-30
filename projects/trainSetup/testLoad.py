from datasets import load_dataset
import itertools

stream = load_dataset("wikimedia/wikipedia", "20231101.en", split="train", streaming=True)
for example in itertools.islice(stream, 5):
    print(example["title"])
