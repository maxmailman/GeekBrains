import logging

logging.basicConfig(
    filename="app.log",
    format="%(levelname)-10s %(asctime)s %(message)s",
    level=logging.INFO
)

log = logging.getLogger('basic')

log.info('Recive message client')
