import matplotlib.pyplot as plt
import numpy as np


def hist_chunk_times():
    with open("chunk_times_64chunks.txt", "r") as datafile:
        data = [float(l) for l in datafile.readlines()]
    plt.hist(data, density=False, bins=20)
    plt.grid()
    plt.ylabel('Counts')
    plt.xlabel('Chunk process time [s]')
    plt.title("64 chunks def file")
    plt.savefig("/home/valeriu/Desktop/64ChunksFile_Chunks_Times_Hist.png")
    plt.close()


def hist_chunk_sizes():
    with open("chunk_sizes_64chunks.txt", "r") as datafile:
        data = [float(l) / 1000. for l in datafile.readlines()]
    plt.hist(data, density=False, bins=20, color="r")
    plt.grid()
    plt.ylabel('Counts')
    plt.xlabel('Chunk sizes [kb]')
    plt.title("64 chunks def file")
    plt.savefig("/home/valeriu/Desktop/64ChunksFile_Chunks_Sizes_Hist.png")
    plt.close()


def size_vs_time():
    with open("chunk_times_64chunks.txt", "r") as datafile:
        times = [float(l) for l in datafile.readlines()]
    with open("chunk_sizes_64chunks.txt", "r") as datafile:
        sizes = [float(l) / 1000. for l in datafile.readlines()]
    data = [(s, t) for s, t in zip(sizes, times)]
    data = sorted(data, key=lambda tup: tup[0])
    x = [d[0] for d in data]
    y = [d[1] for d in data]
    avg_time = np.mean(y)
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.xlabel('Chunk sizes [kb]')
    plt.ylabel('Chunk process time [s]')
    plt.axhline(avg_time, color="g")
    plt.title(f"64 chunks def file; avg time {avg_time}s")
    plt.grid()
    plt.savefig("/home/valeriu/Desktop/64ChunksFile_Sizes_vs_Times.png")


hist_chunk_times()
hist_chunk_sizes()
size_vs_time()
