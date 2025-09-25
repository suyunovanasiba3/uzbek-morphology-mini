# Uzbek Morphology Mini-Tool

<p align="center">
  <img src="assets/morphology-preview.png" width="880" alt="Uzbek Morphology Mini-Tool">
</p>

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A **toy morphological analyzer** for Uzbek words written in Latin script. This tool
demonstrates basic stemming by stripping common suffixes and outputting the stem
and suffix chain.

## ✨ Features

* Splits an input word into its stem and suffix chain.
* Supports a small set of common Uzbek suffixes (easily extendable).
* Useful as an educational prototype for Uzbek language morphology.

## 📂 Project Structure

```
uzbek-morphology-mini/
 ├─ src/morph.py     # analyzer script
 ├─ README.md        # this file
 ├─ CHANGELOG.md     # release notes
 ├─ LICENSE          # MIT license
 └─ requirements.txt # dependencies (none for now)
```

## 🚀 Usage

Run the analyzer from the command line:

```bash
python src/morph.py "kitoblaringizdanmi"
```

Example output:

```
Input: kitoblaringizdanmi
Stem : kitob
Suffix chain: laringiz + danmi
```

## 🔮 Roadmap

* Expand the suffix list to cover more cases.
* Add support for Uzbek Cyrillic script.
* Integrate with existing Uzbek NLP libraries for more advanced morphology.