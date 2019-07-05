#!/bin/sh

PYTHON=${PYTHON:=python}

idc=$1

$PYTHON bench_hub.py --quiet -o result_${idc}.json
$PYTHON bench_local.py --quiet --append result_${idc}.json
$PYTHON bench_pool.py --quiet --append result_${idc}.json
$PYTHON bench_queue.py --quiet --append result_${idc}.json
$PYTHON bench_sendall.py --quiet --append result_${idc}.json
$PYTHON bench_sleep0.py --quiet --append result_${idc}.json
$PYTHON bench_socket.py --quiet --append result_${idc}.json
$PYTHON bench_spawn.py --quiet --append result_${idc}.json
$PYTHON bench_subprocess.py --quiet --append result_${idc}.json
$PYTHON bench_threadpool.py --quiet --append result_${idc}.json
$PYTHON bench_tracer.py --quiet --append result_${idc}.json