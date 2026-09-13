import logging

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        handler = logging.FileHandler('logs/logger.log')
        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s] : %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    logger.setLevel(logging.INFO)
    
    return logger
        
        
    