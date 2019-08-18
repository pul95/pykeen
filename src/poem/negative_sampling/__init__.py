# -*- coding: utf-8 -*-

"""Negative sampling."""

from .base import NegativeSampler
from .basic_negative_sampler import BasicNegativeSampler
from .bern_negative_sampler import BernNegativeSampler

__all__ = [
    'NegativeSampler',
    'BasicNegativeSampler',
    'BernNegativeSampler',
]