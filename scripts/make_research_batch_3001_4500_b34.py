#!/usr/bin/env python3
"""Exact-ID research log from 9500.003 to 1907.001."""
import make_research_batch_3001_4500_b14 as batch

batch.A=('9500','003')
batch.E=('1907','001')
batch.P='tlg_3001_4500_b34'

if __name__ == '__main__':
    batch.main()
