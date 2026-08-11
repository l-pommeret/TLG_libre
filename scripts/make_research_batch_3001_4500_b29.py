#!/usr/bin/env python3
"""Exact-ID research log from 1250.001 to 4093.007."""
import make_research_batch_3001_4500_b14 as batch

batch.A=('1250','001')
batch.E=('4093','007')
batch.P='tlg_3001_4500_b29'

if __name__ == '__main__':
    batch.main()
