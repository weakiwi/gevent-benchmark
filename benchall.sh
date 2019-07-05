#!/bin/sh

PYTHON=${PYTHON:=python}

idc=$1

$PYTHON bench_hub.py -o result_hub_${idc}.json
$PYTHON bench_local.py -o result_local_${idc}.json
$PYTHON bench_pool.py -o result_pool_${idc}.json
$PYTHON bench_queue.py -o result_queue_${idc}.json
$PYTHON bench_sendall.py -o result_sendall_${idc}.json
$PYTHON bench_sleep0.py -o result_sleep0_${idc}.json
$PYTHON bench_socket.py -o result_socket_${idc}.json
$PYTHON bench_spawn.py -o result_spawn_${idc}.json
$PYTHON bench_subprocess.py -o result_subprocess_${idc}.json
$PYTHON bench_threadpool.py -o result_threadpool_${idc}.json
$PYTHON bench_tracer.py -o result_tracer_${idc}.json