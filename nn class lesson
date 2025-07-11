# An AI

## Deep Learning APIs

* **TensorFlow/Keras**
    * **TensorFlow:** A comprehensive, open-source machine learning platform developed by Google. It's known for its robust production deployment capabilities and flexibility for large-scale projects.
    * **Keras:** A high-level API built *on top of* TensorFlow (and other backends like Theano, CNTK, but primarily TensorFlow now). Keras makes deep learning easier and faster to use. It's known for its user-friendliness, simple API, and quick prototyping. Think of Keras as a simplified interface that allows you to build models with fewer lines of code, while TensorFlow is the powerful engine underneath.
    * **Key Features (TensorFlow/Keras):**
        * **Eager Execution (TF 2.x default):** Operations are executed immediately, making debugging easier and code feel more "Pythonic" (similar to PyTorch).
        * **Static Graph Optimization (via `tf.function`):** For production, code can be compiled into highly optimized static graphs for performance.
        * **Comprehensive Ecosystem:** Includes tools for deployment (TensorFlow Serving, Lite, JS), visualization (TensorBoard), and end-to-end ML pipelines (TFX).
        * **Scalability:** Strong support for distributed training on various hardware, including Google's TPUs.

* **PyTorch**
    * An open-source machine learning framework developed by Meta (Facebook AI Research). It's known for its flexibility, Pythonic nature, and strong adoption in the research community.
    * **Key Features:**
        * **Dynamic Computational Graphs (Define-by-Run):** The graph is built as operations are executed, allowing for easy debugging using standard Python tools. This offers great flexibility for experimental models.
        * **Pythonic Interface:** Often feels more intuitive and directly integrated with Python programming paradigms.
        * **Research-Friendly:** Widely adopted in academia and research due to its flexibility and ease of prototyping new ideas.
        * **Growing Production Capabilities:** Tools like TorchScript for serialization and TorchServe for model serving are maturing rapidly.
        * **Strong Community:** A large and active community, especially among researchers and open-source contributors.

## The fastai Library

* This is a high-level deep learning library built on top of PyTorch.
* It simplifies common deep learning workflows, making it much easier to achieve state-of-the-art results with less code.
* It's designed to be both approachable and rapidly productive (for beginners and practitioners) while also being deeply hackable and configurable (for researchers who want to customize things).
* Fastai provides specialized modules for various deep learning applications, including:
    * **Computer Vision:** Image classification, object detection, image segmentation.
    * **Natural Language Processing (NLP):** Text classification, language modeling, summarization, etc.
    * **Tabular Data:** Applying deep learning to structured data (like spreadsheets).
    * **Collaborative Filtering:** Building recommendation systems.
    * **Time Series Analysis:** For forecasting and anomaly detection.
* It leverages PyTorch's flexibility and power but adds layers of abstraction to make common tasks very straightforward. For example, you can often train a highly accurate image classifier in just a few lines of code.

## Neural Network Metrics

Metrics are used to evaluate the performance of a model during training and testing. They don't affect model training (the actual learning process where weights are updated), but they only help us understand how well the model is performing. They provide a quantitative way to gauge the model's success.

Common metrics include:

1.  **Accuracy**
    * **Definition:** The proportion of correctly predicted instances out of the total instances.
    * **Formula:** $\frac{\text{Number of Correct Predictions}}{\text{Total Number of Predictions}}$
    * **Use Case:** Most intuitive and commonly used for classification problems, especially when classes are balanced.
    * **Limitation:** Can be misleading if classes are imbalanced (e.g., if 95% of cases are negative, a model predicting "negative" always would have 95% accuracy but be useless).

2.  **Precision** (for binary classification, typically focusing on the positive class)
    * **Definition:** Out of all instances the model *predicted as positive*, how many were *actually positive*? It answers: "When the model says it's positive, how often is it right?"
    * **Formula:** $\frac{\text{True Positives (TP)}}{\text{True Positives (TP) + False Positives (FP)}}$
    * **Use Case:** Important when the cost of a False Positive (incorrectly predicting positive) is high (e.g., spam detection, medical diagnosis for a serious disease).

3.  **Recall / Sensitivity** (for binary classification, typically focusing on the positive class)
    * **Definition:** Out of all the instances that were *actually positive*, how many did the model *correctly identify as positive*? It answers: "Of all the actual positives, how many did the model catch?"
    * **Formula:** $\frac{\text{True Positives (TP)}}{\text{True Positives (TP) + False Negatives (FN)}}$
    * **Use Case:** Important when the cost of a False Negative (failing to detect a true positive) is high (e.g., detecting fraudulent transactions, identifying sick patients).

4.  **F1-Score**
    * **Definition:** The harmonic mean of Precision and Recall. It provides a single score that balances both precision and recall.
    * **Formula:** $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$
    * **Use Case:** Useful when you need a balance between precision and recall, especially in classification tasks with imbalanced datasets.

5.  **AUC (Area Under the Receiver Operating Characteristic Curve)**
    * **Definition:** Measures how well a model distinguishes between classes (e.g., positive vs. negative). It represents the probability that the model will rank a randomly chosen positive instance higher than a randomly chosen negative instance. A higher AUC means the model is better at separating the classes.
    * **Range:** From 0 to 1. A random model has an AUC of 0.5. A perfect model has an AUC of 1.0.
    * **Use Case:** Very common for binary classification, especially with imbalanced datasets, as it's less sensitive to class distribution than accuracy. It evaluates the model's performance across all possible classification thresholds.

6.  **Categorical Accuracy**
    * **Definition:** This is the same as the general "Accuracy" described above, but specifically named for *categorical classification* tasks where inputs are assigned to discrete categories (e.g., "cat," "dog," "bird"). It's the fraction of predictions that exactly match the true label.

7.  **Multi-class Classification Metrics**
    * When you have more than two classes (e.g., classifying images into "cat," "dog," "bird"), precision, recall, and F1-score can be calculated in different ways:
        * **Micro-average:** Calculates metrics globally by counting the total true positives, false negatives, and false positives. This favors larger classes.
        * **Macro-average:** Calculates metrics for each class independently and then takes the unweighted average. This treats all classes equally.
        * **Weighted-average:** Calculates metrics for each class and then takes the average weighted by the number of true instances for each class.
    * **Top-K Accuracy:** (Often used in multi-class classification)
        * **Definition:** Checks if the correct label is among the top 'k' most probable predictions made by the model.
        * **Use Case:** Useful in scenarios where providing a few highly probable options is acceptable, rather than demanding an exact single correct answer (e.g., image search where presenting the correct item in the top 5 results is good enough).

8.  **Sparse Categorical Accuracy**
    * **Definition:** This is a variant of `Categorical Accuracy` used when your target labels (the `y` values) are integers representing categories (e.g., 0, 1, 2 for cat, dog, bird) rather than "one-hot encoded" vectors (e.g., `[1,0,0]` for cat, `[0,1,0]` for dog). It essentially performs the one-hot encoding internally before calculating accuracy.

9.  **Regression Task Metrics**
    * These metrics are used when the model predicts a continuous numerical value (e.g., predicting house prices, temperature, stock values).

    * **MAE (Mean Absolute Error)**
        * **Definition:** The average of the absolute differences between the predicted values and the actual (true) values. It measures the average magnitude of the errors without considering their direction.
        * **Formula:** $\frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|$ (where $y_i$ is actual, $\hat{y}_i$ is predicted, $N$ is number of samples)
        * **Similar to:** L1 Loss.
        * **Interpretation:** Easy to understand; directly tells you the average error in the same units as the output. Less sensitive to outliers than MSE.

    * **MSE (Mean Squared Error)**
        * **Definition:** The average of the squared differences between the predicted values and the actual values. It penalizes larger errors more heavily than MAE due to the squaring.
        * **Formula:** $\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$
        * **Similar to:** L2 Loss.
        * **Interpretation:** Penalizes large errors disproportionately. Often used because squaring makes the error function differentiable, which is good for optimization algorithms. The units are squared, which can be less intuitive.

    * **RMSE (Root Mean Squared Error)**
        * **Definition:** The square root of the MSE. It brings the error back into the same units as the original output variable.
        * **Formula:** $\sqrt{\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2}$
        * **Interpretation:** More interpretable than MSE because it's in the same units as the target variable. Still sensitive to outliers because it's derived from MSE.

    * **R² Score (Coefficient of Determination)**
        * **Definition:** Represents the proportion of the variance in the dependent variable that is predictable from the independent variables. In simpler terms, it indicates how well the model's predictions approximate the real data points.
        * **Range:** From $-\infty$ to 1. A value of 1 indicates a perfect fit. A value of 0 indicates the model explains none of the variability of the response data around its mean. Negative values mean the model is worse than simply predicting the mean.
        * **Formula:** $R^2 = 1 - \frac{\sum_{i=1}^{N} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{N} (y_i - \bar{y})^2}$ (where $\bar{y}$ is the mean of actual values)
        * **Use Case:** Provides a relative measure of fit. Useful for comparing different models on the same dataset.
