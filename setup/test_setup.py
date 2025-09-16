#!/usr/bin/env python3
"""
Setup verification script for COMS 4705 Natural Language Processing
Run this script to verify your environment is properly configured.
"""

import sys
import subprocess
import importlib

def check_package(package_name, min_version=None):
    """Check if a package is installed and optionally verify minimum version."""
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"✅ {package_name}: {version}")
        return True
    except ImportError:
        print(f"❌ {package_name}: Not installed")
        return False

def test_functionality():
    """Test core functionality of installed packages."""
    print("\n" + "="*50)
    print("FUNCTIONALITY TESTS")
    print("="*50)
    
    # Test PyTorch
    try:
        import torch
        print(f"PyTorch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"CUDA version: {torch.version.cuda}")
            print(f"GPU devices: {torch.cuda.device_count()}")
        
        # Simple tensor operation
        x = torch.randn(3, 4)
        y = torch.randn(4, 5)
        z = torch.mm(x, y)
        print(f"✅ PyTorch tensor operations working")
    except Exception as e:
        print(f"❌ PyTorch test failed: {e}")

    # Test Transformers
    try:
        from transformers import pipeline
        classifier = pipeline("sentiment-analysis", 
                            model="distilbert-base-uncased-finetuned-sst-2-english")
        result = classifier("I love this NLP course!")
        print(f"✅ Transformers sentiment analysis: {result[0]['label']}")
    except Exception as e:
        print(f"❌ Transformers test failed: {e}")

    # Test NLTK
    try:
        import nltk
        from nltk.tokenize import word_tokenize
        from nltk.corpus import stopwords
        
        # Download required data if not present
        nltk_downloads = ['punkt', 'stopwords']
        for item in nltk_downloads:
            try:
                nltk.data.find(f'tokenizers/{item}')
            except LookupError:
                print(f"Downloading NLTK {item}...")
                nltk.download(item, quiet=True)
        
        tokens = word_tokenize("Natural Language Processing is fascinating!")
        print(f"✅ NLTK tokenization: {tokens[:5]}...")
    except Exception as e:
        print(f"❌ NLTK test failed: {e}")

    # Test spaCy
    try:
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp("Natural Language Processing at Columbia University")
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        print(f"✅ spaCy NER: {entities}")
    except OSError:
        print("❌ spaCy model 'en_core_web_sm' not found. Run: python -m spacy download en_core_web_sm")
    except Exception as e:
        print(f"❌ spaCy test failed: {e}")

    # Test Jupyter
    try:
        import jupyter
        import notebook
        print(f"✅ Jupyter/Notebook ready for assignments")
    except Exception as e:
        print(f"❌ Jupyter test failed: {e}")

def main():
    print("COMS 4705 Natural Language Processing")
    print("Environment Setup Verification")
    print("="*50)
    print(f"Python version: {sys.version}")
    print("="*50)
    print("PACKAGE INSTALLATION CHECK")
    print("="*50)
    
    # Core packages
    required_packages = [
        'torch', 'transformers', 'datasets', 'tokenizers',
        'nltk', 'spacy', 'numpy', 'pandas', 
        'matplotlib', 'seaborn', 'sklearn',
        'jupyter', 'notebook', 'tqdm'
    ]
    
    optional_packages = ['wandb', 'plotly']
    
    all_good = True
    
    print("Required packages:")
    for package in required_packages:
        if not check_package(package):
            all_good = False
    
    print("\nOptional packages:")
    for package in optional_packages:
        check_package(package)
    
    # Run functionality tests
    test_functionality()
    
    print("\n" + "="*50)
    print("SETUP SUMMARY")
    print("="*50)
    
    if all_good:
        print("🎉 All required packages are installed!")
        print("You're ready to start the course assignments.")
    else:
        print("⚠️  Some required packages are missing.")
        print("Please install missing packages using:")
        print("  conda install <package>  or  pip install <package>")
    
    print("\nNext steps:")
    print("1. Clone the course repository")
    print("2. Review the syllabus and schedule")
    print("3. Complete Assignment 1 when released")
    print("4. Join the course discussion forum")

if __name__ == "__main__":
    main()