import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def hello():
    logger.info("Hello from DevOps Week 02 app")

if __name__ == "__main__":
    hello()
