import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(
    page_title="Customer Churn Prediction Platform",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("📘 About This Project")

    st.info(
        """
        This AI system predicts whether a telecom customer
        is likely to stop using the company's services.

        Customer Churn = Customer Leaves

        Companies use churn prediction to identify
        customers at risk and take action before
        they leave.
        """
    )

    st.markdown("---")

    st.subheader("📖 Feature Guide")

    with st.expander("👤 Customer Profile Features"):
        st.markdown("""
        **Gender**

        Indicates whether the customer is Male or Female. While gender alone is usually not a strong predictor, it helps the model understand customer demographics.

        **Senior Citizen**

        Indicates whether the customer belongs to the senior citizen category. Senior customers may have different service preferences and retention patterns.

        **Partner**

        Shows whether the customer has a spouse or partner. Customers with partners often demonstrate more stable subscription behavior.

        **Dependents**

        Indicates whether the customer has children or dependent family members. Customers with dependents tend to use services more consistently and may be less likely to switch providers.

        **Tenure**

        Represents the number of months the customer has stayed with the company. Longer tenure generally indicates stronger loyalty and lower churn risk.
        """)

    with st.expander("🌐 Service Features"):
        st.markdown("""
        **Phone Service**

        Indicates whether the customer uses the company's phone service.

        **Multiple Lines**

        Shows whether the customer has more than one phone line. Customers using multiple services are often more engaged with the company.

        **Internet Service**

        Type of internet connection used by the customer (DSL, Fiber Optic, or No Internet). Service type can influence customer satisfaction and churn behavior.

        **Online Security**

        Indicates whether the customer subscribes to internet security services. Security-related services often increase customer engagement.

        **Online Backup**

        Shows whether the customer uses cloud or online backup services. Additional services may strengthen customer dependence on the provider.

        **Device Protection**

        Indicates whether the customer has device protection coverage. Customers using protection plans often have stronger service relationships.

        **Tech Support**

        Shows whether the customer receives technical support. Access to support can improve satisfaction and reduce frustration.

        **Streaming TV**

        Indicates whether the customer subscribes to television streaming services.

        **Streaming Movies**

        Indicates whether the customer subscribes to movie streaming services. Customers using multiple entertainment services may be more integrated into the ecosystem.
        """)

    with st.expander("💳 Billing & Contract Features"):
        st.markdown("""
        **Contract**

        Indicates the customer's subscription commitment period. Month-to-month customers can leave at any time, while long-term contracts often improve retention.

        **Paperless Billing**

        Shows whether bills are delivered electronically instead of through paper statements.

        **Payment Method**

        Indicates how the customer pays bills. Payment preferences can sometimes reflect customer convenience and loyalty.

        **Monthly Charges**

        Represents the amount the customer pays every month. Higher monthly costs may increase price sensitivity and churn risk.

        **Total Charges**

        Represents the total amount spent by the customer throughout their relationship with the company. Higher values often indicate long-term engagement.
        """)

# =====================================================
# HEADER
# =====================================================

st.title("📊 Customer Churn Prediction Platform")

st.caption(
    "AI-Powered Customer Retention Analytics Dashboard"
)

# =====================================================
# CUSTOMER INFORMATION
# =====================================================

st.header("👤 Customer Profile")

col1, col2 = st.columns(2)

with col1:

    gender = st.radio(
        "Gender",
        ["Male", "Female"],
        horizontal=True
    )

    SeniorCitizen = st.radio(
        "Senior Citizen",
        [0, 1],
        horizontal=True,
        help="1 = Customer is above 60 years old"
    )

with col2:

    Partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    Dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        24
    )


# =====================================================
# SERVICES
# =====================================================

st.header("🌐 Service Information")

col3, col4 = st.columns(2)

with col3:

    PhoneService = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    MultipleLines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    InternetService = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    OnlineSecurity = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    OnlineBackup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

with col4:

    DeviceProtection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    TechSupport = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    StreamingTV = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    StreamingMovies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

# =====================================================
# BILLING
# =====================================================

st.header("💳 Billing Information")

col5, col6 = st.columns(2)

with col5:

    Contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    PaperlessBilling = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    PaymentMethod = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


with col6:


    MonthlyCharges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=75.0
    )

    TotalCharges = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=1500.0
    )

payload = {
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}

st.markdown("---")

if st.button(
    "🚀 Analyze Customer Churn Risk",
    use_container_width=True
):

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    result = response.json()

    probability = result["churn_probability"] * 100

    st.header("📈 Prediction Results")

    m1, m2, m3 = st.columns(3)

    m1.metric(
        "Churn Probability",
        f"{probability:.2f}%"
    )

    m2.metric(
        "Tenure",
        f"{tenure} Months"
    )

    m3.metric(
        "Monthly Charges",
        f"${MonthlyCharges:.2f}"
    )

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=probability,
            title={"text": "Customer Churn Risk (%)"}
        )
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    if probability < 30:
        st.success("🟢 LOW RISK CUSTOMER")
    elif probability < 60:
        st.warning("🟡 MEDIUM RISK CUSTOMER")
    else:
        st.error("🔴 HIGH RISK CUSTOMER")


    # ==========================================
    # BUSINESS ACTIONS
    # ==========================================

    st.subheader("💡 Business Recommendation")

    recommendations = []
    business_impact = []

    # Contract Analysis

    if Contract == "Month-to-month":

        recommendations.append(
            "Offer an annual or two-year contract with a discounted rate to increase customer commitment."
        )

        business_impact.append(
            "Month-to-month customers can leave at any time and historically exhibit higher churn rates."
        )

    # High Charges

    if MonthlyCharges > 80:

        recommendations.append(
            "Review pricing and offer personalized discounts or bundled plans."
        )

        business_impact.append(
            f"The customer's monthly bill (${MonthlyCharges:.2f}) is relatively high, which may reduce perceived value."
        )

    # New Customer

    if tenure <= 12:

        recommendations.append(
            "Launch an onboarding and engagement campaign to strengthen early customer loyalty."
        )

        business_impact.append(
            f"The customer has only been with the company for {tenure} months and has not yet developed long-term loyalty."
        )

    # No Tech Support

    if TechSupport == "No":

        recommendations.append(
            "Offer complimentary technical support or service check-ins."
        )

        business_impact.append(
            "Customers without technical support often experience unresolved issues and lower satisfaction."
        )

    # No Online Security

    if OnlineSecurity == "No":

        recommendations.append(
            "Promote online security packages as a value-added service."
        )

        business_impact.append(
            "Customers not using security services may have lower product engagement."
        )

    # Fiber Customer

    if InternetService == "Fiber optic":

        recommendations.append(
            "Investigate service quality and network experience for fiber customers."
        )

        business_impact.append(
            "Fiber-optic customers historically show elevated churn despite premium pricing."
        )

    # Electronic Check

    if PaymentMethod == "Electronic check":

        recommendations.append(
            "Encourage migration to automatic payment methods through incentives."
        )

        business_impact.append(
            "Electronic check users often display lower retention than automatic payment users."
        )

    # Loyal Customers

    if tenure >= 36:

        recommendations.append(
            "Offer loyalty rewards or premium upgrades to reinforce customer retention."
        )

        business_impact.append(
            "The customer has demonstrated strong loyalty through long-term usage."
        )

    # Partner + Dependents

    if Partner == "Yes" and Dependents == "Yes":

        recommendations.append(
            "Promote family-oriented service bundles and multi-service packages."
        )

        business_impact.append(
            "Family-oriented customers often respond well to bundled services."
        )

    # Automatic Payments

    if PaymentMethod in [
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]:

        business_impact.append(
            "Automatic payments reduce billing friction and improve retention."
        )

    # ======================================================
    # DISPLAY BUSINESS INSIGHTS
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        st.info("📊 Business Insights")

        if business_impact:

            for item in business_impact:
                st.write(f"• {item}")

    with col2:

        st.success("🎯 Recommended Actions")

        if recommendations:

            unique_recommendations = list(
                dict.fromkeys(recommendations)
            )

            for item in unique_recommendations:
                st.write(f"• {item}")

    # ======================================================
    # EXECUTIVE SUMMARY
    # ======================================================

    st.subheader("📋 Executive Summary")

    if probability >= 70:

        st.error(
            f"""
            This customer has a HIGH churn risk ({probability:.1f}%).
    
            Immediate intervention is recommended because several customer
            attributes indicate dissatisfaction or low commitment.
    
            Estimated Business Priority:
            HIGH
            """
        )

    elif probability >= 40:

        st.warning(
            f"""
            This customer has a MODERATE churn risk ({probability:.1f}%).
    
            Targeted engagement campaigns and service improvements
            may improve retention.
    
            Estimated Business Priority:
            MEDIUM
            """
        )

    else:

        st.success(
            f"""
            This customer has a LOW churn risk ({probability:.1f}%).
    
            The customer currently shows characteristics associated
            with long-term retention.
    
            Estimated Business Priority:
            LOW
            """
        )

