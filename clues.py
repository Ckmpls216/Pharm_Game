clues = {
    'Baclofen': [
        'Clue 1: Oral, I.M., I.V. | 10mg-20mg',
        'Clue 2: Agonist at GABAB Receptors',
        'Clue 3: Sedation, Nausea, Headache',
        'Clue 4: Monitor Liver Function, Avoid Abrupt Discontinuation, Do Not Operate Heavy Machinery',
        'Clue 5: Muscle Relaxant, Antispasticity'
    ],
    'Cyclobenzaprine': [
        'Clue 1: Oral | 5mg-10mg',
        'Clue 2: Alpha-2 Adrenergic Receptor Antagonist',
        'Clue 3: Dizziness, Dry Mouth, Fatigue',
        'Clue 4: Avoid Alcohol Consumption, Use Short-Term Only, Do Not Operate Heavy Machinery',
        'Clue 5: Muscle Relaxant, Analgesic'
    ],
    'Dantrolene': [
        'Clue 1: Oral, I.V. | 25mg-100mg',
        'Clue 2: Inhibits Calcium Release from Sarcoplasmic Reticulum',
        'Clue 3: Diarrhea, Nausea, Dizziness',
        'Clue 4: Monitor Liver Function, Avoid Abrupt Discontinuation, Do Not Use with Alcohol',
        'Clue 5: Muscle Relaxant, Antispasticity'
    ],
    'Morphine': [
        'Clue 1: Oral, I.M., I.V. | 10mg-30mg',
        'Clue 2: Binds to Mu Opioid Receptors',
        'Clue 3: Sedation, Respiratory Depression, Nausea',
        'Clue 4: Monitor for Abuse Potential, Monitor Respiratory Function, Use with Caution in Elderly',
        'Clue 5: Analgesic, Antitussive'
    ],
    'Naloxone': [
        'Clue 1: I.V., Intranasal | 0.4mg-2mg',
        'Clue 2: Competitive Antagonist at Opioid Receptors',
        'Clue 3: Sweating, Tachycardia, Hypertension',
        'Clue 4: Monitor for Withdrawal Symptoms, Use with Caution in Patients with Cardiovascular Disease',
        'Clue 5: Opioid Antagonist'
    ],
    'Sumatriptan': [
        'Clue 1: Oral, Subcutaneous | 25mg-100mg',
        'Clue 2: Agonist at Serotonin 5-HT1B/1D Receptors',
        'Clue 3: Tingling Sensation, Flushing, Dizziness',
        'Clue 4: Do Not Use More than Twice in 24 Hours, Do Not Use with Ergotamines, Avoid Driving or Operating Heavy Machinery',
        'Clue 5: Anti-migraine'
    ],
    'Diphenhydramine': [
        'Clue 1: Oral, I.V., Topical | 25mg-50mg',
        'Clue 2: Antagonist at Histamine H1 Receptors',
        'Clue 3: Drowsiness, Dry Mouth, Blurred Vision',
        'Clue 4: Do Not Use with Alcohol, Use with Caution in Elderly, Avoid Driving or Operating Heavy Machinery',
        'Clue 5: Antihistamine, Sedative'
    ],
    'Fexofenadine': [
        'Clue 1: Oral | 60mg-180mg',
        'Clue 2: Antagonist at Histamine H1 Receptors',
        'Clue 3: Headache, Nausea, Dizziness',
        'Clue 4: Take on an Empty Stomach, Do Not Use with Antacids, Avoid Grapefruit Juice',
        'Clue 5: Antihistamine'
    ],
    'Aspirin': [
        'Clue 1: Oral, Rectal | 325mg-650mg',
        'Clue 2: Inhibits Cyclooxygenase-1 and Cyclooxygenase-2',
        'Clue 3: Nausea, Vomiting, Heartburn',
        'Clue 4: Monitor for Bleeding, Discontinue Prior to Surgery, Avoid Alcohol Consumption',
        'Clue 5: Pain Relief, Anti-inflammatory, Antipyretic'
    ],
    'Ibuprofen': [
        'Clue 1: Oral | 200mg-400mg',
        'Clue 2: Inhibits Cyclooxygenase-1 and Cyclooxygenase-2',
        'Clue 3: Nausea, Vomiting, Heartburn',
        'Clue 4: Monitor for Bleeding, Discontinue Prior to Surgery, Avoid Alcohol Consumption',
        'Clue 5: Pain Relief, Anti-inflammatory, Antipyretic'
    ],
        'Celecoxib': [
        'Clue 1: Oral | 100mg-200mg',
        'Clue 2: Selective Inhibitor of Cyclooxygenase-2',
        'Clue 3: Abdominal Pain, Diarrhea, Nausea',
        'Clue 4: Monitor for Bleeding, Discontinue Prior to Surgery, Avoid Alcohol Consumption',
        'Clue 5: Pain Relief, Anti-inflammatory'
    ],
    'Acetaminophen': [
        'Clue 1: Oral, Rectal, I.V. | 325mg-1000mg',
        'Clue 2: Inhibits Cyclooxygenase-1 and Cyclooxygenase-2 in the CNS',
        'Clue 3: Nausea, Vomiting, Liver Toxicity',
        'Clue 4: Do Not Exceed Maximum Daily Dose, Do Not Use with Alcohol, Avoid Use with Other Acetaminophen-Containing Products',
        'Clue 5: Pain Relief, Antipyretic'
    ],
    'Hydrocortisone': [
        'Clue 1: Topical, Oral, Rectal, I.V. | 1mg-100mg',
        'Clue 2: Binds to Glucocorticoid Receptors, Suppresses Inflammation and Immune Response',
        'Clue 3: Burning, Itching, Dryness',
        'Clue 4: Do Not Use on Infected Areas, Do Not Use with Tight Bandages or Dressings, Avoid Use in Children',
        'Clue 5: Anti-inflammatory, Antipruritic'
    ],
    'Prednisone': [
        'Clue 1: Oral | 5mg-60mg',
        'Clue 2: Binds to Glucocorticoid Receptors, Suppresses Inflammation and Immune Response',
        'Clue 3: Increased Appetite, Weight Gain, Mood Changes',
        'Clue 4: Do Not Stop Abruptly, Take with Food or Milk, Avoid Contact with Sick Individuals',
        'Clue 5: Anti-inflammatory, Immunosuppressant'
    ],
    'Beclomethasone': [
        'Clue 1: Inhalation, Nasal | 40mcg-80mcg',
        'Clue 2: Binds to Glucocorticoid Receptors, Suppresses Inflammation and Immune Response',
        'Clue 3: Dry Mouth, Hoarseness, Cough',
        'Clue 4: Rinse Mouth After Use, Avoid Contact with Eyes, Use Regularly Even if Symptoms Improve',
        'Clue 5: Anti-inflammatory, Antiasthmatic'
    ],
    'Albuterol': [
        'Clue 1: Inhalation, Oral | 2mg-4mg',
        'Clue 2: Agonist at Beta-2 Receptors, Bronchodilator',
        'Clue 3: Nervousness, Tremors, Headache',
        'Clue 4: Do Not Use More Frequently than Prescribed, Do Not Use with Other Sympathomimetic Drugs, Avoid Use in Children under 4 years old',
        'Clue 5: Bronchodilator'
    ],
    'Azelastine': [
        'Clue 1: Nasal Spray | 0.15mg',
        'Clue 2: Histamine H1 Receptor Antagonist',
        'Clue 3: Bitter Taste, Headache, Nasal Irritation',
        'Clue 4: Administer at Regular Intervals, Discard After 200 Sprays, Avoid Alcohol Consumption',
        'Clue 5: Allergic Rhinitis, Vasomotor Rhinitis'
    ],
    'Loratadine': [
        'Clue 1: Oral | 10mg',
        'Clue 2: Histamine H1 Receptor Antagonist',
        'Clue 3: Dry Mouth, Headache, Fatigue',
        'Clue 4: Take with Water, Do Not Crush or Chew, Avoid Alcohol Consumption',
        'Clue 5: Allergic Rhinitis, Chronic Urticaria'
    ],
    'Phenylephrine': [
        'Clue 1: Oral, Intranasal | 5mg-10mg',
        'Clue 2: Alpha-1 Adrenergic Receptor Agonist',
        'Clue 3: Nausea, Vomiting, Headache',
        'Clue 4: Do Not Exceed Recommended Dose, Avoid Alcohol Consumption, Monitor Blood Pressure',
        'Clue 5: Nasal Congestion, Hypotension'
    ],
    'Hydrocodone': [
        'Clue 1: Oral | 5mg-10mg',
        'Clue 2: Mu Opioid Receptor Agonist',
        'Clue 3: Drowsiness, Nausea, Constipation',
        'Clue 4: Do Not Crush or Chew, Avoid Alcohol Consumption, Monitor for Abuse Potential',
        'Clue 5: Pain Relief, Cough Suppressant'
    ],
    'Dextromethorphan': [
        'Clue 1: Oral | 15mg-30mg',
        'Clue 2: NMDA Receptor Antagonist',
        'Clue 3: Dizziness, Nausea, Vomiting',
        'Clue 4: Do Not Exceed Recommended Dose, Avoid Alcohol Consumption, Monitor for Abuse Potential',
        'Clue 5: Cough Suppressant'
    ],
    'Famotidine': [
        'Clue 1: Oral | 20mg-40mg',
        'Clue 2: Histamine H2 Receptor Antagonist',
        'Clue 3: Headache, Dizziness, Constipation',
        'Clue 4: Take with Water, Do Not Crush or Chew, Avoid Alcohol Consumption',
        'Clue 5: Gastroesophageal Reflux Disease, Peptic Ulcer Disease'
    ],
    'Omeprazole': [
        'Clue 1: Oral | 20mg-40mg',
        'Clue 2: Proton Pump Inhibitor',
        'Clue 3: Abdominal Pain, Nausea, Diarrhea',
        'Clue 4: Take on Empty Stomach, Swallow Whole, Avoid Alcohol Consumption',
        'Clue 5: Gastroesophageal Reflux Disease, Peptic Ulcer Disease'
    ],
        'Sucralfate': [
        'Clue 1: Oral | 1g-2g',
        'Clue 2: Forms a Barrier on Ulcers, Erosions, and Lesions',
        'Clue 3: Constipation',
        'Clue 4: Take on an Empty Stomach, Antacids May Decrease Efficacy, Separate Doses of Other Medications',
        'Clue 5: Treatment of Duodenal Ulcers, Treatment of Gastric Ulcers'
    ],
    'Aluminum hydroxide': [
        'Clue 1: Oral | 320mg-1680mg',
        'Clue 2: Antacid that Neutralizes Gastric Acid',
        'Clue 3: Constipation',
        'Clue 4: Separate Doses of Other Medications, Take with Plenty of Water',
        'Clue 5: Treatment of Hyperphosphatemia, Treatment of GERD'
    ],
    'Psyllium': [
        'Clue 1: Oral | 5g-10g',
        'Clue 2: Soluble Fiber Supplement',
        'Clue 3: Constipation',
        'Clue 4: Mix with Water or Juice, Take Immediately After Mixing',
        'Clue 5: Treatment of Constipation, Treatment of Diarrhea'
    ],
    'Docusate sodium': [
        'Clue 1: Oral, Rectal | 50mg-200mg',
        'Clue 2: Emollient Laxative',
        'Clue 3: Diarrhea',
        'Clue 4: Take with Plenty of Water, Do Not Take for More than 1 Week without Consulting Physician',
        'Clue 5: Treatment of Constipation'
    ],
    'Bisacodyl': [
        'Clue 1: Oral, Rectal | 5mg-15mg',
        'Clue 2: Stimulant Laxative',
        'Clue 3: Abdominal Cramping, Diarrhea',
        'Clue 4: Take with Plenty of Water, Do Not Take for More than 1 Week without Consulting Physician',
        'Clue 5: Treatment of Constipation, Preparation for Colonoscopy'
    ],
    'Magnesium hydroxide': [
        'Clue 1: Oral | 240mg-480mg',
        'Clue 2: Antacid and Osmotic Laxative',
        'Clue 3: Diarrhea',
        'Clue 4: Separate Doses of Other Medications, Take with Plenty of Water',
        'Clue 5: Treatment of Hyperphosphatemia, Treatment of GERD, Treatment of Constipation'
    ], 
        'Ondansetron': [
        'Clue 1: Oral, I.V. | 4mg-8mg',
        'Clue 2: Selective 5-HT3 Receptor Antagonist',
        'Clue 3: Headache, Constipation, Fatigue',
        'Clue 4: Assess Electrolyte Imbalances, Monitor ECG for QT Prolongation, Observe for Extrapyramidal Symptoms',
        'Clue 5: Nausea and Vomiting Associated with Chemotherapy, Radiation, and Surgery'
    ],
    'Dexamethasone': [
        'Clue 1: Oral, I.V. | 0.5mg-10mg',
        'Clue 2: Glucocorticoid, Immunosuppressant',
        'Clue 3: Increased Appetite, Insomnia, Mood Changes',
        'Clue 4: Monitor Blood Glucose and Blood Pressure, Assess for Infection, Observe for Adrenal Suppression',
        'Clue 5: Anti-inflammatory, Allergic Reactions, Cancer-Related Symptoms'
    ],
    'Aprepitant': [
        'Clue 1: Oral | 40mg-125mg',
        'Clue 2: Substance P/Neurokinin-1 Receptor Antagonist',
        'Clue 3: Fatigue, Diarrhea, Constipation',
        'Clue 4: Assess for Drug Interactions, Monitor Electrolytes, Observe for Adverse Reactions',
        'Clue 5: Nausea and Vomiting Associated with Chemotherapy'
    ],
    'Prochlorperazine': [
        'Clue 1: Oral, Rectal | 5mg-10mg',
        'Clue 2: Dopamine D2 Receptor Antagonist',
        'Clue 3: Drowsiness, Dry Mouth, Blurred Vision',
        'Clue 4: Assess for Extrapyramidal Symptoms, Monitor Vital Signs, Observe for Adverse Reactions',
        'Clue 5: Nausea and Vomiting Associated with Surgery and Radiation'
    ],
       'Penicillin G': [
        'Clue 1: I.V., I.M. | 1 million units-24 million units',
        'Clue 2: Inhibits Bacterial Cell Wall Synthesis',
        'Clue 3: Hypersensitivity Reactions, Nausea, Diarrhea',
        'Clue 4: Monitor for Allergic Reactions, Observe for Superinfection, Assess for Cross-Sensitivity to Other Antibiotics',
        'Clue 5: Bacterial Infections Including Syphilis, Meningitis, Endocarditis'
    ],
    'Cephalexin': [
        'Clue 1: Oral | 250mg-1000mg',
        'Clue 2: Inhibits Bacterial Cell Wall Synthesis',
        'Clue 3: Nausea, Diarrhea, Allergic Reactions',
        'Clue 4: Monitor for Superinfection, Assess for Renal Function, Observe for Adverse Reactions',
        'Clue 5: Bacterial Infections Including Respiratory, Skin, and Genitourinary Tract Infections'
    ],
    'Imipenem/cilastatin': [
        'Clue 1: I.V., I.M. | 250mg-1000mg',
        'Clue 2: Carbapenem Antibiotic, Inhibits Bacterial Cell Wall Synthesis',
        'Clue 3: Nausea, Diarrhea, Hypersensitivity Reactions',
        'Clue 4: Assess for Seizure Risk, Monitor Renal Function, Observe for Superinfection',
        'Clue 5: Bacterial Infections Including Respiratory, Skin, and Intra-Abdominal Infections'
    ],
    'Vancomycin': [
        'Clue 1: I.V., Oral | 125mg-2000mg',
        'Clue 2: Glycopeptide Antibiotic, Inhibits Bacterial Cell Wall Synthesis',
        'Clue 3: Red Man Syndrome, Nausea, Diarrhea',
        'Clue 4: Monitor Serum Concentrations, Assess for Ototoxicity and Nephrotoxicity, Observe for Allergic Reactions',
        'Clue 5: Bacterial Infections Including Methicillin-Resistant Staphylococcus Aureus (MRSA) and Clostridioides Difficile (C. diff)'
    ],
    'Tetracycline': [
        'Clue 1: Oral | 250mg-500mg',
        'Clue 2: Inhibits Bacterial Protein Synthesis',
        'Clue 3: Photosensitivity, Nausea, Diarrhea',
        'Clue 4: Avoid Use in Pregnancy and Children Under 8, Monitor Liver Function, Observe for Superinfection',
        'Clue 5: Bacterial Infections Including Acne, Chlamydia, and Lyme Disease'
    ],
       'Erythromycin': [
        'Clue 1: Oral, I.V. | 250mg-500mg',
        'Clue 2: Binds to the 50S subunit of the bacterial ribosome',
        'Clue 3: Nausea, Vomiting, Abdominal Cramping',
        'Clue 4: Take with Food, Monitor Liver Function, May Interact with Other Medications',
        'Clue 5: Bacterial Infections, Acne, Diphtheria'
    ],
    'Clindamycin': [
        'Clue 1: Oral, I.V. | 150mg-300mg',
        'Clue 2: Binds to the 50S subunit of the bacterial ribosome',
        'Clue 3: Diarrhea, Abdominal Cramping, Nausea',
        'Clue 4: Take with Food, Monitor Liver Function, May Interact with Other Medications',
        'Clue 5: Bacterial Infections, Acne, Malaria'
    ],
    'Gentamicin': [
        'Clue 1: I.M., I.V. | 80mg-160mg',
        'Clue 2: Binds to the 30S subunit of the bacterial ribosome',
        'Clue 3: Nausea, Vomiting, Tinnitus',
        'Clue 4: Monitor Renal Function, May Interact with Other Medications, Peak and Trough Levels',
        'Clue 5: Bacterial Infections, Septicemia, Meningitis'
    ],
    'Sulfisoxazole': [
        'Clue 1: Oral | 500mg-1000mg',
        'Clue 2: Inhibits Dihydropteroate Synthase',
        'Clue 3: Nausea, Vomiting, Diarrhea',
        'Clue 4: Take with Food, Monitor Renal Function, May Interact with Other Medications',
        'Clue 5: Bacterial Infections, Malaria, Toxoplasmosis'
    ],
    'Isoniazid': [
        'Clue 1: Oral | 300mg-600mg',
        'Clue 2: Inhibits Mycolic Acid Synthesis',
        'Clue 3: Peripheral Neuropathy, Hepatotoxicity, Optic Neuritis',
        'Clue 4: Monitor Liver Function, May Interact with Other Medications, Complete Full Course of Treatment',
        'Clue 5: Tuberculosis, Latent Tuberculosis, Prophylaxis'
    ],
    'Rifampin': [
        'Clue 1: Oral | 150mg-600mg',
        'Clue 2: Inhibits RNA Polymerase',
        'Clue 3: Nausea, Vomiting, Diarrhea',
        'Clue 4: Monitor Liver Function, May Interact with Other Medications, Complete Full Course of Treatment',
        'Clue 5: Tuberculosis, Meningitis, Leprosy'
    ],
        'Ciprofloxacin': [
        'Clue 1: Oral, I.V. | 250mg-750mg',
        'Clue 2: Inhibits Bacterial DNA Synthesis',
        'Clue 3: Nausea, Diarrhea, Headache',
        'Clue 4: Monitor for Tendinitis, Take 2 Hours Before or 6 Hours After Antacids, Maintain Hydration',
        'Clue 5: Antibiotic, Fluoroquinolone'
    ],
    'Amphotericin B': [
        'Clue 1: I.V. | 0.3mg/kg/day',
        'Clue 2: Binds to Fungal Cell Membrane Ergosterol',
        'Clue 3: Nausea, Vomiting, Fever, Chills',
        'Clue 4: Monitor for Nephrotoxicity, Hypokalemia, Hypomagnesemia, and Hypocalcemia',
        'Clue 5: Antifungal, Polyene Macrolide'
    ],
    'Itraconazole': [
        'Clue 1: Oral | 100mg-200mg',
        'Clue 2: Inhibits Fungal Cytochrome P450 Enzymes',
        'Clue 3: Nausea, Vomiting, Abdominal Pain',
        'Clue 4: Monitor for Hepatotoxicity, Take with Food or Acid Reducers',
        'Clue 5: Antifungal, Triazole'
    ],
    'Influenza vaccine': [
        'Clue 1: Intramuscular | 0.5mL',
        'Clue 2: Contains Inactivated Virus Particles',
        'Clue 3: Soreness at Injection Site, Headache, Fatigue',
        'Clue 4: Contraindicated in Those with Severe Allergy to Eggs or Other Vaccine Components, Administer Annually',
        'Clue 5: Prevents Influenza Infection'
    ],
    'Insulin lispro': [
        'Clue 1: Subcutaneous | 5 units-15 units',
        'Clue 2: Rapid-Acting Insulin Analogue',
        'Clue 3: Hypoglycemia, Injection Site Reactions, Lipodystrophy',
        'Clue 4: Monitor Blood Glucose, Administer Before Meals or After Meals Within 15 Minutes',
        'Clue 5: Treats Hyperglycemia, Insulin'
    ],
    'Regular insulin': [
        'Clue 1: Subcutaneous, I.V. | 5 units-15 units',
        'Clue 2: Short-Acting Insulin',
        'Clue 3: Hypoglycemia, Injection Site Reactions, Lipodystrophy',
        'Clue 4: Monitor Blood Glucose, Administer Before Meals or After Meals Within 30 Minutes',
        'Clue 5: Treats Hyperglycemia, Insulin'
    ],
        'NPH insulin': [
        'Clue 1: Subcutaneous | 10-20 Units',
        'Clue 2: Intermediate-Acting Insulin',
        'Clue 3: Hypoglycemia, Weight Gain, Injection Site Reactions',
        'Clue 4: Rotate Injection Sites, Administer 30 minutes before Meals, Store in the Refrigerator',
        'Clue 5: Diabetes Mellitus Type 1 and 2, Hyperglycemia'
    ],
    'Insulin glargine': [
        'Clue 1: Subcutaneous | 10-20 Units',
        'Clue 2: Long-Acting Insulin',
        'Clue 3: Hypoglycemia, Weight Gain, Injection Site Reactions',
        'Clue 4: Rotate Injection Sites, Administer at the Same Time Every Day, Store in the Refrigerator',
        'Clue 5: Diabetes Mellitus Type 1 and 2, Hyperglycemia'
    ],
    'Metformin': [
        'Clue 1: Oral | 500mg-1000mg',
        'Clue 2: Decreases Hepatic Glucose Production and Increases Insulin Sensitivity',
        'Clue 3: Nausea, Diarrhea, Abdominal Discomfort',
        'Clue 4: Monitor Renal Function, Take with Meals, Discontinue Prior to Iodinated Contrast Imaging',
        'Clue 5: Diabetes Mellitus Type 2, Polycystic Ovary Syndrome'
    ],
    'Glyburide': [
        'Clue 1: Oral | 2.5mg-10mg',
        'Clue 2: Stimulates Insulin Secretion',
        'Clue 3: Hypoglycemia, Nausea, Dizziness',
        'Clue 4: Take with Meals, Monitor Blood Glucose Levels, Avoid Alcohol Consumption',
        'Clue 5: Diabetes Mellitus Type 2'
    ],
    'Pioglitazone': [
        'Clue 1: Oral | 15mg-45mg',
        'Clue 2: Increases Insulin Sensitivity',
        'Clue 3: Edema, Weight Gain, Hypoglycemia',
        'Clue 4: Take with or without Food, Monitor Liver Function, Discontinue Prior to Iodinated Contrast Imaging',
        'Clue 5: Diabetes Mellitus Type 2'
    ],
        'Repaglinide': [
        'Clue 1: Oral | 0.5mg-4mg',
        'Clue 2: Stimulates Insulin Release from Pancreatic Beta Cells',
        'Clue 3: Hypoglycemia, Nausea, Headache',
        'Clue 4: Monitor Blood Glucose, Take Before Meals, Avoid Alcohol Consumption',
        'Clue 5: Type 2 Diabetes Mellitus'
    ],
    'Levothyroxine': [
        'Clue 1: Oral, I.V. | 25mcg-300mcg',
        'Clue 2: Replaces or Supplements Thyroid Hormone',
        'Clue 3: Tachycardia, Nervousness, Insomnia',
        'Clue 4: Monitor TSH Levels, Take in Morning on Empty Stomach, Avoid Antacids',
        'Clue 5: Hypothyroidism'
    ],
    'Methimazole': [
        'Clue 1: Oral | 5mg-60mg',
        'Clue 2: Inhibits Thyroid Hormone Synthesis',
        'Clue 3: Rash, Itching, Joint Pain',
        'Clue 4: Monitor TSH and T4 Levels, Take with Food, Avoid Iodine-rich Foods',
        'Clue 5: Hyperthyroidism'
    ],
    'Desmopressin': [
        'Clue 1: Oral, Intranasal, I.V. | 0.1mg-0.4mg',
        'Clue 2: Increases Water Reabsorption in the Kidneys',
        'Clue 3: Headache, Nausea, Abdominal Pain',
        'Clue 4: Monitor Serum Sodium Levels, Take at Bedtime, Avoid Fluids 1 Hour After Dosing',
        'Clue 5: Diabetes Insipidus'
    ],
    'Vasopressin': [
        'Clue 1: I.V. | 0.5 units-1 unit',
        'Clue 2: Increases Blood Pressure and Decreases Urine Output',
        'Clue 3: Palpitations, Headache, Nausea',
        'Clue 4: Monitor Blood Pressure and Fluid Balance, Administer via Central Line, Contraindicated in Coronary Artery Disease',
        'Clue 5: Shock'
    ],
    'Furosemide': [
        'Clue 1: Oral, I.V. | 20mg-160mg',
        'Clue 2: Inhibits Sodium and Chloride Reabsorption in the Kidneys',
        'Clue 3: Dehydration, Hypokalemia, Hypotension',
        'Clue 4: Monitor Serum Electrolytes and Fluid Balance, Administer Slowly via I.V., Avoid Alcohol Consumption',
        'Clue 5: Edema, Hypertension, Heart Failure'
    ],
    'Hydrochlorothiazide': [
        'Clue 1: Oral | 12.5mg-50mg',
        'Clue 2: Inhibits Reabsorption of Sodium and Chloride in the Distal Renal Tubule',
        'Clue 3: Hypokalemia, Hyperuricemia, Hyponatremia',
        'Clue 4: Monitor Electrolyte Levels, Take with Food or Milk, Avoid Sun Exposure',
        'Clue 5: Hypertension, Edema'
    ],
    'Spironolactone': [
        'Clue 1: Oral | 25mg-100mg',
        'Clue 2: Competes with Aldosterone for Receptors in the Distal Renal Tubule',
        'Clue 3: Hyperkalemia, Gynecomastia, Menstrual Irregularities',
        'Clue 4: Monitor Electrolyte Levels, Take with Food or Milk, Avoid Sun Exposure',
        'Clue 5: Hypertension, Edema'
    ],
    'Nitrofurantoin': [
        'Clue 1: Oral | 50mg-100mg',
        'Clue 2: Bactericidal Activity against UTI Pathogens',
        'Clue 3: Nausea, Headache, Brown Urine',
        'Clue 4: Take with Food or Milk, Maintain Hydration, Avoid in Pregnancy at Term',
        'Clue 5: UTI Prophylaxis, Treatment of Acute Cystitis'
    ],
    'Captopril': [
        'Clue 1: Oral | 6.25mg-50mg',
        'Clue 2: Inhibits Angiotensin-Converting Enzyme',
        'Clue 3: Cough, Hypotension, Rash',
        'Clue 4: Monitor Blood Pressure, Take on an Empty Stomach, Avoid Salt Substitutes',
        'Clue 5: Hypertension, Heart Failure'
    ],
    'Lorsartan': [
        'Clue 1: Oral | 25mg-100mg',
        'Clue 2: Blocks Angiotensin II Receptors',
        'Clue 3: Hypotension, Hyperkalemia, Dizziness',
        'Clue 4: Monitor Blood Pressure, Take with or without Food, Avoid in Pregnancy at Term',
        'Clue 5: Hypertension'
    ],
    'Eplerenone': [
        'Clue 1: Oral | 25mg-100mg',
        'Clue 2: Blocks Aldosterone Receptors',
        'Clue 3: Hyperkalemia, Gynecomastia, Menstrual Irregularities',
        'Clue 4: Monitor Electrolyte Levels, Take with Food or Milk, Avoid Sun Exposure',
        'Clue 5: Hypertension, Heart Failure'
    ],
        'Dopamine': [
        'Clue 1: I.V. Infusion | 2-20 mcg/kg/min',
        'Clue 2: Increases Cardiac Output and Blood Pressure',
        'Clue 3: Tachycardia, Arrhythmia, Headache, Nausea, Vomiting',
        'Clue 4: Monitor Vital Signs, Titrate Dose, Administer via Central Line',
        'Clue 5: Shock, Heart Failure, Hypotension'
    ],
    'Lovastatin': [
        'Clue 1: Oral | 20mg-40mg',
        'Clue 2: HMG-CoA Reductase Inhibitor',
        'Clue 3: Abdominal Pain, Diarrhea, Headache',
        'Clue 4: Avoid Grapefruit Juice, Monitor Liver Function Tests',
        'Clue 5: Hypercholesterolemia'
    ],
    'Colesevelam': [
        'Clue 1: Oral | 625mg-1875mg',
        'Clue 2: Bile Acid Sequestrant',
        'Clue 3: Constipation, Abdominal Pain, Nausea',
        'Clue 4: Administer with Meals and Liquid, Monitor Lipid Levels',
        'Clue 5: Hypercholesterolemia'
    ],
    'Ezetimibe': [
        'Clue 1: Oral | 10mg',
        'Clue 2: Cholesterol Absorption Inhibitor',
        'Clue 3: Abdominal Pain, Diarrhea, Fatigue',
        'Clue 4: Monitor Lipid Levels, Administer with Meals',
        'Clue 5: Hypercholesterolemia'
    ],
    'Nitroglycerin': [
        'Clue 1: Sublingual, Topical, I.V. | 0.3mg-0.6mg',
        'Clue 2: Vasodilator',
        'Clue 3: Headache, Dizziness, Hypotension',
        'Clue 4: Store in Dark Container, Protect from Light, Replace every 6 Months',
        'Clue 5: Angina Pectoris, Heart Failure'
    ],
    'Aspirin': [
        'Clue 1: Oral, Rectal | 325mg-650mg',
        'Clue 2: Inhibits Cyclooxygenase-1 and Cyclooxygenase-2',
        'Clue 3: Nausea, Vomiting, Heartburn',
        'Clue 4: Monitor for Bleeding, Discontinue Prior to Surgery, Avoid Alcohol Consumption',
        'Clue 5: Pain Relief, Anti-inflammatory, Antipyretic'
],
'Clopidogrel': [
        'Clue 1: Oral | 75mg-300mg',
        'Clue 2: Inhibits Platelet Aggregation by Irreversibly Blocking ADP P2Y12 Receptors',
        'Clue 3: Nausea, Diarrhea, Bleeding',
        'Clue 4: Monitor for Bleeding, Discontinue Prior to Surgery, Avoid Alcohol Consumption',
        'Clue 5: Prevention of Blood Clots'
],
'Alteplase': [
        'Clue 1: Intravenous',
        'Clue 2: Converts Plasminogen to Plasmin, Which Dissolves Fibrin Clots',
        'Clue 3: Bleeding, Hypotension',
        'Clue 4: Monitor for Bleeding, Do Not Administer with Antiplatelet Agents or Anticoagulants',
        'Clue 5: Treatment of Acute Ischemic Stroke, Pulmonary Embolism, and Acute Myocardial Infarction'
],
'Ferrous sulfate': [
        'Clue 1: Oral | 325mg',
        'Clue 2: Replenishes Iron Stores and Treats Iron Deficiency Anemia',
        'Clue 3: Nausea, Constipation, Black Stools',
        'Clue 4: Take on an Empty Stomach, Do Not Take with Dairy or Antacids, Do Not Crush or Chew Tablets',
        'Clue 5: Treatment of Iron Deficiency Anemia'
],
'Iron dextran': [
        'Clue 1: Intravenous | 100mg-200mg',
        'Clue 2: Replenishes Iron Stores and Treats Iron Deficiency Anemia',
        'Clue 3: Hypotension, Anaphylaxis, Brown Urine',
        'Clue 4: Administer Test Dose Prior to Full Dose, Monitor for Adverse Reactions',
        'Clue 5: Treatment of Iron Deficiency Anemia'
],
'Cyanocobalamin': [
        'Clue 1: Intramuscular, Intravenous | 1000mcg',
        'Clue 2: Essential for DNA Synthesis and Red Blood Cell Formation',
        'Clue 3: Nausea, Diarrhea, Itching',
        'Clue 4: Administer in a Well-Ventilated Area, Monitor for Adverse Reactions',
        'Clue 5: Treatment of Vitamin B12 Deficiency'
],
   'Folic acid': [
        'Clue 1: Oral | 400mcg-1mg',
        'Clue 2: Coenzyme for DNA Synthesis and Cell Growth',
        'Clue 3: Nausea, Bloating, Flatulence',
        'Clue 4: Deficiency may cause Megaloblastic Anemia and Neural Tube Defects',
        'Clue 5: Pregnancy Supplement, Anemia Treatment'
    ],
    'Fluoxetine': [
        'Clue 1: Oral | 10mg-60mg',
        'Clue 2: Selective Serotonin Reuptake Inhibitor',
        'Clue 3: Nausea, Insomnia, Headache',
        'Clue 4: May Increase Risk of Suicidal Thoughts in Children and Adolescents',
        'Clue 5: Depression, Anxiety, Obsessive Compulsive Disorder'
    ],
    'Venlafaxine': [
        'Clue 1: Oral | 37.5mg-225mg',
        'Clue 2: Serotonin-Norepinephrine Reuptake Inhibitor',
        'Clue 3: Nausea, Dizziness, Headache',
        'Clue 4: May Increase Blood Pressure and Heart Rate',
        'Clue 5: Depression, Anxiety, Panic Disorder'
    ],
    'Imipramine': [
        'Clue 1: Oral | 10mg-300mg',
        'Clue 2: Tricyclic Antidepressant',
        'Clue 3: Dry Mouth, Constipation, Blurred Vision',
        'Clue 4: May Increase Risk of Suicide in Children and Adolescents',
        'Clue 5: Depression, Bedwetting, Panic Disorder'
    ],
    'Selegiline': [
        'Clue 1: Oral, Transdermal | 5mg-10mg',
        'Clue 2: Selective Monoamine Oxidase Inhibitor',
        'Clue 3: Insomnia, Nausea, Headache',
        'Clue 4: May Increase Risk of Serotonin Syndrome',
        'Clue 5: Parkinson\'s Disease, Depression'
    ],
    'Bupropion': [
        'Clue 1: Oral | 75mg-450mg',
        'Clue 2: Norepinephrine-Dopamine Reuptake Inhibitor',
        'Clue 3: Dry Mouth, Insomnia, Headache',
        'Clue 4: May Increase Risk of Seizures',
        'Clue 5: Depression, Smoking Cessation'
    ],
    'Diazepam': [
        'Clue 1: Oral, I.M. | 2mg-10mg',
        'Clue 2: Binds to GABA-A Receptors',
        'Clue 3: Drowsiness, Ataxia, Anterograde Amnesia',
        'Clue 4: Avoid Alcohol Consumption, Monitor for Respiratory Depression',
        'Clue 5: Anxiolytic, Sedative, Muscle Relaxant'
    ],
    'Triazolam': [
        'Clue 1: Oral | 0.125mg-0.5mg',
        'Clue 2: Binds to GABA-A Receptors',
        'Clue 3: Drowsiness, Ataxia, Anterograde Amnesia',
        'Clue 4: Avoid Alcohol Consumption, Monitor for Respiratory Depression',
        'Clue 5: Anxiolytic, Sedative, Hypnotic'
    ],
    'Zolpidem': [
        'Clue 1: Oral | 5mg-10mg',
        'Clue 2: Binds to GABA-A Receptors',
        'Clue 3: Drowsiness, Ataxia, Anterograde Amnesia',
        'Clue 4: Avoid Alcohol Consumption, Monitor for Respiratory Depression',
        'Clue 5: Sedative, Hypnotic'
    ],
    'Buspirone': [
        'Clue 1: Oral | 5mg-30mg',
        'Clue 2: Partial Agonist of Serotonin 5-HT1A Receptors',
        'Clue 3: Nausea, Headache, Dizziness',
        'Clue 4: Takes Several Weeks to Reach Therapeutic Effects',
        'Clue 5: Anxiolytic'
    ],
    'Lithium': [
        'Clue 1: Oral, I.V. | 300mg-1200mg',
        'Clue 2: Affects Sodium Transport in Nerve and Muscle Cells',
        'Clue 3: Tremors, Polyuria, Hypothyroidism',
        'Clue 4: Monitor Serum Lithium Levels, Renal and Thyroid Function',
        'Clue 5: Treatment for Bipolar Disorder, Anti-Manic Agent'
    ],
    'Carbamazepine': [
        'Clue 1: Oral | 100mg-400mg',
        'Clue 2: Blocks Voltage-gated Sodium Channels',
        'Clue 3: Nausea, Vomiting, Headache',
        'Clue 4: Monitor Serum Carbamazepine Levels, Liver Function',
        'Clue 5: Treatment for Epilepsy, Bipolar Disorder, Trigeminal Neuralgia'
    ],
    'Valproic acid': [
        'Clue 1: Oral | 250mg-500mg',
        'Clue 2: Increases GABA Concentration in the Brain',
        'Clue 3: Nausea, Vomiting, Headache',
        'Clue 4: Monitor Serum Valproic Acid Levels, Liver Function',
        'Clue 5: Treatment for Epilepsy, Bipolar Disorder'
    ]
}
