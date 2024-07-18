import matplotlib.pyplot as plt


def chunktimes_vs_maxnothreads_oldNetwork():
    timing_files = [
        "/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max1THRD.txt",
        "/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max10THRDS.txt",
        "/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max30THRDS.txt",
        "/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max50THRDS.txt",
        "/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max100THRDS.txt",
        "/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max150THRDS.txt",
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
        "/home/valeriu/testing_PyActiveStorage/datafiles/5threads.txt",
        "/home/valeriu/testing_PyActiveStorage/datafiles/10threads.txt",
        "/home/valeriu/testing_PyActiveStorage/datafiles/30threads.txt",
        "/home/valeriu/testing_PyActiveStorage/datafiles/50threads.txt",
        "/home/valeriu/testing_PyActiveStorage/datafiles/100threads.txt",
        "/home/valeriu/testing_PyActiveStorage/datafiles/150threads.txt",
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

chunktimes_vs_maxnothreads_oldNetwork()
chunktimes_vs_maxnothreads_newNetwork()
