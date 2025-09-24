import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# 設定頁面配置
st.set_page_config(
    page_title="Linear Regression CRISP-DM",
    page_icon="📈",
    layout="wide"
)

# 標題
st.title("🔍 Linear Regression Analysis following CRISP-DM Methodology")
st.markdown("---")

# Sidebar for user inputs
st.sidebar.header("📊 Model Parameters")
st.sidebar.markdown("Adjust the parameters for the linear regression model y = ax + b")

# User input parameters
a_value = st.sidebar.slider("Parameter 'a' (slope)", min_value=-10.0, max_value=10.0, value=2.0, step=0.1)
b_value = st.sidebar.slider("Parameter 'b' (intercept)", min_value=-50.0, max_value=50.0, value=5.0, step=0.5)
noise_level = st.sidebar.slider("Noise Level", min_value=0.0, max_value=10.0, value=2.0, step=0.1)
n_points = st.sidebar.slider("Number of Points", min_value=50, max_value=500, value=100, step=10)

st.sidebar.markdown("---")
st.sidebar.info("💡 資料會在參數調整時自動更新")
manual_seed = st.sidebar.checkbox("🎲 使用固定隨機種子 (可重現結果)", value=True)
if st.sidebar.button("🔄 重新生成資料 (新隨機種子)"):
    # 強制重新生成，使用新的隨機種子
    if 'seed_counter' not in st.session_state:
        st.session_state.seed_counter = 0
    st.session_state.seed_counter += 1

# CRISP-DM Methodology
st.header("🔄 CRISP-DM Methodology Implementation")

# Initialize session state for parameter tracking
if 'last_params' not in st.session_state:
    st.session_state.last_params = None
if 'data_generated' not in st.session_state:
    st.session_state.data_generated = False
if 'seed_counter' not in st.session_state:
    st.session_state.seed_counter = 0

# Current parameters
current_params = (a_value, b_value, noise_level, n_points)

# Check if parameters changed or first time
params_changed = (st.session_state.last_params != current_params)
first_time = not st.session_state.data_generated

# Generate data when parameters change, button is clicked, or first time
if params_changed or first_time:
    # Data generation
    if manual_seed:
        # Use consistent seed but account for parameter changes for variety
        seed = 42 + hash(current_params) % 1000 + st.session_state.seed_counter
    else:
        # Use truly random seed
        seed = None
        
    np.random.seed(seed)
    X = np.random.uniform(-10, 10, n_points)
    noise = np.random.normal(0, noise_level, n_points)
    y = a_value * X + b_value + noise
    
    # Update session state
    st.session_state.last_params = current_params
    st.session_state.data_generated = True
    # Store in session state
    st.session_state.X = X
    st.session_state.y = y

# Use data from session state (will always exist now)
X = st.session_state.X
y = st.session_state.y

# Create DataFrame
df = pd.DataFrame({'X': X, 'y': y})

# CRISP-DM Phase 1: Business Understanding
st.subheader("1️⃣ Business Understanding")
st.markdown("""
**Business Objective**: Understand the linear relationship between variables X and y

**Success Criteria**: 
- Build a simple linear regression model with good fit
- Allow interactive parameter adjustment
- Visualize the relationship clearly

**Business Question**: Can we predict y given X using a linear relationship?
""")

# CRISP-DM Phase 2: Data Understanding
st.subheader("2️⃣ Data Understanding")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**📋 Data Summary**")
    st.write(f"- Number of observations: {len(df)}")
    st.write(f"- X range: [{X.min():.2f}, {X.max():.2f}]")
    st.write(f"- y range: [{y.min():.2f}, {y.max():.2f}]")
    
    st.markdown("**📊 Descriptive Statistics**")
    st.write(df.describe())

with col2:
    st.markdown("**🔗 Data Correlation**")
    correlation = np.corrcoef(X, y)[0, 1]
    st.metric("Pearson Correlation", f"{correlation:.3f}")
    
    st.markdown("**📈 Data Sample**")
    st.write(df.head(10))

# CRISP-DM Phase 3: Data Preparation
st.subheader("3️⃣ Data Preparation")

# Check for missing values and outliers
col1, col2 = st.columns(2)

with col1:
    st.markdown("**🔍 Data Quality Check**")
    st.write(f"- Missing values in X: {pd.isna(X).sum()}")
    st.write(f"- Missing values in y: {pd.isna(y).sum()}")
    st.write(f"- Data type X: {type(X[0]).__name__}")
    st.write(f"- Data type y: {type(y[0]).__name__}")

with col2:
    st.markdown("**📊 Data Distribution**")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    ax1.hist(X, bins=20, alpha=0.7, color='blue')
    ax1.set_title('Distribution of X')
    ax1.set_xlabel('X values')
    ax1.set_ylabel('Frequency')
    
    ax2.hist(y, bins=20, alpha=0.7, color='red')
    ax2.set_title('Distribution of y')
    ax2.set_xlabel('y values')
    ax2.set_ylabel('Frequency')
    
    plt.tight_layout()
    st.pyplot(fig)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X.reshape(-1, 1), y, test_size=0.2, random_state=42
)

st.write(f"**Training set size**: {len(X_train)} samples")
st.write(f"**Test set size**: {len(X_test)} samples")

# CRISP-DM Phase 4: Modeling
st.subheader("4️⃣ Modeling")

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Get model parameters
estimated_a = model.coef_[0]
estimated_b = model.intercept_

# Make predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**🎯 Model Parameters**")
    st.write(f"**True parameters**: a = {a_value}, b = {b_value}")
    st.write(f"**Estimated parameters**: a = {estimated_a:.3f}, b = {estimated_b:.3f}")
    st.write(f"**Parameter Error**: ")
    st.write(f"  - Error in 'a': {abs(estimated_a - a_value):.3f}")
    st.write(f"  - Error in 'b': {abs(estimated_b - b_value):.3f}")
    
    st.info("💡 **注意**: 參數誤差是由於資料中的噪音造成的，這是正常現象。噪音越大，誤差通常越大。")

with col2:
    st.markdown("**📈 Model Equation**")
    st.latex(f"\\hat{{y}} = {estimated_a:.3f}x + {estimated_b:.3f}")
    st.markdown("**🎯 True Equation**")
    st.latex(f"y = {a_value}x + {b_value} + \\epsilon")
    st.caption("其中 ε 是噪音項，ε ~ N(0, σ²)")

# CRISP-DM Phase 5: Evaluation
st.subheader("5️⃣ Evaluation")

# Calculate metrics
r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)
mse_train = mean_squared_error(y_train, y_train_pred)
mse_test = mean_squared_error(y_test, y_test_pred)
rmse_train = np.sqrt(mse_train)
rmse_test = np.sqrt(mse_test)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Training R²", f"{r2_train:.3f}")
    st.metric("Training RMSE", f"{rmse_train:.3f}")

with col2:
    st.metric("Test R²", f"{r2_test:.3f}")
    st.metric("Test RMSE", f"{rmse_test:.3f}")

with col3:
    st.metric("Noise Level", f"{noise_level:.1f}")
    st.metric("Sample Size", f"{n_points}")

# Model performance visualization
st.markdown("**📊 Model Performance Visualization**")

# 添加說明
st.info("""
**圖表說明**:
- 🔵 **藍色/紅色點**: 包含噪音的實際資料點
- 🟢 **綠色實線**: 從資料學習得到的擬合線 (Fitted Line)
- 🟠 **橙色虛線**: 理論上的真實線 (True Line，無噪音)

兩條線之間的小差異是正常的，因為擬合線是從有噪音的資料中學習得到的。
""")

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

# Scatter plot with regression line
ax1.scatter(X_train.flatten(), y_train, alpha=0.6, color='blue', label='Training data')
ax1.scatter(X_test.flatten(), y_test, alpha=0.6, color='red', label='Test data')

# Plot regression line
X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_line_pred = model.predict(X_line)
ax1.plot(X_line, y_line_pred, color='green', linewidth=2, 
         label=f'Fitted line: y = {estimated_a:.2f}x + {estimated_b:.2f}')

# Plot true line
y_line_true = a_value * X_line.flatten() + b_value
ax1.plot(X_line, y_line_true, color='orange', linewidth=2, linestyle='--', 
         label=f'True line: y = {a_value}x + {b_value} (no noise)')

ax1.set_xlabel('X')
ax1.set_ylabel('y')
ax1.set_title('Linear Regression: Fitted vs True Line')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Residuals plot
residuals_train = y_train - y_train_pred
residuals_test = y_test - y_test_pred
ax2.scatter(y_train_pred, residuals_train, alpha=0.6, color='blue', label='Training')
ax2.scatter(y_test_pred, residuals_test, alpha=0.6, color='red', label='Test')
ax2.axhline(y=0, color='black', linestyle='--', alpha=0.8)
ax2.set_xlabel('Predicted values')
ax2.set_ylabel('Residuals')
ax2.set_title('Residuals Plot')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Predicted vs Actual
ax3.scatter(y_train, y_train_pred, alpha=0.6, color='blue', label='Training')
ax3.scatter(y_test, y_test_pred, alpha=0.6, color='red', label='Test')
min_val, max_val = min(y.min(), y_train_pred.min(), y_test_pred.min()), max(y.max(), y_train_pred.max(), y_test_pred.max())
ax3.plot([min_val, max_val], [min_val, max_val], 'k--', alpha=0.8, label='Perfect fit')
ax3.set_xlabel('Actual values')
ax3.set_ylabel('Predicted values')
ax3.set_title('Predicted vs Actual')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Distribution of residuals
ax4.hist(residuals_train, bins=15, alpha=0.7, color='blue', label='Training residuals')
ax4.hist(residuals_test, bins=10, alpha=0.7, color='red', label='Test residuals')
ax4.set_xlabel('Residuals')
ax4.set_ylabel('Frequency')
ax4.set_title('Distribution of Residuals')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
st.pyplot(fig)

# CRISP-DM Phase 6: Deployment
st.subheader("6️⃣ Deployment")
st.markdown("""
**🚀 Model Deployment Strategy**:

1. **Current Implementation**: Interactive Streamlit web application
2. **Model Persistence**: The model can be saved using joblib or pickle
3. **API Integration**: Can be extended to provide REST API endpoints
4. **Docker Support**: Containerized for easy deployment
5. **Monitoring**: Real-time parameter adjustment and visualization

**📋 Deployment Checklist**:
- ✅ Interactive parameter tuning
- ✅ Real-time visualization
- ✅ Model performance metrics
- ✅ Data quality checks
- ✅ CRISP-DM methodology documentation
""")

# Interactive prediction
st.markdown("**🔮 Make a Prediction**")
predict_x = st.number_input("Enter X value for prediction:", value=0.0, step=0.1)
predicted_y = model.predict([[predict_x]])[0]
true_y = a_value * predict_x + b_value

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Input X", f"{predict_x:.2f}")
with col2:
    st.metric("Predicted y", f"{predicted_y:.2f}")
with col3:
    st.metric("True y (no noise)", f"{true_y:.2f}")

# Model summary
st.markdown("---")
st.subheader("📊 Summary")

summary_text = f"""
**Model Summary**:
- **Dataset Size**: {n_points} points
- **Model Type**: Simple Linear Regression
- **True Parameters**: a = {a_value}, b = {b_value}
- **Estimated Parameters**: a = {estimated_a:.3f}, b = {estimated_b:.3f}
- **Model Performance**: R² = {r2_test:.3f}, RMSE = {rmse_test:.3f}
- **Noise Level**: {noise_level}

**CRISP-DM Implementation**: ✅ Complete
All six phases of CRISP-DM methodology have been implemented with interactive capabilities.
"""

st.markdown(summary_text)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>📈 Linear Regression Analysis with CRISP-DM Methodology</p>
        <p>Built with Streamlit | Interactive Machine Learning</p>
    </div>
    """, 
    unsafe_allow_html=True
)