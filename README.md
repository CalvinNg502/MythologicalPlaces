<h1>Mythological Places Scraper and Generator</h1>

<h2>Description</h2>

<p>This project consists of two files: MythologicalPlacesScraper.py and MythologicalPlacesGenerator.py</p>

<p>
    The scraper scrapes <a href="https://en.wikipedia.org/wiki/List_of_mythological_places" >this webpage</a>  and creates a file called "places.txt" to write places and their descriptions.
</p>

<p>
    The generator reads from that file all place-description pairs and will randomly generate a pair each time the user presses enter.  It exits when the user enters 'exit'.
</p>

<p>
    These scripts are written in python and are meant to be run from the commandline.  The scraper uses requests and Beautiful Soup to fetch the page and then parse it.
</p>

<h2> How to Install/Run the Project </h2>

<p>
    This guide assumes you have installed python and pip (python's package installer), but if you haven't, <a href="https://www.python.org/downloads/">follow this link.</a>  Pip will be installed when you install python.
</p>

<p>
    As mentioned above, the scraper requires both Selenium and Beautiful Soup to run.  Run the following commands: 
</p>

<ul>
    <li>pip install requests</li>
    <li>pip install beautifulsoup4</li>
</ul>

<p>
    Alternatively, you can use requirements.txt to install the necessary packages.  To do so, run the following command: pip install -r requirements.txt.  The generator does not require any addtional packages.
</p>

<p>
    Version numbers of python and packages I used when writing this project:
</p>

<ul>
    <li>Python==3.11.0</li>
    <li>requests==2.28.2</li>
    <li>beautifulsoup4==4.11.1</li>
</ul>

<h2> How to Use the Project </h2>

<p>
    You should first run the scraper to generate the place.txt file.  Without that file, the generator cannot function.  You can run either the .py file directly with python, or you can compile them into .exe files and then run them.  Just be aware of the location of the .txt file.  The generator will ask for a path at runtime, or you can choose not to supply a path if the .py or .exe is in the same directory as the .txt file.
</p>