# House-Prediction-Using-ML

A Machine Learning project built using Linear Regression that predicts the approximate flat size (BHK) based on the user's budget in Kolkata.

## Technologies Used

* Python
* Scikit-Learn
* Matplotlib
* Docker

## Clone Repository

```bash
git clone <repository-url>
cd House-Prediction-Using-ML
```

## Build Docker Image

```bash
docker build -t house-prediction .
```

## Run Project

```bash
docker run -it house-prediction
```

## Example

Input:

```text
Enter Your Amount in Lakh:- 70
```

Output:

```text
if you budget is 70 Lakh/- you buy 2.75 Bhk Flat in kolkata
```

## Project Structure

```text
House-Prediction-Using-ML
├── House_prediction.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Author

Shripada Mahato
BCA Student | Machine Learning Enthusiast
