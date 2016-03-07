#!/usr/bin/env python
"""Mixed output in stdout and stderr."""

import sys
print >>sys.stderr, "This is an error message"
print "This is stdout"
print >>sys.stdout, "This is also stdout"

# Floating numbers
# Python offers floating-point numbers, often implemented as
# double-precision numbers, typically using 64
# bits. Floating - point numbers are written in two forms:
# a simple string of digits that includes a decimal
# and a more complex form that includes an explicit exponent.

print 1. / 5.  # 0.20000000000000001
print .2  # 0.20000000000000001

# Complex numbers

print (2 + 3j) * (4 + 5j)
print 3 + 2j.conjugate()

# Number conversions(Factory) Functions


# int(x) Generates an integer from the object x.

print int("1243")
print int(3.14159)

# float(x) Generates a float from object x.

print float(23)
print float("6.02E24")

# long(x) Generates a long integer from x.

print long(2)
print long(6.02E23)
print long(2)**64

# complex(real,/imag/) Generates a complex number from real and imag. If
# the imaginary part is omitted, it is 0.0.

print complex(3, 2)
print complex(4)
print complex("3+4j")

# Built in math Functions

print round(678.456, 2)
print round(678.456, -1)
print abs(4058)
print pow(2, 4)

# String Conversion(or Factory) Functions
# The string conversion functions provide alternate representations for
# numeric values.
print hex(684)
print oct(509)
print bin(509)

# The int(x,b) form converts a string, x, in base b to an integer.
print int('0775', 8)
print int('0x2ac', 16)
print int('101101101101', 2)

# The str() and repr() functions convert any Python object to a string. The str() version is typically
# more readable, where the repr() version is an internalized representation.
print str(40.5)
print str(300)

print repr("am a string")
print repr(2043)
