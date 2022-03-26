# # def solve_fingerprint(seq_list, no_of_col):
# #   seq_dict=dict()
# #   for column in range(no_of_col):
# #     counta,countc,countt,countg=0,0,0,0
# #     for colseq in seq_list: 
# #       if colseq[column]=='A':
# #         counta+=1
# #       elif colseq[column]=='T':
# #         countt+=1
# #       elif colseq[column]=='C':
# #         countc+=1
# #       elif colseq[column]=='G':
# #         countg+=1
# #     seq_dict[column]=[counta,countc,countt,countg]
# #   display_results(seq_dict)

# # def display_results(seq_dict):
# #   print("\tA \tC \tT \tG")
# #   for key in seq_dict:
# #     print("\n",*seq_dict[key],sep="\t")

# # no_of_seq=int(input("Enter the number of sequence: "))
# # print("Enter all the sequences")
# # seq_list=[]
# # for _ in range(no_of_seq):
# #   seq_list.append(list(map(str, input("").split())))
# # solve_fingerprint(seq_list,len(seq_list[0]))


# from random import choice, randint

# def get_sequences() -> tuple[list[str]]:
# 	char_sequence = 'ACTG'
# 	sequence_length = randint(10, 20)
# 	sequence_1 = list('ACCTGTTACTGAT')
# 	sequence_2 = list('ACGTCAACTTGAT')
	
# 	return sequence_1, sequence_2

# def identity(sequence_1 : list[str], sequence_2 : list[str]) -> tuple[int, list[list[int]]]:
	
# 	result_matrix = [[1 if i == j else 0 for j in sequence_1] for i in sequence_2]
# 	result = sum([sum(i) for i in result_matrix])
	
# 	return result, result_matrix

# def print_matrix(matrix : list[list[int]]):
# 	for i in matrix:
# 		print(i)
# 	print()


# if __name__ == "__main__":
# 	sequence_1, sequence_2 = get_sequences()
# 	print("Sequence 1 is>\n", sequence_1)
# 	print("Sequence 2 is>\n", sequence_2)
# 	print("\n")
# 	score = 0 
# 	for i in range(len(sequence_1)-1):
#             for j in range(len(sequence_2)-1):
#                 if sequence_1[i] == sequence_2[j]:
#                     score+=1
        
# 	result, result_matrix = identity(sequence_1, sequence_2)
# 	print("Result matrix is>\n")
# 	print_matrix(result_matrix)
	
# 	print(f"Identity is {round((result / (len(sequence_1) * len(sequence_2))) * 100, 2)}")


from random import choice, randint

def get_sequences() -> tuple[list[str]]:
	char_sequence = 'ACTG'
	sequence_length = randint(10, 20)
	sequence_1 = list('ACCTGTTACTGAT')
	sequence_2 = list('ACGTCAACTTGAT')
	
	return sequence_1, sequence_2

def identity(sequence_1 : list[str], sequence_2 : list[str]) -> tuple[int, list[list[int]]]:
	
	result_matrix = [[1 if i == j else 0 for j in sequence_1] for i in sequence_2]
	result = sum([sum(i) for i in result_matrix])
	
	return result, result_matrix

def print_matrix(matrix : list[list[int]]):
	for i in matrix:
		print(i)
	print()


if __name__ == "__main__":
	sequence_1, sequence_2 = get_sequences()
	print("Sequence 1 is>\n", sequence_1)
	print("Sequence 2 is>\n", sequence_2)
	print("\n")
  
	result, result_matrix = identity(sequence_1, sequence_2)
	print("Result matrix is>\n")
  
	print_matrix(result_matrix)
  print(result_matrix.count(1))
	
	print(f"Identity is {round((result / (len(sequence_1) * len(sequence_2))) * 100, 2)}")
