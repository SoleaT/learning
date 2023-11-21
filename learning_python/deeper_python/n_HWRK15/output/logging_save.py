import logging

logging.basicConfig(filename='./output/log.log',
                    encoding='utf-8',
                    format='{name}: {asctime} {levelname} {funcName} -> {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
