import statistics

outfile = open("stats/stats_kube.txt", "w")

outfile.write("Ping\n")
values = []
with open('results_kube/ping') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("mean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))

outfile.write("Memory test - 1 GB\n")
values = []
with open('results_kube/ping') as infile:
    for line in infile:
        values.append(float(line.strip()))
    values.sort()

outfile.write("mean: {}\n".format(statistics.mean(values)))
outfile.write("10th percentile: {}\n".format(values[10]))
outfile.write("90th percentile: {}\n".format(values[90]))











outfile.close()
