#!/usr/bin/env python3
"""
Filters sensitive information from a log message by replacing specified fields with a redacted value.
This function uses regex substitution to perform the obfuscation.
"""

import re

def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str:
    """
    Replace sensitive fields in a log message with the redaction string.

    Args:
        fields (list[str]): List of fields to obfuscate.
        redaction (str): String used for obfuscation.
        message (str): Log message to be filtered.
        separator (str): Character that separates the fields in the log message.

    Returns:
        str: The log message with sensitive fields replaced by the redaction string.
    """
    return re.sub(r'(' + '|'.join([re.escape(field) for field in fields]) + r')=[^' + re.escape(separator) + r';]+', r'\1=' + redaction, message)
