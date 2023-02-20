import pickle
from pathlib import Path
import torch

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/bigrams.pkl", "rb") as file:
     P,char_to_int,int_to_char = pickle.load(file)

generator = torch.Generator().manual_seed(2147483647)

def generate_name():
    name = []
    ix = 0
    while True:
        probs = P[ix]
        ix = torch.multinomial(probs, num_samples = 1, replacement = True, generator = generator).item()
        name.append(int_to_char[ix])
        if ix == 0:
            break
    name = ''.join(name)
    return name