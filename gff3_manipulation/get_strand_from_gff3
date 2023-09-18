# Simple script to separate strande of gene 

fileIn = open("Macpyr2_GeneModels_FilteredModels3.gff3", "r")
gff = fileIn.readlines()[2:]
fileIn.close()

gene_mRNA_dict = {}

fileOut = open("gene_exon_start_end_exonsize_strand.txt", "w")

print("gene", "exon_number", "exon_start", "exon_end", "exon_size", "exon_strand", sep = "\t", file = fileOut)

for line in gff:
    if not line.startswith("#"):
        line = line.split()
        if line[2] == "gene":
            gene = line[8].split(";")[1].split("|")[2]
            mRNA = line[8].split(";")[0].split("=")[1].split("_")[1]
            gene_mRNA_dict[mRNA] = gene
        if line[2] == "exon":
            exon_contig = line[0]
            exon_mRNA = line[8].split(";")[0].split("_")[1]
            exon_numer = line[8].split(";")[0].split("_")[2]
            exon_mRNA_start = line[3]
            exon_mRNA_end = line[4]
            exon_mRNA_size = int(line[4]) - int(line[3])
            strand = line[6]
            print(gene_mRNA_dict[exon_mRNA], exon_numer, exon_contig, exon_mRNA_start, exon_mRNA_end, exon_mRNA_size, strand, sep="\t", file=fileOut)

