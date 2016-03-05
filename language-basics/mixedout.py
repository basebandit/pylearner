#!/usr/bin/env python
"""Mixed output in stdout and stderr."""

import sys
print >>sys.stderr, "This is an error message"
print "This is stdout"
print >>sys.stdout, "This is also stdout"
