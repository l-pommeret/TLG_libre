#!/usr/bin/env python3
"""Exact-ID research log from 1806.x01 to 9508.003."""
import make_research_batch_3001_4500_b14 as batch

batch.A=('1806','x01')
batch.E=('9508','003')
batch.P='tlg_3001_4500_b28'

if __name__ == '__main__':
    batch.main()
