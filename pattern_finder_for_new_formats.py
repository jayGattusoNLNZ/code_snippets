import os
import collections


class Pattern_Detector(object):
	def __init__(self, start=0, end = 50):
		self.master_seq = collections.OrderedDict()
		self.initialise = True
		self.start = start
		self.end = end
		self.seqs = {}
		self.files_list = []
		self.files_used = 0


	def get_sequence(self, f_path):
		""" grabs the required section of a given binary""" 
		with open(f_path, "rb") as data:
			bytes = data.read()
			return bytes[self.start:self.end]

	def make_master_seq(self, bytes_sequence):
		"""Takes the first presented binary item and makes a sequence pattern on the given length"""
		### convert sequence from text encoded hex to byte codes
		bytes_sequence =  "".join("{:02x}".format(ord(c)) for c in bytes_sequence)
		### coerce bytes pattern into byte sections 
		bytes = [bytes_sequence[i:i + 2] for i in xrange(0, len(bytes_sequence), 2)]
		### create the inital state ordered dict [(sequence order, value)] for the byte parts.  
		for i, byte in enumerate(bytes):
			self.master_seq[i] = byte
		self.files_used += 1

	def test_against_master_seq(self, bytes_sequence):
		"""Takes the nth presented binary item, and checks against the master - replace deltas with a null representative value"""
		current_seq = collections.OrderedDict()
		### convert sequence from text encoded hex to byte codes
		bytes_sequence =  "".join("{:02x}".format(ord(c)) for c in bytes_sequence)
		### coerce bytes pattern into byte sections 
		bytes = [bytes_sequence[i:i + 2] for i in xrange(0, len(bytes_sequence), 2)]
		### check against the inital state ordered dict [(sequence order, value)] for the byte parts. if not the same, replace with None
		for i, byte in enumerate(bytes):
			if byte != self.master_seq[i]:
				self.master_seq[i] = None 
		self.files_used += 1


	def pattern_tester(self):
		for f in self.files_list:
			seq = self.get_sequence(f)
			if self.initialise:
				self.make_master_seq(seq)
				self.initialise = False
			else:
				self.test_against_master_seq(seq)


	def display_pattern(self):
		print "Files used to make pattern: {}, Start offset: {}, End offset: {}".format(self.files_used, self.start, self.end)
		parts = []
		for place, part in self.master_seq.items():

			if part == None: 
				part = "**"
			parts.append(part)

		byte_string = "".join(parts)

		if byte_string.count("*") == len(byte_string):
			print "No pattern detected"
		else:
			print "".join(parts)


folder = "D:\Pathas\MSCOM-1284"


patterns = Pattern_Detector(start = 0, end = 300)


for root, subs, files in os.walk(folder):
	for f in files:
		f_path = os.path.join(root, f)

		if os.path.isfile(f_path):
			filename, file_extension = os.path.splitext(f_path)
			if file_extension == "":
				seq = patterns.get_sequence(f_path)

				### sequence type picker
				if seq.startswith("\x01\x006\x00BOBO"):
					patterns.files_list.append(f_path)


patterns.pattern_tester()
patterns.display_pattern()

