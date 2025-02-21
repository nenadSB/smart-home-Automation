import logging

class ProtocolHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def handle_message(self, message):
        self.logger.info(f"Handling message: {message}")