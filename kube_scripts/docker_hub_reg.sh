kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=/home/u2sethi/.docker/config.json \
    --type=kubernetes.io/dockerconfigjson


kubectl get secret regcred --output=yaml
