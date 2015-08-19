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
# Zonal statistics: calculate areas for PA
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
    InZones = "drc_pa_buffers"
    InZoneField = "Buff"
    InValueRaster = "Hansen_2013_area_drc"
    OutTable = "ZonStatArea_pa_" + mask
    print "Executing " + OutTable
    print "Mask Environment set"

    # Check out ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    print "Spatial analyst extension checked!"

    # Execute ZonalStatistics
    outZStat = ZonalStatisticsAsTable(InZones, InZoneField, InValueRaster, OutTable, "DATA", "SUM")
    print "Zonal stats successful for " + mask

print "Zonal stats successful for Protected Areas!"

# ===============================================================
# Zonal statistics: calculate areas for logging concessions
# ===============================================================

print "Entering stats for logging concessions"

# Set Mask environment
myfiles = r'H:\Confiance_WRI\COD_tcl_30\DRC_tcl_Stats_30\Mask_List.txt'
mymasks = open(myfiles, 'r')
print "Reading raster list successful"

for line in mymasks:
    mask = line.strip('\n')

    arcpy.env.mask = mask
    # Set local variables
    InZones = "drc_lc_buffers"
    InZoneField = "Buff"
    InValueRaster = "Hansen_2013_area_drc"
    OutTable = "ZonStat_Area_lc_" + mask
    print "Executing " + OutTable
    print "Mask Environment set"

    # Check out ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    print "Spatial analyst extension checked!"

    # Execute ZonalStatistics
    outputZStat = ZonalStatisticsAsTable(InZones, InZoneField, InValueRaster, OutTable, "DATA", "SUM")
    print "Zonal stats successful for " + mask

print "Zonal stats successful for logging concessions!"

# ===============================================================
# Zonal statistics: calculaate areas for Supply centers
# ===============================================================

print "Entering stats for Supply centers"

# Set Mask environment
myfiles = r'H:\Confiance_WRI\COD_tcl_30\DRC_tcl_Stats_30\Mask_List.txt'
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

print "Zonal stats successful for supply centers!"

# ===============================================================
# Zonal statistics: calculate areas for Old Provinces
# ===============================================================

print "Entering stats for Old provinces"

# Zonal stats on Old Provinces
myfiles = r'H:\Confiance_WRI\COD_tcl_30\DRC_tcl_Stats_30\Mask_List.txt'
mymasks = open(myfiles, 'r')
print "Reading raster list successful"

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

print "Zonal stats successful for old provinces!"

# ===============================================================
# Zonal statistics: calculate areas for New Provinces
# ===============================================================

print "Entering stats for new provinces"

# Zonal stats on New Provinces
myfiles = r'H:\Confiance_WRI\COD_tcl_30\DRC_tcl_Stats_30\Mask_List.txt'
mymasks = open(myfiles, 'r')
print "Reading raster list successful"

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

print "Zonal stats successful for new provinces!"

print "ALL STATS SUCCESSFUL!"

