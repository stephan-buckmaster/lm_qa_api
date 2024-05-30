import re
# The file has paragraphs separated by empty lines.
# Return the list of these paragraphs as an array
def not_only_whitespace(text):
    return bool(text) and not(text.isspace())

def parse_paragraphs(file_name):
  with open(file_name) as f:
      entries = []
      current_entry = ''
      for line in f:
          if not_only_whitespace(line):
              current_entry += line
          else:
              entries.append(current_entry)
              current_entry = ''
      entries.append(current_entry)
  return entries
