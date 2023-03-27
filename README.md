# AllTheAminoAcids
ChimeraX module to support addition of any amino acid from ligand expo into a protein model for rapid Post Translational Model Development

_Important Note_ - it is not fully working as it doen't swap the amino acid into the protein just yet. The Chimera python module has a method for swappingAA hidden from the docs, and it also instantiates internal parameters for chimera. The most ideal scenario is hooking through that function for the most seamless integration. 

## IMPORTANT NOTE ## 

This package requires some additional dependencies not installed automatically
  - BeautifulSoup4
  - rdkit-pypi
 
The hack for installing these involves launching the embedded ChimeraX python interpreter from outside the running application. I will work on a script to auto-magically pull these in without the headache.
