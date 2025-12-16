ATLAS-Style Lepton, MET, and Jet Analysis (Python/Awkward)

This repository contains a lightweight analysis framework for performing
standard LHC-style physics selections using Awkward Arrays, vector, and
ROOT-converted datasets. The analysis demonstrates reconstruction of:

-   Z → ll (invariant mass)
-   W → lν (transverse mass)
-   Jet kinematics (e.g., leading jet pT)

Directory Structure:
├── analysis_run.py # Main script to run analysis
├── analysis_utils.py # Physics object builders and selection helpers
├── README.txt # This file 
└── data/ # Place your ROOT files here

Requirements: pip install awkward uproot vector matplotlib numpy

Input Dataset: The analysis expects a ROOT file containing lepton, jet,
and MET branches such as: lep_pt, lep_eta, lep_phi, lep_charge,
lep_type, jet_pt, jet_eta, jet_phi, met_px, met_py, met_et

Running the Analysis: python analysis_run.py

Selections and Reconstruction: 
- Z → ll: exactly two same-flavour,
opposite-sign leptons;
- W → lν: exactly one lepton, MT computed using
standard formula; 
- Jet analysis: leading jet pT;

Key Functions: 
- build_electrons; 
- build_muons;
- build_jets;
- build_met;
- select_two_opposite_sign_same_flavour; 
- select_one_lepton; 
- z_mass_numpy;
- transverse_mass; 
- plot_hist.

Output: Histograms for Z invariant mass, W transverse mass, and leading jet pT.

Customization: Modify lepton ID, jet cuts, MET thresholds, or event
masks in analysis_utils.py.


