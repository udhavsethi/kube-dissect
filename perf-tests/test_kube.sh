#!/bin/bash 

TIMEFORMAT=%R

echo "Ping test"
{ for i in {1..100}; do time curl -s yellow13:30036/ping; done } 2>> results_kube/ping

echo "Memory test - 1 GB"
{ for i in {1..100}; do time curl -s yellow13:30036/loadtest/memory/1024/0; done } 2>> results_kube/mem1

echo "Memory test - 4 GB"
{ for i in {1..100}; do time curl -s yellow13:30036/loadtest/memory/4096/0; done } 2>> results_kube/mem4

echo "Memory test - 8 GB"
{ for i in {1..100}; do time curl -s yellow13:30036/loadtest/memory/8192/0; done } 2>> results_kube/mem8

echo "Memory test - 16 GB"
{ for i in {1..100}; do time curl -s yellow13:30036/loadtest/memory/16384/0; done } 2>> results_kube/mem16

echo "Load test - 1 CPU"
{ for i in {1..100}; do time curl -s yellow13:30036/loadtest/cpu/1; done } 2>> results_kube/cpu1

echo "Load test - 4 CPU"
{ for i in {1..100}; do time curl -s yellow13:30036/loadtest/cpu/4; done } 2>> results_kube/cpu4

echo "Load test - 8 CPU"
{ for i in {1..100}; do time curl -s yellow13:30036/loadtest/cpu/8; done } 2>> results_kube/cpu8

echo "Load test - 12 CPU"
{ for i in {1..100}; do time curl -s yellow13:30036/loadtest/cpu/12; done } 2>> results_kube/cpu12
