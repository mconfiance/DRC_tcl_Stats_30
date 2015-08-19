# coding=utf-8
# ============================================================
# Analyzing deforestation around and within PA and LC in DRC
# ============================================================

import arcpy
from arcpy import env
from arcpy.sa import *

print "System modules import successful"

# Set environment settings
env.workspace = r'H:\Confiance_WRI\COD_tcl_30\treecoverloss_years.gdb'
outFolder = env.workspace
arcpy.env.overwriteOutput = True
print "Environment set"

# ===============================================================
# Zonal statistics: calculate areas for PA and LC combined
# ===============================================================

## Execute Zonal statistics as table for each mask (year)
# Set Mask environment

myfiles = r'H:\Confiance_WRI\COD_tcl_30\DRC_tcl_Stats_30\Mask_List.txt'
mymasks = open(myfiles, 'r')
print "Reading raster list successful"

for line in mymasks:
    mask = line.strip('\n')

    arcpy.env.mask = mask
    # Set local variables
    InZones = "cod_atlas_forestier_DBO_PA_LC"
    InZoneField = "Name_ID"
    InValueRaster = "Hansen_2013_area_drc"
    OutTable = "ZonStatArea_PALC_" + mask
    print "Executing " + OutTable
    print "Mask Environment set"

    # Check out ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    print "Spatial analyst extension checked!"

    # Execute ZonalStatistics
    outZStat = ZonalStatisticsAsTable(InZones, InZoneField, InValueRaster, OutTable, "DATA", "SUM")
    print "Zonal stats successful for " + mask

print "Zonal stats successful for individual entities!"

print "ALL STATS SUCCESSFUL!"

