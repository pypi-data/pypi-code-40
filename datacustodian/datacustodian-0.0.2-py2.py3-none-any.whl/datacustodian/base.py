def exhandler(function, parser):
    """If --examples was specified in 'args', the specified function
    is called and the application exits.
    :arg function: the function that prints the examples.
    :arg parser: the initialized instance of the parser that has the
      additional, script-specific parameters.
    """
    args = vars(bparser.parse_known_args()[0])
    if args["examples"]:
        function()
        return
    if args["verbose"]:
        from .msg import set_verbosity
        set_verbosity(args["verbose"])

    args.update(vars(parser.parse_known_args()[0]))
    return args

def _common_parser():
    """Returns a parser with common command-line options for all the scripts
    in the matdb suite.
    """
    import argparse
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--examples", action="store_true",
                        help="See detailed help and examples for this script.")
    parser.add_argument("--verbose", default=0, type=int,
                        help="See verbose output as the script runs.")
    parser.add_argument("--debug", action="store_true",
                        help="Print verbose calculation information for debugging.")

    return parser

bparser = _common_parser()
testmode = False
"""bool: when True, the package is operating in unit test mode, which changes
how plotting is handled.
"""
def set_testmode(testing):
    """Sets the package testing mode.
    """
    global testmode
    testmode = testing

debug = False
"""bool: when True, loggers throughout the `datacustodian` system are set to debug level
to produce more verbose logging output. Can also be `int` corresponding to level
in :mod:`logging`.
"""
def set_debug(debugging):
    """Sets the package testing mode.
    """
    global debug
    debug = debugging
