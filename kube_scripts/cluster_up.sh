sudo swapoff -a
sudo kubeadm init --pod-network-cidr=192.168.0.0/16 > kubeadm_init_output
export KUBECONFIG=/etc/kubernetes/admin.conf
kubectl apply -f https://docs.projectcalico.org/v3.8/manifests/calico.yaml
