"""
COMS 4705 - Basic Text Preprocessing Example
Professor John Hewitt, Columbia University

This module demonstrates fundamental text preprocessing techniques
commonly used in NLP applications.
"""

import re
import string
import nltk
from collections import Counter
from typing import List, Dict

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


class TextPreprocessor:
    """
    A comprehensive text preprocessing pipeline for NLP tasks.
    """
    
    def __init__(self, language='english'):
        """
        Initialize the preprocessor.
        
        Args:
            language (str): Language for stopwords (default: 'english')
        """
        self.language = language
        self.stop_words = set(stopwords.words(language))
        
        # Common contractions mapping
        self.contractions = {
            "ain't": "are not", "aren't": "are not", "can't": "cannot",
            "couldn't": "could not", "didn't": "did not", "doesn't": "does not",
            "don't": "do not", "hadn't": "had not", "hasn't": "has not",
            "haven't": "have not", "he'd": "he would", "he'll": "he will",
            "he's": "he is", "i'd": "i would", "i'll": "i will",
            "i'm": "i am", "i've": "i have", "isn't": "is not",
            "it'd": "it would", "it'll": "it will", "it's": "it is",
            "let's": "let us", "shouldn't": "should not", "that's": "that is",
            "there's": "there is", "they'd": "they would", "they'll": "they will",
            "they're": "they are", "they've": "they have", "we'd": "we would",
            "we're": "we are", "we've": "we have", "weren't": "were not",
            "what's": "what is", "where's": "where is", "who's": "who is",
            "won't": "will not", "wouldn't": "would not", "you'd": "you would",
            "you'll": "you will", "you're": "you are", "you've": "you have"
        }
    
    def clean_text(self, text: str) -> str:
        """
        Basic text cleaning: remove extra whitespace and special characters.
        
        Args:
            text (str): Raw text
            
        Returns:
            str: Cleaned text
        """
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove special characters but keep basic punctuation
        text = re.sub(r'[^\w\s\.\!\?\,\;\:]', '', text)
        
        return text.strip()
    
    def expand_contractions(self, text: str) -> str:
        """
        Expand contractions in text.
        
        Args:
            text (str): Text with contractions
            
        Returns:
            str: Text with expanded contractions
        """
        words = text.split()
        expanded_words = []
        
        for word in words:
            # Remove punctuation for matching
            clean_word = word.lower().strip(string.punctuation)
            
            if clean_word in self.contractions:
                # Preserve original punctuation
                punctuation = ''.join(c for c in word if c in string.punctuation)
                expanded = self.contractions[clean_word] + punctuation
                expanded_words.append(expanded)
            else:
                expanded_words.append(word)
        
        return ' '.join(expanded_words)
    
    def tokenize(self, text: str, method: str = 'word') -> List[str]:
        """
        Tokenize text into words or sentences.
        
        Args:
            text (str): Input text
            method (str): 'word' or 'sentence'
            
        Returns:
            List[str]: List of tokens
        """
        if method == 'word':
            return word_tokenize(text)
        elif method == 'sentence':
            return sent_tokenize(text)
        else:
            raise ValueError("Method must be 'word' or 'sentence'")
    
    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """
        Remove stopwords from token list.
        
        Args:
            tokens (List[str]): List of tokens
            
        Returns:
            List[str]: Tokens without stopwords
        """
        return [token for token in tokens if token.lower() not in self.stop_words]
    
    def remove_punctuation(self, tokens: List[str]) -> List[str]:
        """
        Remove punctuation tokens.
        
        Args:
            tokens (List[str]): List of tokens
            
        Returns:
            List[str]: Tokens without punctuation
        """
        return [token for token in tokens if token not in string.punctuation]
    
    def normalize_case(self, tokens: List[str], method: str = 'lower') -> List[str]:
        """
        Normalize case of tokens.
        
        Args:
            tokens (List[str]): List of tokens
            method (str): 'lower', 'upper', or 'title'
            
        Returns:
            List[str]: Case-normalized tokens
        """
        if method == 'lower':
            return [token.lower() for token in tokens]
        elif method == 'upper':
            return [token.upper() for token in tokens]
        elif method == 'title':
            return [token.title() for token in tokens]
        else:
            raise ValueError("Method must be 'lower', 'upper', or 'title'")
    
    def filter_by_length(self, tokens: List[str], min_length: int = 2, 
                        max_length: int = 20) -> List[str]:
        """
        Filter tokens by length.
        
        Args:
            tokens (List[str]): List of tokens
            min_length (int): Minimum token length
            max_length (int): Maximum token length
            
        Returns:
            List[str]: Filtered tokens
        """
        return [token for token in tokens 
                if min_length <= len(token) <= max_length]
    
    def preprocess(self, text: str, steps: List[str] = None) -> List[str]:
        """
        Full preprocessing pipeline.
        
        Args:
            text (str): Raw text
            steps (List[str]): Preprocessing steps to apply
            
        Returns:
            List[str]: Preprocessed tokens
        """
        if steps is None:
            steps = ['clean', 'expand_contractions', 'tokenize', 'lower', 
                    'remove_punctuation', 'remove_stopwords', 'filter_length']
        
        # Start with raw text
        processed = text
        
        # Apply text-level preprocessing
        if 'clean' in steps:
            processed = self.clean_text(processed)
        
        if 'expand_contractions' in steps:
            processed = self.expand_contractions(processed)
        
        # Tokenize
        if 'tokenize' in steps:
            tokens = self.tokenize(processed, method='word')
        else:
            tokens = processed.split()
        
        # Apply token-level preprocessing
        if 'lower' in steps:
            tokens = self.normalize_case(tokens, method='lower')
        
        if 'remove_punctuation' in steps:
            tokens = self.remove_punctuation(tokens)
        
        if 'remove_stopwords' in steps:
            tokens = self.remove_stopwords(tokens)
        
        if 'filter_length' in steps:
            tokens = self.filter_by_length(tokens)
        
        return tokens


def analyze_text(text: str, preprocessor: TextPreprocessor = None) -> Dict:
    """
    Analyze text and provide statistics.
    
    Args:
        text (str): Input text
        preprocessor (TextPreprocessor): Preprocessor instance
        
    Returns:
        dict: Text analysis results
    """
    if preprocessor is None:
        preprocessor = TextPreprocessor()
    
    # Basic statistics
    sentences = preprocessor.tokenize(text, method='sentence')
    words = preprocessor.tokenize(text, method='word')
    
    # Preprocessing
    processed_tokens = preprocessor.preprocess(text)
    
    # Word frequency
    word_freq = Counter(processed_tokens)
    
    analysis = {
        'num_sentences': len(sentences),
        'num_words': len(words),
        'num_unique_words': len(set(word.lower() for word in words)),
        'num_processed_tokens': len(processed_tokens),
        'num_unique_processed': len(set(processed_tokens)),
        'avg_sentence_length': len(words) / len(sentences) if sentences else 0,
        'most_common_words': word_freq.most_common(10),
        'vocabulary_richness': len(set(processed_tokens)) / len(processed_tokens) if processed_tokens else 0
    }
    
    return analysis


def demo():
    """
    Demonstrate text preprocessing capabilities.
    """
    # Sample text
    sample_text = """
    Hello world! This is a sample text for demonstrating NLP preprocessing.
    It contains various sentences, and we'll see how different preprocessing
    steps affect the text. Can't wait to see the results! The text includes
    contractions, punctuation, and common words that might be considered stopwords.
    """
    
    print("=== Text Preprocessing Demo ===\n")
    print("Original text:")
    print(repr(sample_text))
    print()
    
    # Initialize preprocessor
    preprocessor = TextPreprocessor()
    
    # Step-by-step preprocessing
    print("Step-by-step preprocessing:")
    print("-" * 30)
    
    # Clean text
    cleaned = preprocessor.clean_text(sample_text)
    print("1. Cleaned:", repr(cleaned))
    
    # Expand contractions
    expanded = preprocessor.expand_contractions(cleaned)
    print("2. Expanded contractions:", repr(expanded))
    
    # Tokenize
    tokens = preprocessor.tokenize(expanded)
    print("3. Tokenized:", tokens[:15], "...")
    
    # Full preprocessing
    processed = preprocessor.preprocess(sample_text)
    print("4. Fully processed:", processed[:15], "...")
    print()
    
    # Analysis
    analysis = analyze_text(sample_text, preprocessor)
    print("Text Analysis:")
    print("-" * 15)
    for key, value in analysis.items():
        if key == 'most_common_words':
            print(f"{key}: {value[:5]}")  # Show top 5
        else:
            print(f"{key}: {value}")


if __name__ == "__main__":
    demo()