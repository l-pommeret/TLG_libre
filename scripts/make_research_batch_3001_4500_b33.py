#!/usr/bin/env python3
"""Exact-ID research log from 0602.001 to 9500.002."""
import make_research_batch_3001_4500_b14 as batch

batch.A=('0602','001')
batch.E=('9500','002')
batch.P='tlg_3001_4500_b33'

if __name__ == '__main__':
    batch.main()
