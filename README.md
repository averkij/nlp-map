# Language models diversity on the map

👉 Map is here: https://averkij.github.io/nlp-map/

Languages of the recent multilingual LMs visualized on the map. Made with [plotly](https://plotly.com/).

![](https://i.imgur.com/C9psk9n.png)

## Dataset

- https://www.kaggle.com/datasets/rtatman/world-atlas-of-language-structures
- With some modifications like adding Esperanto somewhere in Antarctica.

## Contribute

- To add new model on the map, please inspect the `langs.csv` dataset and add a new boolean column.
- Set desired languages to True.
- Regenerate the html with `make_html.py` script.
- Make a PR.
