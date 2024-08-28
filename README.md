
# Restaurant-Name-Menu-Generator-Using-Streamlit_Langchain_Hugging-Face-Transformer

Welcome to the **Restaurant Name and Menu Generator** project! This repository features an interactive web application built with Streamlit, leveraging the power of Hugging Face Transformers and LangChain to generate creative restaurant names and delicious food menus based on different cuisines around the world. Whether you're exploring new culinary concepts or need inspiration for your next restaurant, this tool aims to provide unique and culturally relevant suggestions.

## Project Overview

This project is a demonstration of how cutting-edge technologies like natural language processing (NLP) and machine learning can be integrated to create useful and engaging applications. By utilizing the GPT-2 model from Hugging Face Transformers, LangChain for structured prompt management, and Streamlit for creating interactive user interfaces, we create an intuitive and easy-to-use application.

### Features

- **Generate Unique Restaurant Names:** Enter the name of a country, and the app will generate a creative restaurant name that resonates with the cuisine of that country.
- **Create Customized Menus:** Using the generated restaurant name, the app produces a menu featuring traditional and popular dishes, beverages, and more.
- **Interactive UI:** Built with Streamlit, the web interface is simple to navigate, requiring minimal input to generate valuable outputs.
- **Modular Code Structure:** The project is structured with modularity in mind, allowing for easy adjustments and scaling.

## How It Works

1. **Streamlit Integration:** Streamlit is used to create the interactive front-end of the application, allowing users to input the name of a country and view the generated restaurant names and menus.
2. **Hugging Face Transformers:** The GPT-2 model from Hugging Face is employed for generating text based on the prompts provided. It leverages pre-trained language models to understand and generate human-like text.
3. **LangChain:** LangChain is used to manage and structure the prompts, making it easy to customize and control the input provided to the language model. It allows for fine-tuning the behavior of the model based on different scenarios.
4. **Pipeline and Prompts:** The application runs two main pipelines: one for generating restaurant names and another for generating food menus. Each pipeline uses specific prompts tailored to extract meaningful and culturally appropriate names and dishes.

## Installation and Setup

Follow these steps to set up the application locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Restaurant-Name-Menu-Generator-Using-Streamlit_Langchain_Hugging-Face-Transformer.git
   cd Restaurant-Name-Menu-Generator-Using-Streamlit_Langchain_Hugging-Face-Transformer
   ```

2. **Create a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

   This command will launch the Streamlit server, and you can interact with the application through your web browser at `http://localhost:8501`.

## Dependencies

The project requires the following Python packages:

- **Streamlit:** For building the interactive UI.
- **Transformers:** From Hugging Face, used for the text-generation model.
- **LangChain:** For managing and structuring prompts for the LLM (Language Learning Model).
- **torch:** Required for Hugging Face Transformers.

All dependencies are listed in the `requirements.txt` file for easy installation.

## Understanding the Code

### app.py

- **Purpose:** This file contains the main code for the Streamlit application, with separate functions to generate restaurant names and food menus.
- **Key Functions:**
  - `generate_restaurant_names(country_name)`: Generates a restaurant name based on the provided country.
  - `generate_food_menu(restaurant_name, country_name)`: Generates a food menu for the given restaurant name and country.
- **Execution Flow:** When a user inputs a country name and clicks "Generate," the app first generates a restaurant name, then uses that name to generate a corresponding menu.

### function_py.py

- **Purpose:** This script combines the name and menu generation into a single function, making it simpler but less modular.
- **Key Functions:**
  - `generate_restaurant_and_menu(country_name)`: Takes a country name as input and generates both the restaurant name and menu in one output.

## Concepts Used

### Streamlit

Streamlit is an open-source app framework used to create beautiful data-driven applications. It's designed to simplify the process of building and deploying ML and data science projects. With Streamlit, you can transform your Python scripts into shareable web applications in minutes.

### Hugging Face Transformers

Hugging Face Transformers is a library that provides general-purpose architectures for NLP. In this project, we use the GPT-2 model, a transformer-based language model that generates coherent and contextually relevant text. By leveraging pre-trained models, we can generate creative and engaging content with minimal additional training.

### LangChain

LangChain is a library that simplifies working with LLMs by offering prompt templates, chains, and other utilities. It helps manage complex interactions with language models by allowing structured prompt creation and response handling.

## Conclusion

While this project showcases the power of integrating NLP models with interactive applications, the generated outputs may sometimes be ambiguous or less specific than desired. Fine-tuning the GPT-2 model on a specific dataset related to restaurant names and menus could significantly improve the quality and relevance of the generated outputs. If you have experience with fine-tuning models or wish to explore this further, your contributions are most welcome!

## Contributing

If you're interested in improving this project, feel free to fork the repository, make your changes, and submit a pull request. Whether it's fine-tuning the model, optimizing the prompts, or enhancing the UI, all contributions are appreciated.

## Acknowledgments

Special thanks to the developers of Streamlit, Hugging Face, and LangChain for their incredible tools and libraries that made this project possible.

---

