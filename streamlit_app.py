import streamlit as st
# 1
from openai import OpenAI

# 2
client = OpenAI(
    api_key = "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"
)
print("Beep-Boop I write good emails Beep-Boop")
name = input("What is your name? -> ")
recipient = input("Who are you sending this to? -> ")
valid = False
while not valid:
    print("Pick from these writing styles: ")
    print("1. Sad")
    print("2. Energetic")
    print("3. Apologetic")
    print("4. Comedic")
    print("5. Formal")
    style = input("Which style would you like? -> ") 
    valid = True
    if style == "1":
        style = "sad"
    elif style == "2":
        style = "energetic"
    elif style == "3":
        style = "apologetic"
    elif style == "4":
        style = "comedic"
    elif style == "5":
        style = "formal"
    else:
        print("That is not a valid entry, please try again.")
        valid = False
content = input("What would you like this email to be about? -> ")
# 3
content_message = """
Follow standard email format.
For example:
From: Timmy
To: Bob
Subject: Grades
Message: You are cool
"""
assistant_message = "You're supposed to write the best emails possible"
user_prompt = f"Can you write me an email when the writer's name is {name} and the recipient's name is {recipient}. Make sure the email is about {content} and the email style is {style}."
print(user_prompt)
# 4
response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": content_message},
        {"role": "assistant", "content": assistant_message},
        {"role": "user", "content": user_prompt}
    ]
)

# 5
print(response.choices[0].message.content)
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
