#!/usr/bin/env python3
"""Exact-ID research log from 4090.180 to 1908.003."""
import make_research_batch_3001_4500_b14 as batch

batch.A=('4090','180')
batch.E=('1908','003')
batch.P='tlg_3001_4500_b37'

if __name__ == '__main__':
    batch.main()
