#!/usr/bin/env python3
"""Exact-ID research log from 3092.020 to 3230.008."""
import make_research_batch_3001_4500_b14 as batch

batch.A=('3092','020')
batch.E=('3230','008')
batch.P='tlg_3001_4500_b25'

if __name__ == '__main__':
    batch.main()
