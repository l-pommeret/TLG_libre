#!/usr/bin/env python3
"""Exact-ID research log from 2482.001 to 4357.002."""
import make_research_batch_3001_4500_b14 as batch

batch.A=('2482','001')
batch.E=('4357','002')
batch.P='tlg_3001_4500_b38'

if __name__ == '__main__':
    batch.main()
