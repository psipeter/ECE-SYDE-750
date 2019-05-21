# Peter Duggins
# SYDE/ECE 750
# May 22, 2019
# Assignment 2

'''
7. Write a program that reads a string over alphabet {A,C,T,G},
 - the template strand of DNA, and returns a string over {A,C,T,G} for the complementary strand
 - the string over {A,C,U,G} for the corresponding mRNA (messenger RNA).

8. Write a program "ribosome" that takes an mRNA string
	and reads it one codon at a time to return that string of corresponding protein
	as amino acid string (use the twenty letter alphabet from the genetic code table.)
'''

import sys

def transcribe(type):
	file = open("template.txt", 'r')
	template = file.readline()
	print('Printing %s string' %type)
	for base in template:
		if type == 'original':
			print(base),
			continue
		if base == 'C':
			print('G'),
		if base == 'G':
			print('C'),
		if base == 'A':
			if type == 'complement':
				print('T'),
			if type == 'mRNA':
				print('U'),
		if base == 'T':
			print('A'),

def ribosome():
	file = open("mRNA.txt", 'r')
	template = file.readline()
	n_codons = int(len(template)/3)
	protein = ''
	for codon in range(n_codons):
		idx0 = template[codon+0]
		idx1 = template[codon+1]
		idx2 = template[codon+2]
		if idx0 == 'C':
			if idx1 == 'C':
				if idx2 == 'C': protein += 'Proline-'
				if idx2 == 'G': protein += 'Proline-'
				if idx2 == 'A': protein += 'Proline-'
				if idx2 == 'U': protein += 'Proline-'
			if idx1 == 'G':
				if idx2 == 'C': protein += 'Arginine-'
				if idx2 == 'G': protein += 'Arginine-'
				if idx2 == 'A': protein += 'Arginine-'
				if idx2 == 'U': protein += 'Arginine-'
			if idx1 == 'A':
				if idx2 == 'C': protein += 'Histidine-'
				if idx2 == 'G': protein += 'Glutamine-'
				if idx2 == 'A': protein += 'Glutamine-'
				if idx2 == 'U': protein += 'Histidine-'
			if idx1 == 'U':
				if idx2 == 'C': protein += 'Leucine-'
				if idx2 == 'G': protein += 'Leucine-'
				if idx2 == 'A': protein += 'Leucine-'
				if idx2 == 'U': protein += 'Leucine-'
		if idx0 == 'G':
			if idx1 == 'C':
				if idx2 == 'C': protein += 'Alanine-'
				if idx2 == 'G': protein += 'Alanine-'
				if idx2 == 'A': protein += 'Alanine-'
				if idx2 == 'U': protein += 'Alanine-'
			if idx1 == 'G':
				if idx2 == 'C': protein += 'Glycine-'
				if idx2 == 'G': protein += 'Glycine-'
				if idx2 == 'A': protein += 'Glycine-'
				if idx2 == 'U': protein += 'Glycine-'
			if idx1 == 'A':
				if idx2 == 'C': protein += 'Aspartic Acid-'
				if idx2 == 'G': protein += 'Glutamic Acid-'
				if idx2 == 'A': protein += 'Glutamic Acid-'
				if idx2 == 'U': protein += 'Aspartic Acid-'
			if idx1 == 'U':
				if idx2 == 'C': protein += 'Valine-'
				if idx2 == 'G': protein += 'Valine-'
				if idx2 == 'A': protein += 'Valine-'
				if idx2 == 'U': protein += 'Valine-'
		if idx0 == 'A':
			if idx1 == 'C':
				if idx2 == 'C': protein += 'Threonine-'
				if idx2 == 'G': protein += 'Threonine-'
				if idx2 == 'A': protein += 'Threonine-'
				if idx2 == 'U': protein += 'Threonine-'
			if idx1 == 'G':
				if idx2 == 'C': protein += 'Serine-'
				if idx2 == 'G': protein += 'Arginine-'
				if idx2 == 'A': protein += 'Arginine-'
				if idx2 == 'U': protein += 'Serine-'
			if idx1 == 'A':
				if idx2 == 'C': protein += 'Asparagine-'
				if idx2 == 'G': protein += 'Lysine-'
				if idx2 == 'A': protein += 'Lysine-'
				if idx2 == 'U': protein += 'Asparagine-'
			if idx1 == 'U':
				if idx2 == 'C': protein += 'Isoleucine-'
				if idx2 == 'G': protein += 'Methionine-'
				if idx2 == 'A': protein += 'Isoleucine-'
				if idx2 == 'U': protein += 'Isoleucine-'
		if idx0 == 'U':
			if idx1 == 'C':
				if idx2 == 'C': protein += 'Serine-'
				if idx2 == 'G': protein += 'Serine-'
				if idx2 == 'A': protein += 'Serine-'
				if idx2 == 'U': protein += 'Serine-'
			if idx1 == 'G':
				if idx2 == 'C': protein += 'Cysteine-'
				if idx2 == 'G': protein += 'Tryptophan-'
				if idx2 == 'A': protein += 'Stop (Opal)-'
				if idx2 == 'U': protein += 'Cysteine-'
			if idx1 == 'A':
				if idx2 == 'C': protein += 'Tyrosine-'
				if idx2 == 'G': protein += 'Stop (Ochre)-'
				if idx2 == 'A': protein += 'Stop (Amber)-'
				if idx2 == 'U': protein += 'Tyrosine-'
			if idx1 == 'U':
				if idx2 == 'C': protein += 'Phenylalanine-'
				if idx2 == 'G': protein += 'Leucine-'
				if idx2 == 'A': protein += 'Leucine-'
				if idx2 == 'U': protein += 'Phenylalanine-'
	print('mRNA: %s' %template)
	print('translated amino acid chain: %s' %protein)
	

if __name__ == "__main__":
	transcribe('original')
	print('\n')
	transcribe('complement')
	print('\n')
	transcribe('mRNA')
	print('\n')
	ribosome()