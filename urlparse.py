from urllib.parse import urlparse

# Print banner
print("*" * 30)
print("URLsParse - by Wond3r")
print("*" * 30)

# Read the list of URLs from a file
with open("urls.txt", "r") as f:
    url_list = [line.strip() for line in f]

# Loop through each URL
for url in url_list:
    # Extract the domain from the URL
    domain = urlparse(url).netloc
    print(domain)
