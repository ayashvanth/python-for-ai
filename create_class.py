class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Raju", "Pomeranian")
dog2 = Dog("Bookah", "Indie")

print(dog1.name)
print(dog2.breed)

# -------------------- #

class APIconfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

dev_config = APIconfig("sk-dev-key", max_tokens=50)
prod_config = APIconfig("sk-prod-key", model = "gpt-4", max_tokens=1000)

print(dev_config.model)
print(prod_config.max_tokens)
print(dev_config.base_url)

# -------------------- #
