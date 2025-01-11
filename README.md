# Matrix Analyzer

A Python-based tool for analyzing population distribution across various dealerships using transition matrices. This project demonstrates the application of Markov chains to model and predict buyer distribution over time.

## Features
- **Transition Matrix Analysis**: Tracks buyer shifts between dealerships over several years.
- **Population Distribution Forecasting**: Calculates distributions for future years using transition matrices.
- **Preliminary Data Preparation**: Calculates initial population states and models past distributions.
- **New Dealership Impact**: Simulates the introduction of a new dealership and evaluates its effects on the market.

## Problem Statement
The project analyzes the distribution of car buyers among dealerships (Ford, Chevrolet, GM, and Toyota). It also incorporates the introduction of a new Volvo dealership to assess its impact on buyer distribution over time.

### Objectives
1. Calculate the buyer distribution after 1-6 years following the introduction of a new dealership.
2. Compute population distributions for previous years using a given model.
3. Evaluate the model's accuracy in predicting population changes.

## How It Works
1. **Input Data**: Initial buyer distribution and transition matrices for the dealerships.
2. **Matrix Operations**: Applies Markov chain principles to calculate future distributions.
3. **Simulation**: Introduces a new dealership and models the changes in buyer distribution.

### Key Components
- `initial_transition_matrix`: Represents buyer preferences among existing dealerships.
- `new_transition_matrix`: Incorporates the addition of a new dealership.
- `initial_distribution`: Starting population for all dealerships.
- **Output**: Forecasted distributions for 1-6 years and prior year calculations.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/matrix-analyzer.git


## Resume Bullet Points
Transition Matrix Analyzer for Car Buyers (Python/NumPy) | Linear Algebra                                                                           
* Built a program in Python using the NumPy library to forecast the changes in distribution of 2000 car buyers
* Applied the Markov Chain process to predict car buyer trends in the next 6 years in a given system

