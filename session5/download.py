
from urllib import request
from bs4 import BeautifulSoup

# download the files in the following path
# https://repo1.maven.org/maven2/org/ajax4jsf/ajax4jsf/1.0.1/

URL = "https://repo1.maven.org/maven2/org/ajax4jsf/ajax4jsf/1.0.1/"

# step 1: get page
contents = request.urlopen(URL).read()

# step 2: retrieve links
pasedHtml = BeautifulSoup(contents, features="html.parser")
anchorList = pasedHtml.find_all("a")

# step 3: download link
for a in anchorList:
    href = a.get('href')
    if href != "../":
        fileUrl = URL + href
        print(f"downloading: {fileUrl}")
        fileContent = request.urlopen(fileUrl).read()
        fileName = f"./download/{href}"
        with open(fileName, "wb") as file:
            print(f"writing {fileName}")
            file.write(fileContent)







