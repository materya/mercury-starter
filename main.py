import configparser
import importlib
from distutils import util

config = configparser.ConfigParser()
config.read('config.cfg')
params = config['main']

import logging

log_levels = importlib.import_module('logging')
level = getattr(log_levels, params['logging'])
logging.basicConfig(
    level=level,
    format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

from mercury import Engine, Timeframe

def main():
    # Either use a strategy from mercury extras
    # strategies_module = importlib.import_module("mercury.extras.strategies")
    # Strategy = getattr(strategies_module, params['strategy'])

    # or use your own local strategy
    strategies = importlib.import_module('strategies')
    Strategy = getattr(strategies, params['strategy'])

    broker_module = importlib.import_module(
        f"mercury.extras.brokers.{params['broker']}"
    )
    Broker = getattr(broker_module, "Broker")
    broker_config = config[params['broker']]
    broker = Broker(is_paper=bool(util.strtobool(params['is_paper'])),
                    **broker_config)

    engine = Engine(broker=broker, strategy=Strategy)
    engine.start(instrument=broker_config['instrument'],
                 timeframe=Timeframe[params['timeframe']],
                 warmup=int(params['warmup']))

if __name__ == '__main__':
    main()
