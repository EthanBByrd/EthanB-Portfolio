# Clearwater Risk Management Project

This project was completed using Clearwater’s CC|IRM platform to simulate a real-world, enterprise-level risk management process. The objective was to assess information security risks for a case organization by identifying assets, evaluating vulnerabilities, determining risks, and planning appropriate responses.

This README provides a full walkthrough of the steps followed to complete the Clearwater RM project, including asset inventory import, risk assessment, and mitigation strategy development.

---

## Table of Contents

1. Project Overview  
2. Asset Inventory  
3. Component Groups  
4. Risk Threshold  
5. Risk Determination  
6. Risk Response  
7. Generating Deliverables  
8. Final Submission Checklist  

---

## 1. Project Overview

The project was completed over several phases, mimicking the real-world processes used by information security professionals:

- Importing and evaluating organizational assets
- Assigning assets to component groups
- Setting a risk threshold for acceptable risk levels
- Completing five detailed risk determination questionnaires
- Responding to identified risks with mitigation strategies
- Generating and formatting required documentation

The project was executed using the Clearwater CC|IRM cloud-based platform.

---

## 2. Asset Inventory

### Importing Assets

1. Navigate to Assets > Asset Inventory Import.
2. Download the asset inventory spreadsheet template.
3. Fill in the spreadsheet using data from the case organization, including:

- Asset Name and Description
- Type(s) of Sensitive Data (e.g., PII, ePHI, PCI, FERPA)
- Component Types (based on how assets are accessed, processed, or stored)
- Importance, RTO, and RPO
- Percentage of Employees Using Asset and Percentage of Sensitive Records
- Source and Destination of Data
- Asset Business Owner

Estimates were made where exact numbers were not available. Importance, RTO, and RPO were assigned based on project guidance.

4. Save the spreadsheet without changing the file name.
5. Upload the spreadsheet using the “Import Assets Now” button.
6. Go to the Asset Inventory List to verify data import.
7. Set all assets to “Enabled” using the Asset Status menu.

---

## 3. Component Groups

1. Go to Assets > Component Groups.
2. Rename all “No Group Name” entries with clear labels (e.g., “Workstation Group,” “Server Group”).
3. Answer all required group detail questions, using estimates where needed.
4. Ensure assets are correctly assigned to their respective groups. Use the “+” icon to verify asset association.
5. If any assets are missing, revisit the Component Type field in the asset setup and correct it.

---

## 4. Risk Threshold

1. Go to Framing/Governance > Risk Threshold.
2. Set the threshold value to 8 using the dropdown.
3. Confirm your selection.

This sets the organization's tolerance for risk. All risks scoring below this threshold will be considered acceptable.

---

## 5. Risk Determination

### Completing Risk Questionnaires

1. Go to Risk Determination > Risk Questionnaire List.
2. Select your assigned Component Group (based on the first letter of your last name).
3. Complete five Risk Questionnaire forms:
   - Select “In Progress” or “No” for each control listed.
   - Assign a Likelihood and Impact rating that results in a total score of 8 or higher.
   - For each, write a Risk Determination Note using the following format:  
     `RD: I selected the Risk Likelihood of [value] because [reason]. I selected the Risk Impact of [value] because [reason].`

Do not complete more than five questionnaires rated 8 or higher. Each should include a detailed and unique note.

### Verifying Risk Assessments

- Go to Risk Determination > Rating Review.
- Sort by Risk Rating.
- Confirm you have exactly five entries with scores of 8 or higher.
- Ensure each has a Risk Note entered (check for “1” in the note column).

---

## 6. Risk Response

### Developing Risk Mitigation Plans

1. Go to Risk Response > Risk Response List.
2. Filter for your assigned component group and sort by Risk Rating.
3. For each of the five rated risks:
   - Select “Mitigate” as the Risk Treatment Type.
   - Assign yourself as Risk Owner.
   - Choose “Add” or “Enhance” for each control.
   - Set Effectiveness and Feasibility ratings.
   - Enter Residual Likelihood and Impact values resulting in a score below 8.
   - Write a Risk Response Note using this format:  
     `RR: I chose Mitigate as the recommended risk treatment strategy because [reason]. I reduced the residual risk from [previous rating] to [new rating] because [reason].`

4. Close each expanded row to prevent freezing errors.

### Verifying Responses

- All five risks should have:
  - “Mitigate” selected
  - Residual risk score below 8
  - A complete RR note properly formatted

---

## 7. Generating Deliverables

Export and save the following three reports as PDFs. Use the naming convention: `COURSE_SEMESTER_NETID_reportname.pdf`

### 1. Asset Inventory Report

- Go to Reports > Enterprise Extracts > Asset Inventory.
- Clean up the Excel file:
  - Delete unused columns
  - Wrap text
  - Bold headers
  - Adjust column widths
- Export to PDF in landscape format.

### 2. Risk Rating Detail Report

- Go to Reports > Enterprise Extracts > Risk Rating Detail.
- Sort by Risk Rating (high to low).
- Apply the same formatting steps as above.
- Export to PDF in landscape format.

### 3. Risk Response List

- Go to Risk Response > Risk Response List.
- Set Component Filter to “Select All.”
- Click the printer icon and export the PDF.

---

This concludes the Clearwater Risk Management Project documentation.


