import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(
    page_title="Customer Churn Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("📘 Customer Churn Analytics")

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

st.title("Customer Churn Intelligence Platform")

st.caption(
    "Machine Learning based customer retention and churn intelligence platform"
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

    try:

        response = requests.post(
            "https://customer-churn-api-z5wl.onrender.com/predict",
            json=payload,
            timeout=60
        )

        result = response.json()

    except Exception as e:

        st.error(f"API Error: {e}")
        st.stop()

    probability = result["churn_probability"] * 100

    annual_revenue = MonthlyCharges * 12
    revenue_at_risk = annual_revenue * probability / 100
    clv = TotalCharges

    # =====================================================
    # CUSTOMER HEALTH OVERVIEW
    # =====================================================

    st.header("Customer Health Overview")

    if tenure < 12:
        segment = "New"

    elif tenure < 36:
        segment = "Established"

    else:
        segment = "Loyal"

    if probability >= 70:
        priority = "High"

    elif probability >= 40:
        priority = "Medium"

    else:
        priority = "Low"

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.metric(
            "Churn Risk",
            f"{probability:.1f}%"
        )

    with k2:
        st.metric(
            "Retention Priority",
            priority
        )

    k3.metric(
        "Customer Value",
        f"${clv:.0f}"
    )

    with k4:
        st.metric(
            "Customer Segment",
            segment
        )

    st.markdown("---")

    # =====================================================
    # STATUS CARD
    # =====================================================

    if probability < 30:

        st.success(
            """
            Customer currently demonstrates healthy retention behaviour.
            The likelihood of churn is low based on current service usage,
            billing behaviour, and customer tenure.
            """
        )

    elif probability < 60:

        st.warning(
            """
            Customer demonstrates moderate churn risk.
            Proactive engagement is recommended.
            """
        )

    else:

        st.error(
            """
            Customer demonstrates high churn risk.
            Immediate retention action is recommended.
            """
        )

    # =====================================================
    # ESTIMATED CHURN DRIVERS
    # =====================================================

    risk_breakdown = []
    retention_breakdown = []

    # -----------------------------
    # RISK CONTRIBUTORS
    # -----------------------------

    if Contract == "Month-to-month":
        risk_breakdown.append(
            (
                "Month-to-Month Contract",
                "+18%",
                "Customer can leave at any time without contractual commitment."
            )
        )

    if MonthlyCharges >= 80:
        risk_breakdown.append(
            (
                "High Monthly Charges",
                "+12%",
                "Higher monthly bills often increase price sensitivity."
            )
        )

    if tenure <= 12:
        risk_breakdown.append(
            (
                "Short Customer Tenure",
                "+10%",
                "New customers generally have lower loyalty and higher churn probability."
            )
        )

    if TechSupport == "No":
        risk_breakdown.append(
            (
                "No Technical Support",
                "+8%",
                "Customers without support may experience unresolved issues."
            )
        )

    if OnlineSecurity == "No":
        risk_breakdown.append(
            (
                "No Online Security",
                "+6%",
                "Lower service adoption may indicate weaker engagement."
            )
        )

    if PaymentMethod == "Electronic check":
        risk_breakdown.append(
            (
                "Electronic Check Payment",
                "+5%",
                "Historically associated with higher churn than automatic payments."
            )
        )

    if InternetService == "Fiber optic":
        risk_breakdown.append(
            (
                "Fiber Internet Service",
                "+4%",
                "Fiber customers showed slightly higher churn in historical telecom datasets."
            )
        )

    # -----------------------------
    # RETENTION CONTRIBUTORS
    # -----------------------------

    if tenure >= 36:
        retention_breakdown.append(
            (
                "Long Customer Tenure",
                "-15%",
                "Long-term customers usually demonstrate stronger loyalty."
            )
        )

    if Contract in ["One year", "Two year"]:
        retention_breakdown.append(
            (
                "Long-Term Contract",
                "-12%",
                "Contract commitments reduce switching behaviour."
            )
        )

    if PaymentMethod in [
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]:
        retention_breakdown.append(
            (
                "Automatic Payments",
                "-8%",
                "Automatic billing reduces payment friction and improves retention."
            )
        )

    if TechSupport == "Yes":
        retention_breakdown.append(
            (
                "Technical Support Enabled",
                "-6%",
                "Support services improve customer satisfaction."
            )
        )

    if OnlineSecurity == "Yes":
        retention_breakdown.append(
            (
                "Online Security Enabled",
                "-5%",
                "Additional services increase engagement and platform dependency."
            )
        )

    if Partner == "Yes":
        retention_breakdown.append(
            (
                "Partner Account",
                "-3%",
                "Customers with partners often demonstrate more stable subscriptions."
            )
        )

    if Dependents == "Yes":
        retention_breakdown.append(
            (
                "Dependents on Account",
                "-3%",
                "Family-oriented customers typically maintain services longer."
            )
        )

    # =====================================================
    # DISPLAY SECTION
    # =====================================================

    st.subheader("Estimated Churn Drivers")

    left, right = st.columns(2)

    with left:

        st.error("Risk Contributors")

        if risk_breakdown:

            for factor, score, explanation in risk_breakdown:
                st.markdown(
                    f"""
    **{factor} ({score})**

    {explanation}

    ---
    """
                )

        else:

            st.success(
                "No major churn risk drivers were identified for this customer."
            )

    with right:

        st.success("Retention Contributors")

        if retention_breakdown:

            for factor, score, explanation in retention_breakdown:
                st.markdown(
                    f"""
    **{factor} ({score})**

    {explanation}

    ---
    """
                )

        else:

            st.info(
                "No strong retention indicators were identified."
            )
    # ======================================================
    # BUSINESS INSIGHTS & RECOMMENDATIONS
    # ======================================================

    st.subheader("📌 Business Insights & Recommendations")

    recommendations = []
    business_impact = []

    monthly_revenue = MonthlyCharges
    annual_revenue = MonthlyCharges * 12

    # --------------------------------------
    # Dynamic Recommendations
    # --------------------------------------

    if Contract == "Month-to-month":

        recommendations.append(
            "Promote annual or multi-year contracts through targeted retention offers."
        )

        business_impact.append(
            "The customer is on a month-to-month contract, which provides flexibility to switch providers without long-term commitment."
        )

    if MonthlyCharges > 80:

        recommendations.append(
            "Evaluate pricing competitiveness and consider personalized discounts or bundled services."
        )

        business_impact.append(
            f"The customer pays ${MonthlyCharges:.2f} per month, which may increase price sensitivity."
        )

    if tenure <= 12:

        recommendations.append(
            "Strengthen onboarding and engagement initiatives during the early customer lifecycle."
        )

        business_impact.append(
            "Newer customers typically have weaker loyalty and are more vulnerable to churn."
        )

    if TechSupport == "No":

        recommendations.append(
            "Offer technical support services or proactive customer assistance."
        )

        business_impact.append(
            "Lack of technical support may lead to unresolved issues and lower satisfaction."
        )

    if OnlineSecurity == "No":

        recommendations.append(
            "Promote security-related services as value-added offerings."
        )

        business_impact.append(
            "Customers without security services may be less engaged with the overall ecosystem."
        )

    if InternetService == "Fiber optic":

        recommendations.append(
            "Monitor service quality and customer experience for fiber subscribers."
        )

        business_impact.append(
            "Fiber-optic customers historically exhibited slightly higher churn behaviour in the training dataset."
        )

    if PaymentMethod == "Electronic check":

        recommendations.append(
            "Encourage migration toward automated payment methods."
        )

        business_impact.append(
            "Electronic check users often demonstrate lower retention compared with automatic-payment customers."
        )

    if tenure >= 36:

        recommendations.append(
            "Reward loyalty through premium upgrades, loyalty benefits, or exclusive offers."
        )

        business_impact.append(
            "The customer has demonstrated long-term commitment to the company."
        )

    if Partner == "Yes" and Dependents == "Yes":

        recommendations.append(
            "Promote family-oriented service bundles and household packages."
        )

        business_impact.append(
            "Household customers may respond positively to bundled service offerings."
        )

    if PaymentMethod in [
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]:

        business_impact.append(
            "Automatic payment methods generally improve retention by reducing billing friction."
        )

    recommendations = list(
        dict.fromkeys(recommendations)
    )

    # ======================================================
    # DISPLAY INSIGHTS
    # ======================================================

    col_a, col_b = st.columns(2)

    with col_a:

        st.info("Business Insights")

        if business_impact:

            for item in business_impact:
                st.write(f"• {item}")

        else:

            st.write(
                "• No significant churn-related business concerns detected."
            )

    with col_b:

        st.success("Recommended Actions")

        if recommendations:

            for item in recommendations:
                st.write(f"• {item}")

        else:

            st.write(
                "• Continue maintaining customer satisfaction and service quality."
            )

    # ======================================================
    # REVENUE IMPACT
    # ======================================================

    st.subheader("💰 Revenue Impact Assessment")

    revenue_at_risk = annual_revenue * (probability / 100)

    r1, r2, r3 = st.columns(3)

    r1.metric(
        "Monthly Revenue",
        f"${monthly_revenue:.2f}"
    )

    r2.metric(
        "Annual Revenue",
        f"${annual_revenue:.2f}"
    )

    r3.metric(
        "Revenue At Risk",
        f"${revenue_at_risk:.2f}"
    )

    # ======================================================
    # EXECUTIVE SUMMARY
    # ======================================================

    st.subheader("📋 Executive Summary")

    if probability >= 70:

        st.error(
            f"""
Customer churn probability is **{probability:.1f}%**.

This customer falls into the high-risk category and requires immediate retention attention.

Potential business loss if the customer leaves:
**${annual_revenue:.2f} per year**

Priority Level: HIGH
"""
        )

    elif probability >= 40:

        st.warning(
            f"""
Customer churn probability is **{probability:.1f}%**.

This customer shows moderate churn risk and should be targeted through engagement campaigns and service improvement initiatives.

Potential business loss if the customer leaves:
**${annual_revenue:.2f} per year**

Priority Level: MEDIUM
"""
        )

    else:

        st.success(
            f"""
Customer churn probability is **{probability:.1f}%**.

Current customer behaviour suggests healthy retention and long-term engagement.

Potential business loss if the customer leaves:
**${annual_revenue:.2f} per year**

Priority Level: LOW
"""
        )


st.subheader("Model Information")

st.info(
    """
    Model: Random Forest Classifier

    Dataset: Telco Customer Churn Dataset

    Accuracy: 78.56%

    F1 Score: 64.55%

    Features Used: 19

    Purpose:
    Predict customer churn and support retention decision-making.
    """
)

st.markdown("---")

st.caption(
    """
    Customer Churn Intelligence Platform

    Built using:
    Python • Scikit-Learn • FastAPI • Streamlit • MLflow • Docker Ready
    
    End-to-End MLOps Workflow:
    Data Processing → Model Training → API Serving → Business Analytics Dashboard
    """
)
