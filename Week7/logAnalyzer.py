import logging

logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - %(levelname)s - %(message)s',
handlers=[
logging.FileHandler('analysis_audit.log'),
logging.StreamHandler()
]
)