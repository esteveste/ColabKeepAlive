# Keep Google Colab Working

A python script that makes sure that colab continues connected

## Requirements

```bash
pip install selenium
```
## Getting Started
### How to use
Modify the email and the desired colab notebook parameters in the **colab.py**.
```python
email="" # to login in to colab
colab_url = 'https://colab.research.google.com' # colab link to execute
open_url='https://console.clouderizer.com/projects' # opens a new tab after colab starts executing 
```

You can also specify an url to open after colab starts working. Else leave it as a empty string

Then simply run:

```bash
python colab.py
```

This script was design to be used with [clouderizer](https://clouderizer.com/).(a good way to use google colab with fastai for free btw)

## Licence
MIT