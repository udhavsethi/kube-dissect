# create credentials from docker config file
kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=/home/u2sethi/.docker/config.json \
    --type=kubernetes.io/dockerconfigjson
# test if credentails have been created
kubectl get secret regcred --output=yaml