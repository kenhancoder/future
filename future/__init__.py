# -*- coding: utf-8 -*-
"""Main application package."""

import os

from future.application import create_app

from future.configs import DevConfig, ProdConfig, BetaConfig, LocalConfig

if os.environ.get('RUNTIME_ENV') == 'prod':
    CONFIG = ProdConfig
elif os.environ.get('RUNTIME_ENV') == 'dev':
    CONFIG = DevConfig
elif os.environ.get('RUNTIME_ENV') == 'beta':
    CONFIG = BetaConfig
else:
    CONFIG = LocalConfig

app = create_app()

__all__ = ['CONFIG', 'app']
