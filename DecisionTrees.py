import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeRegressor

# Instantiate a Decision Tree DecisionTreeRegressortree= DecisionTreeRegressor(max_dpeth=5, min_samples_split = 15, min_samples_leag=5)
tree = DecisionTreeRegressor(
    max_depth=5, min_samples_split=15, min_samples_leaf=5)

# Fit the tree to the training data
tree.fit(X_train, Y_train)

# Predict using the trained model above
Y_train_pred = tree.predict(X_train)
Y_test_pred = tree.predict(X_test)
kpi_ML(Y_train, Y_train_pred, Y_test, Y_test_pred, name='Tree')

fig = plt.figure(figsize(15, 6), dpi=300)
ax = fig.gca()
plot_tree(tree, fontsize=3, feature_names=[
          f'M{x-12}' for x in range(12)], rounded=True, filled=True, ax=ax)
fig.savefig('RegressionTree.PNG')
