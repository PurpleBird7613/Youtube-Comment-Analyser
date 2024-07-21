
# YouTube Comment Analyzer📜🔍

## Project Overview
The YouTube Comment Analyzer is a powerful tool that helps analyze and categorize comments on YouTube videos. This project takes a YouTube video link as input, uses a Large Language Model (LLM) to analyze all the comments, and categorizes them into different categories such as good comments, bad comments, suggestions, requests, and more based on the comment context.

## How it Works

### 1. Input
Provide a YouTube video link as input.

### 2. Comment Collection
The tool collects all the comments from the YouTube video.

### 3. LLM Analysis
The Large Language Model (LLM) analyzes each comment to understand its context and sentiment.

### 4. Categorization
The tool categorizes each comment into different categories such as:
* Good comments
* Bad comments
* Suggestions
* Requests
* and more...

### 5. Report Generation
The tool generates a comprehensive report of the analyzed comments, including the categorization and sentiment analysis (Final report in .html for easy viewing...).

### 6. Output
The report is saved to a file for further analysis or review.

## Features
* Analyze 5000-70000 of comments in few minutes
* Accurate categorization using Large Language Model (LLM)
* Supports multiple categories for comment classification
* Generates a comprehensive report of the analyzed comments
* Saves the report to a file for further analysis or review

## Getting Started💻

### 1. Clone the repository
```
git clone https://github.com/PurpleBird7613/Youtube-Comment-Analyser.git
```

### 2. Install the required dependencies
```
pip install -r requirements.txt
```

### 3. Required
```
GEMINI_API_KEY = XXXXXXXXXXXXXXXXXX #Inside .env file
GROQ_API_KEY = XXXXXXXXXXXXXXXXXX #Inside .env file
YOUTUBE_API_KEY = XXXXXXXXXXXXXXXXX # Inside .env file
```

### 4. Run the tool
```
python main.py
```

### 5. Provide the YouTube video link as input
```
🚀 Enter YouTube URL: [insert link here]
```

## 📑Example Report
```
comments.txt - (Extracted comments)
analysed_comments.txt - (Analysed comments)
report_viewer.html - (Analysed comments in html page)
```