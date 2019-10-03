import simulation
import whetherAnalysis
import os

class programLogic():
	print("programLogic")

	def __init__(self, temp):
		# disease detect
		s_Disease = "plant_images\\disease_img.jpg"
		s_Image = "plant_images\\source_img.jpg"
		print("__init__")
		print(temp)
		# programLogic.diseaseDitect(s_Image, s_Disease)
		os.system("CLS")
		print("############## Please fill below details ##############")
		temprature = float(input("ENV TEMPRATURE : "))
		wind_speed = float(input("WIND SPEED : "))
		wind_nature = str(input("WIND NATURE : "))
		co2_level = float(input("CO2 LEVEL : "))
		hclo3_level = float(input("HCLO3 LEVEL : "))
		base_level = float(input("BASE LEVEL : "))
		co_level = float(input("CO LEVEL : "))
		AH_level = float(input("ABSOLUTE HUMIDITY : "))
		RH_level = float(input("RELETIVE HUMIDITY : "))
		soil_moisture = float(input("SOIL MOISTURE : "))
		PH_level = float(input("PH LEVEL : "))
		light_intensity = float(input("LIGHT INTENSITY : "))
		UV_condition = float(input("UV CONDITION : "))
		IR_condition = float(input("IR CONDITION : "))
		print("#######################################################")

		programLogic.pestDitect()
		programLogic.flowerDitect()

		w = whetherAnalysis.whetherAnalysis
		# w.__init__(25, 127,"stormy",100,2,5,20, 10,50, 100, 5.6, 30, 4, 6)
		w.__init__(temprature, wind_speed, wind_nature, co2_level, hclo3_level, base_level, co_level, AH_level, RH_level, soil_moisture, PH_level, light_intensity, UV_condition, IR_condition)

		simulation.simulation(s_Image, s_Disease, temprature, wind_speed, wind_nature, co2_level, hclo3_level, base_level, co_level, AH_level, RH_level, soil_moisture, PH_level, light_intensity, UV_condition, IR_condition)

	def pestDitect():
		print("pestDitect")

	def flowerDitect():
		print("flowerDitect")


pl = programLogic("apple")