# TopScorers
A program which takes as input a CSV file listing people and the score they achieved in a test, and which outputs the top scorers, those people with the highest marks, as well as what that mark was.

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Assumptions
1. Python environment is already setup with Python 3.9.x installed.
2. No complex data transforms are required
3. Output does not require comparison to previous runs


## Installing / Getting started

No additional packages have been installed. Simply clone the repo and call `getTopScorer()`.

## Run

The script can be run by calling `getTopScorer()` as follows:

```python
from top.scorers.TopScorer import getTopScorer

getTopScorer("TestData.csv", True)
```