
# ===============================================================
# Extract deforestation mask(data only) each year for drc
# ===============================================================

import arcpy
from arcpy import env
from arcpy.sa import *

print "System modules import successful"

# Set environment settings
env.workspace = r'H:\Confiance_WRI\COD_tcl_30\treecoverloss_years.gdb'
outFolder = env.workspace
arcpy.env.overwriteOutput = True
print "Environment set"

# Set local variables
mask_file = r'H:\Confiance_WRI\COD_tcl_30\masks_list.txt'
mask_list = open(mask_file, 'r')
print "Reading masks successful"

f = open("Newlist.txt", "w")
for mask in mask_list:
    year_mask = mask.strip('\n')
    print year_mask
    inRaster = year_mask
    inSQLClause = "Value = 1"
    print "local environment set"
    
    # Set the mask for extraction
    arcpy.env.mask = "drc_limit"
    print "Extract boundary set"
    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    print "Spatial analyst extension checked"
    # Execute ExtractByAttributes
    attExtract = ExtractByAttributes(inRaster, inSQLClause)
    print "extraction successful"
    # Save the output
    Output_raster = attExtract.save("Mask_" + year_mask)
    print "Mask extracted and saved for year " + year_mask
    f.write("%s \n" % Output_raster)

f.close()
print "Masks extracted successfully!"
