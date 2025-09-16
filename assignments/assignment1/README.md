# Assignment 1: Language Models and Text Preprocessing

**Due Date**: September 20, 2024, 11:59 PM ET  
**Points**: 100 points  
**Topics**: N-gram models, text preprocessing, language model evaluation

## Overview

In this assignment, you will implement core components of statistical language models and explore text preprocessing techniques. You'll work with real text data to build n-gram models and evaluate their performance.

## Learning Objectives

By completing this assignment, you will:
- Understand and implement text preprocessing pipelines
- Build n-gram language models from scratch
- Apply smoothing techniques to handle unseen events
- Evaluate language models using perplexity
- Compare different model configurations

## Setup

1. Clone this repository and navigate to the assignment1 directory
2. Install required packages: `pip install -r requirements.txt`
3. Download the provided datasets (instructions below)

## Part 1: Text Preprocessing (25 points)

### Task 1.1: Basic Preprocessing (10 points)

Implement the following preprocessing functions in `preprocessing.py`:

```python
def tokenize_text(text):
    """
    Tokenize text into words, handling punctuation appropriately.
    
    Args:
        text (str): Input text
    
    Returns:
        list: List of tokens
    """
    # TODO: Implement tokenization
    pass

def normalize_text(text):
    """
    Normalize text by converting to lowercase and handling contractions.
    
    Args:
        text (str): Input text
    
    Returns:
        str: Normalized text
    """
    # TODO: Implement normalization
    pass

def remove_rare_words(tokens, min_count=2):
    """
    Replace words occurring fewer than min_count times with <UNK>.
    
    Args:
        tokens (list): List of tokens
        min_count (int): Minimum frequency threshold
    
    Returns:
        list: Tokens with rare words replaced
    """
    # TODO: Implement rare word removal
    pass
```

### Task 1.2: Corpus Statistics (15 points)

Analyze the provided corpus and report:
- Total number of tokens
- Vocabulary size (unique words)
- Most frequent words (top 20)
- Distribution of word frequencies (plot)

## Part 2: N-gram Language Models (50 points)

### Task 2.1: N-gram Model Implementation (30 points)

Implement a class for n-gram language models in `language_model.py`:

```python
class NGramLanguageModel:
    def __init__(self, n):
        """
        Initialize n-gram language model.
        
        Args:
            n (int): Order of the n-gram model
        """
        self.n = n
        self.ngram_counts = {}
        self.context_counts = {}
    
    def train(self, tokens):
        """
        Train the language model on tokenized text.
        
        Args:
            tokens (list): List of tokens
        """
        # TODO: Implement training
        pass
    
    def probability(self, word, context):
        """
        Calculate P(word | context) using maximum likelihood estimation.
        
        Args:
            word (str): Target word
            context (tuple): Context (n-1 words)
        
        Returns:
            float: Probability of word given context
        """
        # TODO: Implement probability calculation
        pass
    
    def generate_text(self, seed_text, length=20):
        """
        Generate text using the trained model.
        
        Args:
            seed_text (str): Initial text to start generation
            length (int): Number of words to generate
        
        Returns:
            str: Generated text
        """
        # TODO: Implement text generation
        pass
```

### Task 2.2: Smoothing Techniques (20 points)

Implement two smoothing methods:
1. **Add-one (Laplace) smoothing**
2. **Add-alpha smoothing** with tunable parameter

Compare their effects on model performance.

## Part 3: Model Evaluation (25 points)

### Task 3.1: Perplexity Calculation (15 points)

Implement perplexity evaluation:

```python
def calculate_perplexity(model, test_tokens):
    """
    Calculate perplexity of the model on test data.
    
    Args:
        model: Trained language model
        test_tokens (list): Test tokens
    
    Returns:
        float: Perplexity score
    """
    # TODO: Implement perplexity calculation
    pass
```

### Task 3.2: Model Comparison (10 points)

Compare different model configurations:
- Unigram vs. bigram vs. trigram models
- Effect of different smoothing parameters
- Performance on different text genres

Create visualizations showing the trade-offs.

## Datasets

Use the provided datasets:
1. **Training corpus**: `data/train.txt` (news articles)
2. **Validation corpus**: `data/valid.txt` (news articles)
3. **Test corpus**: `data/test.txt` (news articles)

Download using:
```bash
python download_data.py
```

## Deliverables

Submit the following files:
1. `preprocessing.py` - Text preprocessing functions
2. `language_model.py` - N-gram language model implementation
3. `evaluation.py` - Model evaluation code
4. `assignment1.ipynb` - Jupyter notebook with analysis and results
5. `report.pdf` - Written report (max 4 pages)

### Report Requirements

Your report should include:
1. **Introduction**: Brief overview of the assignment goals
2. **Methods**: Description of your implementation choices
3. **Results**: Performance comparison and analysis
4. **Discussion**: Insights and observations from experiments
5. **References**: Any external sources used

## Grading Rubric

| Component | Points | Criteria |
|-----------|---------|----------|
| Part 1: Preprocessing | 25 | Correct implementation, code quality |
| Part 2: N-gram Models | 50 | Correct implementation, smoothing |
| Part 3: Evaluation | 25 | Correct perplexity, thorough analysis |
| **Total** | **100** | |

### Extra Credit (5 points)

Implement and evaluate an additional smoothing technique:
- Good-Turing smoothing
- Kneser-Ney smoothing
- Interpolation between different n-gram orders

## Tips

- Start early and test your code incrementally
- Use assert statements to verify your implementations
- Visualize your results to gain insights
- Consider edge cases (empty contexts, unknown words)
- Follow Python coding best practices

## Common Pitfalls

- Forgetting to handle beginning/end of sentence markers
- Off-by-one errors in n-gram extraction
- Incorrect probability normalization
- Not handling unseen words in test data

## Help and Resources

- Office hours: [See course schedule]
- Discussion forum: [CourseWorks link]
- Relevant textbook sections: Jurafsky & Martin Ch. 3
- Python documentation for collections.Counter

---
**Academic Integrity Reminder**: This is an individual assignment. While you may discuss concepts with classmates, all code and analysis must be your own work.