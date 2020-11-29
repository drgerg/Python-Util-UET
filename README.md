# Python-Util-UET
Casspop Codelette: A short, useful, educational utility.  Python and Unix Epoch Time

This is what I'm calling a codelette.  It's a little bit of code that does something, but has some value beyond that for learners like me.  (I don't know about you, but I'm always learning.  Always.)

"uet.py" stands for UnixEpochTime.py, and is a command line utility that will do one of two things immediately:
 - it will give you a UET value if you don't provide any command line arguments
 - it will show you the local and GMT human-readable time for any UET value you provide on the command line

There is nothing awe-inspiring about this codelette, but there is a lot that can be learned from it.
For example, in this tiny file, you'll find working examples of:
- logging: sends data to a file called uet.log. I like to use the command <code>tail -fn40 uet.log</code> in a terminal and watch it happen.
- command line arguments parsing. Type <code>./uet.py --help</code> for more info.
- use of the time module to get the current time
- formatting time strings for human consumption
- setting Python files up so they can be either imported or run as a standalone program
  - this involves use of <code>'if \__name__ == "\__main__":'</code>, which is a really helpful thing to understand.
  - this also involves then defining a function using <code> def </code> and calling that function after the aforementioned 'if'.
- working example of a signalhandler, which responds to CTRL-C being pressed while the code is running. (there are two 3-second pauses so you can test this out.)
- a fair example of a <code>try: except: Exception</code> section (way down at the bottom)

The sections at the top (above the <code>## - - - - - TEST CODE BELOW HERE - - - -</code> line) <br>
and at the bottom (below the <code>## - - - - - - END TEST CODE - - - - - - - </code> line) form the framework for a lot of things I write.

Maybe you'll find this useful in some way.  If so, wonderful.  If not, also wonderful.  

And as always, "It may not be pretty, but it works!"

Enjoy it like this:<br>
<code>greg@Valiant:~/pyCode$ ./uet.py -d -uet 1606352880.8765097</code>