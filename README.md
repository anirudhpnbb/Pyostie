<!-- PROJECT SHIELDS -->
[![Upload Python Package](https://github.com/anirudhpnbb/Pyostie/actions/workflows/python-publish.yml/badge.svg)](https://github.com/anirudhpnbb/Pyostie/actions/workflows/python-publish.yml)
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- TABLE OF CONTENTS -->
## Table of Contents


* [About the Project](#about-the-project)
* [Installation](#installation)
* [Usage](#usage)
* [Future Work](#Futurework)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

PYOSTIE is short for Python Open Source Text Information Extractor.

A very elegant and simple library to extract text from many file formats.

This  module can extract text from PDfs, Office files, text files, Image files.
Also, we generate an excel file which gives you some deeper insights into the text. We are now only extracting insights for Image and PDF formats only.( More to come soon.)


## Installation


1. Clone the repo
```sh
git clone https://github.com/anirudhpnbb/Pyostie.git
```

2. Install using pip or pip3
```commandline

pip3 install Pyostie

(or)

pip install Pyostie

```

<!-- USAGE EXAMPLES -->
## Usage


```python
import pyostie

# For image files with insights.

output = pyostie.extract(filename, insights=True, extension="jpg") #### Format of the extension can also be "tif" or "pnb"
df, text = output.start()

# For image files without insights.

output = pyostie.extract(filename, insights=False, extension="jpg")
text = output.start()

# For PDF files:

output = pyostie.extract(filename, extension="pdf")
text = output.start()

# For PDF files with insights:
output = pyostie.extract(filename, insights=True, extension="pdf")
text = output.start()


# For Excel files

output = pyostie.extract(filename, extension="xlsx")
text = output.start() 

# For word files

output = pyostie.extract(filename, extension="docx")
text = output.start()


```

## Future Work


In this version we are only able to extract text from PDFs, Excel, TXT and CSV formats only. Soon, we will be adding doc, ppt, pptx and many more. Watch this space for more updates.

<!-- CONTACT -->
## Contact

Anirudh Palaparthi - [@anirudh8889](https://twitter.com/anirudh8889) - [pnbbanirudh](https://www.linkedin.com/in/pnbbanirudh/) - aniruddhapnbb@gmail.com

NSK - [nskpramod](https://www.linkedin.com/in/pramodnsk/) - nsk.pramod@gmail.com

Project Link: [https://github.com/anirudhpnbb/Pyostie](PYOSTIE)
