import streamlit as st
# 1
from openai import OpenAI

client = OpenAI(
    api_key = "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"
)
name = st.text_input("What is your name?")
recipient = st.text_input("Who are you sending this to?")
style = st.selectbox(
    "Which style would you like?",
    [
        "Sad",
        "Energetic",
        "Apologetic",
        "Comedic",
        "Formal"
    ]
)

content = st.text_area("What would you like this email to be about?")
run = st.button("Submit your request")
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
if run:
    user_prompt = f"Can you write me an email when the writer's name is {name} and the recipient's name is {recipient}. Make sure the email is about {content} and the email style is {style}."
    # 4
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": content_message},
            {"role": "assistant", "content": assistant_message},
            {"role": "user", "content": user_prompt}
        ]
    )
    st.write(response.choices[0].message.content)
# 5



# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )
