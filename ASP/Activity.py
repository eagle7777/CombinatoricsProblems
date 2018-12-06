#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/6/18


class Activity:
    def __init__(self, s, f):
        self.start = s
        self.finish = f

    @staticmethod
    def is_compatible(act1, act2):
        return act1.start >= act2.finish or act2.start >= act1.finish


