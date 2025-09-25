"""
Simple Uzbek morphology analyzer.

This script strips common suffixes from Uzbek words written in Latin script
and outputs the remaining stem along with the suffixes removed.

Usage:

    python src/morph.py <word>

Example:
    python src/morph.py kitoblaringizdanmi

    Input: kitoblaringizdanmi
    Stem : kitob
    Suffix chain: laringiz + danmi
"""

import sys

# List of common Uzbek suffixes (Latin script). This is not exhaustive but
# serves as a starting point and can be extended.
SUFFIXES = [
    "ingizdanmi", "laringizdanmi", "danmi", "dan", "mi",
    "laringiz", "larimiz", "lar", "ingiz", "imiz", "ni", "ga", "da",
]

def analyze(word: str):
    """Return the stem and list of suffixes for a given word.

    The function greedily strips suffixes from the end of the word,
    matching the longest suffixes first. It returns the remaining
    stem and a list of suffixes in the order they were stripped.

    Args:
        word: The input word in lowercase Latin script.

    Returns:
        A tuple (stem, suffixes) where stem is the root of the word and
        suffixes is a list of removed suffixes.
    """
    w = word.lower()
    suffixes = []
    changed = True
    while changed:
        changed = False
        for s in sorted(SUFFIXES, key=len, reverse=True):
            if w.endswith(s) and len(w) > len(s) + 1:
                w = w[:-len(s)]
                suffixes.append(s)
                changed = True
                break
    return w, suffixes


def main():
    if len(sys.argv) < 2:
        print("Usage: python src/morph.py <word>")
        return
    word = sys.argv[1]
    stem, suffixes = analyze(word)
    print(f"Input: {word}")
    print(f"Stem : {stem}")
    if suffixes:
        print(f"Suffix chain: {' + '.join(suffixes)}")
    else:
        print("Suffix chain: (none)")


if __name__ == "__main__":
    main()