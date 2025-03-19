import streamlit as st
import openai
import os
from openai import OpenAI

token = os.environ["TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Streamlit app
def main():
    st.title("Joke Explainer")

    # Text input box for the joke
    joke = st.text_area("Enter your joke here:")

    # Submit button
    if st.button("Submit"):
        if joke:
            # Call OpenAI GPT-4 model for explanation
            response = get_explanation(joke)
            st.subheader("Explanation")
            st.write(response)
        else:
            st.warning("Please enter a joke.")

def get_explanation(joke):
    # Call the OpenAI API
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"Explain the joke: {joke}"}
            ]
        )
        return completion.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    main()