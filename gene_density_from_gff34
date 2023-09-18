# This script makes a gene density to be used on Circlos plotting from the original gff3 file
# Needs a window file created from bedtools

gf = open("Macpyr1_GeneModels_FilteredModels1.gff3", "r")
gff = gf.readlines()[2:]
gf.close()

reg = open("windows_200kb_40kbStep.txt", "r")
regions = reg.readlines()
reg.close()

fileOut = open("gene_density_200kb_40kbStep.txt", "a")

scaffold_print = 0
for region in regions:
    counter = 0
    reg_scaffold = region.strip().split()[0]
    reg_start = region.strip().split()[1]
    reg_end = region.strip().split()[2]
    for line in gff:
        if line.split()[2] == "gene":
            gff_scaffold = line.split()[0]
            gff_location = line.split()[3]
            if gff_scaffold == reg_scaffold and int(reg_start) <= int(gff_location) < int(reg_end):
                counter +=1
    print(region.strip(), counter, sep="\t", file=fileOut)

fileOut.close()
