from datasets import load_dataset
import itertools

dataset = load_dataset("stanfordnlp/imdb")
print(dataset)
print(dataset["train"][0])

dataset = load_dataset("wikimedia/wikipedia", "20231101.en", split="train", streaming=True)

for example in itertools.islice(dataset, 5):
    print(example["title"])

stream._ex_iterable = None
del stream
