import uproot
import awkward as ak
import numpy as np
import vector
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# 1. DATA LOADING
# ----------------------------------------------------------------------

def load_dataset(
    path="ODEO_FEB2025_v0_2J2LMET30_data16_periodD.2J2LMET30.root",
    treename="analysis;1"
):
    """Load the fixed dataset."""
    print(f"Loading dataset: {path}")
    file = uproot.open(path)
    tree = file[treename]
    return tree.arrays(library="ak")


# ----------------------------------------------------------------------
# 2. PHYSICS OBJECT BUILDERS
# ----------------------------------------------------------------------

def build_electrons(events):
  

    # Compute energy since "lep_e" is not in file
    

    lep = ak.zip(
        {
            "pt": events["lep_pt"],
            "eta": events["lep_eta"],
            "phi": events["lep_phi"],
            "mass": events["lep_mass"] if "lep_mass" in events.fields else 0 * events["lep_pt"],
            "energy": events["lep_e"] if "lep_e" in events.fields 
            else np.sqrt(events["lep_pt"]**2 * np.cosh(events["lep_eta"])**2),
            "charge": events["lep_charge"],
            "type": events["lep_type"],
            "isTightID": events["lep_isTightID"],
            "isTightIso": events["lep_isTightIso"],
        },
        with_name="Momentum4D"
    )

    return lep[lep["type"] == 11]  # electrons only
def build_muons(events):
    
    lep = ak.zip(
        {
            "pt": events["lep_pt"],
            "eta": events["lep_eta"],
            "phi": events["lep_phi"],
            "mass": events["lep_mass"] if "lep_mass" in events.fields else 0 * events["lep_pt"],
            "energy": events["lep_e"] if "lep_e" in events.fields 
            else np.sqrt(events["lep_pt"]**2 * np.cosh(events["lep_eta"])**2),
            "charge": events["lep_charge"],
            "type": events["lep_type"],
            "isTightID": events["lep_isTightID"],
            "isTightIso": events["lep_isTightIso"],
        },
        with_name="Momentum4D"
    )


    return lep[lep["type"] == 13]  # Select muons only


def build_jets(events):
    jets = ak.zip({ "pt": events["jet_pt"], 
                   "eta": events["jet_eta"], 
                   "phi": events["jet_phi"], 
                   "energy": events["jet_e"],
                   "btag": events["jet_btag_quantile"], 
                   "jvt": events["jet_jvt"]}, 
                   with_name="Momentum4D")
    return jets


def build_met(events):
    """Return px, py, ET."""
    return events.met_mpx, events.met_mpy, events.met


# ----------------------------------------------------------------------
# 3. SELECTIONS
# ----------------------------------------------------------------------

def select_two_opposite_sign_same_flavour(leps):
    mask_two = (ak.num(leps) == 2)
    leps2 = leps[mask_two]
    mask_os = leps2.charge[:,0] * leps2.charge[:,1] < 0
    

    return leps2[mask_os]


def select_z_mass_window(z_mass, low=81, high=101):
    return (z_mass > low) & (z_mass < high)


def select_one_lepton(leps):
    return ak.num(leps) == 1


# ----------------------------------------------------------------------
# 4. RECONSTRUCTION
# ----------------------------------------------------------------------

def z_mass_numpy(leps):
    # Convert to numpy
    l0 = ak.to_numpy(leps[:,0])
    l1 = ak.to_numpy(leps[:,1])

    # compute px, py, pz, E in numpy
    pxZ = l0["pt"]*np.cos(l0["phi"]) + l1["pt"]*np.cos(l1["phi"])
    pyZ = l0["pt"]*np.sin(l0["phi"]) + l1["pt"]*np.sin(l1["phi"])
    pzZ = l0["pt"]*np.sinh(l0["eta"]) + l1["pt"]*np.sinh(l1["eta"])
    EZ  = l0["energy"] + l1["energy"]

    return np.sqrt(EZ**2 - pxZ**2 - pyZ**2 - pzZ**2)
   


def transverse_mass(lep, met_px, met_py):
    """Compute W transverse mass."""
    dphi = lep.phi - np.arctan2(met_py, met_px)
    met = np.hypot(met_px, met_py)
    return np.sqrt(2 * lep.pt * met * (1 - np.cos(dphi)))


# ----------------------------------------------------------------------
# 5. PLOTTING
# ----------------------------------------------------------------------

def plot_hist(values, bins, xlabel, ylabel="Events", title=None):
    plt.figure(figsize=(7, 5))
    plt.hist(values, bins=bins)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    plt.grid(True)
    plt.xlim(0, 400)
    plt.tight_layout()
    plt.show()
