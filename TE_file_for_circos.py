# This code makes a TE density file for Circlos plotting based on TE output from Repeat Modeler

te = open("TEs_for_circos.txt", "r")
TEs = te.readlines()
te.close()

reg = open("windows_200kb_40kbStep.txt", "r")
regions = reg.readlines()
reg.close()

fileOut_complete = open("Complete_TEs_for_circos.txt", "w")
fileOut_Unknown = open("Unknown_TEs_for_circos.txt", "w")
fileOut_DNA = open("DNA_TEs_for_circos.txt", "w")
fileOut_LTR = open("LTR_TEs_for_circos.txt", "w")
fileOut_LINE = open("LINE_TEs_for_circos.txt", "w")
fileOut_RC = open("RC_TEs_for_circos.txt", "w")

print("Scaffold", "start", "end", "Unknown", "DNA", "LTR", "LINE", "RC", "total", sep="\t", file= fileOut_complete)

for region in regions:
    counter_unknown = 0
    counter_DNA = 0
    counter_LTR = 0
    counter_LINE =0
    counter_RC = 0

    reg_scaffold = region.strip().split()[0]
    reg_start = region.strip().split()[1]
    reg_end = region.strip().split()[2]
    for line in TEs:
        if line.startswith("scaffold"):
            line = line.split()
            TE = line[3]
            TE_scaffold = line[0]
            TE_start = line[1]
            TE_end = line[2]
            if reg_scaffold == TE_scaffold and int(reg_start) <= int(TE_start) < int(reg_end):
                if TE == "Unknown":
                    counter_unknown +=1
                elif TE == "DNA":
                    counter_DNA +=1
                elif TE == "LTR":
                    counter_LTR +=1
                elif TE == "LINE":
                    counter_LINE +=1
                elif TE == "RC":
                    counter_RC +=1
        total = counter_unknown + counter_DNA + counter_LTR + counter_LINE + counter_RC
    print(region.strip(), counter_unknown, counter_DNA, counter_LTR, counter_LINE, counter_RC, total, sep="\t", file= fileOut_complete)
    print(region.strip(), counter_unknown, sep="\t", file= fileOut_Unknown)
    print(region.strip(), counter_DNA, sep="\t", file= fileOut_DNA)
    print(region.strip(), counter_LTR, sep="\t", file= fileOut_LTR)
    print(region.strip(), counter_LINE, sep="\t", file= fileOut_LINE)
    print(region.strip(), counter_RC, sep="\t", file= fileOut_RC)

