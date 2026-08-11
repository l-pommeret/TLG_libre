#!/usr/bin/env python3
"""Exact-ID research log from 1265.x01 to 1271.009."""
import make_research_batch_3001_4500_b14 as batch

batch.A=('1265','x01')
batch.E=('1271','009')
batch.P='tlg_3001_4500_b31'

if __name__ == '__main__':
    batch.main()
