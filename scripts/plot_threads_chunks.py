import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

datadir = Path(__file__).parent.parent/'datafiles'
plotdir = Path(__file__).parent.parent/'plots'


def chunktimes_vs_maxnothreads_oldNetwork():
    timing_files = [
        datadir/"chunk_times_3400chunks-max1THRD.txt",
        datadir/"chunk_times_3400chunks-max10THRDS.txt",
        datadir/"chunk_times_3400chunks-max30THRDS.txt",
        datadir/"chunk_times_3400chunks-max50THRDS.txt",
        datadir/"chunk_times_3400chunks-max100THRDS.txt",
        datadir/"chunk_times_3400chunks-max150THRDS.txt",
    ]
    counts05s = []
    counts1s = []
    for timing_file in timing_files:
        with open(timing_file, "r") as datafile:
            times = [float(l) for l in datafile.readlines()]
            times_05s = [t for t in times if t > 0.5]  # threshold at 0.5s
            times_1s = [t for t in times if t > 1.0]  # threshold at 1s
            counts05s.append(len(times_05s))
            counts1s.append(len(times_1s))
    threads = [1., 10., 30., 50., 100., 150.]
    plt.scatter(threads, counts05s)
    plt.plot(threads, counts05s, label=">0.5s oldnet")
    plt.scatter(threads, counts1s)
    plt.plot(threads, counts1s, label=">1s oldnet")
    plt.ylabel('no of chunks with chunk time >0.5s and >1s')
    plt.xlabel('No max threads')
    plt.title("3400 chunks bnl file (old network): counts chunk time >0.5s and >1s vs max threads")
    plt.grid()
    plt.legend()
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile_ChunkTimeMore-1s_vs_NoMaxThreads.png")


def chunktimes_vs_maxnothreads_newNetwork():
    timing_files = [
        datadir/"5threads.txt",
        datadir/"10threads.txt",
        datadir/"30threads.txt",
        datadir/"50threads.txt",
        datadir/"100threads.txt",
        datadir/"150threads.txt",
    ]
    counts05s = []
    counts1s = []
    for timing_file in timing_files:
        with open(timing_file, "r") as datafile:
            times = [float(l) for l in datafile.readlines()]
            times_05s = [t for t in times if t > 0.5]  # threshold at 0.5s
            times_1s = [t for t in times if t > 1.0]  # threshold at 1s
            counts05s.append(len(times_05s))
            counts1s.append(len(times_1s))
    threads = [1., 10., 30., 50., 100., 150.]
    plt.scatter(threads, counts05s)
    plt.plot(threads, counts05s, label=">0.5s newnet")
    plt.scatter(threads, counts1s)
    plt.plot(threads, counts1s, label=">1s newnet")
    plt.ylabel('no of chunks with chunk time >0.5s and >1s')
    plt.xlabel('No max threads')
    plt.title("3400 chunks bnl file (new network)\ncounts chunk time >0.5s and >1s vs max threads")
    plt.grid()
    plt.grid()
    plt.legend()
    plt.show()
    # plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile_ChunkTimeMore-1s_vs_NoMaxThreads_NewNetwork.png")


# total times for 3400 bnl file with new proxy / old proxy
# --- new proxy
npd = [np.mean([50.0, 48.9, 48.5]),
       np.mean([37.3, 31.4, 35.7]),
       np.mean([22.9, 26.0, 25.9]),
       np.mean([24.8, 23.4, 22.1]),
       np.mean([21.6, 24.2, 26.9]),
       np.mean([21.9, 24.3, 24.4]),
]

# --- old proxy
opd = [np.mean([52.8, 55.6]),
       np.mean([33.5, 35.0]),
       np.mean([29.1, 25.7]),
       np.mean([26.6, 28.1]),
       np.mean([27.3, 25.9]),
       np.mean([26.9, 28.1]),
]


def totalTimes_vs_maxnothreads_NewNetwork(title=True,format='png'):
    threads = [1., 10., 30., 50., 100., 150.]
    old_netwk_timing_files = [
        datadir/"chunk_times_3400chunks-max1THRD.txt",
        datadir/"chunk_times_3400chunks-max10THRDS.txt",
        datadir/"chunk_times_3400chunks-max30THRDS.txt",
        datadir/"chunk_times_3400chunks-max50THRDS.txt",
        datadir/"chunk_times_3400chunks-max100THRDS.txt",
        datadir/"chunk_times_3400chunks-max150THRDS.txt",
    ]
    old_net = []
    for timing_file, n in zip(old_netwk_timing_files, threads):
        with open(timing_file, "r") as datafile:
            times = [float(l) for l in datafile.readlines()]
            old_net.append(np.sum(times) / n + 20.)
    new_proxy = npd
    old_proxy = opd
    plt.scatter(threads, old_net)
    plt.plot(threads, old_net, label="ON")
    plt.scatter(threads, old_proxy)
    plt.plot(threads, old_proxy, label="NN-OP")
    plt.scatter(threads, new_proxy)
    plt.plot(threads, new_proxy, label="NN-NN")
    plt.grid()
    plt.ylim(10, 1000)
    plt.semilogy()
    plt.ylabel('Time [s]')
    plt.xlabel('No max threads')
    if title:
        plt.title("3400 chunks bnl file (old network (ON), new network(NN))\ntotal runtime vs max threads")
    plt.legend()
    # plt.show()
    if format == 'pdf':
        ff = "pdf/3400ChunksFile_RunTimevsMaxThreads_OldNewNetwork.pdf"
    else:
        ff = "3400ChunksFile_RunTimevsMaxThreads_OldNewNetwork.png"
    plt.savefig(plotdir/ff)

# chunktimes_vs_maxnothreads_oldNetwork()
# chunktimes_vs_maxnothreads_newNetwork()
totalTimes_vs_maxnothreads_NewNetwork(title=False, format='pdf')
