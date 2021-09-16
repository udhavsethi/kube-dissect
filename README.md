# Kubernetes Dissection and Benchmarking

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

### Initializing Master Node
1. Run ```source cluster-up.sh```  
Note that this script must be run with source otherwise environment cannot be set. This script should be only run on yellow13 once.
2. Login docker by ```sudo docker login```, enter credentials
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
1. Create application and test locally
2. Create docker image and test locally
   1. Build image ```docker build -t xiyangf1997/<image-name>:<tag> .```
   2. Run image ```docker run --rm -p <local port>:<docker port> xiyangf1997/<image name>:<tag>```
3. Push docker to docker hub
   1. Create repo with the corresponding image name on xiyang's docker hub
   2. Push image ```docker push xiyangf1997/<image-name>:<tag>```
4. Create deployment
   1. Run ```kubectl apply -f <deployment yaml file>```
   2. To delete deployment ```kubectl delete -f <deployment yaml file>```
5. Create service
   1. Run ```kubectl apply -f <service yaml file>```
   2. To delete service ```kubectl delete -f <service yaml file>```
6. Test
7. Rolling Upgrade (Alternatively we can delete and redeploy)
   1. Update application and test
   2. Rebuild docker file and push to docker hub
   3. Rolling upgrade ```kubectl set image deployments/<deployment name> <container name>=<new image>```  
   For upgrading we should only change image tag. If there should be a major change, let's create a new deployment instead.
   
## Performance Benchmarking
Test kubernetes performance on ping, cpu intensive task and memory intensive tasks.

* Run python http server: ```server.py```. Default access port: 8080
* See routing info: ```curl <hostname>:<port>```
* Run ping test: ```curl <hostname>:<port>/ping```
* Run cpu test: ```curl <hostname>:<port>/loadtest/cpu/<cpu-cores>```
  * cpu-cores: number of cpu cores to run computation intensive task.
* Run memory test ```curl <hostname>:<port>/loadtest/memory/<size>/<time>```
  * size: Memory to be consumed in MBs.
  * time: Duration for which to occupy the memory.
