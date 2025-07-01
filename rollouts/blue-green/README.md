# rollouts-demo

This repository demonstrates a basic Argo Rollouts BlueGreen deployment on Kubernetes using Minikube and NGINX Ingress.

## Prerequisites

- [Minikube](https://minikube.sigs.k8s.io/docs/) installed and running
- [kubectl](https://kubernetes.io/docs/tasks/tools/) installed
- [Rollouts + kubectl argo rollouts plugin](https://argo-rollouts.readthedocs.io/en/stable/installation/) installed using thats official guide
- Add the following entry to your `/etc/hosts` file, replacing `<MINIKUBE_IP>` with the output of `minikube ip`:
  ```
  <MINIKUBE_IP> active.ginger-ous.click preview.ginger-ous.click
  ```

## Usage

1. Enable the NGINX ingress addon in Minikube and deploy resources:
   ```sh
   bash run.sh
   ```

2. Access the application at [http://active.ginger-ous.click](http://active.ginger-ous.click)

## Accessing the Argo Rollouts Dashboard

.Start the dashboard:
```sh
kubectl argo rollouts dashboard
```

This will open the dashboard in your browser (default: http://localhost:3100).

## BlueGreen Deployment Demo

- To trigger a rollout, edit [`rollouts.yaml`](rollouts.yaml) and change the image tag under `spec.template.spec.containers[0].image` from `argoproj/rollouts-demo:blue` to another tag (e.g., `green`).
- Apply the changes:
  ```sh
  kubectl apply -f rollouts.yaml
  ```

- Access preview at [http://preview.ginger-ous.click](http://preview.ginger-ous.click)

- Access active at [http://active.ginger-ous.click](http://active.ginger-ous.click)

Go to the Rollouts dashboard, click Promote, then sit back and let the magic happen! 

---

**Note:** Make sure Minikube is running before executing the script.
