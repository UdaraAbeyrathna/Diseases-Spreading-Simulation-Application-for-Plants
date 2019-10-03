import xml.etree.ElementTree as ET
import showLogData

temp_high = 0
temp_low = 0
wind_high = 0
wind_low = 0
wind_nat = ""
wind_acid_co2_min = 0
wind_acid_co2_high = 0
wind_acid_HCLO3_min = 0
wind_acid_HCLO3_high = 0
wind_base_min = 0
wind_base_max = 0
wind_toxic_co_min = 0
wind_toxic_co_high = 0
AH_high = 0
AH_low = 0
RH_high = 0
RH_low = 0
SOIL_M_MIN = 0
SOIL_M_MAX = 0
PH_top = 0
PH_bottom = 0
intencity_top = 0
intencity_bottom = 0
UV_top = 0
UV_bottom = 0
IR_top = 0
IR_bottom = 0

class whetherAnalysis:
	print("whetherAnalysis")
	# temprature = []
	temprature = 0
	wind = 0
	wind_direction = 0
	humidity = 0
	soileMoisture = 0
	wind_content = ""

	def __init__(_temp, _wind_s, _wind_dir, _wind_co2, _wind_clo3, _wind_base, _wind_co, A_hue, R_hue, _soil, _ph, _intensity, _uv, _ir):
		print("__init__")
		temprature = _temp
		
		A_humidity = A_hue
		R_humidity = R_hue

		soileMoisture = _soil

		wind = _wind_s
		wind_nat = _wind_dir
		wind_co2 = _wind_co2
		wind_clo3 = _wind_clo3
		wind_base = _wind_base
		wind_co = _wind_co

		ph_level = _ph

		intensity_level = _intensity
		UV_level = _uv
		IR_level = _ir
		print(intensity_level)
		print(UV_level)
		print(IR_level)

		print(temprature)
		print(wind)
		print(A_humidity)
		print(R_humidity)

		print(soileMoisture)

		path = "E:\\ZZZZZ\\FIT\\suwa project\\demoFlower.xml"
		tree = ET.parse(path)
		root = tree.getroot()

		for child in root:
			print(child.tag)

		full_xml_data = ET.tostring(root, encoding='utf8').decode('utf8')
		print(full_xml_data)

		whetherAnalysis.getFlowerXML_Data()
		whetherAnalysis.tempratureAnalysis(temprature)
		whetherAnalysis.windAnalysis(wind, wind_nat, wind_co2, wind_clo3, wind_base, wind_co)
		whetherAnalysis.humidityAnalysis(A_humidity, R_humidity)
		whetherAnalysis.soileMoistureAnalysis(soileMoisture)
		whetherAnalysis.phAnalysis(ph_level)
		whetherAnalysis.intensityAnalysis(intensity_level, UV_level, IR_level)



	def tempratureAnalysis(temprature):
		print("tempratureAnalysis", temprature)
		# get ranges from xml
		# 1 read xml val
		global temp_high
		global temp_low

		try:
			if(temp_high == temprature or temp_high > temprature):
				bTempHigh = True
			
			if(temp_low == temprature or temp_low < temprature):
				bTempLow = True

			if(bTempHigh == True & bTempLow == True):
				# Print on the log
				showLogData.printLogData("THE TEMPRATURE "+str(temprature)+"'C IS SUITABLE FOR PLANT")
			elif(bTempHigh == False | bTempLow == False):
				showLogData.printLogData("THE TEMPRATURE "+str(temprature)+"'C IS HARMFUL FOR PLANT(OUT OF RANGE)")
			else:
				showLogData.printLogData("TEMPRATURE NOT HAS BEEN DEFINED")
		except:
			showLogData.printLogData("TEMPRATURE CAPTURE FALURE")



	def windAnalysis(wind_speed, wind_nature, co2_level, hclo3_level, sope_water_level, co_level):
		global wind_high
		global wind_low

		global wind_nat

		global wind_acid_co2_min
		global wind_acid_co2_high

		global wind_acid_HCLO3_min
		global wind_acid_HCLO3_high

		global wind_base_min
		global wind_base_max

		global wind_toxic_co_min
		global wind_toxic_co_high

		# wind_speed
		bWindHigh = False
		bWindLow = False
		if(wind_high == wind_speed or wind_high > wind_speed):
			bWindHigh = True
			
		if(wind_low == wind_speed or wind_low < wind_speed):
			bWindLow = True

		if(bWindHigh == True & bWindLow == True):
			# Print on the log
			showLogData.printLogData(str(wind_speed)+" km h^-1 OF WIND SPEED IS SUITABLE FOR PLANT")
		elif(bWindHigh == False or bWindLow == False):
			showLogData.printLogData(str(wind_speed)+" km h^-1 OF WIND SPEED IS HARMFUL FOR PLANT(OUT OF RANGE)")
		else:
			showLogData.printLogData("WIND SPEED NOT HAS BEEN DEFINED")

		# wind_nature
		if(wind_nature == wind_nat):
			# Print on the log
			showLogData.printLogData("WIND NATURE : "+wind_nature+", STATUS : OK")
		else:
			showLogData.printLogData("WIND NATURE : "+wind_nature+", STATUS : NOT OK")

		# co2_level
		bco2_levelHigh = False
		bco2_levelLow = False
		if(wind_acid_co2_high == co2_level or wind_acid_co2_high > co2_level):
			bco2_levelHigh = True
			
		if(wind_acid_co2_min == co2_level or wind_acid_co2_min < co2_level):
			bco2_levelLow = True

		if(bco2_levelHigh == True & bco2_levelLow == True):
			# Print on the log
			showLogData.printLogData(str(co2_level)+"g m^-3 OF CO2 IS SUITABLE FOR PLANT")
		elif(bco2_levelHigh == False or bco2_levelLow == False):
			showLogData.printLogData(str(co2_level)+"g m^-3 OF CO2 IS HARMFUL FOR PLANT(OUT OF RANGE)")
		else:
			showLogData.printLogData("CO2 LEVEL NOT HAS BEEN DEFINED")

		# hclo3_level
		bHCLO3_levelHigh = False
		bHCLO3_levelLow = False
		if(wind_acid_HCLO3_high == hclo3_level or wind_acid_HCLO3_high > hclo3_level):
			bHCLO3_levelHigh = True
			
		if(wind_acid_HCLO3_min == hclo3_level or wind_acid_HCLO3_min < hclo3_level):
			bHCLO3_levelLow = True

		if(bHCLO3_levelHigh == True & bHCLO3_levelLow == True):
			# Print on the log
			showLogData.printLogData(str(hclo3_level)+"g m^-3 OF HCLO3 IS SUITABLE FOR PLANT")
		elif(bHCLO3_levelHigh == False or bHCLO3_levelLow == False):
			showLogData.printLogData(str(hclo3_level)+"g m^-3 OF HCLO3 IS HARMFUL FOR PLANT(OUT OF RANGE)")
		else:
			showLogData.printLogData("HCLO3 VAPOUR AMOUNT NOT HAS BEEN DEFINED")

		# sope_water_level
		bSOPE_levelHigh = False
		bSOPE_levelLow = False
		if(wind_base_max == sope_water_level or wind_base_max > sope_water_level):
			bSOPE_levelHigh = True
			
		if(wind_base_min == sope_water_level or wind_base_min < sope_water_level):
			bSOPE_levelLow = True

		if(bSOPE_levelHigh == True & bSOPE_levelLow == True):
			# Print on the log
			showLogData.printLogData(str(sope_water_level)+"g m^-3 OF SOAP VAPOUR IS SUITABLE FOR PLANT")
		elif(bSOPE_levelHigh == False or bSOPE_levelLow == False):
			showLogData.printLogData(str(sope_water_level)+"g m^-3 OF SOAP VAPOUR IS HARMFUL FOR PLANT(OUT OF RANGE)")
		else:
			showLogData.printLogData("SOAP VAPOUR AMOUNT NOT HAS BEEN DEFINED")

		# co_level
		bCO_levelHigh = False
		bCO_levelLow = False
		if(wind_toxic_co_high == co_level or wind_toxic_co_high > co_level):
			bCO_levelHigh = True
			
		if(wind_toxic_co_min == co_level or wind_toxic_co_min < co_level):
			bCO_levelLow = True

		if(bCO_levelHigh == True & bCO_levelLow == True):
			# Print on the log
			showLogData.printLogData(str(co_level)+"g m^-3 OF CO IS SUITABLE FOR PLANT")
		elif(bCO_levelHigh == False or bCO_levelLow == False):
			showLogData.printLogData(str(co_level)+"g m^-3 OF CO IS HARMFUL FOR PLANT(OUT OF RANGE)")
		else:
			showLogData.printLogData("CO AMOUNT NOT HAS BEEN DEFINED")


	def humidityAnalysis(A_humidity, R_humidity):

		global AH_high
		global AH_low
		global RH_high
		global RH_low

		# A_humidity
		bAHumidity_levelHigh = False
		bAHumidity_levelLow = False
		if(AH_high == A_humidity or AH_high > A_humidity):
			bAHumidity_levelHigh = True
			
		if(AH_low == A_humidity or AH_low < A_humidity):
			bAHumidity_levelLow = True

		if(bAHumidity_levelHigh == True & bAHumidity_levelLow == True):
			# Print on the log
			showLogData.printLogData(str(A_humidity)+"g m^-3 OF WATER VAPOUR IS SUITABLE FOR PLANT")
		elif(bAHumidity_levelHigh == False or bAHumidity_levelLow == False):
			showLogData.printLogData(str(A_humidity)+"g m^-3 OF WATER VAPOUR IS HARMFUL FOR PLANT(OUT OF RANGE)")
		else:
			showLogData.printLogData("WATER VAPOUR AMOUNT NOT HAS BEEN DEFINED")

		# R_humidity
		bRHumidity_levelHigh = False
		bRHumidity_levelLow = False
		if(RH_high == R_humidity or RH_high > R_humidity):
			bRHumidity_levelHigh = True
			
		if(RH_low == R_humidity or RH_low < R_humidity):
			bRHumidity_levelLow = True
		
		if(bRHumidity_levelHigh == True & bRHumidity_levelLow == True):
			# Print on the log
			showLogData.printLogData(str(R_humidity)+"g m^-3 OF WATER VAPOUR IS SUITABLE FOR PLANT")
		elif(bRHumidity_levelHigh == False or bRHumidity_levelLow == False):
			showLogData.printLogData(str(R_humidity)+"g m^-3 OF WATER VAPOUR IS HARMFUL FOR PLANT(OUT OF RANGE)")
		else:
			showLogData.printLogData("WATER VAPOUR PERCENTAGE NOT HAS BEEN DEFINED")


	def soileMoistureAnalysis(soileMoisture):
		global SOIL_M_MIN
		global SOIL_M_MAX

		# soileMoisture
		bSoil_levelHigh = False
		bSoil_levelLow = False
		if(SOIL_M_MAX == soileMoisture or SOIL_M_MAX > soileMoisture):
			bSoil_levelHigh = True
			
		if(SOIL_M_MIN == soileMoisture or SOIL_M_MIN < soileMoisture):
			bSoil_levelLow = True

		if(bSoil_levelHigh == True & bSoil_levelLow == True):
			# Print on the log
			showLogData.printLogData(str(soileMoisture)+"g kg^-1 OF SOILE MOISTURE IS SUITABLE FOR PLANT")
		elif(bSoil_levelHigh == False or bSoil_levelLow == False):
			showLogData.printLogData(str(soileMoisture)+"g kg^-1 OF SOILE MOISTURE IS HARMFUL FOR PLANT(OUT OF RANGE)")
		else:
			showLogData.printLogData("SOILE MOISTURE AMOUNT NOT HAS BEEN DEFINED")

	def phAnalysis(ph_level):
		global PH_top
		global PH_bottom

		# ph_level
		bPH_levelHigh = False
		bPH_levelLow = False
		if(PH_top == ph_level or PH_top > ph_level):
			bPH_levelHigh = True
			
		if(PH_bottom == ph_level or PH_bottom < ph_level):
			bPH_levelLow = True

		if(bPH_levelHigh == True & bPH_levelLow == True):
			# Print on the log
			showLogData.printLogData(str(ph_level)+" OF ph LEVEL IS SUITABLE FOR PLANT")
		elif(bPH_levelHigh == False or bPH_levelLow == False):
			showLogData.printLogData(str(ph_level)+" OF ph LEVEL IS HARMFUL FOR PLANT(OUT OF RANGE)")
		else:
			showLogData.printLogData("ph LEVEL NOT HAS BEEN DEFINED")

	def intensityAnalysis(intensity_C, UV_C, IR_C):
		global intencity_top
		global intencity_bottom
		global UV_top
		global UV_bottom
		global IR_top
		global IR_bottom

		# intensity_C
		bIntensity_levelHigh = False
		bIntensity_levelLow = False
		if(intencity_top == intensity_C or intencity_top > intensity_C):
			bIntensity_levelHigh = True
			
		if(intencity_bottom == intensity_C or intencity_bottom < intensity_C):
			bIntensity_levelLow = True

		if(bIntensity_levelHigh == True & bIntensity_levelLow == True):
			# Print on the log
			showLogData.printLogData(str(intensity_C)+" W m^-2 OF INTENCITY LEVEL IS SUITABLE FOR PLANT")
		elif(bIntensity_levelHigh == False or bIntensity_levelLow == False):
			showLogData.printLogData(str(intensity_C)+" W m^-2 OF INTENCITY LEVEL IS HARMFUL FOR PLANT(OUT OF RANGE)")
		else:
			showLogData.printLogData("INTENCITY LEVEL NOT HAS BEEN DEFINED")

		# UV_C
		bUV_levelHigh = False
		bUV_levelLow = False
		if(UV_top == UV_C or UV_top > UV_C):
			bUV_levelHigh = True
			
		if(UV_bottom == UV_C or UV_bottom < UV_C):
			bUV_levelLow = True

		if(bUV_levelHigh == True & bUV_levelLow == True):
			# Print on the log
			showLogData.printLogData(str(UV_C)+" W m^-2 OF UV LEVEL IS SUITABLE FOR PLANT")
		elif(bUV_levelHigh == False or bUV_levelLow == False):
			showLogData.printLogData(str(UV_C)+" W m^-2 OF UV LEVEL IS HARMFUL FOR PLANT(OUT OF RANGE)")
		else:
			showLogData.printLogData("UV LEVEL NOT HAS BEEN DEFINED")

		# IR_C
		bIR_levelHigh = False
		bIR_levelLow = False
		if(IR_top == IR_C or IR_top > IR_C):
			bIR_levelHigh = True
			
		if(IR_bottom == IR_C or IR_bottom < IR_C):
			bIR_levelLow = True

		if(bIR_levelHigh == True & bIR_levelLow == True):
			# Print on the log
			showLogData.printLogData(str(IR_C)+" W m^-2 OF IR LEVEL IS SUITABLE FOR PLANT")
		elif(bIR_levelHigh == False or bIR_levelLow == False):
			showLogData.printLogData(str(IR_C)+" W m^-2 OF IR LEVEL IS HARMFUL FOR PLANT(OUT OF RANGE)")
		else:
			showLogData.printLogData("IR LEVEL NOT HAS BEEN DEFINED")

	def getFlowerXML_Data():
		global temp_high
		global temp_low
		global wind_high
		global wind_low
		global wind_nat
		global wind_acid_co2_min
		global wind_acid_co2_high
		global wind_acid_HCLO3_min
		global wind_acid_HCLO3_high
		global wind_base_min
		global wind_base_max
		global wind_toxic_co_min
		global wind_toxic_co_high
		global AH_high
		global AH_low
		global RH_high
		global RH_low
		global SOIL_M_MIN
		global SOIL_M_MAX
		global PH_top
		global PH_bottom
		global intencity_top
		global intencity_bottom
		global UV_top
		global UV_bottom
		global IR_top
		global IR_bottom

		# get path
		path = "E:\\ZZZZZ\\FIT\\suwa project\\demoFlower.xml"
		tree = ET.parse(path)
		root = tree.getroot()

		for temp in root.iter('TEMPRATURE'):
			temp_high = float(temp.find('HIGH').text)
			temp_low = float(temp.find('LOW').text)

		for temp in root.iter('WIND'):
			wind_high = float(temp.find('WIND_SPEED_MAX').text)
			wind_low = float(temp.find('WIND_SPEED_MIN').text)
			wind_nat = temp.find('WIND_NATURE').text
			# wind_cont = temp.find('WIND_CONTENT').text
			for wind_c in root.iter('WIND_CONTENT'):
				for wind_a in root.iter('ACID'):
					# wind_acid = wind_c.find('ACID').text
					for wind_a1 in root.iter('CO2'):
						wind_acid_co2_min = float(wind_a1.find('CO2_MIN').text)
						wind_acid_co2_high = float(wind_a1.find('CO2_MAX').text)
					for wind_a2 in root.iter('HCLO3'):
						wind_acid_HCLO3_min = float(wind_a2.find('HCLO3_MIN').text)
						wind_acid_HCLO3_high = float(wind_a2.find('HCLO3_MAX').text)
				for wind_b in root.iter('BASE'):
					# wind_acid = wind_c.find('ACID').text
					for wind_b1 in root.iter('SOAP_VAPOUR'):
						wind_base_min = float(wind_b1.find('SOAP_VAPOUR_MIN').text)
						wind_base_max = float(wind_b1.find('SOAP_VAPOUR_MAX').text)
				for wind_t in root.iter('TOXIC'):
					wind_toxic_co_min = float(wind_t.find('CO_MIN').text)
					wind_toxic_co_high = float(wind_t.find('CO_MAX').text)

		for temp in root.iter('HUMIDITY'):
			AH_high = float(temp.find('ABSOLUTE_HUMIDITY_TOP').text)
			AH_low = float(temp.find('ABSOLUTE_HUMIDITY_BOTTOM').text)
			RH_high = float(temp.find('RELATIVE_HUMIDITY_TOP').text)
			RH_low = float(temp.find('RELATIVE_HUMIDITY_BOTTOM').text)

		for temp in root.iter('SOILE'):
			for water_cont in root.iter('WATER_CONTENT'):
				SOIL_M_MIN = float(water_cont.find('WATER_CONTENT_MIN').text)
				SOIL_M_MAX = float(water_cont.find('WATER_CONTENT_MAX').text)

		for ph in root.iter('PH'):
			PH_top = float(ph.find('PH_TOP').text)
			PH_bottom = float(ph.find('PH_BOTTOM').text)

		for light in root.iter('LIGHTING'):
			for intencity in root.iter('INTENCITY'):
				intencity_top = float(intencity.find('INTENCITY_TOP').text)
				intencity_bottom = float(intencity.find('INTENCITY_BOTTOM').text)
			for UV in root.iter('UV_CONDITION'):
				UV_top = float(UV.find('UV_CONDITION_TOP').text)
				UV_bottom = float(UV.find('UV_CONDITION_BOTTM').text)
			for IR in root.iter('IR_CONDITION'):
				IR_top = float(IR.find('IR_CONDITION_TOP').text)
				IR_bottom = float(IR.find('IR_CONDITION_BOTTOM').text)

		
		print("############# END OF GATHERING XML DATA ##########")	
		print("getFlowerXML_Data")
		print("____________________")
		print("temp_high",temp_high)
		print("temp_low : ",temp_low)
		print("____________________")
		print("wind_high : ",wind_high)
		print("wind_low : ",wind_low)

		print("wind_nat : ",wind_nat)

		print("wind_acid_co2_min : ",wind_acid_co2_min)
		print("wind_acid_co2_high : ",wind_acid_co2_high)

		print("wind_acid_HCLO3_min : ",wind_acid_HCLO3_min)
		print("wind_acid_HCLO3_high : ",wind_acid_HCLO3_high)

		print("wind_base_min : ",wind_base_min)
		print("wind_base_max : ",wind_base_max)

		print("wind_toxic_co_min : ",wind_toxic_co_min)
		print("wind_toxic_co_high : ",wind_toxic_co_high)
		print("____________________")
		print("ABSOLUTE_HUMIDITY_TOP : ", AH_high)
		print("ABSOLUTE_HUMIDITY_BOTTOM : ", AH_low)

		print("RELATIVE_HUMIDITY_TOP : ", RH_high)
		print("RELATIVE_HUMIDITY_BOTTOM : ", RH_low)
		print("____________________")
		print("WATER_CONTENT_MIN : ", SOIL_M_MIN)
		print("WATER_CONTENT_MAX : ", SOIL_M_MAX)
		print("____________________")
		print("PH_TOP : ", PH_top)
		print("PH_BOTTOM : ", PH_bottom)
		print("____________________")
		print("INTENCITY_TOP : ", intencity_top)
		print("INTENCITY_BOTTOM : ", intencity_bottom)

		print("UV_CONDITION_TOP : ", UV_top)
		print("UV_CONDITION_BOTTOM : ", UV_bottom)

		print("IR_CONDITION_TOP : ", IR_top)
		print("IR_CONDITION_BOTTOM : ", IR_bottom)
		print("____________________")

		print("############# END OF GATHERING XML DATA ##########")




# w = whetherAnalysis
# w.__init__(25, 127,"stormy",100,2,5,20, 10,50, 100, 5.6, 30, 4, 6)

# w.tempratureAnalysis()
# w.windAnalysis()
# w.humidityAnalysis()
# w.soileMoistureAnalysis()