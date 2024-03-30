import streamlit as st 
from openai import OpenAI

client = OpenAI(api_key="")
# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"):
# INSERT THE BODY OF YOUR get_completions FUNCTION FROM LAB 2!
    completion=client.chat.completions.create(
      model=model,
      messages=[
      {"role":"system","content": "You are a chatbot evaluate customers' eligibility for different housing aid programs"},
      {"role":"user","content":prompt},
      ]
  )
    if completion.choices:
     return completion.choices[0].message.content
    else:
     return "Sorry, unable to generate a response for this prompt."


with st.form(key = "chat"):
    prompt = st.text_input("Ask me any questions or concerns related to housing aid programs") # TODO!
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write(get_completion(prompt))
