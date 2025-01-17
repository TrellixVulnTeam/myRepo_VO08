'''This lab is meant to challenge you with a more realistic engineering
application of generators: producing record data from a text file of
unbounded length, where each record spans multiple lines.

WARC, or Web ARChive, is an archival format for web pages.
There's an example in this folder in 'crawl-data.warc'.

For this lab, you mainly need to know that a WARC file has a header
section, followed by two blank lines, and then one or more
records. Each record is separated by a blank line, and consists of the following:

 - a version line ("WARC/1.0")
 - one or more key-value pairs (one per line)
 - another blank line, followed by page content (on one line)

You function will read crawl-data.warc (in this directory), so peek in
that file.  Your job is to write a generator function named
warc_records that takes a path to a WARC file, skips over its header,
and gives you a sequence of records as a dictionary. In addition to
the key-value metadata, add a key called 'Content' that has the
web page content.

Hint: Some idioms for processing lines of text in a file (the 'U' mode
means "universal newlines", so that \r\n, \n, etc. are all reported as
simply "\n"):

  # Stream through the lines
  with open(path, 'U') as file_handle:
      for line in file_handle:
          do_something_with(line)
  # Process lines more manually
  with open(path, 'U') as file_handle:
      while True:
          line = file_handle.readline()
          if line == "":
              break # No more lines
          do_something_with(line)
  # Process lines manually, generator style
  with open(path, 'U') as file_handle:
      while True:
          # Next line raises StopIteration if there are no
          # more lines to read.
          line = next(file_handle)
          do_something_with(line)


>>> records = warc_records('crawl-data.warc')
>>> type(records)
<type 'generator'>

>>> next_record = next(records)
>>> sorted(next_record.keys())
['Content', 'Content-Length', 'Content-Type', 'WARC-Block-Digest', 'WARC-Date', 'WARC-Record-ID', 'WARC-Refers-To', 'WARC-Target-URI', 'WARC-Type', 'WARC-Warcinfo-ID']
>>> next_record['WARC-Date']
'2013-06-20T00:32:15Z'
>>> next_record['WARC-Target-URI']
'http://09231204.tumblr.com/post/44534196170/high-res-new-photos-of-the-cast-of-neilhimself'
>>> next_record['Content'][:30]
'Side Effects high res. New pho'

>>> next_record = next(records)
>>> sorted(next_record.keys())
['Content', 'Content-Length', 'Content-Type', 'WARC-Block-Digest', 'WARC-Date', 'WARC-Record-ID', 'WARC-Refers-To', 'WARC-Target-URI', 'WARC-Type', 'WARC-Warcinfo-ID']
>>> next_record['WARC-Date']
'2013-06-20T00:39:36Z'
>>> next_record['WARC-Target-URI']
'http://1000bulbs.com/product/59005/HLF-150HSW100MHQ.html'
>>> next_record['Content'][:30]
'100 Watt Metal Halide Wall Pac'

>>> next(records)['WARC-Target-URI']
'http://1000bulbs.com/product/60347/PLT-28224.html'

>>> next(records)['WARC-Target-URI']
'http://1000notas.tumblr.com/post/26084820560'

>>> next(records)['WARC-Target-URI']
'http://1027kord.com/tags/regis-kelly/feed/'

>>> next(records)['WARC-Target-URI']
'http://1037theloon.com/tags/from-the-beginning/feed/'

>>> next(records)
Traceback (most recent call last):
...
StopIteration

'''

# Write your code here:

# Version 1: using file_handle.readline()
def warc_records(path):
    prev_line = None
    with open(path, 'U') as file_handle:
        # skip header
        while True:
            line = file_handle.readline()
            if (prev_line == "\n" and line == "\n"):
                break
            prev_line = line
        # read records
        while True:
            record = {}
            line = file_handle.readline()
            if line == "":
                raise StopIteration
            # skip metadata header
            assert line == 'WARC/1.0\n', line
            line = file_handle.readline()
            # read metadata
            while line != "\n":
                assert line != ""
                key, value = line.rstrip('\n').split(": ", 1)
                record[key] = value
                line = file_handle.readline()
            # read content
            assert 'Content' not in record
            record['Content'] = file_handle.readline().rstrip('\n')
            # produce value
            yield record
            # skip next blank line
            line = file_handle.readline()
            assert line == '\n', line

# Version 2: using next(file_handle)
def warc_records(path):
    prev_line = None
    with open(path, 'U') as file_handle:
        # skip header
        for line in file_handle:
            if (prev_line == "\n" and line == "\n"):
                break
            prev_line = line
        # read records
        while True:
            record = {}
            line = next(file_handle)
            # skip metadata header
            assert line == 'WARC/1.0\n', line
            # read metadata
            line = next(file_handle)
            while line != "\n":
                assert line != ""
                key, value = line.rstrip('\n').split(": ", 1)
                record[key] = value
                line = next(file_handle)
            # read content
            assert 'Content' not in record
            record['Content'] = next(file_handle).rstrip('\n')
            # produce value
            yield record
            # skip next blank line
            line = next(file_handle)
            assert line == '\n', line


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.
