from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)


# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )


@app.route("/")
def ask_questions():
    """Generates the homepage form for users to input words."""

    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)

@app.route("/story")
def generate_story():
    """Generates the Madlibs story based on user inputs to form.""" 

    # Also same as request.args:
    # answers = {}
    # for prompt in story.prompts:
    #     answers[prompt] = request.form[prompt]

    storytext = story.generate(request.args)
    return render_template("story.html", storytext=storytext)

if __name__ == "__main__":
    app.run(debut=True)
