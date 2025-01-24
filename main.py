import streamlit as st
from phi.agent import Agent
from phi.tools.googlesearch import GoogleSearch
from phi.model.groq import Groq
from dotenv import load_dotenv
load_dotenv()
book_recommendation_agent=Agent(
    name="book search agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[GoogleSearch(fixed_max_results=10)],
    instructions=[ "You are a book search agent specialized in recommending the best books based on user preferences, such as genre, year, and author.",
    "If the exact match is not available, suggest similar books within the same genre and by the author, prioritizing quality and relevance.",
    "A detailed description of the book, including its plot, themes, and why it aligns with the user's preferences.",
],
    show_tools_call=True,
    markdown=True,
)
st.title("Book recommender by ai agents")

st.subheader("give me genre,year,author")
genre=st.text_input("enter the genre of book"),
year=st.text_input("enter year in which book was published"),
author=st.text_input("enter author name"),
count = st.slider("Number of Recommendations:", min_value=1, max_value=10, value=5),
if st.button("predict"):
    query=(
    f"you are agent looking for a book:"
    f" Genre:{genre},Year:{year},author name:{author}"
    f"give me recommendation count:{count}"
    )
    with st.spinner("finding best recommendation for you"):
        response=book_recommendation_agent.run(query)
        st.write(response.content)



