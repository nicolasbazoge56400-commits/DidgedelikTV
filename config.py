# Configuration Settings for DidgedelikTV

# Model Paths
MODEL_PATH = '/path/to/model'
PRETRAINED_MODEL_PATH = '/path/to/pretrained/model'

# CUDA Device Settings
CUDA_DEVICE = 'cuda:0'  # Use GPU 0

# RAG Parameters
RAG_PARAMS = {
    'num_beams': 5,
    'top_k': 50,
    'top_p': 0.95,
}

# Training Hyperparameters
TRAINING_HYPERPARAMS = {
    'learning_rate': 5e-5,
    'batch_size': 32,
    'num_epochs': 10,
    'weight_decay': 0.01,
}