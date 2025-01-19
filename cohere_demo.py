


import cohere

# Initialize Cohere Client
co = cohere.Client("GXB9IJYyU8KiOGeEoGzSY4VHeGoZqsCvuEbq8Oz2")  # Replace with your API key

def generate_response(prompt):
    # Get response from Cohere API
    response = co.generate(
        model="command-r-plus",  # Use an appropriate model that you have access to
        prompt=f"You: {prompt}\nAI:",  # Structured as a conversation
        max_tokens=100
    )
    return response.generations[0].text.strip()
def generate_response2(prompt):
    # Get response from Cohere API
    response = co.generate(
        model="command-r-plus",  # Use an appropriate model that you have access to
        prompt=f"You: {prompt}\nAI:",  # Structured as a conversation
        max_tokens=100
    )
    return response.generations[0].text.strip()



# def ask_query():
#     print("Ask the AI a question ('exit' to quit):")
    
#     # Keep conversation going until the user wants to exit
#     while True:
#         user_query = input("You: "wh)  # Take input from the user
        
#         if user_query.lower() == "exit":
#             print("Ending conversation...")
#             break
        
#         # Send the message to Cohere using the generate method
#         response = co.generate(
#             model="command-r-plus",  # Replace with an available model from the list
#             prompt=f"You: {user_query}\nAI:",  # Formatting the input as a conversation
#             max_tokens=100
#         )
        
#         # Output the AI's response
#         ai_response = response.generations[0].text.strip()
#         print(f"AI: {ai_response}")

# if __name__ == "__main__":
#     ask_query()

