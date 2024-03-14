## Provenance

- in `3400ChunksFile_*png` and `64ChunksFile_*png` plots I used:
  - Kerchunk-based pipeline
  - max 100 threads AND max 1 thread (`max100THRDS` and `max1THRD` plot and datafile labels)
  - 3400 chunks file: `ch330a.pc19790301-bnl.nc`
  - 64 chunks file: `ch330a.pc19790301-def.nc`
  - times: time it took each `_process_chunk()` to run
  - sizes: chunk `size` key-val that enters in `request_data` dictionary to Reductionist
  - runs on my computer at work `Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz`
