import requests
import re

# Fixed webpage URL
url = "https://www.python.org/"

# Fetch the webpage
response = requests.get(url)

# Extract the title using regex
match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE)
title = match.group(1) if match else "No title found"

# Save the title to a file
with open("webpage_title.txt", "w", encoding="utf-8") as f:
    f.write(title)

print(f"✅ Title saved to 'webpage_title.txt': {title}")
