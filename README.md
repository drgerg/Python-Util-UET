# Python-Util-UET
Casspop Codelette: A short, useful, educational Python Unix Epoch Time utility.

This is what I'm calling a codelette.  It's a little bit of code that does something, but has some value beyond that for learners like me.  (I don't know about you, but I'm always learning.  Always.)

"et.py" stands for EpochTime.py, and is a command line utility that will do one of two things immediately:
 - it will give you a UET value if you don't provide any command line arguments
 - it will show you the local and GMT human-readable time for any UET value you provide on the command line

There is nothing awe-inspiring about this codelette, but there is a lot that can be learned from it.
For example, in this tiny file, you'll find working examples of:
- logging
- command line arguments parsing
- use of the time module to get the current time
- formatting time strings for human consumption
- setting Python files up so they can be either imported or run as a standalone program
  - this involves use of <code>'if \__name__ == "\__main__":'</code>, which is a really helpful thing to understand.
  - this also involves then defining a function using <code> def </code> and calling that function after the aforementioned 'if'.

import time,os,logging,argparse,traceback,signal,sys