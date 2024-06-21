from flask import Flask, render_template, request
from stories import stories

app = Flask(__name__)

@app.route("/")
def select_story():
    """Show list-of-stories form."""

    all_stories = stories.values()
    return render_template("select-story.html", stories=all_stories)

@app.route("/questions")
def ask_questions():
    """Generate and show form for user to input words."""

    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts

    return render_template("questions.html", story_id=story_id, title=story.title, prompts=prompts)

@app.route("/story")
def show_story():
    """Show story result."""
    
    story_id = request.args["story_id"]
    story = stories[story_id]

    storytext = story.generate(request.args)

    return render_template("story.html", title=story.title, storytext=storytext)