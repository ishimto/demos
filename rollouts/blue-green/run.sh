#!/bin/bash


minikube addons enable nginx
kubectl apply -f rollouts.yaml
kubectl apply -f services.yaml
kubectl apply -f ingresses.yaml
