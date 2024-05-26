import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
## Function to get response from LLama 2 model
def getLLamaResponse(input_text,no_words,blog_style):
    ###Load LLama 2 model
    ###To use LangChain with C Transformers model
    llm=CTransformers(model='C:\Project\Blog Generation\llama-2-7b-chat.ggmlv3.q8_0.bin',model_type='llama', config={'max_new_tokens':256,'temperature':0.01})

    #Prompt Template
    template="""Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words."""

    #creating Promppt Template
    prompt=PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                           template=template)
    
    #generate response from LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


###################STREAMLINE#####################
st.set_page_config(page_title="Blog Generation",page_icon="*",layout="centered",initial_sidebar_state="collapsed")
st.header("Generate Blogs")
input_text=st.text_input("Enter the Blog Topic")
col1,col2=st.columns([5,5])
with col1:
    no_words=st.text_input("Number of Words")
with col2:
    blog_style=st.selectbox('Writing the blog for ',
                            ('General','Students','Researchers','Data Scientist'),index=0)

submit=st.button("Generate")

if submit:
    st.write(getLLamaResponse(input_text,no_words,blog_style)) 