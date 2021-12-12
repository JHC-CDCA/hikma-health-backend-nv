from events.event import Event
from admin_api.patient_data_import import PatientDataRow
import json

def get_field(data, field):
    if data.get(field) is None:
        return None
    return 'Si' if data.get(field) else 'No'

def get_text_field(data, field, text_field):
    if data.get(field) is None:
        return None
    if data.get(field) is not None and not data.get(text_field):
        return 'Si' if data.get(field) else 'No'
    return data.get(text_field) if data.get(field) else 'No'

def get_text_field_positive(data, field, text_field):
    if data.get(field) is None:
        return None
    if data.get(field) is not None and not data.get(text_field):
        return 'Positivo' if data.get(field) else 'Negativo'
    return data.get(text_field) if data.get(field) else 'Negativo'

def get_feeding_center(data):
    if data.get('feedingCenter') == 'Other':
        return 'Otro'
    return data.get('feedingCenter')    

def write_patient_details_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.medical_num = data.get('medicalNum')
    row.dental_num = data.get('dentalNum')
    row.optometry_num = data.get('optometryNum')
    row.patient_id = data.get('patientId')
    row.community = data.get('community')
    row.zone = data.get('zone')
    row.block = data.get('block')
    row.lot = data.get('lot')
    row.emergency_phone = data.get('emergencyPhone')
    row.mother = data.get('mother')
    row.mother_phone = data.get('motherPhone')
    row.father = data.get('father')
    row.father_phone = data.get('fatherPhone')
    row.partner = data.get('partner')
    row.partner_phone = data.get('partnerPhone')
    row.employer = data.get('employer')
    row.insurance = data.get('insurance')

def write_vitals_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_v = data.get('doctor')
    row.glycemia = data.get('glycemia')
    row.weight = data.get('weight')
    row.weight_lb = data.get('weightLb')
    row.ideal_weight = data.get('idealWeight')
    if data.get('systolic') and data.get('diastolic'):
        row.blood_pressure = f"{data.get('systolic')}/{data.get('diastolic')}"
    row.pulse = data.get('pulse')
    row.respiration = data.get('respiration')
    row.o2_sats = data.get('sats')
    row.height = data.get('height')
    row.temperature = data.get('temp')

def write_medical_hx_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_mh = data.get('doctor')
    row.malnutrition = data.get('malnutrition')
    row.prenatal = data.get('prenatal')
    row.sexual_hx = data.get('sexualHx')
    row.nutrition = data.get('nutrition')
    row.parasite_treatment = data.get('parasiteTreatment')
    row.family_hx = data.get('familyHx')
    row.surgery_hx = data.get('surgeryHx')
    row.vaccinations = data.get('vaccinations')
    row.blood_type = data.get('bloodType')

def write_evaluation_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_ce = data.get('doctor')
    row.visit_date = data.get('visitDate')
    row.reason = data.get('reason')
    row.observations = data.get('observations')
    row.medications = data.get('medications')
    row.breast_exam = get_field(data, 'breastExam')
    row.diagnosis = data.get('diagnosis')
    row.treatment = data.get('treatment')
    row.community_visit = get_text_field(data, 'communityVisit', 'communityVisitDate')
    row.promoter_visit = get_text_field(data, 'promoterVisit', 'promoterVisitDate')
    row.refusal = get_text_field(data, 'refusal', 'refusalDate')
    row.next_visit_date = data.get('nextVisitDate')
    row.next_visit_reason = data.get('nextVisitReason')

def write_med_stock_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_s = data.get('doctor')
    row.medicine_s = data.get('medicine')
    row.format_s = data.get('format')
    row.dosage_s = data.get('dosage')
    row.days_s = data.get('days')

def write_med_otc_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_otc = data.get('doctor')
    row.medicine_otc = data.get('medicine')
    row.format_otc = data.get('format')
    row.dosage_otc = data.get('dosage')
    row.days_otc = data.get('days')

def write_controlled_med_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_c = data.get('doctor')
    row.medicine_c = data.get('medicine')
    row.format_c = data.get('format')
    row.dosage_c = data.get('dosage')
    row.days_c = data.get('days')

def write_med_pathologies_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_mp = data.get('doctor')
    row.miscarriages =  get_text_field(data, 'miscarriages', 'miscarriagesNumber')
    row.food_allergies = get_text_field(data, 'foodAllergies', 'foodAllergiesText') 
    row.animal_allergies = get_text_field(data, 'animalAllergies', 'animalAllergiesText') 
    row.atmosphere_allergies = get_text_field(data, 'atmosphereAllergies', 'atmosphereAllergiesText') 
    row.insect_allergies = get_text_field(data, 'insectAllergies', 'insectAllergiesText') 
    row.latex_allergies = get_text_field(data, 'latexAllergies', 'latexAllergiesText') 
    row.medicine_allergies = get_text_field(data, 'medicineAllergies', 'medicineAllergiesText') 
    row.other_allergies = get_text_field(data, 'otherAllergies', 'otherAllergiesText') 
    row.tonsillitis = get_text_field(data, 'tonsillitis', 'tonsillitisText') 
    row.anemic = get_text_field(data, 'anemic', 'anemicText') 
    row.arthritis = get_text_field(data, 'arthritis', 'arthritisText') 
    row.asthma = get_text_field(data, 'asthma', 'asthmaText') 
    row.neck_pain = get_text_field(data, 'neckPain', 'neckPainText') 
    row.cervicovaginitis = get_text_field(data, 'cervicovaginitis', 'cervicovaginitisText') 
    row.c_section = data.get('cSection')
    row.sciatic_pain = get_text_field(data, 'sciaticPain', 'sciaticPainText') 
    row.cholesterol = get_text_field(data, 'cholesterol', 'cholesterolText') 
    row.infant_colic = get_text_field(data, 'infantColic', 'infantColicText') 
    row.conjunctivitis = get_text_field(data, 'conjunctivitis', 'conjunctivitisText') 
    row.covid = get_text_field(data, 'covid', 'covidText') 
    row.malnourishment = get_text_field(data, 'malnourishment', 'malnourishmentText')
    row.diabetes = get_text_field(data, 'diabetes', 'diabetesText')
    row.migraines = get_text_field(data, 'migraines', 'migrainesText') 
    row.diarrhea = get_text_field(data, 'diarrhea', 'diarrheaText') 
    row.ecocardiogram = get_text_field(data, 'ecocardiogram', 'ecocardiogramText') 
    row.electrocardiogram = get_text_field(data, 'electrocardiogram', 'electrocardiogramText') 
    row.pregnant = get_field(data, 'pregnant')
    row.pregnancies = data.get('pregnancies')
    row.chikungunya = get_text_field(data, 'chikungunya', 'chikungunyaText') 
    row.dengue = get_text_field(data, 'dengue', 'dengueText') 
    row.malaria = get_text_field(data, 'malaria', 'malariaText') 
    row.other_mosquito = get_text_field(data, 'otherMosquito', 'otherMosquitoText') 
    row.zika = get_text_field(data, 'zika', 'zikaText') 
    row.copd = get_text_field(data, 'copd', 'copdText') 
    row.gastritis = get_text_field(data, 'gastritis', 'gastritisText') 
    row.scabies = get_text_field(data, 'scabies', 'scabiesText') 
    row.distress = get_text_field(data, 'distress', 'distressText')
    row.last_PAP = data.get('lastPAP') 
    row.vaginal_fluid = get_text_field(data, 'vaginalFluid', 'vaginalFluidText') 
    row.hypertension = get_text_field(data, 'hypertension', 'hypertensionText') 
    row.hypothyroidism = get_text_field(data, 'hypothyroidism', 'hypothyroidismText') 
    row.bacterial_resp = get_text_field(data, 'bacterialResp', 'bacterialRespText') 
    row.viral_resp = get_text_field(data, 'viralResp', 'viralRespText') 
    row.uti = get_text_field(data, 'uti', 'utiText') 
    row.renal_failure = get_text_field(data, 'renalFailure', 'renalFailureText') 
    row.breastfeeding = get_text_field(data, 'breastfeeding', 'breastfeedingText') 
    row.lumbago = get_text_field(data, 'lumbago', 'lumbagoText') 
    row.menopause = get_text_field(data, 'menopause', 'menopauseText') 
    row.nausea = get_text_field(data, 'nausea', 'nauseaText') 
    row.nephrolithiasis_renal = get_text_field(data, 'nephrolithiasisRenal', 'nephrolithiasisRenalText') 
    row.diabetic_neuropathy = get_text_field(data, 'diabeticNeuropathy', 'diabeticNeuropathyText') 
    row.obesity = get_text_field(data, 'obesity', 'obesityText') 
    row.osteoarthritis = get_text_field(data, 'osteoarthritis', 'osteoarthritisText') 
    row.otitis = get_text_field(data, 'otitis', 'otitisText') 
    row.paralysis = get_text_field(data, 'paralysis', 'paralysisText') 
    row.parasites = get_text_field(data, 'parasites', 'parasitesText') 
    row.skin_healthy = get_text_field(data, 'skinHealthy', 'skinHealthyText') 
    row.skin_ulcers = get_text_field(data, 'skinUlcers', 'skinUlcersText') 
    row.skin_infected = get_text_field(data, 'skinInfected', 'skinInfectedText') 
    row.lice = get_text_field(data, 'lice', 'liceText') 
    row.postnatal_visit = get_field(data, 'postnatalVisit')
    row.prenatal_visit = get_field(data, 'prenatalVisit')
    row.eye_prob = get_text_field(data, 'eyeProb', 'eyeProbText') 
    row.emotional_prob = get_text_field(data, 'emotionalProb', 'emotionalProbText') 
    row.gynecological_prob = get_text_field(data, 'gynecologicalProb', 'gynecologicalProbText') 
    row.parkinsons = get_text_field(data, 'parkinsons', 'parkinsonsText') 
    row.epilepsy = get_text_field(data, 'epilepsy', 'epilepsyText') 
    row.neurological_prob = get_text_field(data, 'neurologicalProb', 'neurologicalProbText') 
    row.therapist_referred = get_text_field(data, 'therapistReferred', 'therapistReferredText') 
    row.developmentally_delayed = get_text_field(data, 'developmentallyDelayed', 'developmentallyDelayedText') 
    row.vitamins = get_text_field(data, 'vitamins', 'vitaminsText') 
    row.last_menstruation = get_text_field(data, 'lastMenstruation', 'lastMenstruationText') 
    row.hiv = get_text_field(data, 'hiv', 'hivText') 
    row.vomiting = get_text_field(data, 'vomiting', 'vomitingText') 
    row.other_mp = data.get('other')

def write_psych_pathologies_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_pp = data.get('doctor')
    row.anxiety = get_text_field(data, 'anxiety', 'anxietyText')
    row.nuclear_family = get_text_field(data, 'nuclearFamily', 'nuclearFamilyText')
    row.self_esteem = get_text_field(data, 'selfEsteem', 'selfEsteemText')
    row.self_injury = get_text_field(data, 'selfInjury', 'selfInjuryText')
    row.attention_deficit = get_text_field(data, 'attentionDeficit', 'attentionDeficitText')
    row.depression = get_text_field(data, 'depression', 'depressionText')
    row.grief = get_text_field(data, 'grief', 'griefText')
    row.stress = get_text_field(data, 'stress', 'stressText')
    row.disfunctional_family = get_text_field(data, 'disfunctionalFamily', 'disfunctionalFamilyText')
    row.hyperactivity = get_text_field(data, 'hyperactivity', 'hyperactivityText')
    row.suicidal = get_text_field(data, 'suicidal', 'suicidalText')
    row.inappropriate_play = get_text_field(data, 'inappropriatePlay', 'inappropriatePlayText')
    row.language_problems = get_text_field(data, 'languageProblems', 'languageProblemsText')
    row.behavioral_problems = get_text_field(data, 'behavioralProblems', 'behavioralProblemsText')
    row.school_problems = get_text_field(data, 'schoolProblems', 'schoolProblemsText')
    row.psychosis = get_text_field(data, 'psychosis', 'psychosisText')
    row.personality_disorders = get_text_field(data, 'personalityDisorders', 'personalityDisordersText')
    row.trauma_pp = get_text_field(data, 'trauma', 'traumaText')
    row.psychological_evaluations = get_text_field(data, 'psychologicalEvaluations', 'psychologicalEvaluationsText')
    row.domestic_violence_family = get_text_field(data, 'domesticViolenceFamily', 'domesticViolenceFamilyText')
    row.domestic_violence_spouse = get_text_field(data, 'domesticViolenceSpouse', 'domesticViolenceSpouseText')
    row.referral_hospital = get_text_field(data, 'referralHospital', 'referralHospitalText')
    row.other_pp = get_text_field(data, 'other', 'otherText')

def write_household_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_he = data.get('doctor')
    row.potable_water = get_field(data, 'potableWater')
    row.animals = data.get('animals')
    row.gas_cooking = get_field(data, 'gasCooking')
    row.wood_cooking = get_field(data, 'woodCooking')
    row.household_size = data.get('householdSize')
    row.toilet = get_field(data, 'toilet')
    row.latrine = get_field(data, 'latrine')
    row.family_violence = get_text_field(data, 'familyViolence', 'familyViolenceText')

def write_lab_orders_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_lo = data.get('doctor')
    row.hematic_biometry = get_field(data, 'hematicBiometry')
    row.urinalysis = get_field(data, 'urinalysis')
    row.peripherical_exam = get_field(data, 'periphericalExam')
    row.biochemistry = get_field(data, 'biochemistry')
    row.lipid_profile = get_field(data, 'lipidProfile')
    row.pregnancy_test = get_field(data, 'pregnancyTest')
    row.immunology_test = get_field(data, 'immunologyTest')
    row.PAP_test = get_field(data, 'PAPTest')
    row.serology_test = get_field(data, 'serologyTest')
    row.stool_test = get_field(data, 'stoolTest')
    row.fecal_antigens = get_field(data, 'fecalAntigens')
    row.blood_type_lo = get_field(data, 'bloodType')
    row.HIV_test = get_field(data, 'HIVTest')
    row.other_lo = data.get('other')

def write_lab_tests_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_lt = data.get('doctor')
    row.CBCWBC = data.get('CBCWBC')
    row.CBCRBC = data.get('CBCRBC')
    row.CBC_hemoglobin = data.get('CBCHemoglobin')
    row.CBC_hematocrit = data.get('CBCHematocrit')
    row.CBC_platelets = data.get('CBCPlatelets')
    row.CBCMCV = data.get('CBCMCV')
    row.CBCMCH = data.get('CBCMCH')
#  row.CBC_Immature = data.get('CBCImmature')
    row.CBCMCHC = data.get('CBCMCHC')
    row.CBC_segmented = data.get('CBCSegmented')
    row.CBC_eosinophils = data.get('CBCEosinophils')
    row.CBC_basophils = data.get('CBCBasophils')
    row.CBC_monocytes = data.get('CBCMonocytes')
    row.CBC_lymphocytes = data.get('CBCLymphocytes')
 #   row.CBC_platelet_count = data.get('CBCPlateletCount')
    row.biochem_uric = data.get('biochemUric')
    row.biochem_creatinine = data.get('biochemCreatinine')
    row.biochem_glucose = data.get('biochemGlucose')

    row.lipid_cholesterol = data.get('lipidCholesterol')
    row.lipid_triglycerides = data.get('lipidTriglycerides')
    row.lipid_HDL = data.get('lipidHDL')
    row.lipid_VLDL = data.get('lipidVLDL')
    row.lipid_LDL = data.get('lipidLDL')

    row.fecal_color = data.get('fecalColor')
    row.fecal_consistency = data.get('fecalConsistency')
    row.fecal_observations = data.get('fecalObservations')
    row.fecal_PH = data.get('fecalPH')
    row.fecal_reducers = data.get('fecalReducers')
    row.fecal_occult = data.get('fecalOccult')
    row.fecal_cysts = data.get('fecalCysts')
    row.fecal_trophozoites = data.get('fecalTrophozoites')
    row.fecal_others = data.get('fecalOthers')
    row.fecal_leukocytes = data.get('fecalLeukocytes')
    row.fecal_erythrocytes = data.get('fecalErythrocytes')
    row.fecal_bacteria = data.get('fecalBacteria')
    row.fecal_polymophonuclear = data.get('fecalPolymophonuclear')
    row.fecal_mononuclear = data.get('fecalMononuclear')

    row.pregnancy_hemogravindex = get_text_field_positive(data, 'pregnancyHemogravindex', 'pregnancyHemogravindexText')
    row.pregnancy_gravindex = get_text_field_positive(data, 'pregnancyGravindex', 'pregnancyGravindexText')
    row.fecal_antigens = get_text_field_positive(data, 'fecalAntigens', 'fecalAntigensText')
    row.microbiology_pilori = get_text_field_positive(data, 'microbiologyPilori', 'microbiologyPiloriText')
    row.microbiology_malaria = get_text_field_positive(data, 'microbiologyMalaria', 'microbiologyMalariaText')
    row.serology_strep = get_text_field_positive(data, 'serologyStrep', 'serologyStrepText')
    row.serology_rheumatoid = get_text_field_positive(data, 'serologyRheumatoid', 'serologyRheumatoidText')
    row.serology_others = get_text_field_positive(data, 'serologyOthers', 'serologyOthersText')
    row.serology_protein = get_text_field_positive(data, 'serologyProtein', 'serologyProteinText')
    row.serology_VDRL = get_text_field_positive(data, 'serologyVDRL', 'serologyVDRLText')
    row.serology_VIH = get_text_field_positive(data, 'serologyVIH', 'serologyVIHText')
    row.serology_VSG = data.get('serologyVSG')
    row.blood_type_lt = data.get('bloodType')
    row.RH_factor = get_text_field_positive(data, 'RHFactor', 'RHFactorText')

def write_urine_tests_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_lu = data.get('doctor') 
    row.color_physical = data.get('colorPhysical') 
    row.aspects_physical = data.get('aspectsPhysical') 
    row.sediment_physical = data.get('sedimentPhysical') 
    row.density_physical = data.get('densityPhysical') 
    row.proteins_chem = get_text_field_positive(data, 'proteinsChem', 'proteinsChemDate') 
    row.hemoglobin_chem = get_text_field_positive(data, 'hemoglobinChem', 'hemoglobinChemDate') 
    row.ketonic_chem = get_text_field_positive(data, 'ketonicChem', 'ketonicChemDate') 
    row.pH_chem = data.get('pHChem')
    row.urobilinogen_chem = get_text_field_positive(data, 'urobilinogenChem', 'urobilinogenChemDate') 
    row.glucose_chem = get_text_field_positive(data, 'glucoseChem', 'glucoseChemDate') 
    row.bilirubins_chem = get_text_field_positive(data, 'bilirubinsChem', 'bilirubinsChemDate') 
    row.leukocytes_chem = get_text_field_positive(data, 'leukocytesChem', 'leukocytesChemDate') 
    row.nitrite_chem = get_text_field_positive(data, 'nitriteChem', 'nitriteChemDate') 
    row.epithelial_micro = data.get('epithelialMicro') 
    row.leukocytes_micro = data.get('leukocytesMicro') 
    row.erythrocytes_micro = data.get('erythrocytesMicro') 
    row.cylinders_micro = data.get('cylindersMicro') 
    row.crystals_micro = data.get('crystalsMicro') 
    row.bacteria_micro = data.get('bacteriaMicro') 
    row.yeasts_micro = data.get('yeastsMicro') 
    row.cRenal_micro = data.get('cRenalMicro') 
    row.h_mucous_micro = data.get('hMucousMicro') 
    row.observations_micro = data.get('observationsMicro')

def write_pap_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_pap = data.get('doctor')
    row.adequate_cyto = get_text_field(data, 'adequateCyto', 'adequateCytoText')
    row.incomplete_cyto = get_text_field(data, 'incompleteCyto', 'incompleteCytoText')
    row.cellularity_cyto = get_text_field(data, 'cellularityCyto', 'cellularityCytoText')
    row.fixation_cyto = get_text_field(data, 'fixationCyto', 'fixationCytoText')
    row.hemorrhage_cyto = get_text_field(data, 'hemorrhageCyto', 'hemorrhageCytoText')
    row.exudate_cyto = get_text_field(data, 'exudateCyto', 'exudateCytoText')
    row.endocervical_cyto = get_text_field(data, 'endocervicalCyto', 'endocervicalCytoText')
    row.inadequate_cyto = get_text_field(data, 'inadequateCyto', 'inadequateCytoText')
    row.bleeding_cyto = get_text_field(data, 'bleedingCyto', 'bleedingCytoText')
    row.fixation_inadequate_cyto = get_text_field(data, 'fixationInadequateCyto', 'fixationInadequateCytoText')
    row.squamous = get_text_field(data, 'squamous', 'squamousText')
    row.US_squamous = get_text_field(data, 'USSquamous', 'USSquamousText')
    row.H_squamous = get_text_field(data, 'HSquamous', 'HSquamousText')
    row.lgsil = get_text_field(data, 'lgsil', 'lgsilText')
    row.cellular_lgsil = get_text_field(data, 'cellularLgsil', 'cellularLgsilText')
    row.dysplasia_lgsil = get_text_field(data, 'dysplasiaLgsil', 'dysplasiaLgsilText')
    row.hgsil = get_text_field(data, 'hgsil', 'hgsilText')
    row.cin_hgsil = get_text_field(data, 'cinHgsil', 'cinHgsilText')
    row.dysplasia_hgsil = get_text_field(data, 'dysplasiaHgsil', 'dysplasiaHgsilText')
    row.carcinoma_hgsil = get_text_field(data, 'carcinomaHgsil', 'carcinomaHgsilText')
    row.neg_intraepithelial = get_text_field(data, 'negIntraepithelial', 'negIntraepithelialText')
    row.ais_carcinoma = get_text_field(data, 'aisCarcinoma', 'aisCarcinomaText')
    row.invasive_carcinoma = get_text_field(data, 'invasiveCarcinoma', 'invasiveCarcinomaText')
    row.agc_carcinoma = get_text_field(data, 'agcCarcinoma', 'agcCarcinomaText')
    row.endocervical_carcinoma = get_text_field(data, 'endocervicalCarcinoma', 'endocervicalCarcinomaText')
    row.endometrial_carcinoma = get_text_field(data, 'endometrialCarcinoma', 'endometrialCarcinomaText')
    row.neoplasia_carcinoma = get_text_field(data, 'neoplasiaCarcinoma', 'neoplasiaCarcinomaText')
    row.nos_carcinoma = get_text_field(data, 'nosCarcinoma', 'nosCarcinomaText')
    row.iscc = get_text_field(data, 'iscc', 'isccText')
    row.atrophy = get_text_field(data, 'atrophy', 'atrophyText')
    row.coccoid = get_text_field(data, 'coccoid', 'coccoidText')
    row.regenerative = get_text_field(data, 'regenerative', 'regenerativeText')
    row.candida = get_text_field(data, 'candida', 'candidaText')
    row.bv = get_text_field(data, 'bv', 'bvText')
    row.herpes = get_text_field(data, 'herpes', 'herpesText')
    row.inflammation = get_text_field(data, 'inflammation', 'inflammationText')
    row.trichomonas = get_text_field(data, 'trichomonas', 'trichomonasText')
    row.other_pap = data.get('other')

def write_ultrasound_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_u = data.get('doctor')
    row.abdominal = get_field(data, 'abdominal')
    row.joints = get_field(data, 'joints')
    row.neck = get_field(data, 'neck')
    row.doppler = get_field(data, 'doppler')
    row.breast = get_field(data, 'breast')
    row.first_OB = get_field(data, 'firstOB')
    row.second_OB = get_field(data, 'secondOB')
    row.third_OB = get_field(data, 'thirdOB')
    row.soft_tissues = get_field(data, 'softTissues')
    row.pelvic = get_field(data, 'pelvic')
    row.prostate = get_field(data, 'prostate')
    row.renal = get_field(data, 'renal')
    row.testicular = get_field(data, 'testicular')
    row.other_u = get_field(data, 'other')
    row.goiter = data.get('goiter')
    row.wrapped_cord = data.get('wrappedCord')
    row.cholelithiasis = data.get('cholelithiasis')
    row.prostate1 = data.get('prostate1')
    row.prostate2 = data.get('prostate2')
    row.prostate3 = data.get('prostate3')
    row.prostate4 = data.get('prostate4')
    row.endometrial_thickening = data.get('endometrialThickening')
    row.splenomegaly = data.get('splenomegaly')
    row.mild_hepatic = data.get('mildHepatic')
    row.moderate_hepatic = data.get('moderateHepatic')
    row.severe_hepatic = data.get('severeHepatic')
    row.hepatomegaly = data.get('hepatomegaly')
    row.cirrhosis = data.get('cirrhosis')
    row.venous_insufficiency = data.get('venousInsufficiency')
    row.mild_renal = data.get('mildRenal')
    row.moderate_renal = data.get('moderateRenal')
    row.severe_renal = data.get('severeRenal')
    row.nephrolithiasis = data.get('nephrolithiasis')
    row.complex_masses = data.get('complexMasses')
    row.benign_nodules = data.get('benignNodules')
    row.malignant_nodules = data.get('malignantNodules')
    row.thyroid_nodules = data.get('thyroidNodules')
    row.thyroiditis = data.get('thyroiditis')
    row.normal_ultrasound = data.get('normalUltrasound')
    row.polycystic_ovaries = data.get('polycysticOvaries')
    row.simple_ovarian_cysts = data.get('simpleOvarianCysts')
    row.other_result = data.get('otherResult')

def write_family_planning_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_fp = data.get('doctor') 
    row.age_sexual_relations = data.get('ageSexualRelations') 
    row.number_children = data.get('numberChildren') 
    row.more_children = get_field(data, 'moreChildren') 
    row.abnormal_bleeding = get_field(data, 'abnormalBleeding') 
    row.varicose = get_field(data, 'varicose') 
    row.tubal_sterilization = get_text_field(data, 'tubalSterilization', 'tubalSterilizationDate') 
    row.vasectomy_sterilization = get_text_field(data, 'vasectomySterilization', 'vasectomySterilizationDate') 
    row.std_type = get_text_field(data, 'stdType', 'stdTypeText') 
    row.injection = get_text_field(data, 'injection', 'injectionDate') 
    row.injection_repeat = get_text_field(data, 'injectionRepeat', 'injectionRepeatDate') 
    row.iud_BC = get_text_field(data, 'iudBC', 'iudBCType') 
    row.iud_BC_repeat = get_text_field(data, 'iudBCRepeat', 'iudBCRepeatType')
    row.implant_BC = get_text_field(data, 'implantBC', 'implantBCDate') 
    row.implant_BC_repeat = get_text_field(data, 'implantBCRepeat', 'implantBCRepeatDate') 
    row.monthly_BC = get_text_field(data, 'monthlyBC', 'monthlyBCDate') 
    row.monthly_BC_repeat = get_text_field(data, 'monthlyBCRepeat', 'monthlyBCRepeatDate') 
    row.pills_BC = get_text_field(data, 'pillsBC', 'pillsBCDate') 
    row.pills_BC_repeat = get_text_field(data, 'pillsBCRepeat', 'pillsBCRepeatDate') 
    row.condoms = get_field(data, 'condoms')
    row.condoms_repeat = get_field(data, 'condomsRepeat')
    row.sex_orientation = data.get('sexOrientation')
    row.married = get_text_field(data, 'married', 'marriedText') 
    row.permanent_partner = get_text_field(data, 'permanentPartner', 'permanentPartnerText') 

def write_dental_origin_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_do = data.get('doctor')
    row.feeding_center = get_feeding_center(data)
    row.other_feeding_center = data.get('otherFeedingCenter')

def write_dental_treatment_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_dt = data.get('doctor')
    row.toothbrush = get_text_field(data, 'toothbrush', 'toothbrushText')
    row.consult = get_text_field(data, 'consult', 'consultText')
    row.extraction = get_text_field(data, 'extraction', 'extractionText')
    row.fluoride = get_text_field(data, 'fluoride', 'fluorideText')
    row.floss = get_text_field(data, 'floss', 'flossText')
    row.cleaning_first = get_text_field(data, 'cleaningFirst', 'cleaningFirstText')
    row.cleaning_firstYear = get_text_field(data, 'cleaningFirstYear', 'cleaningFirstYearText')
    row.cleaning_second = get_text_field(data, 'cleaningSecond', 'cleaningSecondText')
    row.toothpaste = get_text_field(data, 'toothpaste', 'toothpasteText')
    row.xray = get_text_field(data, 'xray', 'xrayText')
    row.amalgama_restoration = get_text_field(data, 'amalgamaRestoration', 'amalgamaRestorationText')
    row.metal_restoration = get_text_field(data, 'metalRestoration', 'metalRestorationText')
    row.ionomero_restoration = get_text_field(data, 'ionomeroRestoration', 'ionomeroRestorationText')
    row.mri_restoration = get_text_field(data, 'mriRestoration', 'mriRestorationText')
    row.space_restoration = get_text_field(data, 'spaceRestoration', 'spaceRestorationText')
    row.resin_restoration = get_text_field(data, 'resinRestoration', 'resinRestorationText')
    row.zoe_restoration = get_text_field(data, 'zoeRestoration', 'zoeRestorationText')
    row.acetate_restoration = get_text_field(data, 'acetateRestoration', 'acetateRestorationText')
    row.pulpotomy_restoration = get_text_field(data, 'pulpotomyRestoration', 'pulpotomyRestorationText')
    row.sd_fluoride = get_text_field(data, 'sdFluoride', 'sdFluorideText')
    row.sealant = get_text_field(data, 'sealant', 'sealantText')
    row.teaching = get_text_field(data, 'teaching', 'teachingText')
    row.impression = get_text_field(data, 'impression', 'impressionText')
    row.other_dt = get_text_field(data, 'other', 'otherText')

def write_program_trainings_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_pt = data.get('doctor')
    row.asthma_subject = get_text_field(data, 'asthmaSubject', 'asthmaSubjectText')
    row.pregnancy_subject = get_text_field(data, 'pregnancySubject', 'pregnancySubjectText')
    row.dispensarizados1_subject = get_text_field(data, 'dispensarizados1Subject', 'dispensarizados1SubjectText')
    row.dispensarizados2_subject = get_text_field(data, 'dispensarizados2Subject', 'dispensarizados2SubjectText')
    row.dispensarizados3_subject = get_text_field(data, 'dispensarizados3Subject', 'dispensarizados3SubjectText')
    row.dispensarizados4_subject = get_text_field(data, 'dispensarizados4Subject', 'dispensarizados4SubjectText')
    row.breastfeeding_subject = get_text_field(data, 'breastfeedingSubject', 'breastfeedingSubjectText')
    row.girls_group_subject = get_text_field(data, 'girlsGroupSubject', 'girlsGroupSubjectText')
    row.lbgtq_subject = get_text_field(data, 'lbgtqSubject', 'lbgtqSubjectText')
    row.boys_older_subject = get_text_field(data, 'boysOlderSubject', 'boysOlderSubjectText')
    row.boys_younger_subject = get_text_field(data, 'boysYoungerSubject', 'boysYoungerSubjectText')
    row.new_mothers_subject = get_text_field(data, 'newMothersSubject', 'newMothersSubjectText')
    row.family_planning_subject = get_text_field(data, 'familyPlanningSubject', 'familyPlanningSubjectText')
    row.toddler_mothers_subject = get_text_field(data, 'toddlerMothersSubject', 'toddlerMothersSubjectText')
    row.health_promoters_subject = get_text_field(data, 'healthPromotersSubject', 'healthPromotersSubjectText')
    row.hiv_subject = get_text_field(data, 'hivSubject', 'hivSubjectText')
    row.other_subject = get_text_field(data, 'otherSubject', 'otherSubjectText')

def write_xray_orders_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_xo = data.get('doctor')
    row.hip_antero = get_field(data, 'hipAntero')
    row.hip_lateral = get_field(data, 'hipLateral')
    row.hip_posterior = get_field(data, 'hipPosterior')
    row.retrograde_cystogram = get_field(data, 'retrogradeCystogram')
    row.cranial_antero = get_field(data, 'cranialAntero')
    row.cranial_lateral = get_field(data, 'cranialLateral')
    row.cranial_posterior = get_field(data, 'cranialPosterior')
    row.femur_antero = get_field(data, 'femurAntero')
    row.femur_lateral = get_field(data, 'femurLateral')
    row.femur_posterior = get_field(data, 'femurPosterior')
    row.foot_antero = get_field(data, 'footAntero')
    row.standing_lateral = get_field(data, 'standingLateral')
    row.standing_oblique = get_field(data, 'standingOblique')
    row.foot_posterior = get_field(data, 'footPosterior')
    row.iv_pyelogram = get_field(data, 'ivPyelogram')
    row.knee_antero = get_field(data, 'kneeAntero')
    row.knee_lateral = get_field(data, 'kneeLateral')
    row.knee_posterior = get_field(data, 'kneePosterior')
    row.tibia_antero = get_field(data, 'tibiaAntero')
    row.tibia_lateral = get_field(data, 'tibiaLateral')
    row.tibia_posterior = get_field(data, 'tibiaPosterior')
    row.ankle_antero = get_field(data, 'ankleAntero')
    row.ankle_lateral = get_field(data, 'ankleLateral')
    row.ankle_posterior = get_field(data, 'anklePosterior')
    row.chest_antero = get_field(data, 'chestAntero')
    row.chest_lateral = get_field(data, 'chestLateral')
    row.chest_posterior = get_field(data, 'chestPosterior')

def write_xray_results_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_xr = data.get('doctor')
    row.arthritis = get_text_field(data, 'arthritis', 'arthritisText')
    row.cardiomegaly = get_text_field(data, 'cardiomegaly', 'cardiomegalyText')
    row.ureteral_duplication = get_text_field(data, 'ureteralDuplication', 'ureteralDuplicationText')
    row.lung_disease = get_text_field(data, 'lungDisease', 'lungDiseaseText')
    row.fibrosis = get_text_field(data, 'fibrosis', 'fibrosisText')
    row.fractures = get_text_field(data, 'fractures', 'fracturesText')
    row.pneumonia = get_text_field(data, 'pneumonia', 'pneumoniaText')
    row.pulmonary_nodule = get_text_field(data, 'pulmonaryNodule', 'pulmonaryNoduleText')
    row.osteoarthritis_xray = get_text_field(data, 'osteoarthritis', 'osteoarthritisText')
    row.osteoporosis = get_text_field(data, 'osteoporosis', 'osteoporosisText')
    row.ectopic_kidney = get_text_field(data, 'ectopicKidney', 'ectopicKidneyText')
    row.rinon_herradura = get_text_field(data, 'rinonHerradura', 'rinonHerraduraText')
    row.tumor = get_text_field(data, 'tumor', 'tumorText')

def write_optometry_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_o = data.get('doctor')
    row.cataract = get_text_field(data, 'cataract', 'cataractText')
    row.cataract_operation = get_text_field(data, 'cataractOperation', 'cataractOperationDate')
    row.glasses = data.get('glasses')
    row.glasses_duration = data.get('glassesDuration')
    row.orange_reflection = get_field(data, 'orangeReflection')
    row.visualAcuity_OD = data.get('visualAcuityOD')
    row.visualAcuity_OS = data.get('visualAcuityOS')
    row.autorefractor_OD = data.get('autorefractorOD')
    row.autorefractor_OS = data.get('autorefractorOS')
    row.phoropter_OD = data.get('phoropterOD')
    row.phoropter_OS = data.get('phoropterOS')
    row.phoropterADD = data.get('phoropterADD')
    row.lenses_OD = data.get('lensesOD')
    row.lenses_OS = data.get('lensesOS')
    row.lenses_ADD = data.get('lensesADD')
    row.visual_acuity_lenses_OD = data.get('visualAcuityLensesOD')
    row.visual_acuity_lenses_OS = data.get('visualAcuityLensesOS')

def write_accident_report_event(row:PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_ar = data.get('doctor')
    row.accident_work = get_text_field(data, 'accidentWork', 'accidentWorkText')
    row.description = data.get('description')
    row.trauma = get_text_field(data, 'trauma', 'traumaText')
    row.trauma_details = data.get('traumaDetails')
    row.referral_specialist = get_text_field(data, 'referralSpecialist', 'referralSpecialistText')
    row.follow_up_visit = get_text_field(data, 'followUpVisit', 'followUpVisitText')
    row.other_ar = data.get('other')

def write_nursing_care_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.doctor_nc = data.get('doctor')
    row.wound_care = get_text_field(data, 'woundCare', 'woundCareDate')
    row.iv = get_text_field(data, 'IV', 'IVDate')
    row.injections = get_text_field(data, 'injections', 'injectionsDate')
    row.nebulization = get_text_field(data, 'nebulization', 'nebulizationDate')