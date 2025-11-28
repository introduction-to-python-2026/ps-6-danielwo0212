def create_codon_dict(file_path):
  path = file_path
  file = open(path, "r")
  rows = file.readlines()
  file.close()
  codon_dict = {}
  for row in rows:
    cell = row.strip().strip("\n").split('\t')
    codon = cell[0]
    amino_acid = cell[2]
    codon_dict[codon] = amino_acid
  return codon_dict
