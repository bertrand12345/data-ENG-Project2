from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search Wikipedia for the given name."""
    print(f"Searching for: {name}")
    try:
        return wikipedia.search(name)
    except wikipedia.exceptions.WikipediaException as e:
        print(f"An error occurred while searching: {e}")
        return []


def summarize_wikipedia(name1, sentences=3):
    """Summarize Wikipedia article for the given name."""
    print(f"Finding Wikipedia summary for: {name1}")
    try:
        return wikipedia.summary(name1, sentences=sentences)
    except wikipedia.exceptions.WikipediaException as e:
        print(f"An error occurred while summarizing: {e}")
        return ""


def get_text_blob(text):
    """Convert text to a TextBlob object."""
    return TextBlob(text)


def get_phrases(name2):
    """Find Wikipedia summary for the name and return noun phrases."""
    summary = summarize_wikipedia(name2)
    if summary:
        blob = get_text_blob(summary)
        return blob.noun_phrases
    else:
        return []

