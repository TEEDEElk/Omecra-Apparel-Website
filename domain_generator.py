import random

# Base name
base_name = "omecra"

# Domain extensions
extensions = [".com", ".in", ".co", ".net", ".apparel"]

# Function to generate a domain name
def generate_domain(base, extensions):
    # Randomly select an extension
    extension = random.choice(extensions)
    # Combine base name with the selected extension
    domain_name = base + extension
    return domain_name

# Generate a domain name
for _ in range(5):  # Generate 5 random domain names
    print(generate_domain(base_name, extensions))