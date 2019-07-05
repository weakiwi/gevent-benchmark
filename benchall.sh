#!/bin/sh

PYTHON=${PYTHON:=python}

idc=$1

$PYTHON bench_hub.py -o result_${idc}.json
$PYTHON bench_local.py --append result_${idc}.json
$PYTHON bench_pool.py --append result_${idc}.json
$PYTHON bench_queue.py --append result_${idc}.json
$PYTHON bench_sendall.py --append result_${idc}.json
$PYTHON bench_sleep0.py --append result_${idc}.json
$PYTHON bench_socket.py --append result_${idc}.json
$PYTHON bench_spawn.py --append result_${idc}.json
$PYTHON bench_subprocess.py --append result_${idc}.json
$PYTHON bench_threadpool.py --append result_${idc}.json
$PYTHON bench_tracer.py --append  result_${idc}.json