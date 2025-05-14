import streamlit as st

st.title("Human Feedback UI")

# Display a text prompt and model output
prompt = st.text_input("Prompt", "What is the capital of France?")
output = "Paris"  # This should come from the LLM output

st.write(f"Model Output: {output}")

# Feedback form
feedback = st.radio("Was the output correct?", ("Correct", "Needs Correction"))

if feedback == "Needs Correction":
    correct_output = st.text_input("Provide the correct output:")
    st.write(f"Feedback: {correct_output}")
else:
    st.write("Feedback: Correct")

# Here you would typically log the feedback
if st.button("Submit Feedback"):
    st.write("Feedback submitted!")
    # Add functionality to send feedback to the backend or database
