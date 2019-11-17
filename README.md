# CS754 Kubernetes

## Installation
1. Disable Ubuntu proxy by commenting the lines in  ```/etc/apt/apt.conf```  
2. Run ```sudo ./install.sh```  
This script will install docker and kubeadm on the machine  
## Cluster Setup
We use SYN cluster as our testing environment.  
| Node     | Role    | Kube Status  |
| -------- | ------- | ------------ |
| yellow12 | testing | NA           |
| yellow13 | Master  | Running      |
| yellow14 | Slave   | Running      |
| yellow15 | Slave   | Running      |
### To initial master node
1. Run ```source cluster-up.sh```  
Note that this script must be run with source otherwise environment cannot be set. This script should be only run on yellow13 once.
2. Login docker by ```sudo docker login``` with xiyangf1997 and password
3. Add docker credentials to kubernetes by ```sudo docker-repo-reg.sh```
This will allow kubernetes to pull image from docker hub. This script should be only run on yellow13 once.
### To join nodes
1. Run ```sudo cluster-join.sh```
Note that every time we initialize a new cluster, this script shold be updated with new cluster's token which can be found at ```./cluster-info```. This script should be only run on each slave node once.
### To tear down cluster
Ideally we shouldn't need to tear down the cluster
* For slave node: simply run ```sudo kubeadm reset```
* For master node: drain all nodes before resetting cluster  
  * ```kubectl drain <node name> --delete-local-data --force --ignore-daemonsets```
  * ```kubectl delete node <node name>```
  * ```sudo kubeadm reset```  

## Deployment Pipeline