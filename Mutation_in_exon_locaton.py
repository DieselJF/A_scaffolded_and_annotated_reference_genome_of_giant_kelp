# This file will define which exon a mutation belongs to.

fileIn_exon = open("gene_exon_start_end_exonsize_strand.txt", "r")
gene_exons = fileIn_exon.readlines()[1:]
fileIn_exon.close()

gene_dict_exons = {}

for line in gene_exons:
    line = line.split()
    gene = line[0]
    exon_n = line[1]
    exon_start = line[3]
    exon_end = line[4]
    gene_strand = line[6]
    exon_size = line[5]
    if gene in gene_dict_exons.keys():
        gene_dict_exons[gene] += [[exon_n, exon_start, exon_end, exon_size]]
    else:
        gene_dict_exons[gene] = [[exon_n, exon_start, exon_end, exon_size]]


fileIn_mut = open("gene_exon_contig_start_end_size_strand_mutPosition_mutEffect_mutImpact.txt", "r")
muts = fileIn_mut.readlines()
fileIn_mut.close()


fileOut = open("gene_exon_start_end_size_strand_mutPosition_mutEffect_mutImpact_relativeMutLocationToAllExons_relativeMutLocationToItsOwnExon.txt", "w")


for line in muts:
    counter_mut_exon = 0
    line = line.split()
    mut_gene = line[0]
    mut_exon = line[1]
    mut_exon_start = line[3]
    mut_exon_end = line[4]
    mut_exon_size = line[5]
    mut_position = line[7]
    mut_strand = line[6]
    mut_effect = line[8]
    mut_impact = line[9]

    if mut_strand == "+":
        counter_mut_exon = 0
        exon_mut_position = int(mut_position) - int(mut_exon_start)
        relative_mut_location_to_exon = int(exon_mut_position)/int(mut_exon_size)

        if int(mut_exon) == 1:
            counter_mut_exon = exon_mut_position
        else:
            for i in range(0,int(mut_exon) - 1):
                counter_mut_exon += int(gene_dict_exons[mut_gene][i][3])
            counter_mut_exon += exon_mut_position

        counter_all_exons = 0
        for i in gene_dict_exons[mut_gene]:
            counter_all_exons += int(i[3])
        relative_mut_location_to_all_exons = counter_mut_exon/counter_all_exons

        print(mut_gene, mut_exon, mut_exon_start, mut_exon_end, mut_exon_size, mut_strand, mut_position, mut_effect, mut_impact, relative_mut_location_to_all_exons, relative_mut_location_to_exon, sep = "\t", file = fileOut)




    if mut_strand == "-":
        counter_mut_exon = 0
        exon_mut_position = int(mut_exon_end) - int(mut_position)
        relative_mut_location_to_exon = int(exon_mut_position)/int(mut_exon_size)

        if int(mut_exon) == 1:
            counter_mut_exon = exon_mut_position
        else:
            for i in range(0,int(mut_exon) - 1):
                counter_mut_exon += int(gene_dict_exons[mut_gene][i][3])
            counter_mut_exon += exon_mut_position

        counter_all_exons = 0
        for i in gene_dict_exons[mut_gene]:
            counter_all_exons += int(i[3])
        relative_mut_location_to_all_exons = counter_mut_exon/counter_all_exons

        print(mut_gene, mut_exon, mut_exon_start, mut_exon_end, mut_exon_size, mut_strand, mut_position, mut_effect, mut_impact, relative_mut_location_to_all_exons, relative_mut_location_to_exon, sep = "\t", file = fileOut)
