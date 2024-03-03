# This repository contains the backend code for our [mega puzzle solver](https://github.com/kylewandishin/mega-problem-solver-backend/tree/main/semantle) as well as additional development code for testing diifferent approaches
The flask server/backend API for our extension is within [app.py](https://github.com/kylewandishin/mega-problem-solver-backend/blob/main/semantle/app.py)

The flask app relies on our semantle solving algorithm which uses gensim and the [GoogleNews word2vec model](https://github.com/mmihaltz/word2vec-GoogleNews-vectors?tab=readme-ov-file)

to run, make sure to install the required dependencies
```
pip install gensim
```

Also move and extract the `GoogleNews-vectors-negative300.bin.gz` into the [/semantle/ folder](https://github.com/kylewandishin/mega-problem-solver-backend/tree/main/semantle)

After, run app.py
```
cd semantle
python3 app.py
```

To utilise the self-hosted backend, you would have to edit the site permissions for semantle and change `Insecure content` to `Allow`
