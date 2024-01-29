# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

# Solution
import re

def domain_name(url):
    pattern = r'(https?://)?(www\.)?([a-zA-Z0-9-]+)\.[a-zA-Z]+'
    match = re.search(pattern, url)
    if match:
        return match.group(3)
    else:
        return "Invalid URL"
