import streamlit as st
from transformers import pipeline
from langchain import PromptTemplate, LLMChain
from langchain_huggingface import HuggingFacePipeline

# Initialize Hugging Face text generation pipeline with GPT-2
generator = pipeline('text-generation', model='gpt2', max_length=100)
llm = HuggingFacePipeline(pipeline=generator)

# Function to generate restaurant name and menu using LLMChain
def generate_restaurant_and_menu(country_name):
    prompt_template = PromptTemplate(
        input_variables=['country'],
        template="Generate a unique restaurant name and a menu with 5-6 items based on the cuisine of {country}. The restaurant name should be creative, and the menu should include traditional dishes and drinks."
    )
    chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )
    response = chain.run({'country': country_name})
    return response

# Streamlit app
def main():
    st.title('Restaurant Name and Menu Generator')

    country = st.text_input('Enter the name of a country to generate a restaurant and menu:', '')

    if st.button('Generate'):
        if country:
            result = generate_restaurant_and_menu(country)
            st.subheader(f'Results for {country} Cuisine:')
            st.write(result)
        else:
            st.write('Please enter a country name.')

if __name__ == "__main__":
    main()

