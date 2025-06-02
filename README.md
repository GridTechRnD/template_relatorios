# Template PDF
The parameters of this model are used as input for a PDF generation process.
The model ensures that all required data is present and correctly formatted before the PDF is created.

## Fields

| Field Name                     | Type        | Description                                                                 |
|------------------------------- |------------ |-----------------------------------------------------------------------------|
| `enterprise_logo`              | `str`       | Base64-encoded string representing the enterprise logo image.                |
| `document_name`                | `str`       | Name of the document.                                                        |
| `date`                         | `str`       | Date of the document.                                                        |
| `document_content`             | `str`       | Main content of the document.                                                |
| `ap_type`                      | `str`       | Type of access point.                                                        |
| `device_id`                    | `str`       | Identifier for the device.                                                   |
| `ami_id`                       | `str`       | AMI (Advanced Metering Infrastructure) identifier.                           |
| `address`                      | `str`       | General address information.                                                 |
| `municipality`                 | `str`       | Municipality name.                                                           |
| `lat`                          | `str`       | Latitude coordinate.                                                         |
| `long`                         | `str`       | Longitude coordinate.                                                        |
| `antenna`                      | `str`       | Antenna information.                                                         |
| `dbi_gain`                     | `str`       | Antenna gain in dBi.                                                         |
| `azimute`                      | `str`       | Azimuth value.                                                               |
| `tx`                           | `str`       | Transmission information.                                                    |
| `rx`                           | `str`       | Reception information.                                                       |
| `dbm`                          | `str`       | Signal strength in dBm.                                                      |
| `structure_type`               | `str`       | Type of structure.                                                           |
| `m_dan`                        | `str`       | DAN measurement.                                                             |
| `grounding`                    | `str`       | Grounding information.                                                       |
| `grid_voltage`                 | `str`       | Grid voltage value.                                                          |
| `power`                        | `str`       | Power information.                                                           |
| `conductor_type`               | `str`       | Type of conductor used.                                                      |
| `device_installation_address`  | `str`       | Address where the device is installed.                                       |
| `antenna_installation_address` | `str`       | Address where the antenna is installed.                                      |
| `info`                         | `str`       | Additional information.                                                      |
| `more_info`                    | `str`       | More detailed information.                                                   |
| `images`                       | `list[str]` | List of base64-encoded strings representing images to be included in the PDF.|

## Notes

- **Base64 Fields:**  
  - `enterprise_logo` and each entry in `images` must be valid base64-encoded image strings.
- **String Fields:**  
  - All other fields are plain strings and should contain the relevant textual data.
