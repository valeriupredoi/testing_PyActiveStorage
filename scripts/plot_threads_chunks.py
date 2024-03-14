import matplotlib.pyplot as plt


def chunktimes_vs_maxnothreads():
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
    plt.scatter(counts05s, threads)
    plt.plot(counts05s, threads, label=">0.5s")
    plt.scatter(counts1s, threads)
    plt.plot(counts1s, threads, label=">1s")
    plt.xlabel('No of chunks with chunk time >0.5s and >1s')
    plt.ylabel('No max threads')
    plt.title("3400 chunks bnl file: counts chunk time >0.5s and >1s vs no max threads")
    plt.grid()
    plt.legend()
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile_ChunkTimeMore-1s_vs_NoMaxThreads.png")


chunktimes_vs_maxnothreads()
