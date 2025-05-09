# Email Spam Classifier 📧🛡️

This project is a simple machine learning-based email spam classifier built using Python and Scikit-learn. It uses TF-IDF feature extraction and a Logistic Regression model to classify emails as "spam" or "ham" (not spam).

## 📁 Dataset

The project uses a CSV file (`mail_data.csv`) containing labeled messages. Each message is categorized as either:
- **spam**: Unwanted emails
- **ham**: Legitimate emails

## 🔍 Features

- Text preprocessing using TF-IDF (`TfidfVectorizer`)
- Train-test split (80/20)
- Model training using Logistic Regression
- Model evaluation using accuracy score

## 🚀 How to Run

1. Clone the repository.
2. Place `mail_data.csv` in the project directory.
3. Open the `Email_spam_classifier.ipynb` notebook.
4. Run the notebook step by step.

## 🛠️ Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn

Install requirements:
```bash
pip install numpy pandas scikit-learn
