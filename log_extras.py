import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(test_key)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

logger.info('this is the log message', extra={'test_key': 'test_value'})
