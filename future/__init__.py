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

from future.school.api import bp_v1 as school_bp_v1
from future.utils.protocol import JSONHttpProtocol

__all__ = ['CONFIG', 'app', 'school_bp_v1', 'JSONHttpProtocol']
