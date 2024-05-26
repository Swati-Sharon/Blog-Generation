# Blog Generation Application
- LLama 2 for the model.
- LangChain for the language model handling.
- Streamlit for the web interface.

## Ensure you have the LLama 2 model file
https://www.kaggle.com/datasets/rodrigostallsikora/llama-2-7b-chat-ggmlv3-q8-0-bin/data
- Update the model path in `app.py` if necessary:

##  Install the required dependencies:
- pip install -r requirements.txt

## Imports:
- streamlit is used for creating the web interface.
- PromptTemplate from langchain.prompts helps in creating the prompt for the language model.
- CTransformers from langchain_community.llms is used to load and interact with the LLama 2 model.

## Function to Get Response from LLama 2 Model:
- Parameters: input_text (the topic of the blog), no_words (desired word count), and blog_style (target audience or style).
- Model Loading: Loads the LLama 2 model using CTransformers with specified configuration (max_new_tokens limits the generated text length, temperature controls the randomness).
- Prompt Template: Defines the template for the blog prompt.
- Prompt Creation: Creates a prompt using the input variables.
- Response Generation: Generates and prints the response from the model based on the formatted prompt.
- Return: Returns the generated blog text.

## Streamlit Configuration:
- Sets up the page title, icon, layout, and sidebar state.
- Adds a header to the web page.
- Adds input fields for the blog topic, word count, and blog style.

## Button and Action:
- Create a button labeled "Generate".
- When clicked, it calls the getLLamaResponse function with the provided inputs and displays the generated blog text on the webpage.

## Usage
To run the blog generation application:
1. Navigate to the project directory.
2. Start the Streamlit application:
    - streamlit run app.py
3. Open your web browser and go to the provided URL (usually `http://localhost:8501`).
4. Enter the blog topic, specify the number of words, select the blog style, and click "Generate" to create your blog.

Here is the Blog Generation snapshot:  [blog_generation.png](blog_gen_app.png)
