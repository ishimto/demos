#!/bin/bash


minikube addons enable nginx
kubectl apply -f rollouts.yaml
kubectl apply -f svcs.yaml
kubectl apply -f ingress.yaml
