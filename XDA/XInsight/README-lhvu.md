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