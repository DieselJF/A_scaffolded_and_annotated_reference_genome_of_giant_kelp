# File to get gene and position from gff3 file
# Gene and position are used to extract coordinates in the VCF file

gf = open("Macpyr2_GeneModels_FilteredModels3.gff3", "r")
gff = gf.readlines()[2:]
gf.close()

fileOut = open("Gene_position.txt", "w")

for line in gff:
    line = line.strip().split()
    if line[2] == "gene":
        protein = line[8].split("Macpyr2|")[1].split(";")[0]
        scaffold = line[0]
        pos1 = line[3]
        pos2 = line[4]
        print(protein, scaffold, pos1, pos2, sep="\t", file=fileOut)
