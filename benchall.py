from bench_hub import *
from bench_local import *
from bench_pool import *
from bench_queue import *
#from bench_sendall import *
from bench_sleep0 import *
#from bench_socket import *
#from bench_spawn import *
from bench_subprocess import *
from bench_threadpool import *
from bench_tracer import *

def _populate(l):
    for i in range(10):
        setattr(l, 'attr' + str(i), i)

def main():
    runner = perf.Runner()

    runner.bench_func('multiple wait ready',
                      bench_wait_func_ready,
                      inner_loops=N)

    runner.bench_func('wait ready',
                      bench_wait_ready,
                      inner_loops=N)

    runner.bench_func('cancel wait',
                      bench_cancel_wait,
                      inner_loops=N)

    runner.bench_func('switch',
                      bench_switch,
                      inner_loops=N)
    for name, obj in (('gevent', glocal()),
                      ('gevent sub', GLocalSub()),
                      ('native', nlocal()),
                      ('native sub', NativeSub())):
        _populate(obj)

        benchmarks.append(
            runner.bench_time_func('getattr ' + name,
                                   bench_getattr,
                                   obj,
                                   inner_loops=10))

        benchmarks.append(
            runner.bench_time_func('setattr ' + name,
                                   bench_setattr,
                                   obj,
                                   inner_loops=10))

    runner.bench_func('bench_bounded_queue_noblock',
                      bench_bounded_queue_noblock,
                      inner_loops=N)

    runner.bench_func('bench_bounded_queue_block',
                      bench_bounded_queue_block,
                      inner_loops=N)

    runner.bench_func('bench_channel',
                      bench_bounded_queue_block,
                      queue.Channel,
                      inner_loops=N)

    runner.bench_func('bench_bounded_queue_block_hub',
                      bench_bounded_queue_block,
                      queue.Queue, True,
                      inner_loops=N)

    runner.bench_func('bench_channel_hub',
                      bench_bounded_queue_block,
                      queue.Channel, True,
                      inner_loops=N)

    runner.bench_func('bench_unbounded_priority_queue_noblock',
                      bench_unbounded_queue_noblock,
                      queue.PriorityQueue,
                      inner_loops=N)

    runner.bench_func('bench_bounded_priority_queue_noblock',
                      bench_bounded_queue_noblock,
                      queue.PriorityQueue,
                      inner_loops=N)
    for arg in (0, -1, 0.00001, 0.001):
        runner.bench_time_func('gevent sleep(%s)' % (arg,),
                               bench_gevent, arg,
                               inner_loops=N)
        runner.bench_time_func('eventlet sleep(%s)' % (arg,),
                               bench_eventlet, arg,
                               inner_loops=N)
    runner.bench_time_func('spawn native no close_fds',
                           bench_spawn_native,
                           False,
                           inner_loops=N)
    runner.bench_time_func('spawn gevent no close_fds',
                           bench_spawn_gevent,
                           False,
                           inner_loops=N)

    runner.bench_time_func('spawn native close_fds',
                           bench_spawn_native,
                           inner_loops=N)
    runner.bench_time_func('spawn gevent close_fds',
                           bench_spawn_gevent,
                           inner_loops=N)
    runner.bench_time_func('imap_unordered_seq',
                           bench_imap_un_seq)

    runner.bench_time_func('imap_unordered_par',
                           bench_imap_un_par)

    runner.bench_time_func('imap_seq',
                           bench_imap_seq)

    runner.bench_time_func('imap_par',
                           bench_imap_par)

    runner.bench_time_func('map_seq',
                           bench_map_seq)

    runner.bench_time_func('map_par',
                           bench_map_par)

    runner.bench_time_func('apply',
                           bench_apply)

    runner.bench_time_func('spawn',
                           bench_spawn_wait)
    runner.bench_time_func(
        "no tracer",
        bench_no_trace,
        inner_loops=N
    )

    runner.bench_time_func(
        "trivial tracer",
        bench_trivial_tracer,
        inner_loops=N
    )

    runner.bench_time_func(
        "monitor tracer",
        bench_monitor_tracer,
        inner_loops=N
    )

    runner.bench_time_func(
        "max switch tracer",
        bench_max_switch_tracer,
        inner_loops=N
    )

    runner.bench_time_func(
        "hub switch tracer",
        bench_hub_switch_tracer,
        inner_loops=N
    )
    
if __name__ == '__main__':
    main()