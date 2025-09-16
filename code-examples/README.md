# Code Examples - COMS 4705 NLP

This directory contains code examples, tutorials, and implementation guides to help you understand and implement NLP concepts covered in class.

## Directory Structure

### `basic-nlp/`
Fundamental NLP operations and classical methods:
- Text preprocessing and tokenization
- N-gram language models  
- Part-of-speech tagging
- Named entity recognition
- Basic sentiment analysis

### `neural-models/`
Neural network approaches to NLP:
- Word embeddings (Word2Vec, GloVe)
- Recurrent neural networks (RNNs, LSTMs)
- Sequence-to-sequence models
- Attention mechanisms

### `transformers/`
Modern transformer-based models:
- BERT fine-tuning examples
- GPT text generation
- T5 text-to-text transfer
- Hugging Face integration

### `utils/`
Utility functions and helper code:
- Data loading and preprocessing
- Evaluation metrics
- Visualization tools
- Common patterns and templates

## How to Use These Examples

### Prerequisites
1. Complete the environment setup (see `setup/README.md`)
2. Install required packages: `pip install -r setup/requirements.txt`
3. Download any required data (instructions in each example)

### Running Examples
Each directory contains:
- **README.md**: Overview and instructions
- **Jupyter notebooks**: Interactive tutorials
- **Python scripts**: Standalone implementations
- **requirements.txt**: Additional dependencies (if any)

### Learning Path
1. Start with `basic-nlp/` to understand fundamentals
2. Progress to `neural-models/` for deep learning approaches
3. Explore `transformers/` for state-of-the-art methods
4. Use `utils/` for helper functions in your projects

## Examples by Topic

### Text Preprocessing
- `basic-nlp/tokenization.ipynb`: Tokenization techniques
- `basic-nlp/normalization.py`: Text normalization
- `utils/preprocessing.py`: Common preprocessing utilities

### Language Models
- `basic-nlp/ngram_lm.ipynb`: N-gram language models
- `neural-models/neural_lm.ipynb`: Neural language models
- `transformers/gpt_generation.ipynb`: GPT text generation

### Classification
- `basic-nlp/sentiment_analysis.ipynb`: Rule-based and ML approaches
- `neural-models/text_classification.ipynb`: Neural classifiers
- `transformers/bert_classification.ipynb`: BERT fine-tuning

### Sequence Labeling
- `basic-nlp/pos_tagging.ipynb`: HMM POS tagging
- `neural-models/sequence_labeling.ipynb`: LSTM sequence labeling
- `transformers/token_classification.ipynb`: BERT for NER

### Machine Translation
- `neural-models/seq2seq_translation.ipynb`: Sequence-to-sequence models
- `transformers/machine_translation.ipynb`: Transformer translation

## Code Style and Standards

### Python Conventions
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Include docstrings for all functions
- Use meaningful variable and function names

### Documentation
- Each example includes extensive comments
- Jupyter notebooks have markdown explanations
- README files explain the purpose and usage

### Dependencies
- Minimize external dependencies
- Use standard libraries when possible
- Clearly document any special requirements

## Contributing

### For Students
- Report bugs or unclear examples via course forum
- Suggest improvements or additional examples
- Share your own implementations (with proper attribution)

### Guidelines
- Test all code before submitting
- Include clear documentation
- Follow existing code style
- Add appropriate error handling

## Getting Help

### Debugging Code
1. Check that your environment is set up correctly
2. Ensure all dependencies are installed
3. Read error messages carefully
4. Use print statements or debugger to trace issues

### Understanding Concepts
1. Read the accompanying explanations and comments
2. Experiment with different parameters
3. Compare with textbook explanations
4. Ask questions during office hours

### Performance Issues
1. Start with small datasets for testing
2. Use appropriate hardware (GPU when available)
3. Consider batch processing for large datasets
4. Monitor memory usage

## Best Practices

### Development Workflow
1. Start with provided examples
2. Modify and experiment with parameters
3. Apply to your own datasets
4. Extend for assignment requirements

### Learning Tips
1. Run examples step by step
2. Change parameters to see effects
3. Visualize intermediate results
4. Compare different approaches

### Project Integration
1. Use examples as starting points
2. Adapt code for your specific needs
3. Combine multiple techniques
4. Cite any code you adapt or extend

## External Resources

### Additional Code Examples
- [Hugging Face Transformers Examples](https://github.com/huggingface/transformers/tree/main/examples)
- [PyTorch NLP Examples](https://github.com/pytorch/examples/tree/main/nlp)
- [AllenNLP Tutorials](https://github.com/allenai/allennlp/tree/main/tutorials)

### Related Courses
- [Stanford CS224N Code](https://github.com/stanfordnlp/cs224n-winter-2023)
- [Fast.ai NLP Course](https://github.com/fastai/course-nlp)
- [Hugging Face Course](https://github.com/huggingface/course)

---

**Happy coding!** Remember, the best way to learn NLP is by implementing and experimenting with the algorithms yourself.