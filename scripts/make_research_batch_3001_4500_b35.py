#!/usr/bin/env python3
"""Exact-ID research log from 1907.002 to 2877.001."""
import make_research_batch_3001_4500_b14 as batch

batch.A=('1907','002')
batch.E=('2877','001')
batch.P='tlg_3001_4500_b35'

if __name__ == '__main__':
    batch.main()
