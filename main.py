"""Notes From a Passive-Aggressive Fridge — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The twist: the fridge blames the owner's willpower, not the electricity bill.
TEXT = "I noticed you opened me at 3 AM again. The light bill is not my problem, but your willpower clearly is."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
