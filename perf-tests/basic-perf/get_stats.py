import statistics

#################################################################
outfile = open("stats/stats_kube.txt", "w")

outfile.write("Ping\n")
values = []
with open('results_kube/ping') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))


outfile.write("\nMemory test - 1 GB\n")
values = []
with open('results_kube/mem1') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nMemory test - 4 GB\n")
values = []
with open('results_kube/mem4') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nMemory test - 8 GB\n")
values = []
with open('results_kube/mem8') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nMemory test - 16 GB\n")
values = []
with open('results_kube/mem16') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nLoad test - 1 CPU\n")
values = []
with open('results_kube/cpu1') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nLoad test - 4 CPU\n")
values = []
with open('results_kube/cpu4') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nLoad test - 8 CPU\n")
values = []
with open('results_kube/cpu8') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nLoad test - 12 CPU\n")
values = []
with open('results_kube/cpu12') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.close()

#################################################################
outfile = open("stats/stats_docker.txt", "w")

outfile.write("Ping\n")
values = []
with open('results_docker/ping') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))


outfile.write("\nMemory test - 1 GB\n")
values = []
with open('results_docker/mem1') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nMemory test - 4 GB\n")
values = []
with open('results_docker/mem4') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nMemory test - 8 GB\n")
values = []
with open('results_docker/mem8') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nMemory test - 16 GB\n")
values = []
with open('results_docker/mem16') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nLoad test - 1 CPU\n")
values = []
with open('results_docker/cpu1') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nLoad test - 4 CPU\n")
values = []
with open('results_docker/cpu4') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nLoad test - 8 CPU\n")
values = []
with open('results_docker/cpu8') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nLoad test - 12 CPU\n")
values = []
with open('results_docker/cpu12') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.close()

#################################################################
outfile = open("stats/stats_bare.txt", "w")

outfile.write("Ping\n")
values = []
with open('results_bare/ping') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))


outfile.write("\nMemory test - 1 GB\n")
values = []
with open('results_bare/mem1') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nMemory test - 4 GB\n")
values = []
with open('results_bare/mem4') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nMemory test - 8 GB\n")
values = []
with open('results_bare/mem8') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nMemory test - 16 GB\n")
values = []
with open('results_bare/mem16') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nLoad test - 1 CPU\n")
values = []
with open('results_bare/cpu1') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nLoad test - 4 CPU\n")
values = []
with open('results_bare/cpu4') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nLoad test - 8 CPU\n")
values = []
with open('results_bare/cpu8') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("\nLoad test - 12 CPU\n")
values = []
with open('results_bare/cpu12') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("\nmean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.close()
