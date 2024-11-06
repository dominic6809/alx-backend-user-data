#!/usr/bin/env python3
"""
Module for filtering sensitive information from log messages
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message obfuscated
    Args:
        fields: list of strings representing all fields to obfuscate
        redaction: string representing what the field will be obfuscated with
        message: string representing the log line
        separator: string representing separator between fields in the log line
    Returns:
        The obfuscated log message
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}', f'{field}={redaction}{separator}', message)
    return message
