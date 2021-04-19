<!-- PROJECT SHIELDS -->
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

This  module can extract text from PDfs, Office files, text files, Image files.( More to come soon.)


## Installation


1. Clone the repo
```sh
git clone https://github.com/anirudhpnbb/Pyostie.git
```

2. Install using pip or pip3
```commandline

pip3 install pyostie

(or)

pip install pyostie

```

<!-- USAGE EXAMPLES -->
## Usage


```python
import pyostie

# For PDF files:

output = pyostie.extract(filename, extension="pdf")
text = output.start()


# For Excel files

output = pyostie.extract(filename, extension="xlsx")
text = output.start() 

or

output = pyostie.extract(filename, extension="xls")
text = output.start()

```

## Future Work


In this version we are only able to extract text from PDFs, Excel, TXT and CSV formats only. Soon, we will be adding doc, docx, ppt, pptx, jpg, tif, png and many more. Watch this space for more updates.

<!-- CONTACT -->
## Contact

Anirudh Palaparthi - [@anirudh8889](https://twitter.com/anirudh8889) - aniruddhapnbb@gmail.com

Project Link: [https://github.com/anirudhpnbb/Pyostie](PYOSTIE)
