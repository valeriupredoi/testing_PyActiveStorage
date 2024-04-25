
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Table of Contents
-----------------
* [PyActiveStorage](#PyActiveStorage)
* [Tests](#Tests)
* [Provenance](#Provenance)

# PyActiveStorage

Seee the [PyActiveStorage GitHub repository](https://github.com/valeriupredoi/PyActiveStorage).

# Tests

We ran tests with two large netCDF4 files, chunked differently:

- 3400 HDF5 chunks file: `ch330a.pc19790301-bnl.nc`
- 64 HDF5 chunks file: `ch330a.pc19790301-def.nc`

Using the two approaches we have available:

- [Kerchunk](https://github.com/fsspec/kerchunk)-based engine
- [bnlawrence/Pyfive](https://github.com/bnlawrence/pyfive/tree/issue60)-based engine

## Kerchunk-based engine: 3400 HDF5 chunks

- see specific code used, and timing results in https://github.com/valeriupredoi/PyActiveStorage/issues/191 with a TL;DR beow
- time to run optimized Kerchunk-based engine:
  - single Reductionist machine 95s via max 100 threads
  - 3x Reductionist machines 75-80s (so about 16-20% faster overall, about 25-30% better for just Reductionist ops)
  - bear in mind time in Kerchunk (`_via_kerchunk()`) is 25s flat
- time to run optimized Kerchunk-based engine: 720s via max 1 (one) thread

Chunks times (time to run each `_process_chunk()` instance; that includes internal slicing/indexing and external Reductionist) and sizes analysis shows the following:

- max 100 threads: bimodal distribution of chunk process times: chi-squared distribution (implying a parametric distribution) and non-parametric Gaussian distribution; mode means around 0.3s and 2.8s

![max100ThreadsChunkTimes](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile-max100THRDS_Chunks_Times_Hist.png)

- max 150 threads:

Single Reductionist Machine

![max100ThreadsChunkTimes](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile-max150THRDS_Chunks_Times_Hist.png)

3x Reductionist Machines

![max100ThreadsChunkTimes](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile-max150THRDS-3RED-Machines_Chunks_Times_Hist.png)

**3400 chunks, 150 client threads: 1x vs 3x Reductionist machines**

- one machine average chunk processing time: 2.74s
- three machines average chunk processing time: 2.19s
- **gain from 3x vs 1x machines: 20% speedup per average chunk processing time**
- one machine total chunk processing time: 9325s
- three machines average chunk processing time: 7432s
- **gain from 3x vs 1x machines: 20% speedup per total chunk processing time**

- max 1 (one) thread: single-mode distribution of chunk process times: chi-squared distribution (implying a parametric distribution), mode mean at 0.2s

![max1ThreadChunkTimes](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile-max1THRD_Chunks_Times_Hist.png)

Chunks sizes:

![chunkSize34001](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile-max100THRDS_Chunks_Sizes_Hist.png)
![chunkSize34002](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile-max1THRD_Chunks_Sizes_Hist.png)

Chunk sizes show a bimodal distribution with a heavy mode around 80-85kb and a much lighter mode around 50kb.

The Gaussian mode for chunks analysis time for 100 threads is explained by the time spent inactive, while threads become available; the real time needed to process a single chunk is 0.2-0.3s; this is obvious from the chunks size vs time plot:

![ChunksvsTimes3400](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile-max1THRD_Sizes_vs_Times.png)

**Conclusion: multi-threading with max 100 threads gets us around 0.2s or about 3s of process time for one chunk of average size of 70kb - the latter time is 90% comprised of thread waiting and only 10% of actual analysis time; using a single thread shows us the real chunk analysis time is about 0.2 for a chunk of averge size of 70kb.**

## Kerchunk-based engine: 64 HDF5 chunks

- see specific code used, and timing results in https://github.com/valeriupredoi/PyActiveStorage/issues/191 with a TL;DR beow
- time to run optimized Kerchunk-based engine:
  - single Reductionist machine: 10s via max 100 client threads
  - 3x Reductionist machines: 9s via max 100 client threads
  - bear in mind time via Kerchunk (`_via_kerchunk()`) is 5-6s flat, so 50-60% of total runtime
- time to run optimized Kerchunk-based engine: 25s via max 1 (one) thread 

Chunks times (time to run each `_process_chunk()` instance; that includes internal slicing/indexing and external Reductionist) and sizes analysis shows the following:

- max 100 threads: bimodal distribution of chunk process times: chi-squared distribution (implying a parametric distribution) and non-parametric Gaussian distribution; mode means around 1.5s and 2.8s

Single Reductionist machine

![max100ThreadsChunkTimes](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/64ChunksFile-max100THRDS_Chunks_Times_Hist.png)

3x Reductionist Machines

![max100ThreadsChunkTimes](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/64ChunksFile-max100THRDS-3RED-Machines_Chunks_Times_Hist.png)

**64 chunks, 100 client threads: 1x vs 3x Reductionist machines**

- one machine average chunk processing time: 2.43s
- three machines average chunk processing time: 1.84s
- **gain from 3x vs 1x machines: 24% speedup per average chunk processing time**
- one machine total chunk processing time: 156s
- three machines average chunk processing time: 118s
- **gain from 3x vs 1x machines: 24% speedup per total chunk processing time**

- max 1 (one) thread: single-mode distribution of chunk process times: chi-squared distribution (implying a parametric distribution), mode mean at 0.3s

![max1ThreadChunkTimes](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/64ChunksFile-max1THRD_Chunks_Times_Hist.png)

Chunks sizes:

![chunkSize34001](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/64ChunksFile-max100THRDS_Chunks_Sizes_Hist.png)

Chunk sizes show a bimodal distribution with a mode around 3800kb and another mode around 4400kb.

The Gaussian mode for chunks analysis time for 100 threads is explained by the time spent inactive, while threads become available; the real time needed to process a single chunk is 0.3s; this is obvious from the chunks size vs time plot:

![ChunksvsTimes64](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/64ChunksFile-max1THRD_Sizes_vs_Times_Zoom.png)

**Conclusion: single-threading with max 1 thread gets us around 0.3s of process time for one chunk of average size of 4000kb. Which is only marginally longer than 0.2s for a chunk 60 times smaller!**

## Chunk times vs max number of threads

Runs with different max threads and counting the number of chunks that have analysis times >0.5s and >1.0s - given that a normal analysis time for any given chunk is in the region of 0.3s, this accounts for numbers of chunks that take roughly twice or three times a normal analysis time (mostly due to thread freeing blockages).

![ChunksTimesvsMaxThreads3400](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile_ChunkTimeMore-1s_vs_NoMaxThreads.png)

## Understanding Reductionist

### Response times

We measured how long it takes for each instance of Reductionist's response time in `activestorage.reductionist.py::reduce_chunk()`:

```
response = request(session, url, request_data)
```

and found out that, per chunk, the `response` time is always close to or identical to the time `activestorage.active._process_chunk()` takes, as seen from this plot:

![ChunksvsTimes64](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile-max150THRD_Reductionist_Chunks_Times.png)

in that plot, the red histogram (behind the transparent blue histogram) is the Reductionist `response` times, whereas the blue (transparency=50%) histogram is the histogram of Active's `_process_chunk()`. A clear bimodal distribution is visible.

Furthermore, we looked at timeseries of Reductionist `response` times, both for the 3400 chunks, and for the 64 chunks files

![ChunksvsTimes64series](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile-max150THRD_Reductionist_Times_Timeseries.png)
![OtherSeries](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/64ChunksFile-max150THRD_Reductionist_Times_Timeseries.png)

These plots have been obtained from running Active with `max_threads=150`. In the case of the file with 3400 chunks a lot of small chunks are being prepared and sent to Reductionist via 150 Active threads, resulting in saturation and wait times for a LOT of the chunks of roughly 5s.

Using one single thread by Active, results give a muchsmaller Reductionist `response` time, and consistent accross the run:

![ChunksvsTimes64series](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile-max1THRD_Reductionist_Times_Timeseries.png)

We note no particlar correlation between the Reductionist's `response` time and chunk size, as seen from this plot:

![chunksTimes](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/64ChunksFile-max150THRDS_Sizes_vs_ReductionistResponseTimes.png)

and

![chunksTimes](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile-max1THRD_Sizes_vs_ReductionistResponseTimes.png)

# Provenance

- in `3400ChunksFile_*png` and `64ChunksFile_*png` plots I used:
  - Kerchunk-based pipeline
  - max 100 threads AND max 1 thread (`max100THRDS` and `max1THRD` plot and datafile labels)
  - 3400 chunks file: `ch330a.pc19790301-bnl.nc`
  - 64 chunks file: `ch330a.pc19790301-def.nc`
  - times: time it took each `_process_chunk()` to run
  - sizes: chunk `size` key-val that enters in `request_data` dictionary to Reductionist
  - runs on my computer at work `Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz`
