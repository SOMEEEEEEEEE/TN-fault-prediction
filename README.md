# Telecom Fault Prediction (Exploratory Project)

## Overview
This project is an exploratory study on predicting short-term network faults using historical telecom incident data.

The goal is to understand whether temporal and device-level patterns can provide useful signals for fault prediction.

## Motivation
In real-world telecom operations, large volumes of fault logs are generated daily.  
This project explores whether these logs can be used to identify early warning signals and improve operational efficiency.

This work was conducted as a lightweight ML exploration prior to building a full AIOps system (LogInsight).

## Data
The dataset contains telecom network fault records with fields such as:
- timestamp
- location
- device_id
- fault_type

Note: The full dataset is not included in this repository due to confidentiality. A sample schema is provided in `data/sample.csv`.

## Modeling Approach
- time-based handling delays
- fault severity indicators
- region and team information
- repeated ticket frequency

A LightGBM baseline classifier is used to estimate the probability of ticket timeout.

## Status
Exploratory baseline model.