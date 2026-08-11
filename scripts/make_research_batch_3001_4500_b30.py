#!/usr/bin/env python3
"""Exact-ID research log from 1797.001 to 2802.004."""
import make_research_batch_3001_4500_b14 as batch

batch.A=('1797','001')
batch.E=('2802','004')
batch.P='tlg_3001_4500_b30'

if __name__ == '__main__':
    batch.main()
