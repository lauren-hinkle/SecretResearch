import sys, re, mmap

# run with python parse.py filename
# output format is meme_title ; first_line ; second_line on each line

with open(sys.argv[1], 'r+') as f:
  data = mmap.mmap(f.fileno(), 0)
  meme = re.findall('gt;Meme: (.*)\n\n\&gt;\* (.*)\n\&gt;\* (.*)', data)
  for me in meme:
    print me[0].lower(), ';', me[1].lower(), ';', me[2].lower()
