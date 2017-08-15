# knock-knock-bot

## Introduction

**knock-knock-bot** is a [kakaotalk plus-friends](https://center-pf.kakao.com/login) chatbot.

## Feature

- Tracking a shipment in kakaotalk
- Scheduling a pickup in kakaotalk

## Installation and Settings

### Installation

```bash
$ pip install -r requirements.txt
```

### Settings

You have to set `API_KEY` from [`SweetTracker`](https://tracking.sweettracker.co.kr)

**../knock-knock-bot/app/config.py**

```python
...

API_KEY = '***********'
```

### Run!

```bash
$ python run.py
```