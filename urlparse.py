from urllib.parse import urlparse

# Print banner
print("*" * 30)
print("URLsParse By Wond3r")
print("*" * 30)

# Read the list of URLs from a file
with open("urls.txt", "r") as f:
    url_list = [line.strip() for line in f]

# Loop through each URL and extract the domain
domain_list = [urlparse(url).netloc for url in url_list]

# Remove duplicate domains
unique_domains = list(set(domain_list))

# Print the unique domains
for domain in unique_domains:
    print(domain)
