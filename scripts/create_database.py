# this scripts takes a fasta file downloaded from NCBI and creates a text and a fasta files, compatible with qiime
# this is useful for people interested in creating their own databases
# date created: 20-08-2014
# created by Ahmed Abdelfattah
# corresponding email: ahmed.abdelfattaah@gmail.com 
# place Cairo, Egypt

import os
from os.path import exists

file_object = open( .fasta' ,'a+')

if exists("fasta_file.fasta") == True:
	os.remove("fasta_file.fasta")
	fasta_object = open("fasta_file.fasta","a")
else:
	fasta_object = open("fasta_file.fasta","a")	

if exists("txt_file.txt") == True:
	os.remove("txt_file.txt")
	txt_object = open("txt_file.txt","a")
else:
	txt_object = open("txt_file.txt","a")	

count = 0
for l in file_object:
	count = count + 1

file_object.seek(0,0)

mirror1 = 0
mirror2 = 0	
i = 0
no_spaces = 0

while i < count+1:
	str = file_object.readline()
	if str[0] == '>':
		no_spaces = 0
		flag_seq = 0
		b= str.split('|')
		accession_no=">" + b[3]
		print accession_no
		fasta_object.write(accession_no)
		fasta_object.write('\n')
		mirror1 = mirror1 + 1
		str2 = str.split()
		name1 = str2[1]
		name2 = str2[2]
		name = name1 + '_' + name2
		print name
		acc_no_txt = accession_no.strip('>')
		txt_object.write(acc_no_txt)
		txt_object.write('\t')
		txt_object.write(name)
		txt_object.write('\n')
	elif str.isupper():
		no_spaces = 0
		str = str.strip('\n')
		if flag_seq == 0:
			sequence_no = str
			flag_seq = 1
		elif flag_seq == 1:
			sequence_no = sequence_no + str
	elif str[0] == '\n':
		no_spaces = no_spaces + 1
		if no_spaces == 2:
			break
		print sequence_no
		fasta_object.write(sequence_no)
		fasta_object.write('\n')
		mirror2 = mirror2 + 1
	i = i + 1
if mirror1 != mirror2:
	print sequence_no
	fasta_object.write(sequence_no)
	fasta_object.write('\n')
