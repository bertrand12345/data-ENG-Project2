import unittest
from unittest.mock import patch
import corenlp


class TestCoreNLP(unittest.TestCase):

    @patch('corenlp.wikipedia.search')
    def test_search_wikipedia(self, mock_search):
        mock_search.return_value = ['Test article 1', 'Test article 2']
        result = corenlp.search_wikipedia('Python')
        mock_search.assert_called_with('Python')
        self.assertEqual(result, ['Test article 1', 'Test article 2'])

    @patch('corenlp.wikipedia.summary')
    def test_summarize_wikipedia(self, mock_summary):
        mock_summary.return_value = "Python is a programming language."
        result = corenlp.summarize_wikipedia('Python')
        mock_summary.assert_called_with('Python')
        self.assertEqual(result, "Python is a programming language.")

    @patch('corenlp.summarize_wikipedia')
    @patch('corenlp.get_text_blob')
    def test_get_phrases(self, mock_get_text_blob, mock_summarize_wikipedia):
        mock_summarize_wikipedia.return_value = "Python is a programming language."
        mock_get_text_blob.return_value.noun_phrases = ['python', 'programming language']
        
        result = corenlp.get_phrases('Python')
        
        mock_summarize_wikipedia.assert_called_with('Python')
        mock_get_text_blob.assert_called_with("Python is a programming language.")
        self.assertEqual(result, ['python', 'programming language'])

if __name__ == '__main__':
    unittest.main()
