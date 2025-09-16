"""
COMS 4705 - Assignment 1: N-gram Language Models
Student: [Your Name]
UNI: [Your UNI]

This module implements n-gram language models with various smoothing techniques.
"""

import math
import random
from collections import defaultdict, Counter
from typing import List, Tuple, Dict
from preprocessing import get_ngrams


class NGramLanguageModel:
    """
    N-gram language model with support for different smoothing techniques.
    """
    
    def __init__(self, n: int, smoothing: str = "none", alpha: float = 1.0):
        """
        Initialize n-gram language model.
        
        Args:
            n (int): Order of the n-gram model (1=unigram, 2=bigram, etc.)
            smoothing (str): Smoothing technique ("none", "laplace", "add_alpha")
            alpha (float): Smoothing parameter for add-alpha smoothing
        """
        self.n = n
        self.smoothing = smoothing
        self.alpha = alpha
        
        # Dictionaries to store counts
        self.ngram_counts = defaultdict(int)  # n-gram counts: (context, word) -> count
        self.context_counts = defaultdict(int)  # context counts: context -> count
        self.vocabulary = set()  # all unique words seen during training
        
    def train(self, tokens: List[str]) -> None:
        """
        Train the language model on tokenized text.
        
        Args:
            tokens (list): List of tokens including sentence markers
        """
        # TODO: Implement training
        # Extract n-grams from tokens
        # Count n-grams and contexts
        # Build vocabulary
        pass
    
    def _get_context_and_word(self, ngram: Tuple[str, ...]) -> Tuple[Tuple[str, ...], str]:
        """
        Split n-gram into context and target word.
        
        Args:
            ngram: N-gram tuple
            
        Returns:
            tuple: (context, word) where context has n-1 words
        """
        # TODO: Implement context/word splitting
        pass
    
    def probability(self, word: str, context: Tuple[str, ...]) -> float:
        """
        Calculate P(word | context) using the specified smoothing.
        
        Args:
            word (str): Target word
            context (tuple): Context (n-1 words)
        
        Returns:
            float: Probability of word given context
        """
        # TODO: Implement probability calculation with smoothing
        if self.smoothing == "none":
            return self._probability_mle(word, context)
        elif self.smoothing == "laplace":
            return self._probability_laplace(word, context)
        elif self.smoothing == "add_alpha":
            return self._probability_add_alpha(word, context)
        else:
            raise ValueError(f"Unknown smoothing method: {self.smoothing}")
    
    def _probability_mle(self, word: str, context: Tuple[str, ...]) -> float:
        """Maximum likelihood estimation (no smoothing)."""
        # TODO: Implement MLE probability
        pass
    
    def _probability_laplace(self, word: str, context: Tuple[str, ...]) -> float:
        """Add-one (Laplace) smoothing."""
        # TODO: Implement Laplace smoothing
        pass
    
    def _probability_add_alpha(self, word: str, context: Tuple[str, ...]) -> float:
        """Add-alpha smoothing."""
        # TODO: Implement add-alpha smoothing
        pass
    
    def generate_text(self, seed_text: str, length: int = 20) -> str:
        """
        Generate text using the trained model.
        
        Args:
            seed_text (str): Initial text to start generation
            length (int): Number of words to generate
        
        Returns:
            str: Generated text
        """
        # TODO: Implement text generation
        # Start with seed text
        # Repeatedly sample next word based on context
        # Return generated sequence
        pass
    
    def _sample_next_word(self, context: Tuple[str, ...]) -> str:
        """
        Sample next word given context based on model probabilities.
        
        Args:
            context: Context tuple
            
        Returns:
            str: Sampled word
        """
        # TODO: Implement word sampling
        # Calculate probabilities for all possible next words
        # Sample according to these probabilities
        pass


class UnigramModel(NGramLanguageModel):
    """Unigram language model (for comparison)."""
    
    def __init__(self, smoothing: str = "none", alpha: float = 1.0):
        super().__init__(n=1, smoothing=smoothing, alpha=alpha)


class BigramModel(NGramLanguageModel):
    """Bigram language model."""
    
    def __init__(self, smoothing: str = "none", alpha: float = 1.0):
        super().__init__(n=2, smoothing=smoothing, alpha=alpha)


class TrigramModel(NGramLanguageModel):
    """Trigram language model."""
    
    def __init__(self, smoothing: str = "none", alpha: float = 1.0):
        super().__init__(n=3, smoothing=smoothing, alpha=alpha)


if __name__ == "__main__":
    # Test your model here
    from preprocessing import tokenize_text, add_sentence_markers
    
    # Sample text for testing
    sample_text = "the cat sat on the mat. the cat ran quickly."
    tokens = tokenize_text(sample_text.lower())
    tokens = add_sentence_markers(tokens)
    
    print("Tokens:", tokens)
    
    # Test bigram model
    model = BigramModel(smoothing="laplace")
    model.train(tokens)
    
    # Test probability calculation
    context = ("the",)
    word = "cat"
    prob = model.probability(word, context)
    print(f"P({word} | {context}) = {prob}")
    
    # Test text generation
    generated = model.generate_text("the", length=10)
    print("Generated text:", generated)