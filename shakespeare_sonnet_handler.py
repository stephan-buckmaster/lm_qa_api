from base_handler import BaseHandler
from parse_paragraphs import parse_paragraphs
import re
import random

SONNETS = parse_paragraphs('sonnets.txt')

def extract_integer(text):
  match = re.search(r"\d+", text)  # Find one or more digits
  return int(match.group()) if match else None

class ShakespeareSonnetHandler(BaseHandler):
	def complete(self):
		if self.request.messages:
			if self.request.messages[-1]:
				x = extract_integer(self.request.messages[-1].content)
				if x:
					return '\n\n'.join([random.choice(SONNETS) for x in range(x)])

		return random.choice(SONNETS)
