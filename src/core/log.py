from pydantic import BaseModel


class LogConfig(BaseModel):
    # Logging config
    version: int = 1
    disable_existing_loggersL: bool = True
    formatters: dict = {
        'default': {
            '()': 'uvicorn.logging.DefaultFormatter',
            'fmt': '%(levelprefix)s | %(asctime)s | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'use_colors': 'None',
        },
        'access': {
            '()': 'uvicorn.logging.AccessFormatter',
            'fmt': '%(levelprefix)s %(client_addr)s - \'%(request_line)s\' %(status_code)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'use_colors': 'None',
        },
    }
    handlers: dict = {
        'default': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
        'access': {
            'formatter': 'access',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
    }
    loggers: dict = {
        'app': {'handlers': ['default'], 'level': 'INFO', 'propagate': False},
        'app.fastapi': {'handlers': ['default'], 'level': 'DEBUG', 'propagate': False},
        'uvicorn': {
            'handlers': ['default'],
            'level': 'INFO',
        },
        'uvicorn.access': {
            'handlers': ['access'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'uvicorn.error': {
            'handlers': ['default'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
