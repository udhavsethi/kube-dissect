# disable swap
sudo swapoff -a
# we use Calico as the network interface for kubernetes
sudo kubeadm init --pod-network-cidr=192.168.0.0/16 > cluster-info
# the following command need to be run with source
# otherwise the environment variable will not be set
export KUBECONFIG=/etc/kubernetes/admin.conf
# Setup Calico Network Interface
kubectl apply -f https://docs.projectcalico.org/v3.8/manifests/calico.yaml
