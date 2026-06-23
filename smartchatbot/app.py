from google import genai

client = genai.Client(api_key="[ENCRYPTION_KEY]")           # enter your api key from gemini api key 

print("Chatbot: Hello! Type 'exit' to quit.")

while True:                                                 # loops used to run the program 
    user_input = input("You: ")                             # input to the model 

    if user_input.lower() == "exit":                        # to exit the loop 
        print("Chatbot: Goodbye!")
        break

    response = client.models.generate_content(                  # response from the API as output 
        model="gemini-2.5-flash",                               # model used 
        contents=user_input                                     # input for the model 
    )

    print("Chatbot:", response.text)