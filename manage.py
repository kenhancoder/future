# coding: utf-8

import sys
import getopt

from future import app
from future.protocol import JSONHttpProtocol
from future.school import school_bp_v1


class Usage(Exception):

    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hp:", ["help", "port="])

            app.blueprint(school_bp_v1)
            app.run(host='0.0.0.0', debug=True, protocol=JSONHttpProtocol)
        except getopt.error as msg:
            raise Usage(msg)
    except Usage as err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())
