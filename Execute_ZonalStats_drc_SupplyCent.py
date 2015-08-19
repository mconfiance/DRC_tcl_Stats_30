
# coding=utf-8
# ============================================================
# Analyzing deforestation around and within PA and LC in DRC
# ============================================================

import arcpy
from arcpy import env
from arcpy.sa import *

print "System modules import successful"

# Set environment settings
env.workspace = "H:/Confiance_WRI/COD_Defor/drc.gdb"
outFolder = env.workspace
arcpy.env.overwriteOutput = True
print "Environment set"

# ===============================================================
# Zonal statistics: calculte areas for Supply centers
# ===============================================================

# Execute Zonal statistics as table for each mask (year)
# Set Mask environment
myfiles = r'H:\Confiance_WRI\COD_Defor\drc.gdb\Newlist.txt'
mymasks = open(myfiles, 'r')
print "Reading raster list successful"

for line in mymasks:
    mask = line.strip('\n')

    arcpy.env.mask = mask
    # Set local variables
    InZones = "drc_sup_cent_buf_sing"
    InZoneField = "Zone"
    InValueRaster = "Hansen_2013_area_drc"
    OutTable = "ZonStatArea_SC_" + mask
    print OutTable
    print "Mask Environment set"

    # Check out ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    print "Spatial analyst extension checked!"

    # Execute ZonalStatistics
    outZStat = ZonalStatisticsAsTable(InZones, InZoneField, InValueRaster, OutTable, "DATA", "SUM")
    print "Zonal stats successful for " + mask
    del outZStat,OutTable
print "Zonal stats Process complete successfully!"

# Zonal stats on Old Provinces

for line in mymasks:
    mask = line.strip('\n')
    print mask
    arcpy.env.mask = mask
    # Set local variables
    InZones = "cod_atlas_forestier_DBO_provinces"
    InZoneField = "nom_prov"
    InValueRaster = "Hansen_2013_area_drc"
    OutTable = "ZonStatArea_OP_" + mask
    print OutTable
    print "Mask Environment set"

    # Check out ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    print "Spatial analyst extension checked!"

    # Execute ZonalStatistics
    outZStat1 = ZonalStatisticsAsTable(InZones, InZoneField, InValueRaster, OutTable, "DATA", "SUM")
    print "Zonal stats successful for " + mask

print "Zonal stats Process complete successfully!"


# Zonal stats on New Provinces

print "got to third for-loop"
for line in mymasks:
    mask = line.strip('\n')

    arcpy.env.mask = mask
    # Set local variables
    InZones = "drc_province26"
    InZoneField = "NOM"
    InValueRaster = "Hansen_2013_area_drc"
    OutTable = "ZonStatArea_NP_" + mask
    print OutTable
    print "Mask Environment set"

    # Check out ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    print "Spatial analyst extension checked!"

    # Execute ZonalStatistics
    outZStat2 = ZonalStatisticsAsTable(InZones, InZoneField, InValueRaster, OutTable, "DATA", "SUM")
    print "Zonal stats successful for " + mask

print "Zonal stats Process complete successfully!"
