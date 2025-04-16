import torch
import logging

logger = logging.getLogger(__name__)

class ModelManager:
    _model = None
    _tokenizer = None
    _device = None
    
    @classmethod
    def determine_device(cls):
        if torch.cuda.is_available():
            device = "cuda"
        elif torch.backends.mps.is_available():
            device = "mps"
        else:
            device = "cpu"
        return device
    
    @classmethod
    def load_model(cls, model_name: str):
        if cls._model is None:
            logger.info(f"Loading model: {model_name}")
            from transformers import AutoModel, AutoTokenizer
            
            if cls._device is None:
                cls._device = cls.determine_device()
                
            cls._tokenizer = AutoTokenizer.from_pretrained(model_name, do_lower_case=True)
            cls._model = AutoModel.from_pretrained(model_name).to(cls._device)
            logger.info(f"Model {model_name} loaded on {cls._device}.")
        return cls._model, cls._tokenizer, cls._device
    
    @classmethod
    def get_model(cls):
        return (cls._model, cls._tokenizer, cls._device) if cls._model else None

if __name__ == "__main__":
    import argparse
    logging.basicConfig(level=logging.WARNING)
    logger.setLevel(logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, help="Embedding model name or path")
    args = parser.parse_args()
    ModelManager.load_model(args.model_name)