from os import makedirs
from os.path import join
import argparse
from concurrent.futures import ThreadPoolExecutor
from subprocess import call

parser = argparse.ArgumentParser()
parser.add_argument('--rollouts', type=int, help="Total number of rollouts.")
parser.add_argument('--threads', type=int, help="Number of threads")
parser.add_argument('--rootdir', type=str, help="Directory to store rollout "
                    "directories of each thread")
parser.add_argument('--policy', type=str, choices=['brown', 'white'],
                    help="Policy for rollout directories of each thread",
                    default='brown')
args = parser.parse_args()

rpt = args.rollouts // args.threads + 1

def _threaded_generation(i):
    tdir = join(args.rootdir, 'thread_{}'.format(i))
    makedirs(tdir, exist_ok=True)
    cmd = ["python", "-m", "data.carracing", "--dir",
            tdir, "--rollouts", str(rpt), "--policy", args.policy]
    cmd = " ".join(cmd)
    print(cmd)
    call(cmd, shell=True)
    return True

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(_threaded_generation, i) for i in range(args.threads)]
        results = [future.result() for future in futures]
