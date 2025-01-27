# Configure API key
configure({"apiKey": "your_api_key"})

# Example usage of chat function
response = chat(model="example_model", history=["Hello", "How are you?"])
print(response)

# Example usage of create function
response = create(model="example_model", message="New message")
print(response)
