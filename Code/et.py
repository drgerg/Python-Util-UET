#!/usr/bin/env python3
#
#     Copyright (c) 2019,2020 - Gregory Allen Sanders.

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import time,os,logging,argparse,traceback,signal,sys

parserET = argparse.ArgumentParser()
parserET.add_argument('-d', '--debug', help="Turn on debugging output to et.log file.", action="store_true")
parserET.add_argument('-uet', help="Unix Epoch Time value.", action="store")
ETHome = os.getcwd()
logger = logging.getLogger(__name__)
argsET = parserET.parse_args()

logger.debug('Checked for commandline argument: argsET.uet.')
if argsET.uet:
    ETRaw = float(argsET.uet)
    print(' Input UET: ' + str(ETRaw))


if argsET.debug:
    logging.basicConfig(filename=ETHome + '/et.log', format='[%(name)s]:%(levelname)s: %(message)s. - %(asctime)s', datefmt='%D %H:%M:%S', level=logging.DEBUG)
    logging.info("Debugging output enabled")
else:
    logging.basicConfig(filename=ETHome + '/et.log', format='%(asctime)s - %(message)s', datefmt='%a, %d %b %Y %H:%M:%S', level=logging.INFO)
#
logger.info(" - - - - epochTime.py DATA LOGGING STARTED - - - - ")
logger.info("  epochTime.py INITIAL CONFIGURATION COMPLETE  ")
logger.info("'HOME' path is: " + ETHome)

#
## - - - - - TEST CODE BELOW HERE - - - -
#

def main(input):
    logger.debug(' Input UET: ' + str(ETRaw))
    epoch = float(input)
    gmtTime = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.gmtime(epoch))
    locTime = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(epoch))
    print('Local time: ' + str(locTime))
    print('       GMT: ' + str(gmtTime))
    logger.debug('Local time: ' + str(locTime))
    logger.debug('       GMT: ' + str(gmtTime))

## - - - - - - END TEST CODE - - - - - - - 
#

def SignalHandler(signal, frame):
    if signal == 2:
        sigStr = 'CTRL-C'
        logger.info('* * * ' + sigStr + ' caught. * * * ')
    print("SignalHandler invoked")
    logger.info("Shutting down gracefully")
    logger.debug("Wrote to log in SignalHandler")
    logger.info("That's all folks.  Goodbye")
    logger.info(" - - - - test.py DATA LOGGING STOPPED INTENTIONALLY - - - - ")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, SignalHandler)  ## This one catches CTRL-C from the local keyboard
    signal.signal(signal.SIGTERM, SignalHandler) ## This one catches the Terminate signal from the system    
    try:
        if argsET.uet:
            main(argsET.uet)
        else:
            uet = time.time()
            print("\nYou didn't supply a Unix Epoch Time value.  Here's one: " + str(uet) + '\n Learn more by typing "./et.py --help".\n')
            logger.debug('No time value was provided, so we provided this: ' + str(uet))
        pass
        logger.info(" - - - - epochTime.py COMPLETED ITS MISSION - - - - ")
    except Exception:
        logger.info("Exception caught at bottom of try.", exc_info=True)
        error = traceback.print_exc()
        logger.info(error)
        logger.info("That's all folks.  Goodbye")
        logger.info(" - - - - epochTime.py DATA LOGGING STOPPED BY EXCEPTION - - - - ")

