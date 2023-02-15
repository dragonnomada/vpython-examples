# 
# Make README.md
#
# This script make the readme with examples 
#
# Author: Alan Badillo Salas <alan@nomadacode.com>
# Created: 2023/02/15
#

import os
import re
from datetime import date

author = "Unknown"
email = "unknown@example.com"
buffer = ""

for base, dirs, files in os.walk("./"):
    
    #print(base)

    # Find python files in pattern 
    if base == "./":
        
        #print(files)
        
        for file in files:
            
            pattern = r"(\d+)\_([^.]+)\.py$"
            match = re.search(pattern, file)
            
            #print(file, match)
            
            if match:
                code = match.group(1)
                name = match.group(2)
                print(file, code, name)

                # Get code lines
                isHeader = True
                headers = []
                lines = []
                created = None

                for line in open(base + file):

                    line = re.sub(r"\n$", "", line)
                    
                    # print(line)

                    if isHeader and re.match(r"^\#", line):
                        if re.search(r"Author", line):
                            match = re.search(r"Author:\s*([^<]+)<?([^>]*)>?", line)
                            if match:
                                author = match.group(1).strip()
                                email = match.group(2).strip()
                            continue
                        if re.search(r"Created", line):
                            match = re.search(r"Created:\s*(\d+)/(\d+)/(\d+)", line)
                            if match:
                                year = int(match.group(1))
                                month = int(match.group(2))
                                day = int(match.group(3))
                                created = date(year, month, day).strftime("%a, %d %b %Y")
                            continue
                        # if re.search(r"^#\s*$", line):
                        #     continue
                        headers.append(re.sub(r"^#\s*", "", line))
                    else:
                        isHeader = False
                        lines.append(line)

                print(author)
                print(email)

                print(created)

                headers.pop(0)
                headers.pop()
                
                print(headers)
                print(lines)

                title = re.sub(r"VPython\s*", "", headers.pop(0))

                buffer += f"## {title}\n"

                # Process headers
                for header in headers:
                    buffer += f"{header}\n"

                # Process gallery
                # buffer += f"<div><center>![{code}_{name}](screenshots/{code}.1.png)</center></div>\n"
                # buffer += f"<img class='screenshot' src='screenshots/{code}.1.png' style='height:100px;width:100%;object-fit:contain;background-color:black;padding:40px 0px;' />\n\n"
                buffer += f"<div style='background:black;'><center><img src='screenshots/{code}.1.png' /></center></div>\n\n"

                buffer += f"> [{file}](./{file})\n\n"

                # Process code
                buffer += "```py\n"
                buffer += "\n".join(lines).strip() + "\n"
                buffer += "```\n\n"


# styles = """
# <style>
# img.screenshot {
#     height:100px !important;
#     width:100% !important;
#     object-fit:contain !important;
#     background-color:black !important;
#     padding:40px 0px !important;
# }
# </style>

# """

buffer = f"# VPython Examples\n\nAuthor: [{author}](mailto:{email})\n\n" + buffer.strip()

print(buffer)

with open("README.md", "w") as f:
    f.write(buffer)
                