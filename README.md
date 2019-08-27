## Description
Copies SAP® co- and data files and generates a ZIP file.

## Usage
```
gtrans.py <directory> <transport_request> "<description>"
```

## Example
```
python gtrans.py \\NETWORKDIR\trans SY1K900123 "zip_file_name_without_extension"
```
Will result in a zip file containing the co- and data files of SY1K900123 like this:
**SY1K900123_zip_file_name_without_extension_dd-mm-YYYY.zip**

##
SAP® and other trademarks are registered trademarks of SAP SE and / or its affiliates.
