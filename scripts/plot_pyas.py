import matplotlib.pyplot as plt
import numpy as np


def hist_chunk_times():
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max1THRD.txt", "r") as datafile:
        data = [float(l) for l in datafile.readlines()]
    plt.hist(data, density=False, bins=50)
    plt.grid()
    plt.ylabel('Counts')
    plt.xlabel('Chunk process time [s]')
    plt.title("3400 chunks (max 1 thread) bnl file")
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile-max1THRD_Chunks_Times_Hist.png")
    plt.close()


def hist_chunk_sizes():
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_sizes_3400chunks-max1THRD.txt", "r") as datafile:
        data = [float(l) / 1000. for l in datafile.readlines()]
    plt.hist(data, density=False, bins=50, color="r")
    plt.grid()
    plt.ylabel('Counts')
    plt.xlabel('Chunk sizes [kb]')
    plt.title("3400 chunks (max 1 thread) bnl file")
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile-max1THRD_Chunks_Sizes_Hist.png")
    plt.close()


def size_vs_time():
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max1THRD.txt", "r") as datafile:
        times = [float(l) for l in datafile.readlines()]
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_sizes_3400chunks-max1THRD.txt", "r") as datafile:
        sizes = [float(l) / 1000. for l in datafile.readlines()]
    data = [(s, t) for s, t in zip(sizes, times)]
    data = sorted(data, key=lambda tup: tup[0])
    x = [d[0] for d in data]
    y = [d[1] for d in data]
    avg_time = np.mean(y)
    plt.scatter(x, y)
    plt.plot(x, y)
    # plt.ylim([0.1, 0.5])
    plt.xlabel('Chunk sizes [kb]')
    plt.ylabel('Chunk process time [s]')
    plt.axhline(avg_time, color="g")
    plt.title(f"3400 chunks (max 1 thread) bnl file; avg time {avg_time}s\nKerchunk-based Total run on 2.6GHz CPU: 12min")
    plt.grid()
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile-max1THRD_Sizes_vs_Times.png")


hist_chunk_times()
hist_chunk_sizes()
size_vs_time()
