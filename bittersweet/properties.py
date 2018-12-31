from pychem.pychem import Chem, constitution, connectivity, kappa, bcut,\
    moran, geary, molproperty, charge, moe, estate, basak


def generate_chemopy_props(mol):
    """ Generated properties from an RDKit Mol Object """

    props = dict()

    try:
        props.update(constitution.GetConstitutional(mol))
        props.update(connectivity.GetConnectivity(mol))
        props.update(kappa.GetKappa(mol))
        props.update(bcut.GetBurden(mol))
        props.update(estate.GetEstate(mol))
        props.update(basak.Getbasak(mol))
        props.update(moran.GetMoranAuto(mol))
        props.update(geary.GetGearyAuto(mol))
        props.update(molproperty.GetMolecularProperty(mol))
        props.update(charge.GetCharge(mol))
        props.update(moe.GetMOE(mol))
    except:
        raise Exception("Properties could not be generated.")

    return props


def generate_chemopy_props_from_smiles(smiles):
    """ Generated properties from an RDKit Mol Object """

    try:
        mol = Chem.MolFromSmiles(smiles)
    except:
        raise Exception("Please check if the SMILES is formatted correctly.")

    return generate_chemopy_props(mol)
    

def get_chemopy_props_from_smilesfile(f):
    """ Generates properties from a SMILES file. The expected formatting for the 
    SMILES file is as follows (without headers):

    'name_1','CCCCC'
    'name_2','Ar'
    """


    smilesf = data = pd.read_csv(f, sep=',', encoding='utf-8', header=None)
    
    properties = list()
    try:
        for i, row in smilesf.iterrows():
            mol = Chem.MolFromSmiles(row[0])
            name = str(row[1])

            props = {'name': name}
            try:
                props.update(generate_chemopy_props(mol))
            except:
                logging.error("Properties could not be generated for: " + name)

            properties.append(props)
    except KeyError:
        raise Exception(
            "Please ensure that the input data is in the correct format. See docs for more info.")

    return properties


def generate_properties(f, dtype):
    if dtype == 'smiles':
        return generate_chemopy_props_from_smiles(f)
    elif dtype == 'smiles-file':
        return get_chemopy_props_from_smilesfile(f)
    else:
        raise Exception("Please enter a valid option for dtype.")

