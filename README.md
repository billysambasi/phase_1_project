# Aviation Accident Risk Analysis Project

## Description of the Project

The project focuses on enabling the company's entry into the aviation industry by analyzing data to identify aircraft that pose the lowest operational and safety risks. The goal is to provide data-driven insights into aircraft models, incident rates and failure points including environmental factors such as weather conditions and locations. By assessing historical safety records, incidents and trends in failure types, this analysis creates comprehensive risk profiles for various aircraft. The findings aim to guide the aviation division in selecting aircraft that are not only safe but also operationally reliable, minimizing risks and maximizing efficiency in the new venture.

## Business Questions
1. How have aviation accident trends evolved over time, and what do they indicate about industry safety?
2. Which aircraft models and engine types are most frequently involved in incidents?
3. What weather conditions are most associated with high-severity aviation accidents?
4. What types of aircraft damage occur most commonly in accidents, and what are their operational implications?

## Project Objectives

- Understand historical trends in aviation accidents
- Determine which aircraft models and engine types are most frequently involved in incidents
- Assess the influence of weather conditions on accident severity
- Identify the most common types of aircraft damage

## Modelling Objectives

- Predict the severity of an aviation accident
- Classify the likely type of aircraft damage
- Predict the likelihood of fatality/injury based on conditions
- Identify high-risk aircraft or conditions
- (For consideration) Recommender system to suggest safer aircraft configurations or operating conditions — based on learned patterns.

## Data Analysis Process

### 1. Data Loading and Understanding
- Imported necessary libraries for data analysis and visualization
- Loaded the AviationData.csv file with proper encoding (latin-1) and memory optimization
- Examined dataset structure: 88,889 entries with 31 columns
- Identified data types and missing values patterns
- No duplicate rows found

### 2. Data Cleaning and Preprocessing
- Filtered data from 1982 onwards due to significant changes in aviation industry
- Standardized aircraft make names (converted to title case and stripped whitespace)
- Created derived features:
  - Year and Month columns from Event.Date
  - Total.Injuries column combining all injury types
- Handled missing values appropriately for analysis
- Identified and analyzed outliers in injury data

### 3. Exploratory Data Analysis

#### Objective 1: Historical Trends in Aviation Accidents
- **Yearly Trends**: Analyzed accident frequency over time showing general decline
- **Monthly Trends**: Identified seasonal patterns with higher incidents in summer months (June, July, August)
- **Flight Phase Analysis**: Examined accidents by phase of flight
- **Fatal Injuries Over Time**: Tracked fatality trends across years

#### Objective 2: Aircraft Models and Engine Types Analysis
- **Top Aircraft Makes**: Identified Cessna, Piper, and Beechcraft as most frequently involved
- **Aircraft Models**: Analyzed specific models with highest incident rates
- **Engine Types**: Examined reciprocating engines as most common in incidents
- **Damage vs Injuries**: Analyzed relationship between aircraft damage and injury severity

#### Objective 3: Weather Conditions Impact
- **Weather Distribution**: Found majority of accidents occur in clear weather conditions
- **Severity Analysis**: Examined relationship between weather and accident outcomes

#### Objective 4: Aircraft Damage Patterns
- **Damage Types**: Analyzed distribution of damage categories (Destroyed, Substantial, Minor, Unknown)
- **Operational Implications**: Connected damage patterns to safety considerations


## Key Findings

### Accident Trends
- **Declining Trend**: Overall reduction in accidents over time, likely due to improved safety measures and technology
- **Seasonal Patterns**: Higher accident rates during summer months, possibly due to increased air traffic
- **Clear Weather Paradox**: Most accidents occur in clear weather, suggesting human error or mechanical failure as primary factors

### Aircraft and Engine Analysis
- **High-Volume Aircraft**: Cessna, Piper, and Beechcraft show high incident numbers, likely due to their popularity in general aviation
- **Engine Types**: Reciprocating engines most commonly involved, reflecting their prevalence in smaller aircraft
- **Model-Specific Risks**: Certain models show higher incident rates that may indicate design or operational considerations

### Weather and Damage Patterns
- **Weather Impact**: Clear weather conditions dominate accident scenarios
- **Damage Severity**: Analysis reveals patterns between damage types and injury outcomes
- **Operational Factors**: Flight phase analysis shows critical periods for safety 

## Recommendations

### Aircraft Selection Strategy
1. **Focus on Low-Risk Models**: Prioritize aircraft with historically lower incident rates
2. **Engine Type Considerations**: Evaluate engine reliability records when selecting aircraft
3. **Comprehensive Safety Assessment**: Consider multiple factors including make, model, and engine type

### Operational Safety Measures
1. **Enhanced Training**: Implement comprehensive pilot training programs, especially for clear weather operations
2. **Seasonal Awareness**: Increase safety protocols during high-risk summer months
3. **Maintenance Programs**: Establish robust maintenance schedules based on aircraft-specific risk profiles

### Risk Management
1. **Data-Driven Decisions**: Use historical accident data to inform aircraft acquisition decisions
2. **Continuous Monitoring**: Establish systems to track safety performance of fleet aircraft
3. **Emergency Preparedness**: Develop protocols based on common accident scenarios and damage patterns

## Technical Implementation

### Tools and Libraries Used
- **Data Analysis**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Machine Learning**: scikit-learn, xgboost, lightgbm
- **Model Evaluation**: Various metrics and cross-validation techniques
- **Jupyter Environment**: jupyterlab, ipykernel

### Data Processing Pipeline
1. **Data Ingestion**: Loaded and validated aviation accident data (88,889 records)
2. **Data Cleaning**: Standardized formats, handled missing values, created derived features
3. **Exploratory Analysis**: Comprehensive statistical and visual analysis
4. **Feature Engineering**: Prepared ML-ready features for damage prediction modeling
5. **Visualization**: Generated insights through various chart types and statistical summaries

### 4. Feature Engineering for Machine Learning
- **Dataset Preparation**: Processed 88,882 records for modeling
- **Feature Selection**: Selected 9 key features including:
  - Aircraft specifications (Make, Model, Engine Type)
  - Environmental factors (Weather Condition)
  - Operational factors (Flight Phase, Purpose of Flight, Amateur Built)
  - Temporal features (Month, Year)
- **Encoding**: Applied label encoding to categorical variables
- **Target Variable**: Aircraft damage classification (Substantial, Destroyed, Minor, Unknown)
- **Train-Test Split**: Created stratified 80-20 split (71,105 training samples)
- **Output Files**:
  - `aviation_features.csv`: Feature-engineered dataset
  - `model_damaged.pkl`: Serialized train-test splits and encoders 

## Project Structure

```
phase_1_project/
├── data/
│   ├── aviation_features.csv      # Feature-engineered dataset for ML
│   ├── CleanedAviationData.csv    # Cleaned aviation dataset
│   └── model_damaged.pkl          # Pickled train-test splits and encoders
├── misc/
│   ├── embedded_images/           # Images embedded in documentation
│   ├── index_files/               # Generated visualization outputs
│   └── project_presentation.pdf   # Project presentation
├── .gitattributes                 # Git attributes configuration
├── .gitignore                     # Git ignore file
├── exploratory_data_analysis.ipynb # EDA notebook
├── feature_engineering.ipynb      # Feature engineering for ML models
├── index.ipynb                    # Main analysis notebook
├── LICENSE                        # Project license
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
└── utils.py                       # Utility functions for data processing
```

## Current Progress

### Completed
- ✅ Data loading and understanding (88,889 records)
- ✅ Data cleaning and preprocessing
- ✅ Comprehensive exploratory data analysis
- ✅ Feature engineering pipeline for ML models
- ✅ Train-test split preparation (71,105 training samples)
- ✅ Label encoding for categorical features
- ✅ Data serialization for model training

### In Progress
- 🔄 Machine learning model development for damage prediction
- 🔄 Model evaluation and optimization

## Future Enhancements

1. **Predictive Modeling**: Complete implementation of ML models for damage classification
2. **Model Evaluation**: Comprehensive performance metrics and cross-validation
3. **Real-time Monitoring**: Develop systems for ongoing safety assessment
4. **Interactive Dashboards**: Create dynamic visualizations for stakeholder use
5. **External Data Integration**: Incorporate weather, maintenance, and operational data
6. **Recommendation Engine**: Build system to suggest optimal aircraft configurations

## Links

- [GitHub Repository](https://github.com/billysambasi/phase_1_project.git)
- [Tableau Project Dashboards](https://public.tableau.com/app/profile/billy.sambasi/viz/ProjectDashboards_17429896470220/Story1)
