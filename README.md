
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
- time to run optimized Kerchunk-based engine: 95s via max 100 threads
- time to run optimized Kerchunk-based engine: 720s via max 1 (one) thread

Chunks times (time to run each `_process_chunk()` instance; that includes internal slicing/indexing and external Reductionist) and sizes analysis shows the following:

- max 100 threads: bimodal distribution of chunk process times: chi-squared distribution (implying a parametric distribution) and non-parametric Gaussian distribution; mode means around 0.3s and 2.8s

![max100ThreadsChunkTimes](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/3400ChunksFile-max100THRDS_Chunks_Times_Hist.png)

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
- time to run optimized Kerchunk-based engine: 10s via max 100 threads
- time to run optimized Kerchunk-based engine: 25s via max 1 (one) thread 

Chunks times (time to run each `_process_chunk()` instance; that includes internal slicing/indexing and external Reductionist) and sizes analysis shows the following:

- max 100 threads: bimodal distribution of chunk process times: chi-squared distribution (implying a parametric distribution) and non-parametric Gaussian distribution; mode means around 1.5s and 2.8s

![max100ThreadsChunkTimes](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/64ChunksFile-max100THRDS_Chunks_Times_Hist.png)

- max 1 (one) thread: single-mode distribution of chunk process times: chi-squared distribution (implying a parametric distribution), mode mean at 0.3s

![max1ThreadChunkTimes](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/64ChunksFile-max1THRD_Chunks_Times_Hist.png)

Chunks sizes:

![chunkSize34001](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/64ChunksFile-max100THRDS_Chunks_Sizes_Hist.png)

Chunk sizes show a bimodal distribution with a mode around 3800kb and another mode around 4400kb.

The Gaussian mode for chunks analysis time for 100 threads is explained by the time spent inactive, while threads become available; the real time needed to process a single chunk is 0.3s; this is obvious from the chunks size vs time plot:

![ChunksvsTimes64](https://github.com/valeriupredoi/testing_PyActiveStorage/blob/main/plots/64ChunksFile-max1THRD_Sizes_vs_Times_Zoom.png)

**Conclusion: single-threading with max 1 thread gets us around 0.3s of process time for one chunk of average size of 4000kb. Which is only marginally longer than 0.2s for a chunk 60 times smaller!**

# Provenance

- in `3400ChunksFile_*png` and `64ChunksFile_*png` plots I used:
  - Kerchunk-based pipeline
  - max 100 threads AND max 1 thread (`max100THRDS` and `max1THRD` plot and datafile labels)
  - 3400 chunks file: `ch330a.pc19790301-bnl.nc`
  - 64 chunks file: `ch330a.pc19790301-def.nc`
  - times: time it took each `_process_chunk()` to run
  - sizes: chunk `size` key-val that enters in `request_data` dictionary to Reductionist
  - runs on my computer at work `Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz`
