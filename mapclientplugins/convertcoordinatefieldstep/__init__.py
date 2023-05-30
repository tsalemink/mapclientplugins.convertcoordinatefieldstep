
"""
MAP Client Plugin - Generated from MAP Client v0.17.2
"""

__version__ = '0.2.0'
__author__ = 'Hugh Sorby'
__stepname__ = 'Convert Coordinate Field'
__location__ = ''

# import class that derives itself from the step mountpoint.
from mapclientplugins.convertcoordinatefieldstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc