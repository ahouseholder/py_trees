#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/yujinrobot/gopher_crazy_hospital/license/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
.. module:: common
   :platform: Unix
   :synopsis: Common variables and methods used by all elements in py_trees.

----

"""

##############################################################################
# Imports
##############################################################################

from enum import Enum
##############################################################################
# Status
##############################################################################

# """ An enumerator representing the status of a behaviour """
# Status = Enum('Status', 'SUCCESS FAILURE RUNNING INVALID')


class Status(Enum):
    """ An enumerator representing the status of a behaviour """

    """Behaviour reports success."""
    SUCCESS = "SUCCESS"
    """Behaviour, or condition check failed."""
    FAILURE = "FAILURE"
    """Behaviour is executing"""
    RUNNING = "RUNNING"
    """Behaviour is in an invalid state"""
    INVALID = "INVALID"

