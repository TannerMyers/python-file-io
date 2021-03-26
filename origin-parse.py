#! /usr/bin/env python3

import sys
import re

def find_mention(in_stream,
        start_regex = None,
        stop_regex = None):
    """

    """


def record_occurrences(in_stream, out_stream,
        target_regex,
        start_regex = None,
        stop_regex = None):
    """
    Counts the occurrences of words matching the targeted regular expression
    and records the line number it occurs on.
    ------------------------------------------------------------------------
    Parameters
    ------------------------------------------------------------------------
    in_stream : A file object
        Input, in this case, 'On the Origin of Species'
    out_stream : A file object
        Output containing line number and words matching regular expression
    target_regex : A regular expression object
        Search item in `in_stream`
    start_regex : A regular expression object
        Where the targeted regular expression object can begin to be searched for
        in `in_stream`
    stop_regex :
        Where the targeted regular expression object can no longer be searched for
        in `in_stream`
    """    
    occurrences = 0
    for line_index, match_obj in find_mention(in_stream, target_regex,
            start_regex, stop_regex):
        occurrences += 1
        for target_str in match_obj.groups():
            out_stream.write("{line_num}\t{string}\n".format(
                    line_num = line_index + 1,
                    string = target_str))
    return occurrences



if __name__ == '__main__':
    target_pattern = re.compile(r'(^\w*herit\w*$)', re.IGNORECASE)
    start.pattern = re.compile(r'^\*\*START.*$')
    stop.pattern = re.compile(r'^END$')