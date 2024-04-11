import logging
import logging.config

import boto3
import watchtower

from src.core.log import LogConfig

APP_LOGGER = logging.getLogger('app')


def make_logger(region_name: str):
    logging.config.dictConfig(LogConfig().dict())
    logger = logging.getLogger('app')

    handler = watchtower.CloudWatchLogHandler(
        boto3_client=boto3.client('logs', region_name=region_name), log_group_name='app'
    )
    logger.addHandler(handler)

    return logger


def log_info(request, response):
    logger = logging.getLogger('app.fastapi')
    logger.info(f'{request.method} {request.url}')
    if request.method == 'POST':
        logger.info(f'Request Body: {request._json}')
    if response.body:
        logger.info('Response: ' + response.body.decode('utf8').replace('\"', '\'').replace(':', ': '))
