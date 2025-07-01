# rollouts-demo

This repository demonstrates a basic Argo Rollouts canary deployment on Kubernetes using Minikube and NGINX Ingress.

## Prerequisites

- [Minikube](https://minikube.sigs.k8s.io/docs/) installed and running
- [kubectl](https://kubernetes.io/docs/tasks/tools/) installed
- [Rollouts + kubectl argo rollouts plugin](https://argo-rollouts.readthedocs.io/en/stable/installation/) installed using thats official guide
- Add the following entry to your `/etc/hosts` file, replacing `<MINIKUBE_IP>` with the output of `minikube ip`:
  ```
  <MINIKUBE_IP> rollouts.ginger-ous.click
  ```

## Usage

1. Enable the NGINX ingress addon in Minikube and deploy resources:
   ```sh
   bash run.sh
   ```

2. Access the application at [http://rollouts.ginger-ous.click](http://rollouts.ginger-ous.click)

## Accessing the Argo Rollouts Dashboard

3. Start the dashboard:
```sh
kubectl argo rollouts dashboard
```

This will open the dashboard in your browser (default: http://localhost:3100).

## Canary Deployment Demo

- To trigger a rollout, edit [`rollouts.yaml`](rollouts.yaml) and change the image tag under `spec.template.spec.containers[0].image` from `argoproj/rollouts-demo:blue` to another tag (e.g., `yellow`).
- Apply the changes:
  ```sh
  kubectl apply -f rollouts.yaml
  ```
- Open the Argo Rollouts dashboard and verify that the rollout progresses and the new version replaces the old one.

---

**Note:** Make sure Minikube is running before executing the script.
