import logging

from adapter import CustomAdapter

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(message)s - %(test_key)s - %(pass_through_key)s')
ch.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(ch)

adapter = CustomAdapter(
    logger,
    {
        'adapter_key': 'adapter prepends this',
        'pass_through_key': 'pass through from adapter',
        'test_key': 'overridden extra from adapter'
    },
)
adapter.setLevel(logging.DEBUG)

adapter.info(
    'this is the main log message',
    extra={'test_key': 'extra from logger call'},
)
logger.info(
    'this is the log message that bypasses the adapter',
    extra={
        'test_key': 'extra from logger call',
        'pass_through_key': 'logging formatter crashes without this key, so we have to provide it in the log extras since we are bypassing the adapter',
    },
)
