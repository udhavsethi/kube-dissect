#!/bin/bash 

TIMEFORMAT=%R

echo "Ping test"
{ for i in {1..100}; do time curl -s yellow13:3030/ping; done } 2>> results_bare/ping

echo "Memory test - 1 MB"
{ for i in {1..10}; do time curl -s yellow13:3030/loadtest/memory/1/5; done } 2>> results_bare/mem1

echo "Memory test - 4 MB"
{ for i in {1..10}; do time curl -s yellow13:3030/loadtest/memory/4/5; done } 2>> results_bare/mem4

echo "Memory test - 8 MB"
{ for i in {1..10}; do time curl -s yellow13:3030/loadtest/memory/8/5; done } 2>> results_bare/mem8

echo "Memory test - 100 MB"
{ for i in {1..10}; do time curl -s yellow13:3030/loadtest/memory/100/5; done } 2>> results_bare/mem100

echo "Load test - 1 CPU"
{ for i in {1..10}; do time curl -s yellow13:3030/loadtest/cpu/1; done } 2>> results_bare/cpu1

echo "Load test - 4 CPU"
{ for i in {1..10}; do time curl -s yellow13:3030/loadtest/cpu/4; done } 2>> results_bare/cpu4

echo "Load test - 8 CPU"
{ for i in {1..10}; do time curl -s yellow13:3030/loadtest/cpu/8; done } 2>> results_bare/cpu8
