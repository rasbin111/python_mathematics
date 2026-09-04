# Install dependencies
We have use matplotlib for plotting 

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Plot

1. Can plot using jupyter notebook 
2. Plot on terminal  

To plot on terminal, install tk. For Arch,
```bash
sudo pacman -S tk
```

And add this line 
```python
import matplotlib
matplotlib.use("TkAgg")
```
