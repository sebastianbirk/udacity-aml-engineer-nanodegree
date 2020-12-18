
import argparse
import joblib
import numpy as np
import pandas as pd
from azureml.core.dataset import Dataset
from azureml.core.run import Run
from azureml.core.workspace import Workspace
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from xgboost import XGBClassifier


def data_prep(df):
    """
    Prepare data for model training
    :param df: Dataframe that contains target and feature columns
    :return: Splitted training feature and target data as well as validation feature and target data
    """
    
    # Split data into target and features
    X = df.loc[:, df.columns != "Attrition"]
    y = df.loc[:, "Attrition"]
    
    # Encode classes
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    # One-hot-encode features
    enc = OneHotEncoder(handle_unknown='ignore')
    X = enc.fit_transform(X)
    
    # Split data into train and validation set
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_val, y_train, y_val


def main():
    
    run = Run.get_context()
    ws = run.experiment.workspace
    
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument("--learning_rate", type=float, default=0.3, help="Boosting learning rate (xgb's 'eta')")
    parser.add_argument("--n_estimators", type=int, default=100, help="Number of boosting rounds")
    parser.add_argument("--max_depth", type=int, default=6, help="Maximum tree depth for base learners")
    parser.add_argument("--min_child_weight", type=int, default=1, help="Minimum sum of instance weight(hessian) needed in a child")
    parser.add_argument("--gamma", type=float, default=0, help="Minimum loss reduction required to make a further partition on a leaf node of the tree")
    parser.add_argument("--subsample", type=float, default=1.0, help="Subsample ratio of the training instance")
    parser.add_argument("--colsample_bytree", type=float, default=1.0, help="Subsample ratio of columns when constructing each tree")
    parser.add_argument("--reg_lambda", type=float, default=1.0, help="L1 regularization term on weights")
    parser.add_argument("--reg_alpha", type=float, default=0, help="L2 regularization term on weights")

    args = parser.parse_args()

    run.log("learning_rate:", np.float(args.learning_rate))
    run.log("n_estimators:", int(args.n_estimators))
    run.log("max_depth:", int(args.max_depth))
    run.log("min_child_weight:", int(args.min_child_weight))
    run.log("gamma:", np.float(args.gamma))
    run.log("subsample:", np.float(args.subsample))
    run.log("colsample_bytree:", np.float(args.colsample_bytree))
    run.log("reg_lambda:", np.float(args.reg_lambda))
    run.log("reg_alpha:", np.float(args.reg_alpha))
    
    dataset = Dataset.get_by_name(ws, name="attrition_train")
    df = dataset.to_pandas_dataframe()
    
    X_train, X_val, y_train, y_val = data_prep(df)
    
    clf = XGBClassifier(
        learning_rate=args.learning_rate,
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        min_child_weight=args.min_child_weight,
        gamma=args.gamma,
        subsample=args.subsample,
        colsample_bytree=args.colsample_bytree,
        reg_lambda=args.reg_lambda,
        reg_alpha=args.reg_alpha
    )
    
    clf.fit(X_train, y_train)

    accuracy = np.round(clf.score(X_val, y_val), 3)
    run.log("accuracy", np.float(accuracy))
    
    auc_weighted = np.round(roc_auc_score(y_val, clf.predict(X_val), average='weighted'), 3)
    run.log("AUC_weighted", np.float(auc_weighted))
    
    os.makedirs("outputs", exist_ok=True)
    # files saved in the "outputs" folder are automatically uploaded into run history
    joblib.dump(clf, "outputs/hyperdrive_model.pkl")

if __name__ == '__main__':
    main()
