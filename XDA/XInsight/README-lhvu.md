`Setup of XInsights (including blip and java 11) can be found here: https://chatgpt.com/g/g-p-690d1cba3994819192465de38a37976d-longvu/c/692e56f0-4bc4-832e-a78e-7d9b011316f4`

`conda create --name xinsights-3.10  python=3.10`

`cd ...reliableAI/XDA/XInsight`

`pip install -r requirements.txt`

`Need an Oracle account, download and unzip: jdk-11.0.13_linux-x64_bin.tar.gz`

With this setup, Synthetic `run_one(node_num=5, idx=2)` runs successfully.

### Main changed points

- reduce simulated/synthetic data to 1000 rows
- simulate 5 node graph
- disable REAL as it is not available, not open source, only on Windows
- trying with blip for run_one2: `Synthetic.py: sl_algo = "blip", run_one2(node_num=node_num, idx=idx, sl_algo=sl_algo)`


### Output of the VSCode run on Synthetic run_one2(), after creating the csv file (from within VSCode, project starts at ..../XDA/XInsight)

```
2025-12-02 10:05:30,451 - GENERATE SYNTHETIC DAG
2025-12-02 10:05:30,452 - FORWARD SAMPLING
2025-12-02 10:05:30,475 - GENERATE PAG
/data/lhvu/projects/reliableAI/XDA/XInsight/src
2025-12-02 10:05:30,530 - LEARNING SKELETON [BLIP]
Starting Fast Adjacency Search.
Depth=1, working on node 4: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5/5 [00:00<00:00, 705.42it/s]
Finishing Fast Adjacency Search.
{'f1': 0.5, 'precision': 1.0, 'recall': 0.3333333333333333, 'skl_f1': 0.5, 'skl_precision': 1.0, 'skl_recall': 0.3333333333333333, 'node num': 5, 'idx': 2}
```