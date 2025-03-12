# Empty file is fine - just marks 'app' as a package

# Define what should be available when someone does 'from app import *'
__all__ = ['main']

# You could also initialize important variables
VERSION = '1.0.0'

# Or import key functions to make them available at package level
from .main import predict

# Keep it empty for now
