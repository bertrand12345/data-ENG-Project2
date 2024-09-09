from nlplogic.corenlp import get_phrases

def test_get_phrases():
    phrases = get_phrases("Golden State Warriors")
    assert 'golden state' in [phrase.lower() for phrase in phrases]
