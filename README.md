# taxSee
Batch Retrieval of NCBI taxonomy information for scientific names

This program taxSee has two versions: a GUI version (taxSee.py) and a command-line version (taxSeeCLI.py).

## What does taxSee do?
taxSee takes a text file that contains scientific names as input (each new line should have a scientific name).
Then it retrieves the following information (if they are available for that scientific name) from NCBI (National Center for Biotechnology Information) for each scientific name and saves the file in .csv (comma separated values) format.

1)superkingdom
2)kingdom
3)subkingdom
4)superphylum
5)phylum
6)subphylum
7)superclass
8)class
9)subclass
10)superorder
11)order
12)suborder
13)superfamily
14)family
15)subfamily
16)tribe
17)subtribe
18)genus
19)subgenus
20)species
21)subspecies
22)taxid

An example input file has been provided (missingTax.txt) in the repository. The output .csv for that is also provided (missingTaxonomyInfo.txt). The program also creates a missingNamesTaxIds.txt file that maps the scientific names to taxids. There will be some intermediate .txt files that contain taxonomy info for each taxid. It will also produce a taxSeeLog.txt that will inform you about how successful the retrieval was.

## Requirements
You should have Python 2.7 or above which can be downloaded from (https://www.python.org/downloads/). The required python modules are numpy, pandas, bs4, requests, sys, tkinter/Tkinter (for the GUI version).

These modules can be installed via the pip package manager that comes with Python as follows. Open a command prompt as administrator (on Windows platform) and type:

python -m pip install numpy

python -m pip install pandas

python -m pip install bs4

python -m pip install beautifulsoup4

python -m pip install requests

python -m pip install lxml

or a terminal window with sudo privileges (Linux/MacOs) and type:

pip install numpy

pip install pandas

pip install bs4

pip install beautifulsoup4

pip install requests

pip install lxml

## How to run the program
If using the GUI version save both the taxSee.py and taxSee_support.py to the same folder. Open a command prompt (on Windows platform) or a terminal window (Linux/MacOs).
Type:

python taxSee.py  

Browse for the txt file that contains the sceintific names and press the taxSee button.

If using the command-line version, assuming you have the scientific names inside a file named missingTax.txt,

Type:

python taxSeeCLI.py missingTax.txt

