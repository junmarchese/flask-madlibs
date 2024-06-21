"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, prompt: answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    # Basic version of app.py:

    # def __init__(self, words, storytext):
    #     """Create story with words and template text."""

    #     self.prompts = words
    #     self.template = storytext

    # def generate(self, answers):
    #     """Substitute answers into text."""

    #     storytext = self.template

    #     for (key, val) in answers.items():
    #         storytext = storytext.replace("{" + key + "}", val)

    #     return storytext

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


    # Part 2 - Further Study version of app.py:
    
#     def __init__(self, code, title, words, storytext):
#         """Create story with words and template text."""

#         self.code = code
#         self.title = title
#         self.prompts = words
#         self.template = storytext

#     def generate(self, answers):
#         """Substitute answers into text."""

#         storytext = self.template

#         for (key, val) in answers.items():
#             storytext = storytext.replace("{" + key + "}", val)

#         return storytext    


# story1 = Story(
#     "history",
#     "A Historical Tale",
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )

# story2 = Story(
#     "good",
#     "Favorite types of Food",
#     ["noun", "verb", "adjective"],
#     """Wow! I love to {verb} {adjective} {noun}!!! """
# )

# stories = {s.code: s for s in [story1, story2]}

# answers = {
#     "place": "castle",
#     "noun": "dragon",
#     "verb": "wear",
#     "adjective": "shiny",
#     "plural_noun": "diamonds"
# }

# generated_story = story.generate(answers)
# print(generated_story)
