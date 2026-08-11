#!/usr/bin/env python3
"""Exact-ID research log from 0086.038 to 3405.001."""
import make_research_batch_3001_4500_b14 as batch

batch.A=('0086','038')
batch.E=('3405','001')
batch.P='tlg_3001_4500_b15'

if __name__ == '__main__':
    batch.main()
