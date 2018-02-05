#!/usr/bin/env python
# -*-coding:utf-8-*-
import unittest
import os
def all():
	suite=unittest.TestLoader().discover(
	start_dir=os.path.join(os.path.dirname(__file__),'testCase'),
	pattern='test_*.py',
	top_level_dir=None
	)
	unittest.TextTestRunner(verbosity=2).run(suite)
all()