with open('results_kube/ping') as f:
    ping_kube = sort(f, key=float)
    print(ping_kube)
