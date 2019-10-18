# CreateContributionTestScript.py
#
# Developed by Jeffrey Rissman
#
# This is a Python script that is used to generate a Vensim command script.
# The Vensim command script will perform one run with all selected policies
# enabled, one run with all policies disabled (a BAU run),
# and one run with each defined subset (or "group") within the set of selected
# policies turned off or turned on (depending on a user setting in this script).


# File Names
# ----------
# Rather than including input and output file names in the code below, we assign all the file
# names to variables in this section.  This allows the names to be easily changed if desired.
ModelFile = "EPS.mdl" # The name of the Vensim model file (typically with .mdl or .vpm extension)
OutputScript = "GeneratedContributionTestScript.cmd" # The desired filename of the Vensim command script to be generated
RunResultsFile = "ContributionTestResults.tsv" # The desired filename for TSV file containing model run results
OutputVarsFile = "OutputVarsToExport.lst" # The name of the file containing a list of variables to be included in the RunResultsFile
                                          # May optionally also be used as a SAVELIST for Vensim (see below)

# Other Settings
# --------------
RunName = "MostRecentRun" # The desired name for all runs performed.  Used as the filename for the VDF files that Vensim creates
EnableOrDisableGroups = "Disable" # Should each group be enabled or disabled in turn?
								 # Essentially, this is testing either the contribution of a group in the proximity of the
								 # BAU case ("Enable") or in the proximity of a scenario defined in the non-zero values of
								 # the policies listed below ("Disable").
PolicySchedule = 1 # The number of the policy implementation schedule file to be used (in InputData/plcy-schd/FoPITY)


# Index definitions
# -----------------
# Each policy is a Python list.  The numbers below are a key to the meaning of the four entries
# that compose each policy, so we can refer to them by meaningful names in the code.
# Note that the fourth entry in each policy, Settings, is itself a list that contains various
# setting values.  Do not change any names or numbers in this section.
Enabled = 0
LongName = 1
ShortName = 2
Settings = 3
Group = 4


# Policy Options
# --------------
# This section specifies which policies should be included in the Vensim command script
# (called here "enabled" policies) and what setting values for those policies should
# be included.  Unless you are using "Enable" Groups mode, all non-repeating
# combinations of the settings for enabled policies will
# be included in the Vensim command script, so do not enable too many policies at once, or
# Vensim will be unable to complete the necessary runs in a reasonable amount of time.
# Each policy is on a single line:
  # You may change the first entry of each policy to "True" to enable the policy or "False" to disable it.
  # The second and third entries are the long and short name of the policy, used internally by this script.  Do not change these names.
  # The fourth entry in each policy is a list of setting values enclosed with square brackets.
    # You may change these values, add more values (separated by commas), and delete values.
    # Any enabled policy must have a minimum of one setting value.  A policy that is disabled
    # and a policy with a setting of zero produce identical results.
  # The fifth entry in each policy is its group name.  By default, each policy is in its own group (and its subscripts share that group).
    # Change the group names so multiple policies share a name (like "financial policies") to cause them to be enabled or disabled together.

PotentialPolicies = (

	# Transportation Sector Policies
	(False,"Percentage Reduction of Separately Regulated Pollutants[LDVs,VOC]","Conventional Pollutant Standards - LDVs VOCs",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[LDVs,CO]","Conventional Pollutant Standards - LDVs CO",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[LDVs,NOx]","Conventional Pollutant Standards - LDVs NOx",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[LDVs,PM10]","Conventional Pollutant Standards - LDVs PM10",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[LDVs,PM25]","Conventional Pollutant Standards - LDVs PM2.5",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[LDVs,SOx]","Conventional Pollutant Standards - LDVs SOx",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[LDVs,BC]","Conventional Pollutant Standards - LDVs BC",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[LDVs,OC]","Conventional Pollutant Standards - LDVs OC",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[HDVs,VOC]","Conventional Pollutant Standards - HDVs VOCs",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[HDVs,CO]","Conventional Pollutant Standards - HDVs CO",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[HDVs,NOx]","Conventional Pollutant Standards - HDVs NOx",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[HDVs,PM10]","Conventional Pollutant Standards - HDVs PM10",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[HDVs,PM25]","Conventional Pollutant Standards - HDVs PM2.5",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[HDVs,SOx]","Conventional Pollutant Standards - HDVs SOx",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[HDVs,BC]","Conventional Pollutant Standards - HDVs BC",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[HDVs,OC]","Conventional Pollutant Standards - HDVs OC",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[aircraft,VOC]","Conventional Pollutant Standards - aircraft VOCs",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[aircraft,NOx]","Conventional Pollutant Standards - aircraft NOx",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[rail,VOC]","Conventional Pollutant Standards - rail VOCs",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[rail,CO]","Conventional Pollutant Standards - rail CO",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[rail,NOx]","Conventional Pollutant Standards - rail NOx",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[rail,PM10]","Conventional Pollutant Standards - rail PM10",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[rail,PM25]","Conventional Pollutant Standards - rail PM2.5",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[rail,BC]","Conventional Pollutant Standards - rail BC",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[rail,OC]","Conventional Pollutant Standards - rail OC",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[ships,VOC]","Conventional Pollutant Standards - ships VOCs",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[ships,CO]","Conventional Pollutant Standards - ships CO",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[ships,NOx]","Conventional Pollutant Standards - ships NOx",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[ships,PM10]","Conventional Pollutant Standards - ships PM10",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[ships,PM25]","Conventional Pollutant Standards - ships PM2.5",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[ships,BC]","Conventional Pollutant Standards - ships BC",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[ships,OC]","Conventional Pollutant Standards - ships OC",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,VOC]","Conventional Pollutant Standards - motorbikes VOCs",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,CO]","Conventional Pollutant Standards - motorbikes CO",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,NOx]","Conventional Pollutant Standards - motorbikes NOx",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,PM10]","Conventional Pollutant Standards - motorbikes PM10",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,PM25]","Conventional Pollutant Standards - motorbikes PM2.5",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,SOx]","Conventional Pollutant Standards - motorbikes SOx",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,BC]","Conventional Pollutant Standards - motorbikes BC",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,OC]","Conventional Pollutant Standards - motorbikes OC",[0,1],"Conventional Pollutant Standard"),
	(False,"EV Charger Deployment","Electric Vehicle Charger Deployment",[0,300],"EV Charger Deployment"),
	(False,"Reduce EV Range Anxiety and Charging Time","Electric Vehicle Range n Charging Time",[0,1],"EV Range n Charging Time"),
	(True,"Additional Minimum Required EV Sales Percentage[passenger,LDVs]","Electric Vehicle Sales Mandate - Passenger LDVs",[0,0.5],"EV Sales Mandate"),
	(False,"Additional Minimum Required EV Sales Percentage[passenger,motorbikes]","Electric Vehicle Sales Mandate - Passenger Motorbikes",[0,1],"EV Sales Mandate"),
	(False,"Additional EV Subsidy Percentage[passenger,LDVs]","Electric Vehicle Subsidy - Passenger LDVs",[0,0.5],"EV Subsidy"),
	(False,"LDVs Feebate Rate","Feebate",[0,1],"Feebate"),
	(False,"Percentage Additional Improvement of Fuel Economy Std[passenger,LDVs]","Fuel Economy Standard - Passenger LDVs",[0,1],"Vehicle Fuel Economy Standards"),
	(False,"Percentage Additional Improvement of Fuel Economy Std[freight,LDVs]","Fuel Economy Standard - Freight LDVs",[0,1],"Vehicle Fuel Economy Standards"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[passenger,HDVs]","Fuel Economy Standard - Passenger HDVs",[0,0.66],"Vehicle Fuel Economy Standards"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[freight,HDVs]","Fuel Economy Standard - Freight HDVs",[0,.66],"Vehicle Fuel Economy Standards"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[passenger,aircraft]","Fuel Economy Standard - Passenger Aircraft",[0,0.54],"Vehicle Fuel Economy Standards"),
	(False,"Percentage Additional Improvement of Fuel Economy Std[freight,aircraft]","Fuel Economy Standard - Freight Aircraft",[0,0.54],"Vehicle Fuel Economy Standards"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[passenger,rail]","Fuel Economy Standard - Passenger Rail",[0,0.2],"Vehicle Fuel Economy Standards"),
	(False,"Percentage Additional Improvement of Fuel Economy Std[freight,rail]","Fuel Economy Standard - Freight Rail",[0,0.2],"Vehicle Fuel Economy Standards"),
	(False,"Percentage Additional Improvement of Fuel Economy Std[passenger,ships]","Fuel Economy Standard - Passenger Ships",[0,0.2],"Vehicle Fuel Economy Standards"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[freight,ships]","Fuel Economy Standard - Freight Ships",[0,0.2],"Vehicle Fuel Economy Standards"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[passenger,motorbikes]","Fuel Economy Standard - Passenger Motorbikes",[0,0.74],"Vehicle Fuel Economy Standards"),
	(False,"Minimum Required Hydrogen Vehicle Sales Percentage[passenger,LDVs]","Hydrogen Vehicle Sales Mandate - Passenger LDVs",[0,1],"Hydrogen Veh Sales Mandate"),
	(False,"Minimum Required Hydrogen Vehicle Sales Percentage[freight,LDVs]","Hydrogen Vehicle Sales Mandate - Freight LDVs",[0,1],"Hydrogen Veh Sales Mandate"),
	(False,"Minimum Required Hydrogen Vehicle Sales Percentage[passenger,HDVs]","Hydrogen Vehicle Sales Mandate - Passenger HDVs",[0,1],"Hydrogen Veh Sales Mandate"),
	(False,"Minimum Required Hydrogen Vehicle Sales Percentage[freight,HDVs]","Hydrogen Vehicle Sales Mandate - Freight HDVs",[0,1],"Hydrogen Veh Sales Mandate"),
	(False,"Minimum Required Hydrogen Vehicle Sales Percentage[passenger,aircraft]","Hydrogen Vehicle Sales Mandate - Passenger Aircraft",[0,1],"Hydrogen Veh Sales Mandate"),
	(False,"Minimum Required Hydrogen Vehicle Sales Percentage[freight,aircraft]","Hydrogen Vehicle Sales Mandate - Freight Aircraft",[0,1],"Hydrogen Veh Sales Mandate"),
	(False,"Minimum Required Hydrogen Vehicle Sales Percentage[passenger,rail]","Hydrogen Vehicle Sales Mandate - Passenger Rail",[0,1],"Hydrogen Veh Sales Mandate"),
	(False,"Minimum Required Hydrogen Vehicle Sales Percentage[freight,rail]","Hydrogen Vehicle Sales Mandate - Freight Rail",[0,1],"Hydrogen Veh Sales Mandate"),
	(False,"Minimum Required Hydrogen Vehicle Sales Percentage[passenger,ships]","Hydrogen Vehicle Sales Mandate - Passenger Ships",[0,1],"Hydrogen Veh Sales Mandate"),
	(False,"Minimum Required Hydrogen Vehicle Sales Percentage[freight,ships]","Hydrogen Vehicle Sales Mandate - Freight Ships",[0,1],"Hydrogen Veh Sales Mandate"),
	(True,"Fraction of TDM Package Implemented[passenger]","Transportation Demand Management - Passengers",[0,1],"Transportation Demand Management"),
	(True,"Fraction of TDM Package Implemented[freight]","Transportation Demand Management - Freight",[0,1],"Transportation Demand Management"),

	# Buildings Sector Policies
	(False,"Fraction of New Bldg Components Shifted to Other Fuels[heating,urban residential]","Building Component Electrification - Urban Residential Heating",[0,1],"Building Component Electrification"),
	(False,"Fraction of New Bldg Components Shifted to Other Fuels[appliances,urban residential]","Building Component Electrification - Urban Residential Appliances",[0,1],"Building Component Electrification"),
	(False,"Fraction of New Bldg Components Shifted to Other Fuels[other component,urban residential]","Building Component Electrification - Urban Residential Other Components",[0,1],"Building Component Electrification"),
	(False,"Fraction of New Bldg Components Shifted to Other Fuels[heating,rural residential]","Building Component Electrification - Rural Residential Heating",[0,1],"Building Component Electrification"),
	(False,"Fraction of New Bldg Components Shifted to Other Fuels[appliances,rural residential]","Building Component Electrification - Rural Residential Appliances",[0,1],"Building Component Electrification"),
	(False,"Fraction of New Bldg Components Shifted to Other Fuels[other component,rural residential]","Building Component Electrification - Rural Residential Other Components",[0,1],"Building Component Electrification"),
	(True,"Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,urban residential]","Building Energy Efficiency Standards - Urban Residential Cooling and Ventilation",[0,0.38],"Building Energy Efficiency Standards"),
	(True,"Reduction in E Use Allowed by Component Eff Std[envelope,urban residential]","Building Energy Efficiency Standards - Urban Residential Envelope",[0,0.38],"Building Energy Efficiency Standards"),
	(True,"Reduction in E Use Allowed by Component Eff Std[lighting,urban residential]","Building Energy Efficiency Standards - Urban Residential Lighting",[0,0.4],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[appliances,urban residential]","Building Energy Efficiency Standards - Urban Residential Appliances",[0,0.65],"Building Energy Efficiency Standards"),
	(True,"Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,rural residential]","Building Energy Efficiency Standards - Rural Residential Cooling and Ventilation",[0,0.38],"Building Energy Efficiency Standards"),
	(True,"Reduction in E Use Allowed by Component Eff Std[envelope,rural residential]","Building Energy Efficiency Standards - Rural Residential Envelope",[0,0.38],"Building Energy Efficiency Standards"),
	(True,"Reduction in E Use Allowed by Component Eff Std[lighting,rural residential]","Building Energy Efficiency Standards - Rural Residential Lighting",[0,0.4],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[appliances,rural residential]","Building Energy Efficiency Standards - Rural Residential Appliances",[0,0.65],"Building Energy Efficiency Standards"),
	(True,"Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,commercial]","Building Energy Efficiency Standards - Commercial Cooling and Ventilation",[0,0.38],"Building Energy Efficiency Standards"),
	(True,"Reduction in E Use Allowed by Component Eff Std[envelope,commercial]","Building Energy Efficiency Standards - Commercial Envelope",[0,0.38],"Building Energy Efficiency Standards"),
	(True,"Reduction in E Use Allowed by Component Eff Std[lighting,commercial]","Building Energy Efficiency Standards - Commercial Lighting",[0,0.4],"Building Energy Efficiency Standards"),
	(True,"Reduction in E Use Allowed by Component Eff Std[other component,commercial]","Building Energy Efficiency Standards - Commercial Other Components",[0,0.11],"Building Energy Efficiency Standards"),
	(False,"Boolean Improved Contractor Edu and Training","Contractor Training",[0,1],"Contractor Training"),
	(False,"Min Fraction of Total Elec Demand to be Met by Distributed Solar PV","Distributed Solar Carve-Out",[0,0.24],"Distributed Solar Promotion"),
	(False,"Boolean Improved Device Labeling","Improved Labeling",[0,1],"Improved Labeling"),
	(True,"Share of Preexisting Buildings Subject to Retrofitting[urban residential]","Retrofit Existing Buildings - Urban Residential",[0,0.5],"Increased Retrofitting"),
	(True,"Share of Preexisting Buildings Subject to Retrofitting[rural residential]","Retrofit Existing Buildings - Rural Residential",[0,0.5],"Increased Retrofitting"),
	(True,"Share of Preexisting Buildings Subject to Retrofitting[commercial]","Retrofit Existing Buildings - Commercial",[0,0.5],"Increased Retrofitting"),
	(False,"Boolean Rebate Program for Efficient Components[cooling and ventilation]","Rebate for Efficient Products - Cooling and Ventilation",[0,1],"Rebate for Efficient Products"),
	
	# Electricity Sector Policies
	(False,"Boolean Ban New Power Plants[natural gas nonpeaker es]","Ban New Power Plants - Natural Gas Nonpeaker",[0,1],"Ban New Power Plants"),
	(False,"Boolean Ban New Power Plants[nuclear es]","Ban New Power Plants - Nuclear",[0,1],"Ban New Power Plants"),
	(False,"Boolean Ban New Power Plants[petroleum es]","Ban New Power Plants - Diesel",[0,1],"Ban New Power Plants"),
	(False,"Boolean Ban New Power Plants[crude oil es]","Ban New Power Plants - Crude Oil",[0,1],"Ban New Power Plants"),
	(False,"Boolean Ban New Power Plants[heavy or residual fuel oil es]","Ban New Power Plants - Heavy Fuel Oil",[0,1],"Ban New Power Plants"),
	(True,"Renewable Portfolio Std Percentage","Carbon-free Electricity Standard",[0,0.62],"Carbon-free Electricity Standard"),
	(False,"Annual Additional Capacity Retired due to Early Retirement Policy[natural gas nonpeaker es]","Early Retirement of Power Plants - Natural Gas Nonpeaker",[0,2000],"Early Retirement of Power Plants"),
	(False,"Annual Additional Capacity Retired due to Early Retirement Policy[geothermal es]","Early Retirement of Power Plants - Desalination Cogen",[0,2000],"Early Retirement of Power Plants"),
	(False,"Annual Additional Capacity Retired due to Early Retirement Policy[petroleum es]","Early Retirement of Power Plants - Diesel",[0,2000],"Early Retirement of Power Plants"),
	(True,"Annual Additional Capacity Retired due to Early Retirement Policy[crude oil es]","Early Retirement of Power Plants - Crude Oil",[0,750],"Early Retirement of Power Plants"),
	(False,"Annual Additional Capacity Retired due to Early Retirement Policy[heavy or residual fuel oil es]","Early Retirement of Power Plants - Heavy Fuel Oil",[0,2000],"Early Retirement of Power Plants"),
	(True,"Percentage Increase in Transmission Capacity vs BAU","Increase Transmission",[0,0.4],"Increase Transmission"),
	(False,"Boolean Use Non BAU Mandated Capacity Construction Schedule[onshore wind es]","KSA 2030 Renewables Target (onshore wind) - Onshore Wind",[0,1],"KSA 2030 Renewables Target"),
	(False,"Boolean Use Non BAU Mandated Capacity Construction Schedule[solar PV es]","KSA 2030 Renewables Target (solar PV) - Solar PV",[0,1],"KSA 2030 Renewables Target"),
	(False,"Boolean Use Non BAU Mandated Capacity Construction Schedule[solar thermal es]","KSA 2030 Renewables Target (solar thermal) - Solar Thermal",[0,1],"KSA 2030 Renewables Target"),
	(False,"Percentage Reduction in Plant Downtime[onshore wind es,newly built]","Reduce Plant Downtime - New Onshore Wind",[0,0.25],"Reduce Plant Downtime"),
	(False,"Percentage Reduction in Plant Downtime[solar PV es,newly built]","Reduce Plant Downtime - New Solar PV",[0,0.3],"Reduce Plant Downtime"),
	(False,"Percentage TnD Losses Avoided","Reduce Transmission n Distribution Losses",[0,0.6],"Reduce TnD Losses"),
	(False,"Subsidy for Elec Production by Fuel[nuclear es]","Subsidy for Electricity Production - Nuclear",[0,200],"Subsidy for Electricity Production"),
	(False,"Subsidy for Elec Production by Fuel[onshore wind es]","Subsidy for Electricity Production - Onshore Wind",[0,200],"Subsidy for Electricity Production"),
	(False,"Subsidy for Elec Production by Fuel[solar PV es]","Subsidy for Electricity Production - Solar PV",[0,200],"Subsidy for Electricity Production"),
	(False,"Subsidy for Elec Production by Fuel[solar thermal es]","Subsidy for Electricity Production - Solar Thermal",[0,200],"Subsidy for Electricity Production"),

	# Industry Sector Policies
	(True,"Fraction of Cement Clinker Substitution Made","Cement Clinker Substitution",[0,1],"Cement Clinker Substitution"),
	(False,"Fraction of Potential Cogeneration and Waste Heat Recovery Adopted","Cogeneration and Waste Heat Recovery",[0,1],"Cogeneration and Waste Heat Recovery"),
	(False,"Fraction of Energy Savings from Early Facility Retirement Achieved","Early Retirement of Industrial Facilities",[0,1],"Early Retirement of Industrial Facilities"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates]","Industry Energy Efficiency Standards - Cement Industry",[0,0.2],"Industry Energy Efficiency Standards"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[natural gas and petroleum systems]","Industry Energy Efficiency Standards - Petroleum and Natural Gas",[0,0.2],"Industry Energy Efficiency Standards"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel]","Industry Energy Efficiency Standards - Iron and Steel Industry",[0,0.2],"Industry Energy Efficiency Standards"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals]","Industry Energy Efficiency Standards - Chemicals Industry",[0,0.2],"Industry Energy Efficiency Standards"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture]","Industry Energy Efficiency Standards - Agriculture",[0,0.2],"Industry Energy Efficiency Standards"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries]","Industry Energy Efficiency Standards - Other Industries",[0,0.2],"Industry Energy Efficiency Standards"),
	(False,"Fraction of Installation and System Integration Issues Remedied","Improved System Design",[0,1],"Improved System Design"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,natural gas if]","Electrification + Hydrogen - Cement Industry Natural Gas Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,petroleum diesel if]","Electrification + Hydrogen - Cement Industry Petroleum Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,crude oil if]","Electrification + Hydrogen - Cement Industry Crude Oil Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,heavy or residual fuel oil if]","Electrification + Hydrogen - Cement Industry Heavy or Residual Fuel Oil Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,LPG propane or butane if]","Electrification + Hydrogen - Cement Industry LPG Propane or Butane Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,natural gas if]","Electrification + Hydrogen - Natural Gas and Petroleum Industry Natural Gas Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,petroleum diesel if]","Electrification + Hydrogen - Natural Gas and Petroleum Industry Petroleum Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,crude oil if]","Electrification + Hydrogen - Natural Gas and Petroleum Industry Crude Oil Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,heavy or residual fuel oil if]","Electrification + Hydrogen - Natural Gas and Petroleum Industry Heavy or Residual Fuel Oil Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,LPG propane or butane if]","Electrification + Hydrogen - Natural Gas and Petroleum Industry LPG Propane or Butane Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,natural gas if]","Electrification + Hydrogen - Iron and Steel Industry Natural Gas Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,petroleum diesel if]","Electrification + Hydrogen - Iron and Steel Industry Petroleum Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,crude oil if]","Electrification + Hydrogen - Iron and Steel Industry Crude Oil Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,heavy or residual fuel oil if]","Electrification + Hydrogen - Iron and Steel Industry Heavy or Residual Fuel Oil Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,LPG propane or butane if]","Electrification + Hydrogen - Iron and Steel Industry LPG Propane or Butane Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,natural gas if]","Electrification + Hydrogen - Chemicals Industry Natural Gas Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,petroleum diesel if]","Electrification + Hydrogen - Chemicals Industry Petroleum Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,crude oil if]","Electrification + Hydrogen - Chemicals Industry Crude Oil Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,heavy or residual fuel oil if]","Electrification + Hydrogen - Chemicals Industry Heavy or Residual Fuel Oil Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,LPG propane or butane if]","Electrification + Hydrogen - Chemicals Industry LPG Propane or Butane Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[waste management,natural gas if]","Electrification + Hydrogen - Water n Waste Natural Gas Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[waste management,petroleum diesel if]","Electrification + Hydrogen - Water n Waste Petroleum Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[waste management,crude oil if]","Electrification + Hydrogen - Water n Waste Crude Oil Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[waste management,heavy or residual fuel oil if]","Electrification + Hydrogen - Water n Waste Heavy or Residual Fuel Oil Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,natural gas if]","Electrification + Hydrogen - Other Industries Natural Gas Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,petroleum diesel if]","Electrification + Hydrogen - Other Industries Petroleum Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,crude oil if]","Electrification + Hydrogen - Other Industries Crude Oil Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,heavy or residual fuel oil if]","Electrification + Hydrogen - Other Industries Heavy or Residual Fuel Oil Use",[0,1],"Electrification + Hydrogen"),
	(False,"Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,LPG propane or butane if]","Electrification + Hydrogen - Other Industries LPG Propane or Butane Use",[0,1],"Electrification + Hydrogen"),
	(False,"Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[cement and other carbonates]","Material Efficiency, Longevity, n Re-Use - Cement Industry",[0,1],"Material Efficiency, Longevity, n Re-Use"),
	(False,"Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[iron and steel]","Material Efficiency, Longevity, n Re-Use - Iron and Steel Industry",[0,1],"Material Efficiency, Longevity, n Re-Use"),
	(False,"Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[chemicals]","Material Efficiency, Longevity, n Re-Use - Chemicals Industry",[0,1],"Material Efficiency, Longevity, n Re-Use"),
	(False,"Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[other industries]","Material Efficiency, Longevity, n Re-Use - Other Industries",[0,1],"Material Efficiency, Longevity, n Re-Use"),
	(True,"Fraction of Methane Capture Opportunities Achieved","Methane Capture",[0,1],"Methane Capture"),
	(True,"Fraction of F Gases Avoided","Reduce F-gases",[0,1],"Reduce F-gases"),
	(False,"Percent Reduction in Fossil Fuel Exports[petroleum gasoline]","Reduce Fossil Fuel Exports - Petroleum Gasoline",[0,1],"Percent Reduction in Fossil Fuel Exports"),
	(False,"Percent Reduction in Fossil Fuel Exports[petroleum diesel]","Reduce Fossil Fuel Exports - Petroleum Diesel",[0,1],"Percent Reduction in Fossil Fuel Exports"),
	(False,"Percent Reduction in Fossil Fuel Exports[jet fuel or kerosene]","Reduce Fossil Fuel Exports - Jet Fuel/Kerosene",[0,1],"Percent Reduction in Fossil Fuel Exports"),
	(False,"Percent Reduction in Fossil Fuel Exports[crude oil]","Reduce Fossil Fuel Exports - Crude Oil",[0,1],"Percent Reduction in Fossil Fuel Exports"),
	(False,"Percent Reduction in Fossil Fuel Exports[heavy or residual fuel oil]","Reduce Fossil Fuel Exports - Heavy/Residual Fuel Oil",[0,1],"Percent Reduction in Fossil Fuel Exports"),
	(False,"Percent Reduction in Fossil Fuel Exports[LPG propane or butane]","Reduce Fossil Fuel Exports - LPG/Propane/Butane",[0,1],"Percent Reduction in Fossil Fuel Exports"),
	(False,"Fraction of Addressable Process Emissions Avoided via Worker Training","Worker Training",[0,1],"Worker Training"),

	# Agriculture, Land Use, and Water Policies
	(False,"Fraction of Afforestation and Reforestation Achieved","Afforestation",[0,1],"Afforestation"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[waste management]","Desalination Energy Efficiency Standards",[0,0.2],"Desalination Energy Efficiency"),
	(False,"Fraction of Abatement from Livestock Measures Achieved","Livestock Measures",[0,1],"Livestock Measures"),
	(False,"Percent Animal Products Shifted to Nonanimal Products","Shift to Non-Animal Products",[0,1],"Shift to Non-Animal Products"),
	(False,"Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[waste management]","Water Conservation",[0,1],"Water Conservation"),

	# Cross-Sector Policies
	(False,"Fraction of Potential Additional CCS Achieved","Carbon Capture, Use, n Sequestration",[0,1],"Carbon Capture, Use, n Sequestration"),
	(False,"Additional Carbon Tax Rate[transportation sector]","Domestic Carbon Pricing - Transportation Sector",[0,400],"Carbon Pricing"),
	(False,"Additional Carbon Tax Rate[electricity sector]","Domestic Carbon Pricing - Electricity Sector",[0,400],"Carbon Pricing"),
	(False,"Additional Carbon Tax Rate[residential buildings sector]","Domestic Carbon Pricing - Residential Bldg Sector",[0,400],"Carbon Pricing"),
	(False,"Additional Carbon Tax Rate[commercial buildings sector]","Domestic Carbon Pricing - Commercial Bldg Sector",[0,400],"Carbon Pricing"),
	(False,"Additional Carbon Tax Rate[industry sector]","Domestic Carbon Pricing - Industry Sector",[0,400],"Carbon Pricing"),
	(True,"Fuel Price Deregulation[natural gas]","Fuel Price Deregulation - Natural Gas",[0,0.5],"Fuel Price Deregulation"),
	(True,"Fuel Price Deregulation[petroleum gasoline]","Fuel Price Deregulation - Petroleum Gasoline",[0,0.5],"Fuel Price Deregulation"),
	(True,"Fuel Price Deregulation[petroleum diesel]","Fuel Price Deregulation - Petroleum Diesel",[0,0.5],"Fuel Price Deregulation"),
	(True,"Fuel Price Deregulation[jet fuel or kerosene]","Fuel Price Deregulation - Jet Fuel/Kerosene",[0,0.5],"Fuel Price Deregulation"),
	(True,"Fuel Price Deregulation[crude oil]","Fuel Price Deregulation - Crude Oil",[0,0.5],"Fuel Price Deregulation"),
	(True,"Fuel Price Deregulation[heavy or residual fuel oil]","Fuel Price Deregulation - Heavy/Residual Fuel Oil",[0,0.5],"Fuel Price Deregulation"),
	(True,"Fuel Price Deregulation[LPG propane or butane]","Fuel Price Deregulation - LPG/Propane/Butane",[0,0.5],"Fuel Price Deregulation"),
	(False,"Fraction of Hydrogen Production Pathways Shifted","Shift Hydrogen Production to Electrolysis",[0,1],"Hydrogen Electrolysis"),

	# Research & Development Levers
	(False,"RnD Building Capital Cost Perc Reduction[heating]","Capital Cost Reduction - Buildings: Heating",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Building Capital Cost Perc Reduction[cooling and ventilation]","Capital Cost Reduction - Buildings: Cooling and Ventilation",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Building Capital Cost Perc Reduction[envelope]","Capital Cost Reduction - Buildings: Envelope",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Building Capital Cost Perc Reduction[lighting]","Capital Cost Reduction - Buildings: Lighting",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Building Capital Cost Perc Reduction[appliances]","Capital Cost Reduction - Buildings: Appliances",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Building Capital Cost Perc Reduction[other component]","Capital Cost Reduction - Buildings: Other Components",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD CCS Capital Cost Perc Reduction","Capital Cost Reduction",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[natural gas nonpeaker es]","Capital Cost Reduction - Electricity: Natural Gas Nonpeaker",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[nuclear es]","Capital Cost Reduction - Electricity: Nuclear",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[onshore wind es]","Capital Cost Reduction - Electricity: Onshore Wind",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[solar PV es]","Capital Cost Reduction - Electricity: Solar PV",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[solar thermal es]","Capital Cost Reduction - Electricity: Solar Thermal",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[biomass es]","Capital Cost Reduction - Electricity: Biomass",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[natural gas peaker es]","Capital Cost Reduction - Electricity: Natural Gas Peaker",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD CCS Capital Cost Perc Reduction[crude oil es]","Capital Cost Reduction - Electricity: Crude Oil",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD CCS Capital Cost Perc Reduction[heavy or residual fuel oil es]","Capital Cost Reduction - Electricity: Heavy or Residual Fuel Oil",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[cement and other carbonates]","Capital Cost Reduction - Industry: Cement",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[natural gas and petroleum systems]","Capital Cost Reduction - Industry: Petroleum and Natural Gas",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[iron and steel]","Capital Cost Reduction - Industry: Iron and Steel",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[chemicals]","Capital Cost Reduction - Industry: Chemicals",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[waste management]","Capital Cost Reduction - Industry: Desalination",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[agriculture]","Capital Cost Reduction - Industry: Agriculture",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[other industries]","Capital Cost Reduction - Industry: Other Industries",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Transportation Capital Cost Perc Reduction[battery electric vehicle]","Capital Cost Reduction - Vehicles: Battery Electric",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Transportation Capital Cost Perc Reduction[gasoline vehicle]","Capital Cost Reduction - Vehicles: Gasoline Engine",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Transportation Capital Cost Perc Reduction[diesel vehicle]","Capital Cost Reduction - Vehicles: Diesel Engine",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Transportation Capital Cost Perc Reduction[nonroad vehicle]","Capital Cost Reduction - Vehicles: Non-road",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Building Fuel Use Perc Reduction[heating]","Fuel Use Reduction - Buildings: Heating",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Building Fuel Use Perc Reduction[cooling and ventilation]","Fuel Use Reduction - Buildings: Cooling and Ventilation",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Building Fuel Use Perc Reduction[lighting]","Fuel Use Reduction - Buildings: Lighting",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Building Fuel Use Perc Reduction[appliances]","Fuel Use Reduction - Buildings: Appliances",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Building Fuel Use Perc Reduction[other component]","Fuel Use Reduction - Buildings: Other Components",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD CCS Fuel Use Perc Reduction","Fuel Use Reduction",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Electricity Fuel Use Perc Reduction[natural gas nonpeaker es]","Fuel Use Reduction - Electricity: Natural Gas Nonpeaker",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Electricity Fuel Use Perc Reduction[nuclear es]","Fuel Use Reduction - Electricity: Nuclear",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Electricity Fuel Use Perc Reduction[natural gas peaker es]","Fuel Use Reduction - Electricity: Natural Gas Peaker",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Electricity Fuel Use Perc Reduction[crude oil es]","Fuel Use Reduction - Electricity: Crude Oil",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Electricity Fuel Use Perc Reduction[heavy or residual fuel oil es]","Fuel Use Reduction - Electricity: Fuel Oil",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[cement and other carbonates]","Fuel Use Reduction - Industry: Cement",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[natural gas and petroleum systems]","Fuel Use Reduction - Industry: Petroleum and Natural Gas",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[iron and steel]","Fuel Use Reduction - Industry: Iron and Steel",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[chemicals]","Fuel Use Reduction - Industry: Chemicals",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[waste management]","Fuel Use Reduction - Industry: Desalination",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[agriculture]","Fuel Use Reduction - Industry: Agriculture",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[other industries]","Fuel Use Reduction - Industry: Other Industries",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Transportation Fuel Use Perc Reduction[battery electric vehicle]","Fuel Use Reduction - Vehicles: Battery Electric",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Transportation Fuel Use Perc Reduction[gasoline vehicle]","Fuel Use Reduction - Vehicles: Gasoline Engine",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Transportation Fuel Use Perc Reduction[diesel vehicle]","Fuel Use Reduction - Vehicles: Diesel Engine",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Transportation Fuel Use Perc Reduction[nonroad vehicle]","Fuel Use Reduction - Vehicles: Non-road",[0,0.4],"RnD Fuel Use Reductions")
)

# Building the Policy List
# ------------------------
# Every policy, whether enabled or not, appears in a tuple called "PotentialPolicies" that was constructed above.
# Now we construct the actual list of policies to be included (named "Policies") by
# checking which of the policies have been enabled.

Policies = []
for PotentialPolicy in PotentialPolicies:
	if PotentialPolicy[Enabled]:
		Policies.append(PotentialPolicy)


# Exit with an error if no policies were enabled in the script.  We write the error to the output
# file because it's likely a user will run this without a console and won't be able to see the
# message produced by sys.exit()
if len(Policies) < 1:
	f = open(OutputScript, 'w')
	ErrorMessage = "Error: No policies were enabled in the Python script.  Before running the script, you must enable at least one policy."
	f.write(ErrorMessage)
	f.close()
	import sys
	sys.exit(ErrorMessage)


# Building the Groups List
# ------------------------
# We create a list of all the unique groups that are used by enabled policies.
Groups = []
for Policy in Policies:
	if Policy[Group] not in Groups:
		Groups.append(Policy[Group])


# Generate Vensim Command Script
# ------------------------------
# We begin by creating a new file to serve as the Vensim command script (overwriting
# any older version at that filename).  We then tell Vensim to load
# the model file, and we give it a RUNNAME that will be used for all runs.  (It is
# overwritten each run.)
f = open(OutputScript, 'w')
f.write('SPECIAL>LOADMODEL|"' + ModelFile + '"\n')
f.write("SIMULATE>RUNNAME|" + RunName + "\n")

# The following options may be useful in certain cases, but they cause Vensim to
# produce an output window for each simulation that acknowledges the completion of
# the command.  These output windows accumulate over the course of many runs and
# cause slow-downs (and potentially crashes).  Therefore, these lines are usually
# best left commented out, unless you are doing only a few runs.
# f.write("SPECIAL>NOINTERACTION\n")
# f.write("SIMULATE>SAVELIST|" + OutputVarsFile + "\n")
f.write("\n")

def PerformRunsWithEnabledGroups():

	# First, we do a run with all of the groups disabled
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdf|" + RunResultsFile + "|" + OutputVarsFile + "|||||:")
	f.write("\tEnabledPolicyGroup=None")
	f.write("\tEnabledPolicies=None\n\n")

	# Next, we do a run with each group enabled in turn
	for EnabledGroup in Groups:

		# We create an empty string that we'll use to track the policies enabled in each group
		EnabledPolicies=""

		# We activate policies if their group name matches the currently enabled group
		for Policy in Policies:
			if Policy[Group] == EnabledGroup:
				f.write("SIMULATE>SETVAL|" + Policy[LongName] + "=" + str(Policy[Settings][1]) + "\n")
				# We add the policy to the EnabledPolicies string
				if len(EnabledPolicies) > 0:
					EnabledPolicies += ", "
				EnabledPolicies += Policy[ShortName]

		# We include a SETVAL instruction to select the correct policy implementation schedule file
		f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
		
		# We perform our run and log the output
		f.write("MENU>RUN|O\n")
		f.write("MENU>VDF2TAB|" + RunName + ".vdf|" + RunResultsFile + "|" + OutputVarsFile + "|+!||||:")
		f.write("\tEnabledPolicyGroup=" + str(EnabledGroup))
		f.write("\tEnabledPolicies=" + EnabledPolicies + "\n\n")
	
	# Finally, we do a run with all of the policy groups enabled (a full policy case run)
	
	# We include a SETVAL instruction to select the correct policy implementation schedule file
	f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
	
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdf|" + RunResultsFile + "|" + OutputVarsFile + "|+!||||:")
	f.write("\tEnabledPolicyGroup=All")
	f.write("\tEnabledPolicies=All")
	f.write("\n")

	# We instruct Vensim to delete the .vdf file, to prevent it from getting picked up by
	# sync software, such as DropBox or Google Drive.  If sync software locks the file,
	# Vensim won't be able to overwrite it on the next model run, ruining the batch.
	f.write("FILE>DELETE|" + RunName + ".vdf")
	f.write("\n\n")
	
def PerformRunsWithDisabledGroups():

	# First, we do a run with all of the groups enabled
	for Policy in Policies:
		f.write("SIMULATE>SETVAL|" + Policy[LongName] + "=" + str(Policy[Settings][1]) + "\n")
	
	# We include a SETVAL instruction to select the correct policy implementation schedule file
	f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
	
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdf|" + RunResultsFile + "|" + OutputVarsFile + "|||||:")
	f.write("\tDisabledPolicyGroup=None")
	f.write("\tDisabledPolicies=None\n\n")

	# Next, we do a run with each group disabled in turn
	for DisabledGroup in Groups:

		# We create an empty string that we'll use to track the policies disabled in each group
		DisabledPolicies=""

		# We activate policies if their group name does not match the currently disabled group
		for Policy in Policies:
			if Policy[Group] != DisabledGroup:
				f.write("SIMULATE>SETVAL|" + Policy[LongName] + "=" + str(Policy[Settings][1]) + "\n")
			# Otherwise, we add the policy to the DisabledPolicies string
			else:
				if len(DisabledPolicies) > 0:
					DisabledPolicies += ", "
				DisabledPolicies += Policy[ShortName]
		
		# We include a SETVAL instruction to select the correct policy implementation schedule file
		f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
		
		# We perform our run and log the output
		f.write("MENU>RUN|O\n")
		f.write("MENU>VDF2TAB|" + RunName + ".vdf|" + RunResultsFile + "|" + OutputVarsFile + "|+!||||:")
		f.write("\tDisabledPolicyGroup=" + str(DisabledGroup))
		f.write("\tDisabledPolicies=" + DisabledPolicies + "\n\n")
	
	# Finally, we do a run with all of the groups disabled (a BAU case run)
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdf|" + RunResultsFile + "|" + OutputVarsFile + "|+!||||:")
	f.write("\tDisabledPolicyGroup=All")
	f.write("\tDisabledPolicies=All")
	f.write("\n")

	# We instruct Vensim to delete the .vdf file, to prevent it from getting picked up by
	# sync software, such as DropBox or Google Drive.  If sync software locks the file,
	# Vensim won't be able to overwrite it on the next model run, ruining the batch.
	f.write("FILE>DELETE|" + RunName + ".vdf")
	f.write("\n\n")
	
if EnableOrDisableGroups == "Enable":
	PerformRunsWithEnabledGroups()
else:
	PerformRunsWithDisabledGroups()

# We are done writing the Vensim command script and therefore close the file.
f.close()