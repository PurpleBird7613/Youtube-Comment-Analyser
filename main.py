import re
from dotenv import load_dotenv
from comments_fetcher import YouTubeCommentsTool
from comments_analyser import comments_analyser
from report_viewer import report_viewer
import time

load_dotenv()

# Extracting video ID fro the link
def extract_video_id(url):
    # This regex will match the video ID from any YouTube URL (normal, shortened, embedded)
    try:
        match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
        return match.group(1) if match else None
    except Exception as e:
        print(e)

def run():
    video_url = input("🚀 Enter YouTube URL: ")
    
    video_id = extract_video_id(video_url)
    if not video_id:
        print("🚨 Invalid YouTube URL provided.")
        exit()
    else:
        print(f"🤖Video ID: {video_id}")
    
    # Used as Tool to extract the comments
    tool = YouTubeCommentsTool()
    
    comments = tool._run(video_id)
    print(comments)

    # Encode the comments with emojis
    encoded_comments = []
    for comment in comments:
        encoded_comment = {'user': comment['user'], 'comment': comment['comment']}
        encoded_comments.append(encoded_comment)
     
    # Saving The Comments in .txt File   
    with open("comments.txt", "w") as f:
        f.write(f"VIDEO URL: {video_url} \nVIDEO ID: {video_id}\nCOMMENTS:  ")
        
    with open("comments.txt","a") as f:
        for comment in comments:
            f.write(f"{comment['user']}: {comment['comment']}\n")   
            
    
    # Analysing the comments
    print("\n📖🔍Analysing the comments.....\n")
    comments_analysed = comments_analyser(video_url,comments)
    print("Comment analysing done!!!💜\n")
    print(comments_analysed)
    
    
    # Making the Report
    try: 
        with open("analysed_comments.txt","r") as f:
            analysed_comments = f.readlines()    
    except:
        pass 
    print("\n📑💻Making the Report....\n")
    final_report = report_viewer(analysed_comments)
    print("Report is done!!!💜\n")
    print(final_report)
    
if __name__ == "__main__":
    run()
