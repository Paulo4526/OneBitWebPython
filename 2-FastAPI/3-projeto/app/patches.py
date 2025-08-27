"""
Patches para compatibilidade com Python 3.13
"""
import sys
from collections.abc import MutableMapping

# Adiciona MutableMapping ao módulo collections para compatibilidade
import collections
collections.MutableMapping = MutableMapping

