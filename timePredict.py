import xml.etree.ElementTree as ET
import numpy as np

temprature    = 0.0
wind_speed    = 0.0
wind_nature   = ""
co2           = 0.0
hclo3         = 0.0
base          =	0.0
co            =	0.0
ah_level      =	0.0
rh_level      =	0.0
soil          =	0.0
ph_level      =	0.0
intensity     =	0.0
uv_level      =	0.0
ir_level      =	0.0

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


class timePredict():
	print("Class timePredict")

	def __init__(self,temprature_in, wind_speed_in, wind_nature_in, co2_in, hclo3_in, base_in, co_in, ah_level_in, rh_level_in, soil_in, ph_level_in, intensity_in, uv_level_in, ir_level_in, img_data):
		print("__init__")

		global temprature
		global wind_speed
		global wind_nature
		global co2
		global hclo3
		global base
		global co
		global ah_level
		global rh_level
		global soil
		global ph_level
		global intensity
		global uv_level
		global ir_level

		temprature    = 	temprature_in
		wind_speed    = 	wind_speed_in
		wind_nature   = 	wind_nature_in
		co2           = 	co2_in
		hclo3         = 	hclo3_in
		base          = 	base_in
		co            = 	co_in
		ah_level      = 	ah_level_in
		rh_level      = 	rh_level_in
		soil          = 	soil_in
		ph_level      = 	ph_level_in
		intensity     = 	intensity_in
		uv_level      = 	uv_level_in
		ir_level      = 	ir_level_in

		print(img_data)
		timePredict.getXMLData()

		# setting waights for each parameter
		# timePredict.tempEffect()
		# timePredict.windSpeedPredict()
		# timePredict.windNaturePredict()
		# timePredict.co2Predict()
		# timePredict.hclo3Predict()
		# timePredict.basePredict()
		# timePredict.coPredict()
		# timePredict.phPredict()
		# timePredict.soilPredict()
		# timePredict.ahPredict()
		# timePredict.rhPredict()
		# timePredict.intensityPredict()
		# timePredict.uvPredict()
		# timePredict.irPredict()

		new_img_data, new_dots = timePredict.calTimeAlgo(img_data)
		print(new_img_data," ",new_dots)

	def getXMLData():
		print("getXMLData")

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
		path = "XML\\demoFlower.xml"
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



	def  calTimeAlgo(i_img_data):
		print("timePredict")
		# setting waights for each parameter
		temprature_weight = 0.0
		wind_speed_weight = 0.0
		wind_nature_weight = 0.0
		o2_weight = 0.0
		clo3_weight = 0.0
		ase_weight = 0.0
		o_weight = 0.0
		h_level_weight = 0.0
		h_level_weight = 0.0
		oil_weight = 0.0
		h_level_weight = 0.0
		ntensity_weight = 0.0
		v_level_weight = 0.0
		r_level_weight = 0.0

		temprature_weight = timePredict.getTimeWeight(temprature, temp_high, temp_low)
		wind_speed_weight = timePredict.getTimeWeight(wind_speed, wind_high, wind_low )
		# wind_nature_weight = timePredict.getTimeWeight(wind_nature, wind_nat)
		co2_weight = timePredict.getTimeWeight(co2, wind_acid_co2_high, wind_acid_co2_min)
		hclo3_weight = timePredict.getTimeWeight(hclo3, wind_acid_HCLO3_high, wind_acid_HCLO3_min)
		base_weight = timePredict.getTimeWeight(base, wind_base_max,wind_base_min)
		co_weight = timePredict.getTimeWeight(co, wind_toxic_co_high, wind_toxic_co_min)
		ah_level_weight = timePredict.getTimeWeight(ah_level, AH_high, AH_low )
		rh_level_weight = timePredict.getTimeWeight(rh_level, RH_high, RH_low )
		soil_weight = timePredict.getTimeWeight(soil,SOIL_M_MAX, SOIL_M_MIN)
		ph_level_weight = timePredict.getTimeWeight(ph_level, PH_top, PH_bottom)
		intensity_weight = timePredict.getTimeWeight(intensity, intencity_top, intencity_bottom)
		uv_level_weight = timePredict.getTimeWeight(uv_level, UV_top, UV_bottom)
		ir_level_weight = timePredict.getTimeWeight(ir_level, IR_top, IR_bottom)

		# default dots 100
		dots = 800
		print("########################################")
		print("temprature_weight : ", temprature_weight)
		# make color more brown
		if(i_img_data[0] > 0):
			i_img_data[0] = 0
		if(i_img_data[1] > 0):
			i_img_data[0] -= (i_img_data[0]/255) * temprature_weight
		if(i_img_data[2] > 0):
			i_img_data[0] -= (i_img_data[0]/255) * temprature_weight

		print("i_img_data : ", i_img_data)

		print("wind_speed_weight : ", wind_speed_weight)
		# spredding speed increasing
		dots = dots*((100+wind_speed_weight)/100)

		print("dots : ", dots)

		print("wind_nature_weight : ", wind_nature_weight)
		# no effect

		print("co2_weight : ", co2_weight)
		# delays the speed of decaing the leaf
		dots = dots*((100-wind_speed_weight)/100)

		print("dots : ", dots)

		print("hclo3_weight : ", hclo3_weight)
		# leaf becomes more yellow
		if(i_img_data[0] > 0 & int(hclo3_weight)> 70):
			i_img_data[0] = ((hclo3_weight-50)/100) * 255
		if(i_img_data[1] > 0):
			i_img_data[0] += (i_img_data[0]/255) * hclo3_weight
		if(i_img_data[2] > 0):
			i_img_data[0] += (i_img_data[0]/255) * hclo3_weight

		print("i_img_data : ", i_img_data)

		print("base_weight : ", base_weight)
		# leaf becomes more bleached (nearly white)
		if(i_img_data[0] > 0 & int(base_weight) > 70):
			i_img_data[0] = (base_weight/100) * 255
		if(i_img_data[1] > 0):
			i_img_data[0] += (i_img_data[0]/255) * base_weight
		if(i_img_data[2] > 0):
			i_img_data[0] += (i_img_data[0]/255) * base_weight

		print("i_img_data : ", i_img_data)

		print("co_weight : ", co_weight)
		# no effect

		print("ah_level_weight : ", ah_level_weight)
		# no effect

		print("rh_level_weight : ", rh_level_weight)
		# leaf becomes more dark green
		if(i_img_data[0] > 0 & int(rh_level_weight) > 70):
			i_img_data[0] -= (i_img_data[0]/255) * rh_level_weight
		if(i_img_data[1] > 0):
			i_img_data[1] = (i_img_data[1]/255) * rh_level_weight
		if(i_img_data[2] > 0):
			i_img_data[0] -= (i_img_data[2]/255) * rh_level_weight

		print("i_img_data : ", i_img_data)

		print("soil_weight : ", soil_weight)
		# leaf becomes more dark green
		if(i_img_data[0] > 0 & int(soil_weight) > 70):
			i_img_data[0] -= (i_img_data[0]/255) * soil_weight
		if(i_img_data[1] > 0):
			i_img_data[1] += (i_img_data[1]/255) * soil_weight
		if(i_img_data[2] > 0):
			i_img_data[2] += (i_img_data[2]/255) * soil_weight

		print("i_img_data : ", i_img_data)

		print("ph_level_weight : ", ph_level_weight)
		# leaf becomes more orange color


		print("intensity_weight : ", intensity_weight)
		# brown dots
		print("uv_level_weight : ", uv_level_weight)
		# yellow dots
		if(i_img_data[0] > 0 & int(uv_level_weight)> 70):
			i_img_data[0] = (uv_level_weight-50/100) * 255
		if(i_img_data[1] > 0):
			i_img_data[1] += (i_img_data[1]/255) * uv_level_weight
		if(i_img_data[2] > 0):
			i_img_data[2] += (i_img_data[2]/255) * uv_level_weight

		print("i_img_data : ", i_img_data)

		print("ir_level_weight : ", ir_level_weight)
		# yellow dots
		if(i_img_data[0] > 0 & int(ir_level_weight)> 70):
			i_img_data[0] = (ir_level_weight-50/100) * 255
		if(i_img_data[1] > 0):
			i_img_data[1] += (i_img_data[1]/255) * ir_level_weight
		if(i_img_data[2] > 0):
			i_img_data[2] += (i_img_data[2]/255) * ir_level_weight

		print("i_img_data : ", i_img_data)

		i_img_data[0] = int(i_img_data[0])
		i_img_data[1] = int(i_img_data[1])
		i_img_data[2] = int(i_img_data[2])
		print(i_img_data)

		print("########################################")

		return i_img_data, dots


	def getTimeWeight(val, max_val, min_val):
		print("getTimeWeight")
		diff_1 = float(val - min_val)
		diff_2 = float(max_val - min_val)

		param_waight = (diff_1/diff_2) * 100
		if (param_waight < 0):
			param_waight = 0.0
		if (param_waight > 100):
			param_waight = 100.0
		# print(param_waight)
		return param_waight

	# # def tempEffect():
	# # 	print("timePredict")

	# def windSpeedPredict():
	# 	print("windSpeedPredict")

	# def windNaturePredict():
	# 	print("windNaturePredict")

	# def co2Predict():
	# 	print("co2Predict")

	# def hclo3Predict():
	# 	print("hclo3Predict")

	# def basePredict():
	# 	print("basePredict")

	# def coPredict():
	# 	print("coPredict")

	# def phPredict():
	# 	print("phPredict")

	# def soilPredict():
	# 	print("soilPredict")

	# def ahPredict():
	# 	print("ahPredict")

	# def rhPredict():
	# 	print("rhPredict")

	# def intensityPredict():
	# 	print("intensityPredict")

	# def uvPredict():
	# 	print("uvPredict")

	# def irPredict():
	# 	print("irPredict")

	def predictionAnalysis():
		print("predictionAnalysis")



x = timePredict(12,5,"apple",5,5,5,5,5,5,8,6,5,8,5, [12,25,36])