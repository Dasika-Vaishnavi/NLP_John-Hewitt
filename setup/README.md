# Environment Setup Guide

This guide will help you set up your development environment for COMS 4705 Natural Language Processing.

## Required Software

### 1. Python 3.8+
We recommend using Python 3.8 or later. You can download it from [python.org](https://www.python.org/downloads/).

**Check your Python version**:
```bash
python --version
# or
python3 --version
```

### 2. Package Manager
We recommend using `conda` (Anaconda/Miniconda) for environment management:
- [Anaconda](https://www.anaconda.com/products/distribution) (full distribution)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (minimal installer)

Alternatively, you can use `pip` with `venv`.

### 3. Git
Download and install Git from [git-scm.com](https://git-scm.com/).

## Environment Setup

### Option 1: Using Conda (Recommended)

1. **Create a new conda environment**:
```bash
conda create -n nlp-course python=3.9
conda activate nlp-course
```

2. **Install required packages**:
```bash
# PyTorch (choose appropriate version for your system)
conda install pytorch torchvision torchaudio -c pytorch

# Core NLP libraries
conda install -c conda-forge transformers datasets tokenizers
pip install torch-audio  # if needed for audio processing

# Traditional NLP tools
conda install -c conda-forge nltk spacy
python -m spacy download en_core_web_sm

# Scientific computing
conda install numpy pandas matplotlib seaborn scikit-learn

# Jupyter notebooks
conda install jupyter notebook

# Additional utilities
pip install wandb tqdm plotly ipywidgets
```

### Option 2: Using pip and venv

1. **Create virtual environment**:
```bash
python -m venv nlp-env
source nlp-env/bin/activate  # On Windows: nlp-env\Scripts\activate
```

2. **Install packages**:
```bash
pip install -r requirements.txt  # See requirements.txt below
```

## Required Python Packages

Create a `requirements.txt` file with these packages:

```txt
torch>=1.12.0
torchvision>=0.13.0
torchaudio>=0.12.0
transformers>=4.20.0
datasets>=2.3.0
tokenizers>=0.12.0
nltk>=3.7
spacy>=3.4.0
numpy>=1.21.0
pandas>=1.4.0
matplotlib>=3.5.0
seaborn>=0.11.0
scikit-learn>=1.1.0
jupyter>=1.0.0
notebook>=6.4.0
tqdm>=4.64.0
wandb>=0.12.0
plotly>=5.9.0
ipywidgets>=7.7.0
```

## Additional Setup

### 1. Download NLTK Data
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('vader_lexicon')
```

### 2. Download spaCy Model
```bash
python -m spacy download en_core_web_sm
```

### 3. Hugging Face Setup (Optional)
For accessing private models or datasets:
```bash
pip install huggingface_hub
huggingface-cli login
```

### 4. Weights & Biases Setup (Optional)
For experiment tracking:
```bash
wandb login
```

## Testing Your Setup

Run this test script to verify your installation:

```python
# test_setup.py
import sys
print(f"Python version: {sys.version}")

# Test PyTorch
try:
    import torch
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
except ImportError:
    print("❌ PyTorch not installed")

# Test Transformers
try:
    import transformers
    print(f"Transformers version: {transformers.__version__}")
    from transformers import pipeline
    classifier = pipeline("sentiment-analysis")
    result = classifier("I love this course!")
    print(f"Sentiment test: {result}")
except ImportError:
    print("❌ Transformers not installed")

# Test NLTK
try:
    import nltk
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize("Hello world!")
    print(f"NLTK tokenization test: {tokens}")
except ImportError:
    print("❌ NLTK not installed")

# Test spaCy
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Hello world!")
    print(f"spaCy test: {[(token.text, token.pos_) for token in doc]}")
except ImportError:
    print("❌ spaCy not installed")

print("✅ Setup test complete!")
```

## Development Environment

### Recommended IDEs
- **Jupyter Notebooks**: Great for exploratory work and assignments
- **VS Code**: Excellent Python support with extensions
- **PyCharm**: Full-featured Python IDE
- **Google Colab**: Cloud-based Jupyter with free GPU access

### VS Code Extensions (Recommended)
- Python
- Jupyter
- Python Docstring Generator
- GitLens
- Bracket Pair Colorizer

## GPU Setup (Optional but Recommended)

### Local GPU (NVIDIA)
If you have an NVIDIA GPU:
```bash
# Check CUDA version
nvidia-smi

# Install CUDA-compatible PyTorch
# Visit https://pytorch.org/get-started/locally/ for specific commands
```

### Cloud Options
- **Google Colab**: Free GPU access, great for assignments
- **Kaggle Kernels**: Free GPU/TPU access
- **AWS SageMaker**: Professional cloud environment
- **Google Cloud Platform**: Educational credits available

## Common Issues and Solutions

### Issue: "Command not found"
**Solution**: Make sure your environment is activated and the package is installed in the correct environment.

### Issue: CUDA out of memory
**Solutions**:
- Reduce batch size
- Use gradient checkpointing
- Clear cache: `torch.cuda.empty_cache()`

### Issue: SSL Certificate errors
**Solution**: 
```bash
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package>
```

### Issue: spaCy model not found
**Solution**: 
```bash
python -m spacy download en_core_web_sm
```

## Getting Help

1. **First**: Check this setup guide and common issues
2. **Course Forum**: Post technical questions on the discussion board
3. **Office Hours**: Bring specific error messages and code
4. **Email TA**: For urgent setup issues preventing assignment progress

## Verification Checklist

Before starting assignments, ensure you can:
- [ ] Run Python 3.8+ in your environment
- [ ] Import torch, transformers, nltk, spacy
- [ ] Load a pre-trained model from Hugging Face
- [ ] Run Jupyter notebooks
- [ ] Use Git for version control
- [ ] Access and run the provided test script successfully

---
*Need help? Contact the course staff or post on the discussion forum!*