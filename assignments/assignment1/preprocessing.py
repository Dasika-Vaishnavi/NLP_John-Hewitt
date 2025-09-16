"""
COMS 4705 - Assignment 1: Text Preprocessing
Student: [Your Name]
UNI: [Your UNI]

This module contains functions for text preprocessing including
tokenization, normalization, and vocabulary management.
"""

import re
import string
from collections import Counter
from typing import List, Dict


def tokenize_text(text: str) -> List[str]:
    """
    Tokenize text into words, handling punctuation appropriately.
    
    Args:
        text (str): Input text
    
    Returns:
        list: List of tokens
    
    Example:
        >>> tokenize_text("Hello, world! How are you?")
        ['Hello', ',', 'world', '!', 'How', 'are', 'you', '?']
    """
    # TODO: Implement tokenization
    # Hint: Consider using regular expressions or string methods
    # Handle punctuation as separate tokens
    pass


def normalize_text(text: str) -> str:
    """
    Normalize text by converting to lowercase and handling contractions.
    
    Args:
        text (str): Input text
    
    Returns:
        str: Normalized text
    
    Example:
        >>> normalize_text("I can't believe it's working!")
        "i cannot believe it is working!"
    """
    # TODO: Implement normalization
    # Convert to lowercase
    # Expand contractions (can't -> cannot, it's -> it is, etc.)
    pass


def remove_rare_words(tokens: List[str], min_count: int = 2) -> List[str]:
    """
    Replace words occurring fewer than min_count times with <UNK>.
    
    Args:
        tokens (list): List of tokens
        min_count (int): Minimum frequency threshold
    
    Returns:
        list: Tokens with rare words replaced by <UNK>
    
    Example:
        >>> tokens = ['the', 'cat', 'sat', 'on', 'mat', 'cat', 'ran']
        >>> remove_rare_words(tokens, min_count=2)
        ['<UNK>', 'cat', '<UNK>', '<UNK>', '<UNK>', 'cat', '<UNK>']
    """
    # TODO: Implement rare word removal
    # Count word frequencies
    # Replace words below threshold with <UNK>
    pass


def add_sentence_markers(tokens: List[str]) -> List[str]:
    """
    Add sentence start and end markers to token list.
    
    Args:
        tokens (list): List of tokens
    
    Returns:
        list: Tokens with <s> and </s> markers
    
    Example:
        >>> add_sentence_markers(['Hello', 'world'])
        ['<s>', 'Hello', 'world', '</s>']
    """
    # TODO: Implement sentence marker addition
    # Add <s> at the beginning and </s> at the end
    pass


def get_ngrams(tokens: List[str], n: int) -> List[tuple]:
    """
    Extract n-grams from a list of tokens.
    
    Args:
        tokens (list): List of tokens
        n (int): Size of n-grams
    
    Returns:
        list: List of n-gram tuples
    
    Example:
        >>> get_ngrams(['<s>', 'hello', 'world', '</s>'], 2)
        [('<s>', 'hello'), ('hello', 'world'), ('world', '</s>')]
    """
    # TODO: Implement n-gram extraction
    # Use sliding window of size n over tokens
    pass


def calculate_vocabulary_stats(tokens: List[str]) -> Dict[str, int]:
    """
    Calculate vocabulary statistics for a token list.
    
    Args:
        tokens (list): List of tokens
    
    Returns:
        dict: Statistics including total_tokens, unique_tokens, etc.
    """
    # TODO: Implement vocabulary statistics calculation
    # Return dictionary with useful statistics
    pass


if __name__ == "__main__":
    # Test your functions here
    sample_text = "Hello, world! This is a test. Can't wait to see the results!"
    
    print("Original text:", sample_text)
    
    # Test tokenization
    tokens = tokenize_text(sample_text)
    print("Tokens:", tokens)
    
    # Test normalization
    normalized = normalize_text(sample_text)
    print("Normalized:", normalized)
    
    # Add more tests as needed