# insuranceqa-corpus-zh

## clone

```
git clone --recursive git@git.kazejs.xyz:KB-QA/insuranceqa-corpus.git
```

## config
```
cp _env.sample _env
source _env
```

## jsonfiy

```
python jsonfiy.py
```

## translate

Convert gz data to json

```
ava --timeout=10h js/main.js
```

Checkout Testcase ```process label2answer``` and ```process InsuranceQA.question.anslabel.raw``` for different tasks.