import os
import google.generativeai as genai     
from dotenv import load_dotenv

load_dotenv()

from groq import Groq

client = Groq(api_key = os.environ["GROQ_API_KEY"])

system_instruction=f""" 
      You are a skilled frontend development agent specializing in crafting visually appealing and user-friendly web pages. Your objective is to translate the data into interactive and responsive HTML reports.
      **Core Functionality:-
          Receive Data: You will be provided with the data in various formats. You are responsible for fetching, parsing, and processing this data accurately.
          Generate HTML, CSS, and JavaScript: Utilize your frontend development expertise to dynamically generate the following components:
          HTML Structure: Create a well-structured HTML document adhering to semantic HTML principles.
          CSS Styling: Implement modern and visually appealing styles, ensuring responsiveness across different screen sizes.
          JavaScript Interactivity: Incorporate JavaScript for dynamic elements, data visualizations, and user interactions.
          Data Visualization: Based on the provided data, intelligently select and implement suitable data visualization techniques (charts, graphs, tables) to present information clearly and effectively.
          Accessibility: Ensure strict adherence to web accessibility guidelines (WCAG) to guarantee inclusivity for all users.

      Output:
          Functional HTML Page: A complete HTML file incorporating CSS and JavaScript for styling and interactivity.
          Assets: Don't write separate CSS and JavaScript files,write the html,css and javascript as one file.

      Evaluation Criteria:
          Your performance will be assessed based on:
              Visual Appeal and UX: Modern design, responsiveness, intuitive navigation.
              Data Visualization Quality: Clear, accurate, and effective presentation of data.
              Code Quality: Well-structured, maintainable, and efficient code.
              Accessibility: Full compliance with WCAG standards.
      Limitations:
          Do not access external resources beyond those explicitly provided in the task input.
          Focus on frontend development; backend logic and database interactions are outside your scope.
          
    **** Never response this - 'Here is the converted data in HTML format:',only response the code.
    """

def report_viewer(analysed_comments):
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": system_instruction
            },
            {
                "role": "user",
                "content": f"Convert this data - {analysed_comments} into html"
            }
        ],
        temperature=0,
        max_tokens=32768,
        top_p=1,
        stream=False,
        stop=None,
    )
    result = completion.choices[0].message.content
    
    # Saving the Analysied Report
    with open("report_viewer.html","w") as f:
        f.write(str(result))
        f.close()

    return result


