from google import genai

client = genai.Client(api_key="[ENCRYPTION_KEY]") # enter your api key from gemini api key 

# instructions  for Gemini based on input 
college_info = """                               
Attendance Requirement: 75%
Library Timings: 8 AM to 8 PM
Placement Cell: Block C
Exam Registration: Through ERP Portal
"""

while True:                                                 # using loops to run the program 
    question = input("Student: ")                           # input from the user

    if question.lower() == "exit":                        # exit condition
        break
        # prompt sent to gemini with instructions with required output to be shown 
    prompt = f"""                                            
    You are a College FAQ Assistant.

    College Information:
    {college_info}

    Student Question:
    {question}

    Instructions:
    Answer only using the college information provided.
    If the information is unavailable, say "I do not have that information."

    Answer:
    """

    response = client.models.generate_content(                  # response from the API as output 
        model="gemini-2.5-flash",                               # model used 
        contents=prompt                                         # input for the model 
    )

    print("Chatbot:", response.text)                            # output for the user   