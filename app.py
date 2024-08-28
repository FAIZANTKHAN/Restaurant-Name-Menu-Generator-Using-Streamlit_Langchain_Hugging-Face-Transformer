import streamlit as st
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFacePipeline  # Updated import based on deprecation warning
from langchain.prompts import PromptTemplate
from transformers import pipeline

# Initialize a Hugging Face text generation pipeline with GPT-2
generator = pipeline(
    'text-generation',
    model='gpt2',
    clean_up_tokenization_spaces=False,
    max_new_tokens=100,  # Adjust this value as needed
    pad_token_id=50256  # Set pad token to eos token
)

# Wrap the generator in HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=generator)


# Function to generate restaurant names based on country
def generate_restaurant_names(country_name):
    name_prompt_template = PromptTemplate(
        input_variables=['country'],
        template="Generate a unique restaurant name based on the cuisine of {country}."
    )
    name_chain = LLMChain(
        llm=llm,
        prompt=name_prompt_template
    )
    restaurant_names = name_chain.run({'country': country_name})
    return restaurant_names


# Function to generate a food menu based on restaurant name and country
def generate_food_menu(restaurant_name, country_name):
    menu_prompt_template = PromptTemplate(
        input_variables=['restaurant', 'country'],
        template="Generate a delicious menu for the restaurant named {restaurant}, which serves {country} cuisine."
    )
    menu_chain = LLMChain(
        llm=llm,
        prompt=menu_prompt_template
    )
    food_menu = menu_chain.run({'restaurant': restaurant_name, 'country': country_name})
    return food_menu


# Streamlit app
def main():
    st.title("Restaurant Name and Menu Generator")

    # Input from user
    country = st.text_input("Enter the name of the country:")

    if st.button("Generate"):
        if country:
            with st.spinner("Generating..."):
                # Generate restaurant name
                restaurant_name = generate_restaurant_names(country)
                st.subheader("Generated Restaurant Name")
                st.write(restaurant_name)

                # Generate food menu
                food_menu = generate_food_menu(restaurant_name, country)
                st.subheader("Generated Food Menu")
                st.write(food_menu)
        else:
            st.error("Please enter a country name.")


if __name__ == "__main__":
    main()
