__author__ = 'ricardo'

import multiprocessing

def find_solution():
    """worker function"""
    print ('Worker')
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=find_solution)
        jobs.append(p)
        p.start()