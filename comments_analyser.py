import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"]) 

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]

generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


prompt = """
    Review the insights and research you got for the video comments.
    Make sure the report is VERY detailed with action steps
    to guide new improved content generation.
    All your results and analysis should be grounded in evidence from the comments, so cite appropriately.
    By citations, I mean showing the comments that led to that conclusion to support the claim.
    expected_output: >
    A fully fledged report with main topics, each with a full section of information.
    Formatted as markdown without code blocks. Make sure to include the full video URL in the intro so the
    user can reference when reading the report.
    Make sure the output file is structured very well and easy to read and digest the content with snippets of
    citations for each claim. By citations, I mean showing the comments that led to that conclusion to support the claim.
"""

def comments_analyser(video_url,comments):
    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    safety_settings = safety_settings ,
    system_instruction=f""" 
        You are a sharp-witted YouTube video comment analyst with a passion in a variety of sector. 
        Skilled in navigating through noise in the comments data of this youtube video[video url: {video_url}] {comments} to find meaningful patterns,    
        you synthesize data into insights that highlight the core message of viewer feedback.
        Your analytical prowess ensures that the subtleties of audience engagement and preferences are captured and understood,
        setting the stage for informed content strategies.All your results should be grounded in evidence from the comments, so cite appropriately.
        By citations, I mean showing the comments that led to that conclusion to support the claim.
    """)

    chat_session = model.start_chat(
      history=[]
    )

    response = chat_session.send_message(prompt)

    # Saving the Analysied Report
    with open("analysed_comments.txt","w") as f:
        f.write(response.text)
        f.close()
        
    return response.text
