# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    """Base configuration."""
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    DB_CONFIG = {

    }


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    DB_CONFIG = {

    }


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    DB_CONFIG = {

    }


class BetaConfig(Config):
    """Beta configuration."""

    ENV = 'beta'
    TESTING = True
    DEBUG = True
    DB_CONFIG = {

    }


class LocalConfig(Config):
    """Local configuration."""

    ENV = 'local'
    TESTING = True
    DEBUG = True
    DB_CONFIG = {
        'database': 'future'
    }


class TestConfig(Config):
    """Test configuration."""

    ENV = 'test'
    TESTING = True
    DEBUG = True
    DB_CONFIG = {

    }