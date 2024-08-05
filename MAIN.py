import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
import streamlit.components.v1 as components

# Set your API key
GROQ_API_KEY = "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"

# Initialize the Groq model
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=GROQ_API_KEY)
parser = StrOutputParser()

# Streamlit UI
st.set_page_config(page_title="KnowledgeBot", layout="wide")

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KnowledgeBot</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  <style>
    * {
      margin: 0;
      padding: 0;
      font-family: sans-serif;
    }

    .bg {
      background-color: #e9f6e9;
    }

    .banner {
      background-image: url(https://static.vecteezy.com/system/resources/thumbnails/020/734/052/original/animated-studying-lo-fi-background-late-night-homework-2d-cartoon-character-animation-with-nighttime-cozy-bedroom-interior-on-background-4k-footage-with-alpha-channel-for-lofi-music-aesthetic-video.jpg);
      background-size: cover;
      width: 100%;
      height: 600px;
    }

    #preview {
      width: 300px;
      height: 300px;
    }

    .container h1 {
      font-size: 80px;
      font-weight: 500;
    }

    .left-col {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
    }

    .animation-container {
      animation: fly-in 1s ease-out both;
      animation-delay: 1s;
      opacity: 0;
      transform: translateX(-100%);
    }

    @keyframes fly-in {
      0% {
        transform: translateX(-100%);
        opacity: 0;
      }
      100% {
        transform: translateX(0);
        opacity: 1;
      }
    }

    #how-to-use {
      background-color: #f0f0f0;
      padding: 50px 0;
    }

    h1, h2, h3 {
      font-family: 'Arial', sans-serif;
    }

    h1 {
      font-family: 'Pacifico', cursive;
      font-size: 36px;
    }

    h2 {
      font-family: 'Lobster', cursive;
      font-size: 28px;
    }

    h3 {
      font-family: 'Montserrat', sans-serif;
      font-size: 24px;
    }

    p {
      font-family: 'Open Sans', sans-serif;
      font-size: 18px;
    }
  </style>
</head>
<body>
  
  <div class="banner d-flex flex-column text-center">
    <div class="container d-flex flex-column align-items-center justify-content-center h-100">
        <h1 class="text-light">KNOWLEDGEBOT</h1>
        <h3 class="text-light"> <span id="typed-text"></span></h3>
    </div>
  </div>

  <div class="container-fluid d-flex justify-content-center align-items-center vh-110 bg" id="a">
    <div class="row mt-5">
      <div class="animation-container p-0 col-md-6 text-center flex-row">
        <h2 class="mt-5 mb-4" style="white-space: nowrap;">ASK YOUR DOUBTS HERE</h2>
      </div>
    </div>
  </div>

  <script>
    document.addEventListener("DOMContentLoaded", function () {
      var typed = new Typed("#typed-text", {
        strings: [
          'Your ultimate study companion.',
          'Get answers to all your academic queries.',
          'Your go-to bot for academic success.',
          'Master complex subjects with ease.'
        ],
        typeSpeed: 50,
        backSpeed: 25,
        backDelay: 2000,
        startDelay: 1000,
        loop: true
      });

      window.addEventListener("scroll", function() {
        const animationContainer = document.querySelector(".animation-container");
        const scrollPosition = window.scrollY + window.innerHeight;

        if (animationContainer.offsetTop < scrollPosition) {
          animationContainer.style.animation = "fly-in 1s ease-out both";
        }
      });
    });
  </script>
  <script src="https://unpkg.com/typed.js@2.0.16/dist/typed.umd.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
</body>
</html>
"""

# Render HTML in Streamlit
components.html(html_content, height=800, scrolling=True)

# Input for user query
user_query = st.text_input("Enter your question or topic:")

if user_query:
    # Create messages for the Groq model
    messages = [
        SystemMessage(content="You are an educational tutor. Provide detailed explanations, answer questions, and offer helpful resources related to the user's query."),
        HumanMessage(content=user_query)
    ]
    
    # Get the response from the model
    try:
        response = parser.invoke(model.invoke(messages))
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error: {e}")
