import matplotlib.pyplot as plt
import numpy as np


def hist_chunk_times():
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_64chunks-max100THRDS.txt", "r") as datafile:
        data = [float(l) for l in datafile.readlines()]
    plt.hist(data, density=False, bins=20)
    plt.grid()
    plt.ylabel('Counts')
    plt.xlabel('Chunk process time [s]')
    plt.ylim(0, 10)
    plt.xlim(0, 3.5)
    plt.axvline(np.mean(data), color="r")
    plt.title(f"64 chunks (max 100 threads, 1x (single) Reductionist Machines) def file\nmean chunk time {np.mean(data)}\ntotal chunk time {np.sum(data)}")
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/64ChunksFile-max100THRDS_Chunks_Times_Hist.png")
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
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/reductionist_response_times_3400chunks-max1THRD.txt", "r") as datafile:
        times = [float(l) for l in datafile.readlines()]
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_sizes_3400chunks-max1THRD-run2.txt", "r") as datafile:
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
    plt.ylabel('Reductionist response time [s]')
    plt.axhline(avg_time, color="g")
    plt.title(f"3400 chunks (max 1 thread) bnl file; avg time {avg_time}s\nKerchunk-based Total run on 2.6GHz CPU: 12min")
    plt.grid()
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile-max1THRD_Sizes_vs_ReductionistResponseTimes.png")


def hist_reductionist_response():
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/reductionist_response_times_3400chunks-max150THRDS.txt", "r") as datafile:
        reductionist_times = [float(l) for l in datafile.readlines()]
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max150THRDS-run2.txt", "r") as datafile:
        chunk_times = [float(l) for l in datafile.readlines()]
    plt.hist(reductionist_times, density=False, bins=50, color="r", label="Red. Time")
    plt.hist(chunk_times, density=False, bins=50, color="b", alpha=0.5, label="Tot. Chunk Time")
    plt.grid()
    plt.legend()
    plt.ylabel('Counts')
    plt.xlabel('Reductionist Response Time / Total Chunk Time [s]')
    plt.title("3400 chunks (max 150 thread) bnl file\nRed. Time: response = request(session, url, request_data)\nChunk time: _process_chunk(...)")
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile-max150THRD_Reductionist_Chunks_Times.png")
    plt.close()


def timeseries_reductionist_response():
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/reductionist_response_times_3400chunks-max1THRD.txt", "r") as datafile:
        reductionist_times = [float(l) for l in datafile.readlines()]
    x = range(len(reductionist_times))
    plt.scatter(x, reductionist_times, color="r")
    plt.grid()
    plt.xlabel('Synthetic time')
    plt.ylabel('Reductionist Response Times per Chunk [s]')
    plt.title("3400 chunks (max 1 thread) bnl file\nRed. Time: response = request(session, url, request_data)")
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile-max1THRD_Reductionist_Times_Timeseries.png")
    plt.close()


def timeseries_chunk_sizes():
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_sizes_3400chunks-max150THRDS.txt", "r") as datafile:
        csizes = [float(l) / 1000. for l in datafile.readlines()]
    x = range(len(csizes))
    plt.scatter(x, csizes, color="g")
    plt.grid()
    plt.xlabel('Synthetic time')
    plt.ylabel('Chunk Sizes [kb]')
    plt.title("3400 chunks (max 150 thread) bnl file")
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile-max150THRD_Chunks_Sizes_Timeseries.png")
    plt.close()


def timeseries_reductionist_response_threadsON():
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/reductionist_response_times_3400chunks_NumThreadsOn50.txt", "r") as datafile:
        reductionist_times = [float(l) for l in datafile.readlines()]
    x = range(len(reductionist_times))
    plt.scatter(x, reductionist_times, color="r")
    plt.grid()
    plt.xlabel('Synthetic time')
    plt.ylabel('Reductionist Response Times per Chunk [s]')
    plt.title("3400 chunks (max 150 thread) bnl file W/ NUM_THREADS=50\nRed. Time: response = request(session, url, request_data)")
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile-max150THRD_Reductionist_Times_Timeseries_wTHREADSON50.png")
    plt.close()


def hist_chunk_times_NN():
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max150THRDS_ThreeReducts.txt", "r", encoding="utf-8") as datafile:
        data0 = [float(l) for l in datafile.readlines()]
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max150THRDS_ThreeReducts_NewNetork_OldProxy.txt", "r", encoding="utf-8") as datafile:
        data1 = [float(l) for l in datafile.readlines()]
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max150THRDS_ThreeReducts_NewNetork_NewProxy.txt", "r", encoding="utf-8") as datafile:
        data2 = [float(l) for l in datafile.readlines()]
    plt.hist(data0, density=False, bins=100, label="oldNwk")
    plt.hist(data1, density=False, bins=100, label="newNwk old proxy")
    plt.hist(data2, density=False, bins=100, label="newNwk new proxy")
    plt.grid()
    plt.ylabel('Counts')
    plt.xlabel('Chunk process time [s]')
    # plt.ylim(0, 10)
    plt.xlim(0, 10)
    # plt.axvline(np.mean(data1), color="b")
    # plt.axvline(np.mean(data2), color="k")
    plt.title(f"3400 chunks (max 150 threads, 3x (activeh) Reductionist)\nmean chunk {np.round(np.mean(data0), 3)} - {np.round(np.mean(data1), 3)} - {np.round(np.mean(data2), 3)} s\nSTD chunk {np.round(np.std(data0), 3)} - {np.round(np.std(data1), 3)} - {np.round(np.std(data2), 3)} s")
    plt.legend()
    # plt.show()
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile-max150THRDS-3RED-Machines_New-Old-Network-Proxy_Chunks_Times_Hist.png")
    plt.close()


def hist_chunk_times_NN_1Reduct():
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max150THRDS.txt", "r", encoding="utf-8") as datafile:
        data0 = [float(l) for l in datafile.readlines()]
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max150THRDS_OneReducts_NewNetork_OldProxy.txt", "r", encoding="utf-8") as datafile:
        data1 = [float(l) for l in datafile.readlines()]
    with open("/home/valeriu/testing_PyActiveStorage/datafiles/chunk_times_3400chunks-max150THRDS_OneReducts_NewNetork_NewProxy.txt", "r", encoding="utf-8") as datafile:
        data2 = [float(l) for l in datafile.readlines()]
    plt.hist(data0, density=False, bins=100, label="oldNwk")
    plt.hist(data1, density=False, bins=100, label="newNwk old proxy")
    plt.hist(data2, density=False, bins=100, label="newNwk new proxy")
    plt.grid()
    plt.ylabel('Counts')
    plt.xlabel('Chunk process time [s]')
    # plt.ylim(0, 10)
    plt.xlim(0, 10)
    # plt.axvline(np.mean(data1), color="b")
    # plt.axvline(np.mean(data2), color="k")
    plt.title(f"3400 chunks (max 150 threads, 1x (active) Reductionist)\nmean chunk {np.round(np.mean(data0), 3)} - {np.round(np.mean(data1), 3)} - {np.round(np.mean(data2), 3)} s\nSTD chunk {np.round(np.std(data0), 3)} - {np.round(np.std(data1), 3)} - {np.round(np.std(data2), 3)} s")
    plt.legend()
    # plt.show()
    plt.savefig("/home/valeriu/testing_PyActiveStorage/plots/3400ChunksFile-max150THRDS-1RED-Machines_New-Old-Network-Proxy_Chunks_Times_Hist.png")
    plt.close()

# hist_chunk_times()
# hist_chunk_sizes()
# size_vs_time()
# hist_reductionist_response()
# timeseries_reductionist_response()
# timeseries_chunk_sizes()
# timeseries_reductionist_response_threadsON()
# timeseries_reductionist_response()
# size_vs_time()
# timeseries_reductionist_response()
# hist_chunk_times()
hist_chunk_times_NN()
hist_chunk_times_NN_1Reduct()
