sudo swapoff -a

sudo kubeadm join 10.0.4.13:6443 --token b46z2l.h0jsx4dqrwvxu9af \
    --discovery-token-ca-cert-hash sha256:b144eb7bb9f0d1d67b634407ccd7521c4ff9698fa4c7eb2d799c3573dc5d0ff7
