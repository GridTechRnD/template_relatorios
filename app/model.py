from pydantic import BaseModel


class Model(BaseModel):
    document_name: str
    date: str
    document_content: str
    ap_type: str
    device_id: str
    ami_id: str
    address: str
    municipality: str
    lat: str
    long: str
    antenna: str
    dbi_gain: str
    azimute: str
    tx: str
    rx: str
    dbm: str
    structure_type: str
    m_dan: str
    grounding: str
    grid_voltage: str
    power: str
    conductor_type: str
    device_installation_address: str
    antenna_installation_address: str
    info: str
    more_info: str
    images: list[str]
