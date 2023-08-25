"""default main file"""
import logging

logging.basicConfig(
    level=logging.INFO, format='%(filename)s:%(lineno)d %(asctime)s %(levelname)s: %(message)s',
)

logging.info("Started application...")

logging.info("Done.")
