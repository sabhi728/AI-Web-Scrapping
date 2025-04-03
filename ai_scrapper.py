# Import the required libraries
import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph

# Set up the Streamlit app
st.title("Web Scraping AI Agent 🕵️‍♂️")
st.caption("This app allows you to scrape a website using OpenAI API")

# Get OpenAI API key from user
openai_access_token = st.text_input("OpenAI API Key", type="password")

if openai_access_token:
    model = st.radio(
        "Select the model",
        ["gpt-3.5-turbo", "gpt-4"],
        index=0,
    )    
    graph_config = {
        "llm": {
            "api_key": openai_access_token,
            "model": model,
        },
    }
    # Get the URL of the website to scrape
    url = st.text_input("Enter the URL of the website you want to scrape")
    # Get the user prompt
    user_prompt = st.text_input("What do you want the AI agent to scrape from the website?")
    
    if url and user_prompt:
        # Create a SmartScraperGraph object
        try:
            smart_scraper_graph = SmartScraperGraph(
                prompt=user_prompt,
                source=url,
                config=graph_config
            )
            # Scrape the website
            if st.button("Scrape"):
                with st.spinner("Scraping website..."):
                    result = smart_scraper_graph.run()
                    st.success("Scraping completed!")
                    st.write(result)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter both URL and scraping prompt to proceed.")